"""Extract original video frames and rectangular crops for GUIDE_NOTE.md.

Run from any directory: python3 scripts/extract_guide1_assets.py
Requires ffmpeg, ffprobe and Pillow. No image generation or retouching is used.
"""

from pathlib import Path
import hashlib
import json
import subprocess

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "guide/guide1.mov"
OUT = ROOT / "assets/guide1"

# Crop boxes are native 2190 x 1224 source coordinates: left, top, right, bottom.
SCENES = [
    ("01-training", 2.7, "수백만 개의 웹사이트를 학습한 모델", [
        ("01-training-claim", "모델 이름과 학습 규모", (410, 180, 1575, 750)),
    ]),
    ("02-request", 4.8, "현대적인 웹사이트를 요청하는 프롬프트", [
        ("02-modern-website-prompt", "프롬프트 카드", (370, 365, 1795, 820)),
    ]),
    ("03-average", 6.7, "모든 것의 평균", [
        ("03-average-result", "평균적인 결과물 도식", (440, 135, 1730, 1070)),
    ]),
    ("04-reference", 10.45, "사용자가 방향을 정하고 Claude가 구현하는 역할", [
        ("04-oryzo-reference", "ORYZO 참고 사이트", (175, 545, 800, 990)),
        ("05-director-clapperboard", "사용자와 Claude의 역할을 보여 주는 슬레이트", (1190, 195, 1845, 665)),
    ]),
    ("05-direction", 12.15, "실제 참고 사이트를 제시하는 장면", [
        ("06-claude-director", "카메라와 모자를 착용한 캐릭터", (45, 575, 690, 1050)),
    ]),
    ("06-iterations", 15.1, "품질 기준에 도달하기 위한 반복", [
        ("07-iteration-diagram", "반복 작업과 품질 기준 도식", (140, 140, 1530, 960)),
    ]),
    ("07-quality", 16.05, "네 번째 시도에서 품질 기준 통과", [
        ("08-quality-cleared", "품질 기준 통과 도식", (140, 140, 1530, 960)),
    ]),
    ("08-mind-reader", 17.5, "Claude는 독심술사가 아니다", [
        ("09-not-a-mind-reader", "독심술사 비유와 캐릭터", (55, 280, 2140, 1120)),
    ]),
    ("09-adjectives", 21.6, "추상적인 스타일 단어로 요청한 결과", [
        ("10-style-adjectives", "스타일 형용사 카드", (175, 225, 1045, 970)),
        ("11-results-meh", "추상적인 요청의 결과 게이지", (1260, 165, 1855, 655)),
    ]),
    ("10-visual-example", 23.3, "구체적인 디자인 예시 FLOEMA", [
        ("12-floema-reference", "FLOEMA 사이트 카드", (230, 350, 1110, 920)),
        ("13-results-better", "참고 이미지를 제시한 뒤의 결과 게이지", (1260, 165, 1855, 655)),
    ]),
    ("11-son-daven", 24.9, "구체적인 디자인 예시 SON DAVEN", [
        ("14-son-daven-reference", "SON DAVEN 사이트 카드", (410, 190, 1230, 760)),
    ]),
    ("12-example-stack", 25.6, "FLOEMA, SON DAVEN, STUDIO 예시", [
        ("15-reference-stack", "세 가지 웹사이트 예시 묶음", (220, 220, 1310, 985)),
        ("16-studio-reference", "STUDIO 사이트 카드", (585, 460, 1300, 960)),
    ]),
    ("13-inspiration", 29.8, "디자이너가 영감을 얻는 사이트", [
        ("17-inspiration-sites", "디자인 참고 사이트 카드 모음", (65, 530, 1690, 1040)),
    ]),
    ("14-categories", 32.1, "여섯 가지 디자인 참고 범주", [
        ("18-six-categories", "여섯 가지 범주 전체", (20, 60, 2165, 860)),
        ("19-category-galleries", "01 갤러리", (25, 470, 345, 850)),
        ("20-category-real-apps", "02 실제 앱", (385, 470, 705, 850)),
        ("21-category-components", "03 컴포넌트", (745, 470, 1065, 850)),
        ("22-category-fonts", "04 글꼴", (1105, 470, 1425, 850)),
        ("23-category-color", "05 색상", (1465, 470, 1785, 850)),
        ("24-category-systems", "06 시스템", (1825, 470, 2145, 850)),
    ]),
    ("15-exact-look", 34.4, "원하는 디자인을 정확히 지시", [
        ("25-exactly-the-look", "원하는 모습 그대로라는 문구", (625, 860, 1200, 1025)),
    ]),
    ("16-in-action", 35.4, "실제 적용 사례", [
        ("26-southside-brewing", "SOUTHSIDE BREWING 웹사이트", (515, 375, 1415, 925)),
        ("27-in-action-sites", "HARBOUR LANE, SOUTHSIDE BREWING 등 적용 사례", (115, 370, 1690, 945)),
    ]),
]


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
    (OUT / "captures").mkdir(parents=True, exist_ok=True)
    (OUT / "crops").mkdir(parents=True, exist_ok=True)
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", str(SOURCE),
    ]))
    video = next(s for s in probe["streams"] if s["codec_type"] == "video")
    if (video["width"], video["height"]) != (2190, 1224):
        raise ValueError("Crop coordinates are specific to the provided 2190 x 1224 video")
    manifest = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "duration_seconds": float(probe["format"]["duration"]),
        "source_dimensions_px": [video["width"], video["height"]],
        "audio_streams": sum(s["codec_type"] == "audio" for s in probe["streams"]),
        "timestamp_note": "Requested seek time from source start; ffmpeg decodes the first available frame at or after that time.",
        "crop_coordinate_convention": "[left, top, right, bottom], source pixels; right and bottom exclusive",
        "processing": "Original decoded frames and rectangular crops only; no retouching, rotation, upscaling or background removal. Preview sheet alone is resized and labelled.",
        "scenes": [],
    }
    rows = ["# guide1.mov 캡처와 크롭", "",
            "[한국어 번역 노트](../../GUIDE_NOTE.md)의 참고 이미지입니다. 원본 영상에서 직접 추출했습니다.", "",
            "`captures/`에는 2190 × 1224 전체 프레임, `crops/`에는 원래 픽셀 크기를 유지한 직사각형 크롭이 있습니다. 배경과 겹친 요소는 원본 그대로입니다. 기울어진 카드나 가려진 영역을 복원하지 않았습니다.", "",
            "![장면 미리보기](contact-sheet.jpg)", "",
            "## 전체 장면", "", "| 시각 | 내용 | 캡처 |", "| --- | --- | --- |"]
    crop_rows = ["", "## 개별 에셋", "", "| 시각 | 에셋 | 크기 | 파일 |", "| --- | --- | --- | --- |"]
    for scene_id, timestamp, title, crop_defs in SCENES:
        frame_path = OUT / "captures" / f"{scene_id}.png"
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", str(timestamp), "-i", str(SOURCE), "-frames:v", "1", str(frame_path),
        ], check=True)
        scene = {"id": scene_id, "timestamp_seconds": timestamp, "description_ko": title,
                 "capture": file_info(frame_path), "crops": []}
        rows.append(f"| 00:{timestamp:05.2f} | {title} | [{scene_id}.png](captures/{scene_id}.png) |")
        with Image.open(frame_path) as frame:
            for crop_id, description, box in crop_defs:
                left, top, right, bottom = box
                assert 0 <= left < right <= frame.width and 0 <= top < bottom <= frame.height
                crop_path = OUT / "crops" / f"{crop_id}.png"
                frame.crop(box).save(crop_path)
                crop = {"id": crop_id, "description_ko": description, "box_ltrb_px": list(box), **file_info(crop_path)}
                scene["crops"].append(crop)
                width, height = crop["dimensions_px"]
                crop_rows.append(f"| 00:{timestamp:05.2f} | {description} | {width} × {height} | [{crop_id}.png](crops/{crop_id}.png) |")
        manifest["scenes"].append(scene)

    sheet = Image.new("RGB", (1600, 4 * 252), "#eeeae0")
    draw = ImageDraw.Draw(sheet)
    for i, scene in enumerate(manifest["scenes"]):
        x, y = (i % 4) * 400, (i // 4) * 252
        with Image.open(OUT / scene["capture"]["path"]) as im:
            thumbnail = ImageOps.contain(im, (394, 220))
            sheet.paste(thumbnail, (x + 3, y + 28))
        draw.text((x + 7, y + 8), f"{scene['id']} / {scene['timestamp_seconds']:.2f}s", fill="#171410")
    sheet.save(OUT / "contact-sheet.jpg", quality=90)
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    rows += crop_rows + ["", "## 추출 정보", "",
        "시각과 크롭 좌표, 파일 크기, SHA-256 해시는 [manifest.json](manifest.json)에 기록했습니다. 전체 프레임에는 영상에 원래 표시된 자막과 발표자, 녹화 테두리가 포함됩니다. 원본 자체가 다른 요소에 가려진 부분도 그대로 남습니다.", "",
        "다시 추출: `python3 scripts/extract_guide1_assets.py` (프로젝트 루트에서 실행).", ""]
    (OUT / "README.md").write_text("\n".join(rows))
    print(f"Created {len(SCENES)} captures and {sum(len(s[3]) for s in SCENES)} crops in {OUT}")


if __name__ == "__main__":
    main()
