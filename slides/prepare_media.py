#!/usr/bin/env python3
"""Convert source figure GIFs into small, browser-friendly presentation media.

The originals are read only. Run with ``python3 slides/prepare_media.py``.
Requires ffmpeg and Pillow. Existing outputs newer than the source and this
script are reused; at most two ffmpeg processes run, each with two threads.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import shutil
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "how-to-turn-your-ai-into-a-world"
OUTPUT = ROOT / "slides" / "media"
SCRIPT_MTIME = Path(__file__).stat().st_mtime
POSTER_TIME_MS = 800
POSTER_TIME_OVERRIDES_MS = {
    # The completed Quanta headline appears after its initial brush animation.
    "figure-19": 1800,
}


def fresh(output: Path, source: Path) -> bool:
    return (
        output.is_file()
        and output.stat().st_size > 0
        and output.stat().st_mtime >= max(source.stat().st_mtime, SCRIPT_MTIME)
    )


def make_poster(source: Path, destination: Path) -> None:
    """Decode a representative frame, retaining its original size."""
    figure = re.match(r"(figure-\d+)-", source.name)
    poster_time_ms = POSTER_TIME_OVERRIDES_MS.get(
        figure.group(1) if figure else "", POSTER_TIME_MS
    )
    temporary = destination.with_name(destination.stem + ".tmp.png")
    with Image.open(source) as animation:
        elapsed = 0
        for index in range(animation.n_frames):
            animation.seek(index)
            duration = animation.info.get("duration", 100) or 100
            if elapsed + duration > poster_time_ms:
                break
            elapsed += duration
        frame = animation.convert("RGBA")
        poster = Image.new("RGB", frame.size, "white")
        poster.paste(frame, mask=frame.getchannel("A"))
        poster.save(temporary, optimize=True)
    temporary.replace(destination)


def convert(source: Path) -> tuple[str, dict[str, str], bool]:
    match = re.match(r"(figure-\d+)-", source.name)
    if not match:
        raise ValueError(f"Unexpected figure filename: {source}")
    name = match.group(1)
    video = OUTPUT / f"{name}.mp4"
    poster = OUTPUT / f"{name}.png"
    converted = False

    if not fresh(video, source):
        temporary = video.with_name(video.stem + ".tmp.mp4")
        command = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-threads", "2", "-ignore_loop", "1", "-i", str(source),
            "-an", "-vf", "fps=24,pad=ceil(iw/2)*2:ceil(ih/2)*2",
            "-c:v", "libx264", "-preset", "medium", "-crf", "22",
            "-pix_fmt", "yuv420p", "-threads", "2", "-filter_threads", "2",
            "-movflags", "+faststart", str(temporary),
        ]
        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as error:
            temporary.unlink(missing_ok=True)
            raise RuntimeError(f"ffmpeg failed for {source.name}: {error.stderr}") from error
        temporary.replace(video)
        converted = True

    if not fresh(poster, source):
        make_poster(source, poster)
        converted = True

    return (
        source.relative_to(ROOT).as_posix(),
        {
            "video": video.relative_to(ROOT).as_posix(),
            "poster": poster.relative_to(ROOT).as_posix(),
        },
        converted,
    )


def main() -> None:
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg is required to prepare presentation media.")
    sources = sorted(SOURCE.glob("figure-*.gif"))
    if not sources:
        raise SystemExit(f"No figure GIFs found in {SOURCE}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(convert, sources))

    manifest = {original: entry for original, entry, _ in results}
    manifest_path = OUTPUT / "manifest.json"
    serialized = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if not manifest_path.exists() or manifest_path.read_text() != serialized:
        manifest_path.write_text(serialized)

    original_bytes = sum(source.stat().st_size for source in sources)
    video_bytes = sum((ROOT / entry["video"]).stat().st_size for entry in manifest.values())
    poster_bytes = sum((ROOT / entry["poster"]).stat().st_size for entry in manifest.values())
    print(json.dumps({
        "figures": len(results),
        "converted": sum(converted for _, _, converted in results),
        "cached": sum(not converted for _, _, converted in results),
        "original_gif_bytes": original_bytes,
        "video_bytes": video_bytes,
        "poster_bytes": poster_bytes,
        "manifest": manifest_path.relative_to(ROOT).as_posix(),
    }, indent=2))


if __name__ == "__main__":
    main()
