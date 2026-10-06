#!/usr/bin/env python3
"""parts/*.html의 <section class="slide"> 조각을 모아 슬라이드 HTML을 만든다.

  python3 deck/build.py            # 전체(00 견본 제외) → deck/index.html
  python3 deck/build.py --part 02  # parts/02-*.html만 → deck/_preview/02.html

조각 안의 경로는 deck/ 기준으로 쓴다(예: ../assets/..., img/...).
각 section에는 다음 속성을 쓸 수 있다.
  data-hdr="top"(기본) | "bottom" | "none"  머리 라벨 위치
  data-hdr-tone="light"                       어두운 사진 위에서 라벨을 밝게
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "parts"
BRAND = "Design Eye for Claude"
PART_LABELS = {
    "00": "Layout Kit",
    "01": "Part 01  Intro",
    "02": "Part 02  8 Techniques",
    "03": "Part 03  Claude Code",
}

SECTION_RE = re.compile(r"<section\b[^>]*class=\"[^\"]*\bslide\b[^\"]*\"[^>]*>.*?</section>", re.S)
STYLE_RE = re.compile(r"<style\b[^>]*>.*?</style>", re.S)


def part_files(only=None):
    files = sorted(PARTS.glob("[0-9][0-9]-*.html"))
    if only:
        return [f for f in files if f.name.startswith(only)]
    return [f for f in files if not f.name.startswith("00")]  # 00-kit.html은 레이아웃 견본


def header(section, part_id, n, total):
    pos = re.search(r'data-hdr="(\w+)"', section)
    pos = pos.group(1) if pos else "top"
    if pos == "none":
        return section
    tone = " light" if 'data-hdr-tone="light"' in section else ""
    cls = "hdr" + (" bottom" if pos == "bottom" else "") + tone
    hdr = (
        f'<div class="{cls}"><span class="brand"><span class="mark"></span>{BRAND}</span>'
        f"<span>{PART_LABELS.get(part_id, '')}</span><span>{n:02d} / {total:02d}</span></div>"
    )
    return re.sub(r"(<section\b[^>]*>)", r"\1" + hdr, section, count=1)


def build(only=None):
    slides, styles = [], []
    for f in part_files(only):
        part_id = f.name[:2]
        text = f.read_text(encoding="utf-8")
        styles += STYLE_RE.findall(text)  # 파트 전용 스타일(섹션 클래스로 범위를 좁혀 쓴다)
        for sec in SECTION_RE.findall(text):
            slides.append((part_id, sec))
    total = len(slides)
    body = "\n".join(header(sec, pid, k + 1, total) for k, (pid, sec) in enumerate(slides))

    if only:
        out, prefix = ROOT / "_preview" / f"{only}.html", "../"
    else:
        out, prefix = ROOT / "index.html", ""
    out.parent.mkdir(exist_ok=True)
    if prefix:  # 미리보기는 한 단계 더 깊다
        body = re.sub(r'(src|href)="(?!https?:|data:|#|/)', rf'\1="{prefix}', body)
        styles = [re.sub(r"url\((['\"]?)(?!https?:|data:|/)", rf"url(\1{prefix}", s) for s in styles]

    html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Claude에게 디자인 안목을 주는 방법</title>
<link rel="stylesheet" href="{prefix}deck.css">
{chr(10).join(styles)}
</head>
<body>
<main class="deck">
{body}
</main>
<div class="progress"></div>
<script src="{prefix}deck.js"></script>
</body>
</html>
"""
    out.write_text(html, encoding="utf-8")
    print(f"{out.relative_to(ROOT.parent)}  slides={total}")
    return out, total


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", help="parts/ 파일 접두사(예: 01, 02, 03)")
    build(ap.parse_args().part)
