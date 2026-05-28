from __future__ import annotations

import html as html_lib
import re
from pathlib import Path

import httpx
from pypdf import PdfReader

from .schemas import Document
from .source_snapshot import build_snapshot_from_html, build_snapshot_from_text, snapshot_to_text


def load_document(source: str) -> Document:
    if source.startswith(("http://", "https://")):
        response = httpx.get(source, follow_redirects=True, timeout=30)
        response.raise_for_status()
        content_type = response.headers.get("content-type", "")
        if "pdf" in content_type or source.lower().endswith(".pdf"):
            text = _read_pdf_bytes(response.content)
            title = _infer_title(text, source)
            snapshot = build_snapshot_from_text(text, source_url=source, title=title)
        else:
            title = _html_title(response.text) or source
            snapshot = build_snapshot_from_html(response.text, source_url=source, title=title)
            text = snapshot_to_text(snapshot)
            title = title if title != source else _infer_title(text, source)
        return Document(title=title, source=source, text=text, snapshot=snapshot)

    path = Path(source)
    if path.suffix.lower() == ".pdf":
        text = _read_pdf_path(path)
        snapshot = build_snapshot_from_text(text, source_url=str(path), title=_infer_title(text, path.name))
    else:
        text = path.read_text(encoding="utf-8")
        snapshot = build_snapshot_from_text(text, source_url=str(path), title=_infer_title(text, path.name))
    return Document(title=_infer_title(text, path.name), source=str(path), text=text, snapshot=snapshot)


def _read_pdf_path(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n\n".join(page.extract_text() or "" for page in reader.pages)


def _read_pdf_bytes(content: bytes) -> str:
    tmp = Path("/tmp/honestlaunch-input.pdf")
    tmp.write_bytes(content)
    return _read_pdf_path(tmp)


def _strip_html(html: str) -> str:
    html = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", html)
    html = re.sub(r"(?is)<br\s*/?>", "\n", html)
    block_tags = (
        "article|aside|blockquote|div|figcaption|figure|footer|form|h1|h2|h3|h4|h5|h6|"
        "header|hr|li|main|nav|ol|p|pre|section|table|tbody|td|th|thead|tr|ul"
    )
    html = re.sub(rf"(?is)</?(?:{block_tags})\b[^>]*>", "\n\n", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    text = html_lib.unescape(text)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    cleaned: list[str] = []
    previous_blank = False
    for line in lines:
        if not line:
            if not previous_blank and cleaned:
                cleaned.append("")
            previous_blank = True
            continue
        cleaned.append(line)
        previous_blank = False
    return "\n".join(cleaned).strip()


def _html_title(html: str) -> str | None:
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", html)
    if not match:
        return None
    title = _strip_html(match.group(1))
    return html_lib.unescape(title).strip() or None


def _infer_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip("# \t")
        if len(stripped) >= 8:
            return stripped[:120]
    return fallback
