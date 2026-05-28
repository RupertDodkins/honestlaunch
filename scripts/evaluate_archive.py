from __future__ import annotations

import json
from pathlib import Path

from honestlaunch.archive_quality import archive_scorecard, improvement_recommendations, write_scorecard_markdown


ROOT = Path(__file__).resolve().parents[1]
GOLD_SET = ROOT / "evaluations" / "gold_set_seed.json"
OUTPUT_MD = ROOT / "docs" / "temporary" / "archive-quality-score.md"
OUTPUT_JSON = ROOT / "docs" / "temporary" / "archive-quality-score.json"


def main() -> None:
    scorecard = archive_scorecard(ROOT, GOLD_SET)
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    write_scorecard_markdown(scorecard, OUTPUT_MD)
    payload = {
        **scorecard,
        "recommendations": improvement_recommendations(scorecard),
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"overall={scorecard['overallScore']}/100")
    for key, value in scorecard["categories"].items():
        print(f"{key}={value}/100")
    print(f"gold_set_reviewed={scorecard['goldSet']['reviewedCount']}")


if __name__ == "__main__":
    main()
