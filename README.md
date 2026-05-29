# HonestLaunch

Grounded adversarial claim audit for dense expert documents.

HonestLaunch reads an AI model report, paper, technical blog post, or other dense expert document, extracts the riskiest factual claims, then dispatches specialist verifier agents to produce an audited launch page plus a structured evidence ledger.

It is not a paper summarizer. The primary output is an audited page view that preserves the source structure, substitutes overstated copy inline, and shows the original wording plus citations on hover or tap. The secondary surface is the claim ledger: original wording, formal verdict, evidence contrast against references, collapsible agent steps, supporting evidence found, contradictions or narrowing evidence, missing context, computed checks when relevant, and the strongest defensible rewrite.

## Current Archive Shape

The current public-facing direction is a reviewed static archive of audited launch pages, not an open live-generation product.

Browse the archive locally:

```bash
cd /Users/rupert/engineering/honestlaunch
python3 -m http.server 8765
```

Then open:

- `http://127.0.0.1:8765/`
- `http://127.0.0.1:8765/examples/index.html`
- `http://127.0.0.1:8765/examples/methodology.html`

The first canonical archive set is:

- Google
- Anthropic
- OpenAI
- xAI

Archive maintenance commands:

```bash
source .venv/bin/activate
python scripts/rebuild_archive.py
python scripts/evaluate_archive.py
```

This rebuilds the featured HTML reports, refreshes archive metadata and evidence-packet sidecars, and writes the current archive-quality score under `docs/temporary/`.

## Hackathon Submission

HonestLaunch was built as a submission to the [Google I/O Hackathon](https://cerebralvalley.ai/e/google-io-hackathon), hosted by Cerebral Valley with the Google DeepMind team.

It was originally submitted under the name `CappinCheck`, before the project was rebranded to `HonestLaunch`.

The project was shaped around the event prompt for Gemini 3.5 Flash: build something new for the agentic era that benefits from fast, low-cost multi-step reasoning. Rather than shipping another chat interface or RAG wrapper, HonestLaunch uses parallel Gemini specialist agents to audit dense public AI model reports and launch posts, compare claims against references, and rewrite overstated claims into wording that is still strong but actually defensible.

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
cd /Users/rupert/engineering/honestlaunch
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the no-key demo:

```bash
honestlaunch audit examples/demo_document.md --mock --profile --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
open examples/demo_report.html
```

For the archive shell, open `examples/index.html` after generating or refreshing artifacts.

The deterministic fixture is `examples/demo_document.md`; use `--mock` for public demos when API access is unavailable or live grounding is flaky.

Run the no-key Evidence Contrast demo:

```bash
honestlaunch audit examples/demo_document.md --mock --contrast --contrast-top 2 --profile --out examples/contrast_demo.md --json examples/contrast_demo.json --html examples/contrast_demo.html
open examples/contrast_demo.html
```

Run with Gemini:

```bash
export GEMINI_API_KEY=...
honestlaunch audit examples/demo_document.md --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
```

Run Evidence Contrast against explicit reference URLs:

```bash
honestlaunch audit examples/demo_document.md \
  --contrast \
  --reference https://ai.google.dev/gemini-api/docs/models \
  --profile \
  --contrast-top 2 \
  --out examples/contrast_live.md \
  --json examples/contrast_live.json \
  --html examples/contrast_live.html
```

V1 uses explicit `--reference` URLs for reliability. Automatic reference discovery is intentionally deferred.

For a real/public source placeholder that avoids copying copyrighted text into the repo, see `examples/real_public_example.md`.

## Demo Script

1. Run the deterministic mock command above.
2. Open `examples/demo_report.html`.
3. Start on the audited launch page: underline styling, hover/tap tooltip, original wording, and explicit-reference citations.
4. Switch to the claim ledger to show formal verdict, Evidence Contrast, Evidence Sources, Agent Steps, missing context, and rewrite.
5. Highlight the numeric contrast row: the source says `84.1%` to `87.3%`, so the defensible improvement is `3.2` points / `3.8%` relative, not `30%`.
6. If `GEMINI_API_KEY` is available, rerun with `--contrast --reference ...` and compare the live grounded report to the deterministic fallback.

## Output

Each audited claim includes:

- Primary audited-page rendering with inline substitutions
- Hover/tap tooltip showing original wording, verdict, and explicit-reference citations
- Original claim
- Claim type
- Formal verdict: `supported`, `overstated`, `missing_context`, `contradicted`, or `not_checkable`
- Verdict definitions:
  - `supported`: available evidence supports the claim as written or with only minor caveats.
  - `overstated`: evidence points in the same direction, but the wording is stronger, broader, or more certain than supported.
  - `missing_context`: the claim may be true, but key scope, baseline, methodology, source, or denominator context is missing.
  - `contradicted`: available evidence conflicts with the claim as written.
  - `not_checkable`: available sources do not provide enough evidence to verify or falsify the claim.
- Stretch score from `0` to `100`
- Evidence Contrast against explicit reference URLs when `--contrast` is enabled
- Evidence Sources split into provided references, Gemini-discovered supporting sources, Gemini-discovered caveat/counter sources, snippets, and mismatch notes
- Agent Steps showing the verifier, contradiction-finder, numeric-calibrator, and aggregator outputs
- Run telemetry covering pipeline wall time, per-claim timing, and per-agent timing
- Supporting evidence found
- Contradictions / narrowing evidence
- Missing context
- Computed checks when the claim has quantities, percentages, units, or table math to verify
- Strongest defensible rewrite

## Evidence Contrast Mode

Evidence Contrast Mode compares selected claims against user-provided reference URLs with URL Context and renders a side-by-side contrast card:

```text
Claim says: ...
Best source says: ...
Delta: narrower_than_claim / missing_context / contradicted / not_checkable
Defensible rewrite: ...
```

This is documented in `DEMO_EXTENSION_PLAN.md`. Evidence Contrast Mode is the intended answer to "show me exactly where the claim differs from existing docs."

Report layout:

- `Audited Launch Page`: the primary surface, preserving source block structure while substituting audited claims inline with hover/tap receipts.
- `Evidence Contrast`: the demo-facing side-by-side card: claim wording, reference wording, delta, final verdict, and defensible rewrite.
- `Audit Ledger`: the secondary inspection/debug surface showing verdicts, contrast, sources, and agent steps.
- `Evidence Sources`: separates explicit user-provided references from Gemini-discovered supporting and caveat/counter sources, with snippets and mismatch notes underneath for inspection.

Reference discovery with Google Search grounding is a v2 extension. The first version prioritizes explicit `--reference` URLs for demo reliability.

## Limitations

HonestLaunch does not prove that a paper is true or false. It identifies claims whose wording may outrun the available evidence. It should be used as a triage and review aid, not as an authority.

The default runtime is local async Gemini execution over repo-local skill files. The experimental managed runtime is implemented but not demo-safe in this environment; see `RUNTIME.md`. Live output depends on model availability, tool support, and grounding quality. The `--mock` path is intentionally deterministic so public demos can run without secrets or network access.
