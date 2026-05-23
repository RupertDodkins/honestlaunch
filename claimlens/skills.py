from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_skill(name: str) -> str:
    path = ROOT / "skills" / name / "SKILL.md"
    return path.read_text(encoding="utf-8")

