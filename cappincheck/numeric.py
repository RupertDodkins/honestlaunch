from __future__ import annotations

import re
from dataclasses import dataclass

from .schemas import RiskyClaim


@dataclass(frozen=True)
class NumericCalibration:
    findings: list[str]
    suggested_rewrite: str | None = None


def calibrate_numeric_claim(document_text: str, claim: RiskyClaim) -> NumericCalibration | None:
    """Handle stable numeric-table checks without pretending to understand prose broadly."""
    if not _looks_numeric(claim.claim):
        return None

    values = _extract_markdown_percent_rows(document_text)
    if len(values) < 2:
        return None

    baseline_label, baseline = values[0]
    method_label, method = values[-1]
    absolute = method - baseline
    if baseline == 0:
        return None
    relative = (absolute / baseline) * 100

    findings = [
        f"Detected benchmark rows: {baseline_label} = {baseline:.1f}%, {method_label} = {method:.1f}%.",
        f"Absolute gain: {method:.1f} - {baseline:.1f} = {absolute:.1f} percentage points.",
        f"Relative gain: ({absolute:.1f} / {baseline:.1f}) * 100 = {relative:.1f}%.",
    ]

    claimed = _extract_claimed_percent(claim.claim)
    if claimed is not None:
        gap = abs(claimed - relative)
        findings.append(
            f"Claimed improvement is {claimed:.1f}%; computed relative improvement is {relative:.1f}% "
            f"(difference {gap:.1f} points)."
        )

    rewrite = (
        f"{method_label} improves from {baseline:.1f}% to {method:.1f}% versus {baseline_label}, "
        f"a {absolute:.1f}-point absolute gain and {relative:.1f}% relative improvement."
    )
    return NumericCalibration(findings=findings, suggested_rewrite=rewrite)


def _looks_numeric(text: str) -> bool:
    return bool(re.search(r"\d+(?:\.\d+)?\s*%", text))


def _extract_claimed_percent(text: str) -> float | None:
    match = re.search(r"(?:improves?|improvement|outperforms?)[^.\n]{0,40}?(\d+(?:\.\d+)?)\s*%", text, re.I)
    return float(match.group(1)) if match else None


def _extract_markdown_percent_rows(text: str) -> list[tuple[str, float]]:
    rows: list[tuple[str, float]] = []
    for line in text.splitlines():
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 2:
            continue
        if set(parts[0]) <= {"-", ":"}:
            continue
        match = re.fullmatch(r"(\d+(?:\.\d+)?)\s*%", parts[-1])
        if match:
            rows.append((parts[0], float(match.group(1))))
    return rows

