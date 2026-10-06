#!/usr/bin/env python3
"""Part 03 슬라이드용: HOW_DESIGN_FROM_CC.md에 나온 공개 참고 사이트의 첫 화면을 찍는다.

  python3 slides/img/sites/capture.py                     # 전체
  python3 slides/img/sites/capture.py --only oryzo,lusion # 일부만
  python3 slides/img/sites/capture.py --only vipp --wait 10 --scroll 300 --channel chrome

결과: slides/img/sites/<slug>.png (1600x1000 뷰포트), 긴 사이트는 <slug>-2.png(두 번째 구간).
"""
import argparse
import asyncio
import re
from pathlib import Path

from playwright.async_api import async_playwright

OUT = Path(__file__).resolve().parent

# slug, url, 두 번째 구간 스크롤 위치(뷰포트 높이 배수, None이면 찍지 않음)
SITES = [
    ("oryzo", "https://oryzo.ai/", 1.6),
    ("lusion", "https://lusion.co/", 1.2),
    ("cafetechnica", "https://www.cafetechnica.com.au/", 1.5),
    ("lacolombe", "https://www.lacolombe.com/", 1.2),
    ("annajona", "https://www.annajona.is/", 1.2),
    ("nimmobay", "https://www.nimmobay.com/", 1.2),
    ("vipp", "https://vipp.com/en/world-of-vipp/our-guesthouses", 1.0),
    ("amangiri", "https://www.aman.com/resorts/amangiri", 1.2),
    ("awwwards", "https://www.awwwards.com/", None),
    ("siteinspire", "https://www.siteinspire.com/", None),
    ("lapaninja", "https://www.lapa.ninja/", None),
    ("mobbin", "https://mobbin.com/", None),
    ("refero", "https://refero.design/", None),
    ("referostyles", "https://styles.refero.design/", None),
    ("21stdev", "https://21st.dev/", None),
    ("reactbits", "https://reactbits.dev/", None),
    ("fontsinuse", "https://fontsinuse.com/", None),
    ("googlefonts", "https://fonts.google.com/", None),
    ("coolors", "https://coolors.co/palettes/trending", None),
    ("brandingstyleguides", "https://brandingstyleguides.com/", None),
    ("pinterest", "https://www.pinterest.com/search/pins/?q=lake%20side%20cabin%20website", None),
    ("toools", "https://www.toools.design/", None),
    ("bookofshapes", "https://www.bookofshapes.com/", None),
    ("gofullpage", "https://gofullpage.com/", None),
    ("gauntlet", "https://somethingbig.ai/gauntlet-loop", None),
    ("claudedesign", "https://claude.com/product/design", None),
    ("frontenddesign", "https://github.com/anthropics/skills/tree/main/skills/frontend-design", None),
]

# 1차 촬영 뒤 다시 찍어 확인한 사이트별 설정 (--no-overrides로 끔)
OVERRIDES = {
    "oryzo": {"wait": 14},                      # 첫 로딩 애니메이션이 끝난 뒤
    "lusion": {"wait": 20},                     # 로더(0→100)가 끝난 뒤
    "cafetechnica": {"second": 0.7},            # 영상 히어로가 전체 화면으로 커진 지점
    "annajona": {"second": 3.0},                # 편지 글 대신 실내 사진 구간
    "refero": {"wait": 7, "kill": "Refero MCP connects"},  # 바뀌는 제목이 다 써진 때, MCP 홍보 창 제거
    "coolors": {"css": ".coolors-new-ad,#popover-hint{display:none!important}"},
    "pinterest": {"kill": "Welcome to Pinterest|Log in to discover"},  # 로그인 창 제거
}

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
ARGS = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist",
        "--disable-blink-features=AutomationControlled"]

CONSENT_RE = (r"^\s*(accept( all)?( cookies)?|accept (and|&) (close|continue)|allow( all)?( cookies)?|"
              r"agree( and continue)?|i agree|i accept|ok|okay|got it!?|close|dismiss|"
              r"i understand|understood|continue|yes,? i agree|alle akzeptieren|accepter|"
              r"no,? thanks|no thank you|maybe later|not now|skip|\u00d7|x)\s*[.!]?\s*$")

CLICK_JS = r"""
(reSrc) => {
  const re = new RegExp(reSrc, 'i');
  const els = [...document.querySelectorAll('button, a, [role=button], input[type=button], input[type=submit]')];
  let n = 0;
  for (const el of els) {
    const t = (el.innerText || el.value || el.getAttribute('aria-label') || '').trim();
    if (!t || t.length > 40 || !re.test(t)) continue;
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    if (r.width < 2 || r.height < 2 || cs.visibility === 'hidden' || cs.display === 'none') continue;
    // 쿠키/동의 문맥 안에 있는 'close/ok/continue'만 누른다
    const generic = /^(ok|okay|close|continue|dismiss|no,? thanks|no thank you|maybe later|not now|skip|\u00d7|x)$/i.test(t);
    if (generic) {
      let p = el, ctx = '', modal = false;
      for (let i = 0; i < 12 && p && p !== document.body; i++, p = p.parentElement) {
        ctx += ' ' + (p.id || '') + ' ' + (typeof p.className === 'string' ? p.className : '');
        const ps = getComputedStyle(p);
        if (ps.position === 'fixed' || p.tagName === 'DIALOG' || p.getAttribute('role') === 'dialog' || p.getAttribute('aria-modal') === 'true') modal = true;
      }
      const near = (el.closest('div,section,aside,dialog') || document.body).innerText.slice(0, 600);
      if (!modal && !/cookie|consent|privacy|gdpr|cmp|banner|popup|modal|newsletter/i.test(ctx + ' ' + near)) continue;
      if (/^continue$/i.test(t) && /email/i.test(near)) continue;  // 이메일 입력 폼의 Continue는 누르지 않음
    }
    try { el.click(); n++; } catch (e) {}
  }
  return n;
}
"""

# 동의 버튼을 누른 뒤에도 남은 쿠키 막(overlay)을 치운다
HIDE_JS = r"""
() => {
  const sel = ['#onetrust-consent-sdk', '#CybotCookiebotDialog', '#CybotCookiebotDialogBodyUnderlay',
    '.cc-window', '.cookie-banner', '#cookie-banner', '.cky-consent-container', '.cky-overlay',
    '#usercentrics-root', '.qc-cmp2-container', '#didomi-host', '.osano-cm-window', '#truste-consent-track',
    '.termly-styles-root', '#termly-code-snippet-support', '[aria-label="cookieconsent"]', '#hs-eu-cookie-confirmation',
    '.fc-consent-root', '#sp_message_container', '[id^=sp_message_container]'];
  sel.forEach(s => document.querySelectorAll(s).forEach(e => e.remove()));
  let n = 0;
  document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') return;
    const t = (el.innerText || '').slice(0, 1500);
    if (/cookie|consent|gdpr|privacy preferences|we use (cookies|tracking)/i.test(t) && t.length < 1500) {
      el.remove(); n++;
    }
  });
  document.documentElement.style.overflow = '';
  document.body.style.overflow = '';
  return n;
}
"""


KILL_JS = r"""
(reSrc) => {
  const re = new RegExp(reSrc, 'i');
  let n = 0;
  document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'absolute' && el.getAttribute('role') !== 'dialog') return;
    const r = el.getBoundingClientRect();
    if (r.width < 200 || r.height < 100) return;
    if (re.test((el.innerText || '').slice(0, 3000))) { el.remove(); n++; }
  });
  // 남은 반투명 배경막(텍스트 없는 전면 고정 요소)
  document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed') return;
    const r = el.getBoundingClientRect();
    if (r.width >= innerWidth * 0.9 && r.height >= innerHeight * 0.9 && !(el.innerText || '').trim() && !el.querySelector('img,video,canvas')) { el.remove(); n++; }
  });
  document.documentElement.style.overflow = 'auto';
  document.body.style.overflow = 'auto';
  document.body.style.position = '';
  return n;
}
"""

AD_RE = re.compile(r"googlesyndication|doubleclick|adservice\.google|googleadservices|amazon-adsystem|adnxs|"
                   r"taboola|outbrain|carbonads|buysellads|srv\.buysellads|ethicalads|adsafeprotected|"
                   r"criteo|pubmatic|rubiconproject|openx\.net|moatads|media\.net|adform|smartadserver")


async def dismiss(page, rounds=2, kill="", no_hide=False):
    total = 0
    for _ in range(rounds):
        for fr in page.frames:
            try:
                total += await fr.evaluate(CLICK_JS, CONSENT_RE)
            except Exception:
                pass
        await page.wait_for_timeout(700)
    try:
        await page.keyboard.press("Escape")
    except Exception:
        pass
    if not no_hide:
        try:
            total += await page.evaluate(HIDE_JS)
        except Exception:
            pass
    if kill:
        try:
            total += await page.evaluate(KILL_JS, kill)
        except Exception:
            pass
    return total


async def snap(page, path):
    try:
        await page.screenshot(path=str(path), timeout=45000)
    except Exception:
        # 웹 글꼴을 기다리다 멈추는 페이지는 CDP로 바로 찍는다
        import base64
        cdp = await page.context.new_cdp_session(page)
        r = await cdp.send("Page.captureScreenshot", {"format": "png"})
        Path(path).write_bytes(base64.b64decode(r["data"]))


async def smooth_scroll(page, y, steps=12):
    cur = await page.evaluate("window.scrollY")
    for i in range(1, steps + 1):
        await page.mouse.wheel(0, (y - cur) / steps)
        await page.wait_for_timeout(120)


async def shoot(browser, slug, url, second, opt, sem):
    if opt.overrides and slug in OVERRIDES:
        opt = argparse.Namespace(**{**vars(opt), **OVERRIDES[slug]})
    dk = {"kill": opt.kill, "no_hide": opt.no_hide}
    async with sem:
        ctx = await browser.new_context(viewport={"width": 1600, "height": 1000}, device_scale_factor=1,
                                        user_agent=UA, locale="en-US", timezone_id="America/New_York")
        await ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
        if opt.block_ads:
            await ctx.route(AD_RE, lambda route: route.abort())
        page = await ctx.new_page()
        msg = []
        try:
            try:
                await page.goto(url, wait_until="load", timeout=60000)
            except Exception as e:
                msg.append(f"goto: {type(e).__name__}")
            try:
                await page.wait_for_load_state("networkidle", timeout=12000)
            except Exception:
                pass
            await page.wait_for_timeout(int(opt.wait * 1000))
            if opt.css:
                await page.add_style_tag(content=opt.css)
            c = await dismiss(page, **dk)
            if c:
                msg.append(f"dismissed {c}")
            await page.mouse.move(800, 500)
            if opt.scroll:
                await smooth_scroll(page, opt.scroll)
                await page.wait_for_timeout(2500)
                await dismiss(page, rounds=1, **dk)
            await page.wait_for_timeout(1500)
            await snap(page, OUT / f"{slug}{opt.suffix}.png")
            if second and not opt.no_second:
                h = await page.evaluate("document.documentElement.scrollHeight")
                y = int(1000 * (opt.second or second))
                if h > y + 600:
                    await smooth_scroll(page, y, steps=16)
                    await page.wait_for_timeout(3500)
                    await dismiss(page, rounds=1, **dk)
                    await snap(page, OUT / f"{slug}-2{opt.suffix}.png")
                    msg.append("second")
        except Exception as e:
            msg.append(f"ERR {type(e).__name__}: {str(e)[:120]}")
        finally:
            await ctx.close()
        print(f"{slug:20s} {' | '.join(msg)}", flush=True)


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--wait", type=float, default=5.0)
    ap.add_argument("--scroll", type=int, default=0, help="찍기 전에 이만큼 스크롤(px)")
    ap.add_argument("--second", type=float, default=0, help="두 번째 구간 위치(뷰포트 배수) 덮어쓰기")
    ap.add_argument("--no-second", action="store_true")
    ap.add_argument("--channel", default="", help="예: chrome (설치된 Google Chrome 사용)")
    ap.add_argument("--headful", action="store_true")
    ap.add_argument("-j", type=int, default=4)
    ap.add_argument("--css", default="", help="찍기 전에 넣을 CSS(광고나 안내 말풍선 숨김)")
    ap.add_argument("--suffix", default="", help="시험용 파일 이름 꼬리표(예: _t)")
    ap.add_argument("--no-hide", action="store_true", help="쿠키 막 제거 JS를 쓰지 않음")
    ap.add_argument("--kill", default="", help="이 정규식과 맞는 글을 가진 고정 레이어(로그인 창 등)를 지움")
    ap.add_argument("--no-overrides", dest="overrides", action="store_false")
    ap.add_argument("--no-block-ads", dest="block_ads", action="store_false")
    opt = ap.parse_args()
    only = {s for s in opt.only.split(",") if s}
    todo = [s for s in SITES if not only or s[0] in only]
    sem = asyncio.Semaphore(opt.j)
    async with async_playwright() as p:
        kw = {"args": ARGS, "headless": not opt.headful}
        if opt.channel:
            kw["channel"] = opt.channel
        browser = await p.chromium.launch(**kw)
        await asyncio.gather(*(shoot(browser, slug, url, sec, opt, sem) for slug, url, sec in todo))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
