# ClaimLens

Grounded adversarial claim audit for dense expert documents.

ClaimLens reads a paper, model report, technical blog post, or other dense expert document, extracts the riskiest factual claims, then dispatches specialist verifier agents to decide whether each claim is no cap, sus, cap, or needs receipts.

It is not a paper summarizer. The output is a claim ledger: original wording, formal verdict, evidence, counter-evidence, cap score, and the strongest defensible rewrite.

## Why Gemini 3.5 Flash

Before Gemini 3.5 Flash and Managed Agents, running multiple grounded subagents in parallel sandboxes, each browsing the web, executing code, and grading a single claim, would have cost dollars and minutes per audit. Today it costs cents and seconds, which is what makes a live claim ledger possible.

This repo is structured around agent skills:

- `skills/verifier/SKILL.md`: finds support and primary evidence.
- `skills/contradiction-finder/SKILL.md`: finds caveats, contrary evidence, and missing context.
- `skills/numeric-calibrator/SKILL.md`: checks percentages, deltas, units, and table math.
- `skills/claim-aggregator/SKILL.md`: turns evidence into verdicts and rewrites.

The initial implementation includes a local async runner that loads those same skills. It can be swapped for Managed Agents / Interactions API without changing the public artifact.

## Quickstart

```bash
cd /Users/rupert/engineering/claimlens
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the no-key demo:

```bash
claimlens audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
open examples/demo_report.html
```

Run with Gemini:

```bash
export GEMINI_API_KEY=...
claimlens audit examples/demo_document.md --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
```

## Output

Each audited claim includes:

- Original claim
- Claim type
- Formal verdict: `supported`, `overstated`, `missing_context`, `contradicted`, or `not_checkable`
- Vibe verdict: `no cap`, `mostly no cap`, `sus`, `cap`, or `needs receipts`
- Cap score from `0` to `100`
- Supporting evidence
- Counter-evidence and missing context
- Strongest defensible rewrite

## Safety and Scope

ClaimLens does not prove that a paper is true or false. It identifies claims whose wording may outrun the available evidence. It should be used as a triage and review aid, not as an authority.

