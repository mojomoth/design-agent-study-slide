"""Extract original video frames and rectangular crops for MOV_NOTE.md.

Run from any directory: python3 scripts/extract_mov_note_assets.py
Requires ffmpeg, ffprobe and Pillow. No image generation or retouching is used.
"""

from pathlib import Path
import hashlib
import json
import subprocess

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "guide/guide1.mov"
OUT = ROOT / "assets/guide1-mov"
FULL = (0, 0, 2190, 1224)

# Full frames: id, requested time in seconds, Korean title.
CAPTURES = [
    ("01-trained-on-counter", 0.90, "학습량 카운터가 올라가는 장면"),
    ("02-millions-of-websites", 3.00, "수백만 개의 웹사이트로 학습"),
    ("03-you-ask-for", 4.85, "현대적인 느낌의 웹사이트를 요청하는 프롬프트"),
    ("04-press-crushing", 5.40, "프레스가 웹사이트를 짓누르는 장면"),
    ("05-average-of-everything", 7.00, "모든 것의 평균"),
    ("06-most-important-thing", 10.20, "가장 중요한 것: 슬레이트와 ORYZO 레퍼런스"),
    ("07-character-with-reference", 12.45, "캐릭터가 ORYZO 레퍼런스를 들어 보이는 장면"),
    ("08-loop-setup", 13.30, "반복 루프 다이어그램의 시작 상태"),
    ("09-loop-iterating", 14.50, "반복이 진행 중인 루프 다이어그램"),
    ("10-loop-cleared", 16.40, "품질 기준선을 통과한 v4"),
    ("11-not-a-mind-reader", 17.75, "독심술사가 아닙니다"),
    ("12-style-first-chips", 20.60, "스타일 형용사 칩이 쌓이기 시작하는 장면"),
    ("13-style-all-chips", 21.55, "형용사 칩 14개와 MEH에 머문 게이지"),
    ("14-chips-crumpled", 21.92, "형용사 카드를 구겨 버리는 장면"),
    ("15-example-floema", 23.70, "FLOEMA 예시와 MUCH BETTER로 바뀐 게이지"),
    ("16-example-son-daven", 25.15, "SON DAVEN 예시가 겹쳐진 장면"),
    ("17-example-studio", 25.80, "세 예시 사이트가 쌓인 장면"),
    ("18-inspiration-sites", 30.00, "디자이너들이 영감을 얻는 사이트"),
    ("19-six-categories", 32.30, "6개 카테고리"),
    ("20-exactly-the-look", 34.00, "정확히 원하는 모습"),
    ("21-in-action", 35.42, "실제 적용 사례"),
]

# Crop boxes are native 2190 x 1224 source coordinates: left, top, right, bottom.
CROPS = [
    ("01-millions-of-websites-card", 3.00, "TRAINED ON MILLIONS OF WEBSITES 카드와 모델 배지", (345, 205, 1590, 750)),
    ("02-you-ask-for-prompt", 4.85, "YOU ASK FOR 프롬프트 카드", (355, 365, 1815, 830)),
    ("03-press-crushing", 5.40, "웹사이트를 짓누르는 프레스", (35, 232, 2155, 985)),
    ("04-average-website-mockup", 6.60, "흐릿한 평균적인 웹사이트 목업", (610, 500, 1562, 1088)),
    ("05-average-of-everything-headline", 7.00, "THE AVERAGE OF EVERYTHING 제목", (435, 128, 1735, 503)),
    ("06-oryzo-hero", 7.80, "ORYZO 레퍼런스 카드의 첫 화면", (155, 540, 800, 1002)),
    ("07-most-important-thing-headline", 10.20, "SO WHAT DO YOU DO? THE MOST IMPORTANT THING 제목", (145, 95, 1175, 405)),
    ("08-oryzo-reference-card", 10.20, "REFERENCE 01 ORYZO 카드", (165, 540, 790, 995)),
    ("09-film-slate", 10.30, "작품, 감독, 출연이 적힌 영화 슬레이트", (1195, 195, 1830, 655)),
    ("10-character-holding-reference", 12.45, "ORYZO 레퍼런스를 들어 보이는 캐릭터", (66, 386, 1128, 1040)),
    ("11-beer-site-annotation", 12.45, "맥주 사이트의 실제 레퍼런스라는 손글씨 주석", (1065, 715, 1693, 840)),
    ("12-loop-diagram-setup", 13.30, "반복 루프 다이어그램 시작 상태", (140, 85, 1520, 905)),
    ("13-loop-diagram-iterating", 14.50, "반복 루프 다이어그램 2회 반복", (140, 85, 1520, 905)),
    ("14-loop-diagram-cleared", 16.40, "반복 루프 다이어그램 4회 반복 후 통과", (140, 85, 1520, 905)),
    ("15-not-a-mind-reader", 17.75, "수정 구슬을 든 캐릭터와 NOT A MIND READER", (45, 290, 2150, 1110)),
    ("16-not-a-mind-reader-headline", 17.75, "NOT A MIND READER 제목", (1175, 305, 2130, 920)),
    ("17-what-style-label", 20.60, "WHAT STYLE DO YOU WANT? 라벨", (80, 55, 870, 130)),
    ("18-style-adjective-chips", 21.55, "make it look… 형용사 칩 14개", (150, 190, 1025, 930)),
    ("19-results-gauge-meh", 21.55, "RESULTS 게이지: MEH", (1265, 165, 1865, 650)),
    ("20-crumpled-paper-ball", 21.92, "구겨진 종이 뭉치", (659, 680, 949, 963)),
    ("21-example-01-floema", 23.70, "EXAMPLE 01 FLOEMA 카드", (226, 338, 1112, 916)),
    ("22-results-gauge-much-better", 23.70, "RESULTS 게이지: MUCH BETTER", (1265, 165, 1865, 650)),
    ("23-example-02-son-daven", 25.15, "EXAMPLE 02 SON DAVEN 카드", (440, 200, 1210, 760)),
    ("24-example-03-studio", 25.80, "EXAMPLE 03 STUDIO 카드", (584, 458, 1280, 948)),
    ("25-example-cards-stack", 25.80, "세 예시 사이트 카드 묶음", (222, 205, 1280, 945)),
    ("26-site-awwwards", 26.13, "AWWWARDS 카드", (64, 680, 640, 1044)),
    ("27-site-siteinspire", 26.22, "SITEINSPIRE 카드", (350, 690, 860, 1044)),
    ("28-site-lapa-ninja", 26.33, "LAPA NINJA 카드", (250, 600, 830, 1044)),
    ("29-site-mobbin", 26.47, "MOBBIN 카드", (255, 515, 905, 1044)),
    ("30-site-refero", 26.50, "REFERO 카드", (590, 685, 1065, 1044)),
    ("31-site-21st-dev-react-bits", 26.73, "21ST.DEV와 REACT BITS 카드", (512, 445, 1190, 1020)),
    ("32-site-fonts-in-use", 26.83, "FONTS IN USE 카드", (700, 440, 1330, 942)),
    ("33-site-google-fonts", 26.93, "GOOGLE FONTS 카드", (905, 555, 1455, 1000)),
    ("34-site-coolors", 27.06, "COOLORS 카드", (1005, 575, 1590, 1040)),
    ("35-site-brandingstyleguides", 27.13, "BRANDINGSTYLEGUIDES 카드", (1100, 590, 1694, 1044)),
    ("36-site-pinterest", 27.22, "PINTEREST 카드", (1060, 690, 1590, 1044)),
    ("37-site-tooools-design", 27.29, "TOOOLS.DESIGN 카드", (1050, 640, 1694, 1044)),
    ("38-in-this-video-headline", 30.00, "IN THIS VIDEO 제목", (130, 85, 1360, 515)),
    ("39-inspiration-sites-fan", 30.00, "영감 사이트 13곳의 카드 부채꼴", (63, 525, 1694, 1044)),
    ("40-six-categories-headline", 32.30, "BROKEN INTO 6 CATEGORIES 제목", (85, 65, 1650, 390)),
    ("41-six-category-tiles", 32.30, "6개 카테고리 타일", (15, 465, 2140, 855)),
    ("42-category-galleries", 32.30, "01 GALLERIES 타일", (25, 470, 345, 850)),
    ("43-category-real-apps", 32.30, "02 REAL APPS 타일", (385, 470, 705, 850)),
    ("44-category-components", 32.30, "03 COMPONENTS 타일", (745, 470, 1065, 850)),
    ("45-category-fonts", 32.30, "04 FONTS 타일", (1105, 470, 1425, 850)),
    ("46-category-color", 32.30, "05 COLOR 타일", (1465, 470, 1785, 850)),
    ("47-category-systems", 32.30, "06 SYSTEMS 타일", (1825, 470, 2145, 850)),
    ("48-explorer-exactly-the-look", 34.00, "탐험가 캐릭터와 EXACTLY THE LOOK 라벨", (9, 465, 1415, 1135)),
    ("49-in-action-sites", 35.00, "실제 적용 사례 사이트 3개", (30, 400, 2120, 1070)),
    ("50-harbour-lane", 35.00, "HARBOUR LANE 사이트", (30, 548, 540, 1000)),
    ("51-southside-brewing", 35.00, "SOUTHSIDE BREWING 사이트", (530, 405, 1640, 1066)),
    ("52-blackwater-cabins", 35.00, "BLACKWATER CABINS 사이트", (1625, 565, 2120, 990)),
]


def frame_times():
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "frame=pts_time", "-of", "csv=p=0", str(SOURCE),
    ], text=True)
    # Some frames carry side data, which ffprobe prints as a trailing comma.
    return [float(line.strip(",")) for line in out.split() if line.strip(",")]


def pick_frame(times, requested):
    """First decoded frame at or after the requested time (4 ms tolerance), else the last frame."""
    return next((t for t in times if t >= requested - 0.004), times[-1])


def decode(pts, cache):
    if pts not in cache:
        path = OUT / ".frames" / f"{pts:.6f}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", f"{max(pts - 0.001, 0):.6f}", "-i", str(SOURCE), "-frames:v", "1", str(path),
        ], check=True)
        cache[pts] = path
    return cache[pts]


def file_info(path):
    with Image.open(path) as im:
        dimensions = list(im.size)
    return {
        "path": str(path.relative_to(OUT)),
        "dimensions_px": dimensions,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main():
    for sub in ("captures", "crops"):
        (OUT / sub).mkdir(parents=True, exist_ok=True)
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", str(SOURCE),
    ]))
    video = next(s for s in probe["streams"] if s["codec_type"] == "video")
    if (video["width"], video["height"]) != FULL[2:]:
        raise ValueError("Crop coordinates are specific to the provided 2190 x 1224 video")
    times = frame_times()
    cache = {}
    manifest = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "duration_seconds": float(probe["format"]["duration"]),
        "source_dimensions_px": [video["width"], video["height"]],
        "decoded_frames": len(times),
        "audio_streams": sum(s["codec_type"] == "audio" for s in probe["streams"]),
        "timestamp_note": "requested_seconds is the time listed in MOV_NOTE.md; frame_pts_seconds is the decoded frame actually used (first frame at or after the request, or the last frame).",
        "crop_coordinate_convention": "[left, top, right, bottom], source pixels; right and bottom exclusive",
        "processing": "Original decoded frames and rectangular crops only; no retouching, rotation, upscaling or background removal. The contact sheet alone is resized and labelled.",
        "captures": [],
        "crops": [],
    }
    for kind, items in (("captures", [(i, t, title, FULL) for i, t, title in CAPTURES]), ("crops", CROPS)):
        for item_id, requested, title, box in items:
            pts = pick_frame(times, requested)
            out = OUT / kind / f"{item_id}.png"
            with Image.open(decode(pts, cache)) as frame:
                left, top, right, bottom = box
                assert 0 <= left < right <= frame.width and 0 <= top < bottom <= frame.height, item_id
                frame.crop(box).save(out)
            manifest[kind].append({
                "id": item_id, "title_ko": title, "requested_seconds": requested,
                "frame_pts_seconds": round(pts, 6), "box_ltrb_px": list(box), **file_info(out),
            })

    columns, tile_w, tile_h = 4, 400, 252
    rows = -(-len(CAPTURES) // columns)
    sheet = Image.new("RGB", (columns * tile_w, rows * tile_h), "#eeeae0")
    draw = ImageDraw.Draw(sheet)
    for i, capture in enumerate(manifest["captures"]):
        x, y = (i % columns) * tile_w, (i // columns) * tile_h
        with Image.open(OUT / capture["path"]) as im:
            sheet.paste(ImageOps.contain(im, (394, 220)), (x + 3, y + 28))
        draw.text((x + 7, y + 8), f"{capture['id']} / {capture['requested_seconds']:.2f}s", fill="#171410")
    sheet.save(OUT / "contact-sheet.jpg", quality=90)
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    for path in cache.values():
        path.unlink()
    (OUT / ".frames").rmdir()
    print(f"Created {len(CAPTURES)} captures and {len(CROPS)} crops in {OUT}")


if __name__ == "__main__":
    main()
