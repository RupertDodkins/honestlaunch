from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/verify_contrast.py <report.json>")
    path = Path(sys.argv[1])
    report = json.loads(path.read_text(encoding="utf-8"))
    audits = report.get("audits", [])
    contrasted = [audit for audit in audits if audit.get("contrast")]
    if not contrasted:
        raise SystemExit("Expected at least one contrasted claim.")
    verdicts = {audit["contrast"].get("recommended_verdict") for audit in contrasted}
    if "overstated" not in verdicts:
        raise SystemExit(f"Expected an overstated contrast verdict; saw {sorted(verdicts)}")
    rewrites = "\n".join(audit["contrast"].get("suggested_rewrite", "") for audit in contrasted)
    if "3.2" not in rewrites:
        raise SystemExit(f"Expected numeric rewrite to include 3.2:\n{rewrites}")
    if "3.8%" not in rewrites:
        raise SystemExit(f"Expected numeric rewrite to include 3.8%:\n{rewrites}")
    missing_sources = [audit["claim"]["id"] for audit in contrasted if not audit["contrast"].get("reference_sources")]
    if missing_sources:
        raise SystemExit(f"Contrasted claims missing reference sources: {missing_sources}")
    print("evidence contrast ok")


if __name__ == "__main__":
    main()
