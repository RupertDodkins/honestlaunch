from __future__ import annotations

import html as html_lib
import re
from html.parser import HTMLParser

from .schemas import SnapshotBlock, SourceSnapshot


def build_snapshot_from_html(html: str, *, source_url: str, title: str) -> SourceSnapshot:
    content_html = _select_content_region(html)
    parser = _SnapshotParser()
    parser.feed(content_html)
    parser.close()
    blocks = _postprocess_blocks(parser.blocks)
    if not blocks:
        return build_snapshot_from_text(_strip_html_to_text(content_html), source_url=source_url, title=title)
    return SourceSnapshot(title=title, source_url=source_url, source_kind="html", blocks=blocks)


def build_snapshot_from_text(text: str, *, source_url: str, title: str) -> SourceSnapshot:
    normalized = text.replace("\r\n", "\n").strip()
    blocks: list[SnapshotBlock] = []
    current_heading: str | None = None
    raw_blocks = [block.strip() for block in re.split(r"\n\s*\n+", normalized) if block.strip()]
    order = 0
    index = 0
    while index < len(raw_blocks):
        block = raw_blocks[index]
        if _is_markdown_table_row(block):
            table_lines = [block]
            index += 1
            while index < len(raw_blocks) and _is_markdown_table_row(raw_blocks[index]):
                table_lines.append(raw_blocks[index])
                index += 1
            blocks.append(
                SnapshotBlock(
                    block_id=f"block-{order}",
                    kind="table",
                    text="\n".join(table_lines),
                    section_heading=current_heading,
                    source_order=order,
                )
            )
            order += 1
            continue
        kind = "paragraph"
        text_value = block
        heading_match = re.match(r"^(#{1,6})\s+(.*)$", block)
        if heading_match:
            level = min(6, len(heading_match.group(1)))
            text_value = heading_match.group(2).strip()
            kind = f"h{level}"
            current_heading = text_value
        elif block.startswith("- "):
            kind = "li"
        blocks.append(
            SnapshotBlock(
                block_id=f"block-{order}",
                kind=kind,
                text=text_value,
                section_heading=current_heading,
                source_order=order,
            )
        )
        order += 1
        index += 1
    return SourceSnapshot(title=title, source_url=source_url, source_kind="text", blocks=blocks)


def snapshot_to_text(snapshot: SourceSnapshot) -> str:
    return "\n\n".join(block.text for block in snapshot.blocks if block.text.strip())


def _is_markdown_table_row(block: str) -> bool:
    stripped = block.strip()
    return stripped.startswith("|") and "|" in stripped[1:]


def _select_content_region(html: str) -> str:
    for tag in ("article", "main"):
        matches = re.findall(rf"(?is)<{tag}\b[^>]*>(.*?)</{tag}>", html)
        if matches:
            return max(matches, key=len)
    body_match = re.search(r"(?is)<body\b[^>]*>(.*?)</body>", html)
    if body_match:
        return body_match.group(1)
    return html


def _strip_html_to_text(html: str) -> str:
    html = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", html)
    html = re.sub(r"(?is)<br\s*/?>", "\n", html)
    html = re.sub(r"(?is)</?(p|div|li|h1|h2|h3|h4|h5|h6|blockquote|pre|section|article|main|table|tr)\b[^>]*>", "\n\n", html)
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


class _SnapshotParser(HTMLParser):
    _BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote", "pre", "table"}
    _IGNORED_TAGS = {"script", "style", "noscript", "svg", "canvas", "form"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[SnapshotBlock] = []
        self._ignore_depth = 0
        self._current_tag: str | None = None
        self._current_parts: list[str] = []
        self._current_heading: str | None = None
        self._source_order = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        tag = tag.lower()
        if tag in self._IGNORED_TAGS:
            self._ignore_depth += 1
            return
        if self._ignore_depth:
            return
        if tag == "br" and self._current_parts is not None:
            self._current_parts.append("\n")
            return
        if tag in {"td", "th"} and self._current_tag == "table":
            if self._current_parts and not self._current_parts[-1].endswith(("| ", "\n")):
                self._current_parts.append("| ")
            return
        if tag == "tr" and self._current_tag == "table" and self._current_parts:
            if not self._current_parts[-1].endswith("\n"):
                self._current_parts.append("\n")
            return
        if tag in self._BLOCK_TAGS:
            self._finalize_block()
            self._current_tag = tag
            self._current_parts = []

    def handle_endtag(self, tag: str) -> None:  # type: ignore[override]
        tag = tag.lower()
        if tag in self._IGNORED_TAGS:
            if self._ignore_depth:
                self._ignore_depth -= 1
            return
        if self._ignore_depth:
            return
        if tag in {"td", "th"} and self._current_tag == "table":
            self._current_parts.append(" | ")
            return
        if tag == "tr" and self._current_tag == "table":
            if not self._current_parts or not self._current_parts[-1].endswith("\n"):
                self._current_parts.append("\n")
            return
        if self._current_tag == tag:
            self._finalize_block()

    def handle_data(self, data: str) -> None:  # type: ignore[override]
        if self._ignore_depth or self._current_tag is None:
            return
        if data:
            self._current_parts.append(data)

    def close(self) -> None:  # type: ignore[override]
        self._finalize_block()
        super().close()

    def _finalize_block(self) -> None:
        if self._current_tag is None:
            return
        text = _normalize_block_text("".join(self._current_parts), kind=self._current_tag)
        if text:
            block = SnapshotBlock(
                block_id=f"block-{self._source_order}",
                kind=self._current_tag,
                text=text,
                section_heading=self._current_heading,
                source_order=self._source_order,
            )
            self.blocks.append(block)
            self._source_order += 1
            if self._current_tag.startswith("h"):
                self._current_heading = text
        self._current_tag = None
        self._current_parts = []


def _normalize_block_text(text: str, *, kind: str) -> str:
    text = html_lib.unescape(text)
    if kind == "table":
        lines = []
        for line in text.splitlines():
            cleaned = re.sub(r"[ \t]+", " ", line).strip(" |")
            if cleaned:
                cells = [cell.strip() for cell in cleaned.split("|") if cell.strip()]
                lines.append(" | ".join(cells))
        return "\n".join(lines).strip()
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    return " ".join(line for line in lines if line).strip()


def _postprocess_blocks(blocks: list[SnapshotBlock]) -> list[SnapshotBlock]:
    if not blocks:
        return []
    trimmed = _drop_leading_noise(blocks)
    trimmed = _drop_preface_toc(trimmed)
    trimmed = _collapse_consecutive_duplicates(trimmed)
    trimmed = _trim_trailing_boilerplate(trimmed)
    return _reindex_blocks(trimmed)


def _drop_leading_noise(blocks: list[SnapshotBlock]) -> list[SnapshotBlock]:
    for index, block in enumerate(blocks):
        if block.kind == "h1":
            return blocks[index:]
    return blocks


def _drop_preface_toc(blocks: list[SnapshotBlock]) -> list[SnapshotBlock]:
    if not blocks:
        return blocks
    first_h2_index = next((index for index, block in enumerate(blocks) if block.kind == "h2"), len(blocks))
    scan_limit = min(first_h2_index, 18)
    index = 0
    filtered: list[SnapshotBlock] = []
    while index < len(blocks):
        if index < scan_limit and blocks[index].kind == "li":
            run_end = index
            while run_end < len(blocks) and blocks[run_end].kind == "li" and len(blocks[run_end].text) <= 100:
                run_end += 1
            run_length = run_end - index
            if run_length >= 4:
                index = run_end
                continue
        filtered.append(blocks[index])
        index += 1
    return filtered


def _collapse_consecutive_duplicates(blocks: list[SnapshotBlock]) -> list[SnapshotBlock]:
    deduped: list[SnapshotBlock] = []
    index = 0
    while index < len(blocks):
        block = blocks[index]
        run_end = index + 1
        while run_end < len(blocks):
            next_block = blocks[run_end]
            if (
                next_block.kind != block.kind
                or next_block.text != block.text
                or next_block.section_heading != block.section_heading
            ):
                break
            run_end += 1
        run_length = run_end - index
        if not (run_length >= 3 and len(block.text) <= 100):
            deduped.append(block)
        index = run_end
    return deduped


def _trim_trailing_boilerplate(blocks: list[SnapshotBlock]) -> list[SnapshotBlock]:
    if not blocks:
        return blocks
    boilerplate_patterns = (
        "one step more",
        "confirm your subscription",
        "already subscribed",
        "different email address",
        "check your inbox",
        "newsletter",
    )
    start_index = max(0, int(len(blocks) * 0.6))
    for index, block in enumerate(blocks[start_index:], start=start_index):
        text = block.text.lower()
        if any(pattern in text for pattern in boilerplate_patterns):
            return blocks[:index]
    return blocks


def _reindex_blocks(blocks: list[SnapshotBlock]) -> list[SnapshotBlock]:
    reindexed: list[SnapshotBlock] = []
    for order, block in enumerate(blocks):
        reindexed.append(
            SnapshotBlock(
                block_id=f"block-{order}",
                kind=block.kind,
                text=block.text,
                section_heading=block.section_heading,
                source_order=order,
            )
        )
    return reindexed
