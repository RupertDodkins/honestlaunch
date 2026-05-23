from __future__ import annotations

import re
from pathlib import Path

import httpx
from pypdf import PdfReader

from .schemas import Document


def load_document(source: str) -> Document:
    if source.startswith(("http://", "https://")):
        response = httpx.get(source, follow_redirects=True, timeout=30)
        response.raise_for_status()
        content_type = response.headers.get("content-type", "")
        if "pdf" in content_type or source.lower().endswith(".pdf"):
            text = _read_pdf_bytes(response.content)
        else:
            text = _strip_html(response.text)
        return Document(title=_infer_title(text, source), source=source, text=text)

    path = Path(source)
    if path.suffix.lower() == ".pdf":
        text = _read_pdf_path(path)
    else:
        text = path.read_text(encoding="utf-8")
    return Document(title=_infer_title(text, path.name), source=str(path), text=text)


def _read_pdf_path(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n\n".join(page.extract_text() or "" for page in reader.pages)


def _read_pdf_bytes(content: bytes) -> str:
    tmp = Path("/tmp/claimlens-input.pdf")
    tmp.write_bytes(content)
    return _read_pdf_path(tmp)


def _strip_html(html: str) -> str:
    html = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()


def _infer_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip("# \t")
        if len(stripped) >= 8:
            return stripped[:120]
    return fallback

