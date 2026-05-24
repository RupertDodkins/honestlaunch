#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


INDEX_PATH = Path(__file__).resolve().parents[1] / "examples" / "index.html"
ANCHOR = """      {
        label: 'Careful Scientific Claim',
"""


def js_string(value: str) -> str:
    return json.dumps(value)


def build_entry(label: str, badge: str, href: str, summary: str, command: str) -> str:
    return (
        "      {\n"
        f"        label: {js_string(label)},\n"
        f"        badge: {js_string(badge)},\n"
        f"        href: {js_string(href)},\n"
        f"        summary: {js_string(summary)},\n"
        f"        command: {js_string(command)}\n"
        "      },\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Register a generated report in examples/index.html.")
    parser.add_argument("--label", required=True)
    parser.add_argument("--badge", required=True)
    parser.add_argument("--href", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--command", required=True)
    args = parser.parse_args()

    content = INDEX_PATH.read_text(encoding="utf-8")
    if f'href: "{args.href}"' in content or f"href: '{args.href}'" in content:
        print(f"{args.href} is already registered in {INDEX_PATH}")
        return 0

    if ANCHOR not in content:
        print(f"Could not find insertion anchor in {INDEX_PATH}", file=sys.stderr)
        return 1

    entry = build_entry(args.label, args.badge, args.href, args.summary, args.command)
    updated = content.replace(ANCHOR, entry + ANCHOR, 1)
    INDEX_PATH.write_text(updated, encoding="utf-8")
    print(f"Registered {args.label} in {INDEX_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
