#!/usr/bin/env python3
"""슬라이드를 1920x1080 PNG로 찍고 목차용 밀착 인화(contact sheet)를 만든다.

  python3 deck/render.py               # deck/index.html → deck/shots/all/
  python3 deck/render.py --part 02     # build.py --part 02 후 → deck/shots/02/
  python3 deck/render.py --pdf         # 전체를 deck/deck.pdf로도 저장

각 PNG는 shots/<name>/NN.png, 밀착 인화는 shots/<name>/contact.jpg.
렌더링 중 생긴 문제(깨진 이미지, 캔버스 밖으로 넘친 요소)는 shots/<name>/issues.txt에 적는다.
"""
import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent

CHECK_JS = r"""
(idx) => {
  const s = document.querySelectorAll('.slide')[idx];
  const out = [];
  const sr = s.getBoundingClientRect();
  s.querySelectorAll('img').forEach(img => {
    if (!img.complete || img.naturalWidth === 0) out.push('broken image: ' + img.getAttribute('src'));
  });
  s.querySelectorAll('*').forEach(el => {
    if (el.closest('.fig')) return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    const pad = 2;
    if (r.right > sr.right + pad || r.bottom > sr.bottom + pad || r.left < sr.left - pad || r.top < sr.top - pad) {
      if (getComputedStyle(el).position !== 'static' || el.children.length === 0) {
        const t = (el.innerText || el.className || el.tagName).toString().slice(0, 40).replace(/\s+/g, ' ');
        out.push('overflow canvas: <' + el.tagName.toLowerCase() + '> ' + t);
      }
    }
  });
  // 글자가 자기 상자를 넘치는지(가로)
  s.querySelectorAll('.d, .lead, .txt, .lbl, .cap').forEach(el => {
    if (el.scrollWidth > el.clientWidth + 4 && getComputedStyle(el).overflow !== 'visible') out.push('text clipped: ' + el.innerText.slice(0, 40));
  });
  return [...new Set(out)];
}
"""


def contact(shots, out, cols=4, w=480):
    h = int(w * 1080 / 1920)
    rows = (len(shots) + cols - 1) // cols
    pad, lab = 16, 26
    sheet = Image.new("RGB", (cols * (w + pad) + pad, rows * (h + pad + lab) + pad), (30, 30, 30))
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype(str(ROOT / "fonts" / "Anton-Regular.ttf"), 18)
    except Exception:
        font = ImageFont.load_default()
    for k, p in enumerate(shots):
        im = Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS)
        x = pad + (k % cols) * (w + pad)
        y = pad + (k // cols) * (h + pad + lab)
        d.text((x, y), p.stem, fill=(240, 235, 224), font=font)
        sheet.paste(im, (x, y + lab))
    sheet.save(out, quality=88)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part")
    ap.add_argument("--pdf", action="store_true")
    a = ap.parse_args()

    if a.part:
        subprocess.run([sys.executable, str(ROOT / "build.py"), "--part", a.part], check=True)
        page_path = ROOT / "_preview" / f"{a.part}.html"
        name = a.part
    else:
        subprocess.run([sys.executable, str(ROOT / "build.py")], check=True)
        page_path = ROOT / "index.html"
        name = "all"

    out_dir = ROOT / "shots" / name
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.png"):
        old.unlink()

    issues = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        pg.goto(page_path.as_uri() + "#1")
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.evaluate("Promise.all([...document.images].map(img => img.decode().catch(() => {})))")
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        shots = []
        for k in range(n):
            pg.evaluate(f"location.hash = '#{k + 1}'")
            pg.wait_for_timeout(250)
            f = out_dir / f"{k + 1:02d}.png"
            pg.screenshot(path=str(f))
            shots.append(f)
            for msg in pg.evaluate(CHECK_JS, k):
                issues.append(f"{k + 1:02d}: {msg}")
        if a.pdf and not a.part:
            pg.emulate_media(media="print")
            pg.pdf(path=str(ROOT / "deck.pdf"), width="1920px", height="1080px", print_background=True)
        b.close()

    contact(shots, out_dir / "contact.jpg")
    (out_dir / "issues.txt").write_text("\n".join(issues) + ("\n" if issues else ""), encoding="utf-8")
    print(f"rendered {len(shots)} slides → {out_dir.relative_to(ROOT.parent)}")
    print(f"issues: {len(issues)}" + ("" if not issues else "\n" + "\n".join(issues[:40])))


if __name__ == "__main__":
    main()
