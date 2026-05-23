# CappinCheck

Grounded adversarial claim audit for dense expert documents.

CappinCheck reads a paper, model report, technical blog post, or other dense expert document, extracts the riskiest factual claims, then dispatches specialist verifier agents to produce a structured evidence ledger.

It is not a paper summarizer. The output is a claim ledger: original wording, formal verdict, supporting evidence found, contradictions or narrowing evidence, missing context, numeric findings, and the strongest defensible rewrite.

## Why Low-Latency Gemini

Before low-latency Gemini models, running multiple grounded specialist passes over the same document would have cost dollars and minutes per audit. Today it can be fast enough for a live claim ledger.

This repo is structured around agent skills:

- `skills/verifier/SKILL.md`: finds support and primary evidence.
- `skills/contradiction-finder/SKILL.md`: finds caveats, contrary evidence, and missing context.
- `skills/numeric-calibrator/SKILL.md`: checks percentages, deltas, units, and table math.
- `skills/claim-aggregator/SKILL.md`: turns evidence into verdicts and rewrites.

The supported default implementation is a local async Gemini runner that loads those same `SKILL.md` files. An experimental `--runtime managed` path uses Google GenAI Interactions; see `RUNTIME.md` for the runtime boundary and caveats.

## Quickstart

```bash
cd /Users/rupert/engineering/cappincheck
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the no-key demo:

```bash
cappincheck audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
open examples/demo_report.html
```

The deterministic fixture is `examples/demo_document.md`; use `--mock` for public demos when API access is unavailable or live grounding is flaky.

Run with Gemini:

```bash
export GEMINI_API_KEY=...
cappincheck audit examples/demo_document.md --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
```

Run the experimental managed runtime:

```bash
cappincheck audit examples/demo_document.md --runtime managed --limit 1 --out examples/managed_report.md --json examples/managed_report.json --html examples/managed_report.html
```

For a real/public source placeholder that avoids copying copyrighted text into the repo, see `examples/real_public_example.md`.

## Demo Script

1. Run the deterministic mock command above.
2. Open `examples/demo_report.html`.
3. Point out the claim ledger: formal verdict, supporting evidence found, contradictions/narrowing evidence, missing context, and rewrite.
4. Highlight the numeric calibration row: the source says `84.1%` to `87.3%`, so the defensible improvement is `3.2` points / `3.8%` relative, not `30%`.
5. If `GEMINI_API_KEY` is available, rerun without `--mock` and compare the live grounded report to the deterministic fallback.

## Output

Each audited claim includes:

- Original claim
- Claim type
- Formal verdict: `supported`, `overstated`, `missing_context`, `contradicted`, or `not_checkable`
- Vibe verdict: `no cap`, `mostly no cap`, `sus`, `cap`, or `needs receipts`
- Cap score from `0` to `100`
- Supporting evidence found
- Contradictions / narrowing evidence
- Missing context
- Strongest defensible rewrite

## Planned: Evidence Contrast Mode

The current report shows evidence lists: verifier support, contradiction/narrowing evidence, and missing context. The next planned mode is sharper: for selected claims, CappinCheck will discover authoritative public sources with Google Search grounding, read those sources with URL Context, and render a side-by-side contrast card:

```text
Claim says: ...
Best source says: ...
Delta: narrower_than_claim / missing_context / contradicted / not_checkable
Defensible rewrite: ...
```

This is documented in `DEMO_EXTENSION_PLAN.md`. Evidence Contrast Mode is the intended answer to "show me exactly where the claim differs from existing docs."

Planned report layout:

- `Evidence Contrast`: the demo-facing side-by-side card: claim wording, best source wording, delta, verdict movement, and defensible rewrite.
- `Evidence Stack`: the raw support, contradiction/narrowing evidence, and missing-context trails underneath for inspection.

## Limitations

CappinCheck does not prove that a paper is true or false. It identifies claims whose wording may outrun the available evidence. It should be used as a triage and review aid, not as an authority.

The default runtime is local async Gemini execution over repo-local skill files. The experimental managed runtime depends on beta Interactions API availability and JSON normalization from managed interaction output. Live output depends on model availability, tool support, and grounding quality. The `--mock` path is intentionally deterministic so public demos can run without secrets or network access.
