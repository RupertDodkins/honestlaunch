# Real Public Example

This example audits a real public AI model announcement and contrasts selected claims against an official technical reference.

Source title: Gemini 3.5: frontier intelligence with action

Source URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/

Reference URL: https://deepmind.google/models/model-cards/gemini-3-5-flash

Why it is useful: it contains benchmark, speed, cost, and enterprise-pilot claims that are public, on-theme for the hackathon, and suitable for checking against official model-card evidence.

Generated artifacts:

- `examples/gemini_35_flash_report.md`
- `examples/gemini_35_flash_report.json`
- `examples/gemini_35_flash_report.html`

Command:

```bash
source .venv/bin/activate
HONESTLAUNCH_TIMEOUT_SECONDS=90 honestlaunch audit \
  https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/ \
  --contrast \
  --reference https://deepmind.google/models/model-cards/gemini-3-5-flash \
  --contrast-top 2 \
  --limit 4 \
  --out examples/gemini_35_flash_report.md \
  --json examples/gemini_35_flash_report.json \
  --html examples/gemini_35_flash_report.html
```

Demo note: use this as the real public input example. Keep `examples/contrast_demo.html` as the deterministic no-network fallback.
