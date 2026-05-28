from __future__ import annotations

from pathlib import Path

from honestlaunch.claims import _mock_claims
from honestlaunch.numeric import calibrate_numeric_claim


def main() -> None:
    document = Path("examples/demo_document.md").read_text(encoding="utf-8")
    calibration = calibrate_numeric_claim(document, _mock_claims()[0])
    if calibration is None:
        raise SystemExit("Expected numeric calibration for demo claim.")
    joined = "\n".join(calibration.findings)
    if "3.2 percentage points" not in joined:
        raise SystemExit(f"Missing absolute gain finding:\n{joined}")
    if "3.8%" not in joined:
        raise SystemExit(f"Missing relative gain finding:\n{joined}")
    print("numeric calibration ok")


if __name__ == "__main__":
    main()
