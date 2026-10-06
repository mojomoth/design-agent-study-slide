#!/usr/bin/env python3
"""Build an offline translated article from the user's saved HTML and media.

The captured JavaScript is never read or executed. Original media is copied
without conversion, and visible images and styles are embedded in the HTML.
"""

from __future__ import annotations

import argparse
import base64
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit

from lxml import etree, html
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "guide/How to turn your AI into a world-class designer.html"
MEDIA = SOURCE.parent / (SOURCE.stem + "_files")
WORK = ROOT / ".work/guide-clone"
ASSETS = ROOT / "assets/how-to-turn-your-ai-into-a-world"
DESTINATION = ROOT / "clone/how-to-turn-your-ai-into-a-world/index.html"
SOURCE_URL = "https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world"
URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I | re.S)
BODY_XPATH = '//article//div[contains(concat(" ",normalize-space(@class)," ")," body ")]'
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def load_json(path: Path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def source_path(value: str) -> Path:
    parts = urlsplit(value)
    if parts.scheme or parts.netloc:
        raise ValueError(f"Expected saved local resource, found: {value}")
    path = (SOURCE.parent / unquote(parts.path)).resolve()
    if not path.is_relative_to(MEDIA.resolve()):
        raise ValueError(f"Resource outside captured media folder: {value}")
    return path


def data_url(path: Path, mime: str | None = None) -> str:
    if mime is None:
        if path.suffix.lower() == ".svg":
            mime = "image/svg+xml"
        else:
            with Image.open(path) as image:
                mime = Image.MIME[image.format]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def class_xpath(class_name: str) -> str:
    return f'.//*[contains(concat(" ",normalize-space(@class)," ")," {class_name} ")]'


def remove(node):
    if node.getparent() is not None:
        node.getparent().remove(node)


def copy_assets(tree) -> tuple[list[dict], dict]:
    body = tree.xpath(BODY_XPATH)[0]
    figures = body.xpath(".//figure")
    if len(figures) != 25:
        raise ValueError(f"Expected 25 article figures, found {len(figures)}")
    figure_sources = {}
    for number, figure in enumerate(figures, 1):
        image = figure.xpath(".//img")[0]
        path = source_path(image.get("src"))
        preceding = figure.xpath("preceding::*[self::p or self::h1 or self::h2 or self::h3]")
        preceding = [node for node in preceding if body in node.iterancestors()]
        headings = [node for node in preceding if node.tag.startswith("h")]
        figure_sources[path.name] = {
            "figure_number": number,
            "figure_id": f"figure-{number:02d}",
            "preceding_text": preceding[-1].text_content().strip() if preceding else "",
            "preceding_heading": headings[-1].text_content().strip() if headings else "",
        }

    files = sorted(path for path in MEDIA.iterdir() if path.suffix.lower() in IMAGE_EXTENSIONS)
    if len(files) != 47:
        raise ValueError(f"Expected all 47 saved images, found {len(files)}")
    ASSETS.mkdir(parents=True, exist_ok=True)
    records = []
    by_source = {}
    for path in files:
        figure_info = figure_sources.get(path.name, {})
        target_name = f'{figure_info["figure_id"]}-{path.name}' if figure_info else path.name
        target = ASSETS / target_name
        source_hash = digest(path)
        if not target.exists() or digest(target) != source_hash:
            shutil.copyfile(path, target)
        with Image.open(path) as image:
            width, height = image.size
            mime = Image.MIME[image.format]
            frames = getattr(image, "n_frames", 1)
            animated = getattr(image, "is_animated", False)
        record = {
            "source_name": path.name,
            "source_path": str(path.relative_to(ROOT)),
            "sha256": source_hash,
            "asset_path": str(target.relative_to(ROOT)),
            "bytes": path.stat().st_size,
            "mime_type": mime,
            "width": width,
            "height": height,
            "animated": animated,
            "frames": frames,
            "figure_number": None,
            "figure_id": None,
            **figure_info,
        }
        records.append(record)
        by_source[path.name] = record
    return records, by_source


def read_translations(preview: bool) -> dict:
    translations = {}
    for path in sorted(WORK.glob("ko-*.json")):
        data = load_json(path)
        pairs = data.items() if isinstance(data, dict) else ((item["id"], item.get("html", item.get("ko"))) for item in data)
        for key, value in pairs:
            if key in translations:
                raise ValueError(f"Duplicate translated segment: {key}")
            translations[key] = value["html"] if isinstance(value, dict) else value
    segments = load_json(WORK / "segments.json")
    required = {segment["id"] for segment in segments}
    if len(required) != 182:
        raise ValueError(f"Expected 182 source blocks, found {len(required)}")
    extra = set(translations) - required
    missing = required - set(translations)
    if extra or (missing and not preview):
        raise ValueError(f"Translation IDs mismatch: missing={sorted(missing)}, extra={sorted(extra)}")
    return translations


def replace_inner_html(node, translated: str):
    # Source headings carry empty anchor wrappers that translators may omit.
    old_anchors = [deepcopy(child) for child in node if child.tag == "div" and (child.get("id") or child.xpath(".//@id"))]
    for child in list(node):
        node.remove(child)
    node.text = None
    fragment = html.fragment_fromstring(translated, create_parent="div")
    node.text = fragment.text
    for child in list(fragment):
        node.append(child)
    current_ids = set(node.xpath(".//@id"))
    for anchor in old_anchors:
        anchor_ids = set(anchor.xpath(".//@id")) | ({anchor.get("id")} if anchor.get("id") else set())
        if not anchor_ids.intersection(current_ids):
            node.insert(0, anchor)


def translate(tree, translations):
    # Resolve all XPaths before touching sibling structure.
    resolved = []
    for segment in load_json(WORK / "segments.json"):
        matches = tree.xpath(segment["xpath"])
        if len(matches) != 1:
            raise ValueError(f'Could not resolve segment {segment["id"]}')
        resolved.append((segment, matches[0]))
    for segment, node in resolved:
        node.set("data-source-block", segment["id"])
        if segment["id"] in translations:
            replace_inner_html(node, translations[segment["id"]])
            node.set("lang", "ko")


def prune_chrome(tree):
    article = tree.xpath("//article")[0]
    header = tree.xpath('//div[@class="main-menu"]')[0]
    keep = set(article.iter()) | set(header.iter()) | set(article.iterancestors()) | set(header.iterancestors())
    body = tree.xpath("//body")[0]
    for node in list(body.iterdescendants()):
        if node not in keep:
            remove(node)

    content = article.xpath(class_xpath("dt-post-body"))[0]
    content_container = content.getparent()
    for child in list(content_container):
        if child is not content:
            remove(child)
    for name in ("visibility-check", "subscribe-widget", "image-link-expand", "post-ufi", "paywall-jump"):
        for node in tree.xpath(class_xpath(name)):
            remove(node)

    # The original header had scrolled above the viewport when it was saved.
    for node in header.xpath('.//*[starts-with(@class,"mainMenuContent-")]'):
        node.set("style", "position: relative; top: 0;")
    # Its spacer compensated for a fixed header, which is now in normal flow.
    for child in list(header):
        if child.tag == "div" and not child.get("class") and not len(child) and child.get("style", "").strip() == "height: 88px;":
            remove(child)
    for node in header.xpath('.//a[not(.//img)]'):
        remove(node)
    for node in tree.xpath("//button|//form|//input|//select|//textarea"):
        remove(node)


def sanitize_css(css: str, source_name: str, inventory: list) -> str:
    for match in URL_RE.finditer(css):
        value = match.group(2).strip()
        if value and not value.startswith("data:"):
            inventory.append({"stylesheet": source_name, "url": value, "resolution": "not captured; disabled for offline use"})
    css = re.sub(r"@font-face\s*\{[^}]*\}", "", css, flags=re.I | re.S)
    css = re.sub(r"@import\s+[^;]+;", "", css, flags=re.I)
    css = re.sub(r"/\*[#@]\s*sourceMappingURL=.*?\*/", "", css, flags=re.S)
    return URL_RE.sub(lambda match: match.group(0) if match.group(2).strip().startswith("data:") else 'url("data:,")', css)


def inline_styles(tree) -> tuple[list, list]:
    inventory = []
    stylesheets = []
    for node in list(tree.xpath("//link|//style")):
        if node.tag == "link":
            if node.get("rel") == "stylesheet":
                path = source_path(node.get("href"))
                style = etree.Element("style", {"data-source-stylesheet": path.name})
                style.text = sanitize_css(path.read_text(), path.name, inventory)
                node.getparent().replace(node, style)
                stylesheets.append({"source_name": path.name, "sha256": digest(path), "bytes": path.stat().st_size})
            else:
                remove(node)
        else:
            node.text = sanitize_css(node.text or "", "inline", inventory)
    for node in tree.xpath("//*[@style]"):
        node.set("style", sanitize_css(node.get("style"), "style attribute", inventory))
    return inventory, stylesheets


def apply_metadata(tree):
    defaults = {
        "title": "AI를 뛰어난 디자이너로 만드는 방법",
        "subtitle": "AI의 숨은 창의력을 끌어내는 디자인 과정",
        "author": "Anshu Chimala",
        "date": "2026년 9월 1일",
    }
    metadata = defaults | load_json(WORK / "article-meta.ko.json", {})
    root = tree.getroot()
    root.set("lang", "ko")
    root.set("dir", "ltr")
    head = tree.xpath("//head")[0]
    for node in list(head):
        if node.tag not in ("style", "title"):
            remove(node)
    title = head.find("title")
    if title is None:
        title = etree.SubElement(head, "title")
    title.text = metadata["title"] + " | Lenny’s Newsletter"
    head.insert(0, etree.Element("meta", charset="utf-8"))
    head.insert(1, etree.Element("meta", name="viewport", content="width=device-width, initial-scale=1"))
    head.insert(2, etree.Element("meta", {"http-equiv": "Content-Security-Policy", "content": "default-src 'none'; img-src data:; style-src 'unsafe-inline'; font-src data:; script-src 'none'; connect-src 'none'; object-src 'none'; frame-src 'none'; base-uri 'none'; form-action 'none'"}))
    head.insert(3, etree.Element("meta", name="original-url", content=SOURCE_URL))
    head.insert(4, etree.Element("meta", name="description", content=metadata["subtitle"]))
    article = tree.xpath("//article")[0]
    article.xpath('.//h1[contains(@class,"post-title")]')[0].text = metadata["title"]
    article.xpath('.//h3[contains(@class,"subtitle")]')[0].text = metadata["subtitle"]
    for node in article.xpath(".//time"):
        node.text = metadata["date"]
        node.set("title", metadata["date"])
    for node in article.xpath('.//a[normalize-space(text())="Anshu Chimala"]'):
        node.text = metadata["author"]
    for node in article.xpath('.//*[normalize-space(text())="∙ Paid"]'):
        node.text = "유료 구독 글"
    article.set("aria-label", metadata["title"])
    return metadata


def sanitize_dom(tree, by_source):
    for node in list(tree.xpath("//script|//iframe|//object|//embed|//base|//noscript|//video|//audio")):
        remove(node)
    for comment in tree.xpath("//comment()"):
        remove(comment)
    # lxml's HTML parser nests img under source for this captured document.
    # Unwrap source rather than deleting its descendant image.
    for node in tree.xpath("//source"):
        node.drop_tag()
    for node in tree.iter():
        if not isinstance(node.tag, str):
            continue
        for attribute in list(node.attrib):
            if attribute.lower().startswith("on") or attribute.startswith("data-") or attribute in ("srcset", "sizes", "ping", "nonce", "integrity", "crossorigin", "autofocus"):
                if attribute not in ("data-source-block", "data-source-stylesheet", "data-figure-id"):
                    del node.attrib[attribute]
        for attribute in ("href", "src", "action", "formaction"):
            if node.get(attribute, "").lower().startswith(("javascript:", "vbscript:")):
                del node.attrib[attribute]
    for image in tree.xpath("//img"):
        path = source_path(image.get("src"))
        record = by_source[path.name]
        image.set("src", data_url(path, record["mime_type"]))
        image.attrib.pop("decoding", None)
        image.attrib.pop("loading", None)
        if record["figure_id"]:
            image.set("data-figure-id", record["figure_id"])
        elif "avatar" in image.get("alt", ""):
            image.set("alt", "Anshu Chimala 프로필 사진")
    for anchor in tree.xpath('//a[contains(concat(" ",normalize-space(@class)," ")," image-link ")]'):
        for attribute in ("href", "target", "rel"):
            anchor.attrib.pop(attribute, None)
    for anchor in tree.xpath("//a[@href]"):
        anchor.set("rel", "noreferrer noopener")
    # SVG names are lowercased by lxml's HTML parser; restore case-sensitive
    # attribute names before browsers parse the final HTML.
    for node in tree.xpath("//svg//*[@viewbox] | //svg[@viewbox]"):
        node.set("viewBox", node.attrib.pop("viewbox"))


def annotate_figures(tree):
    captions = load_json(WORK / "figure-captions.ko.json", {})
    figure_text = load_json(WORK / "figure-text.ko.json", {})
    for number, figure in enumerate(tree.xpath(BODY_XPATH)[0].xpath(".//figure"), 1):
        key = f"figure-{number:02d}"
        figure.set("id", key)
        caption = captions.get(key, captions.get(str(number)))
        if isinstance(caption, dict):
            caption = caption.get("caption", caption.get("text"))
        if caption:
            for existing in figure.xpath("./figcaption"):
                remove(existing)
            node = etree.SubElement(figure, "figcaption")
            node.text = caption
            figure.xpath(".//img")[0].set("alt", caption)
        translated = figure_text.get(key, figure_text.get(str(number)))
        if translated:
            wrapper = etree.SubElement(figure, "div", {"class": "figure-translation", "lang": "ko"})
            replace_inner_html(wrapper, translated)


OFFLINE_CSS = """
/* Offline repairs: system Korean fonts and the captured header's scroll state. */
html, body { min-width: 0; }
.typography { --font-family-body: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif; }
.typography .body, .typography .post-title, .typography .subtitle,
.typography .body h1, .typography .body h2, .typography .body h3 {
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  word-break: keep-all; overflow-wrap: anywhere;
}
.mainMenuContent-DME8DR { position: relative !important; top: 0 !important; }
.image-link { cursor: default !important; }
.body figure img { max-width: 100%; height: auto; }
.body figcaption { font-size: 14px; line-height: 1.6; margin-top: 10px; color: #666; }
.figure-translation { margin: 20px 0; font-size: 16px; line-height: 1.7; }
.figure-translation table { width: 100%; border-collapse: collapse; font-size: 14px; }
.figure-translation th, .figure-translation td { border: 1px solid #ddd; padding: 10px; text-align: left; vertical-align: top; }
@media (max-width: 600px) {
  .main-menu .buttonsContainerContainer-ThaN_w { display: none; }
  .main-menu .logoContainer-p12gJb { flex: 0 0 40px !important; }
  .main-menu .titleContainer-DJYq5v { flex: 1 1 auto !important; min-width: 0; }
  .main-menu .titleWithWordmark-GfqxEZ img { width: 100%; height: auto !important; max-height: 36px; object-fit: contain; }
  .body figure { margin-left: 0; margin-right: 0; }
  .figure-translation { overflow-x: auto; }
}
"""


def build(preview=False, output=None):
    WORK.mkdir(parents=True, exist_ok=True)
    parser = html.HTMLParser(encoding="utf-8", huge_tree=True)
    tree = html.parse(str(SOURCE), parser=parser)
    source_hash = digest(SOURCE)
    records, by_source = copy_assets(tree)
    translations = read_translations(preview)
    translate(tree, translations)
    prune_chrome(tree)
    inventory, stylesheets = inline_styles(tree)
    metadata = apply_metadata(tree)
    annotate_figures(tree)
    sanitize_dom(tree, by_source)
    style = etree.SubElement(tree.xpath("//head")[0], "style")
    style.text = OFFLINE_CSS
    output = Path(output) if output else (WORK / "preview.html" if preview else DESTINATION)
    output.parent.mkdir(parents=True, exist_ok=True)
    tree.write(str(output), encoding="utf-8", method="html", doctype="<!DOCTYPE html>")
    manifest = {
        "source_html": str(SOURCE.relative_to(ROOT)),
        "source_sha256": source_hash,
        "source_url": SOURCE_URL,
        "output_html": str(output.relative_to(ROOT)),
        "output_bytes": output.stat().st_size,
        "metadata": metadata,
        "translation_blocks_expected": 182,
        "translation_blocks_applied": len(translations),
        "article_figures": 25,
        "saved_images": len(records),
        "animated_images": sum(record["animated"] for record in records),
        "scope": "Original publication header, article title/byline/date, complete article body. Comments, recommendations, subscription/account controls, contributor footer and active widgets removed.",
        "offline_changes": ["Saved stylesheets embedded in original order.", "Uncaptured fonts and unused CSS resources disabled; system Korean fonts used.", "All visible images embedded with their original bytes; all 47 saved images copied byte-for-byte to assets.", "Captured scripts, trackers, frames and event handlers removed.", "Original article hyperlinks retained; image navigation and remote srcset removed.", "Source header position repaired after capture while scrolled."],
        "stylesheets": stylesheets,
        "disabled_css_resources": inventory,
        "assets": records,
    }
    (WORK / "assets-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    if digest(SOURCE) != source_hash:
        raise AssertionError("Source HTML changed during build")
    body = tree.xpath(BODY_XPATH)[0]
    assert len(body.xpath(".//figure")) == 25
    assert len(body.xpath('.//*[@data-source-block]')) == 182
    assert not tree.xpath("//script|//iframe|//link|//*[@srcset]")
    print(json.dumps({"output": str(output.relative_to(ROOT)), "bytes": output.stat().st_size, "images_copied": len(records), "figures": 25, "translations": len(translations), "css_resources_disabled": len(inventory)}, ensure_ascii=False))


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--preview", action="store_true", help="Allow incomplete translations and write a staged preview.")
    argument_parser.add_argument("--output", type=Path, help="Override the output HTML path.")
    arguments = argument_parser.parse_args()
    build(preview=arguments.preview, output=arguments.output)
