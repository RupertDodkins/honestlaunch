# CappinCheck Demo Extension Plan

This plan supersedes the broad outstanding-work list for the next hackathon phase. The goal is to make the current project land in a live Google I/O / DeepMind demo: credible on real input, Gemini-native, and reliable under time pressure.

## Current Baseline

CappinCheck is a CLI-first open-source tool that audits AI model reports, dense technical/scientific documents, and technical blog posts for claims that may outrun the evidence. It extracts risky claims, runs specialist verifier/skeptic/numeric-calibrator passes, and emits Markdown, JSON, and static HTML reports.

Already present or in progress:

- `skills/*/SKILL.md` role files for verifier, contradiction finder, numeric calibrator, and aggregator.
- Local async Gemini runtime as the supported default.
- Experimental `--runtime managed` path with caveats documented in `RUNTIME.md`.
- Deterministic `--mock` path for no-network demos.
- Live Gemini path with Google Search, URL Context, Code Execution, and structured JSON repair.
- Numeric calibration for the planted `84.1% -> 87.3%` / `30% improvement` demo.
- Static HTML dashboard with filters/source rendering.

Current evidence behavior:

- The verifier searches for and returns `supporting_evidence`.
- The contradiction finder searches for and returns `counter_evidence` plus `missing_context`.
- The report renders these as evidence lists in the right-side evidence stack.
- This is useful, but it is not yet an explicit side-by-side source comparison.

## Product Decision

Build **Evidence Contrast Mode** before any broader Claim Drift mode.

Rationale:

- It strengthens the existing `audit` workflow instead of adding a second product surface.
- It makes URL Context central to the demo, with Google Search grounding reserved for a later source-discovery extension.
- It is lower risk than cross-surface claim drift while still providing the same core moment: "the claim says X; the best source actually supports narrower Y."
- It is easier to pair with one real public demo document.

Do not build File Search integration, hosted UI, auth, database, chat interface, or a full Managed Agents migration in this phase.

## Demo Risks To Fix First

### 1. Branding Posture

Risk: playful labels can make the tool feel unserious in front of research-heavy judges.

Decision:

- Keep the project name `CappinCheck`.
- Lead reports with formal labels: `Formal Verdict`, `Confidence`, `Evidence`, `Delta`, and `Defensible Rewrite`.
- Remove playful labels from the demo report and JSON schema.
- Use `stretch_score` for the numeric severity measure.

Acceptance criteria:

- HTML selected-claim view shows one reader-facing source of truth: formal verdict, confidence, reason, evidence, and rewrite.
- Markdown report sections start with formal verdict and explanation.
- README demo language emphasizes claim audit, evidence contrast, and defensible rewrites.

### 2. Real Public Demo Target

Risk: the current synthetic demo can look planted.

Decision:

- Keep `examples/demo_document.md` as deterministic fallback.
- Add one real public demo source or source excerpt only if redistribution is clearly public-safe.
- Prefer a real source with one clear numeric, benchmark, generalization, or limitation stretch.
- If full text licensing is unclear, store only the URL, notes, and generated public report.

Acceptance criteria:

- A real/public report exists, even if generated from URL-derived notes rather than copied paper text.
- The report has at least one row that is visually strong in 15 seconds.
- The demo can fall back to the deterministic fixture without changing commands dramatically.

## Evidence Contrast Mode

Evidence Contrast Mode is the explicit "claim vs existing docs" feature. It should not merely add more evidence snippets. It should show, for each selected claim, the contrast between the document wording and the best available source wording.

### User Experience

Add optional flags to the existing audit command. V1 should use explicit reference URLs:

```bash
cappincheck audit examples/evidence_contrast_demo.md \
  --mock \
  --contrast \
  --reference https://example.com/reference-1 \
  --reference https://example.com/reference-2 \
  --contrast-top 3 \
  --out examples/contrast_demo.md \
  --json examples/contrast_demo.json \
  --html examples/contrast_demo.html
```

Live path:

```bash
cappincheck audit <public-url-or-file> \
  --contrast \
  --reference https://example.com/model-card \
  --reference https://example.com/paper-or-benchmark \
  --contrast-top 2 \
  --out examples/contrast_live.md \
  --json examples/contrast_live.json \
  --html examples/contrast_live.html
```

Do not add a `--live` flag. Non-mock mode is already live.

V2 can add automatic source discovery:

```bash
cappincheck audit <public-url-or-file> --contrast --discover-references
```

Do not build `--discover-references` until explicit `--reference` mode is complete and demo-stable.

### What It Does

For the top risky claims, Evidence Contrast Mode:

1. Uses user-provided `--reference` URLs as the source-of-truth candidates.
2. Reads selected source URLs with URL Context.
3. Compares the exact claim wording against those sources.
4. Adds an evidence contrast card under each selected claim.

Reference discovery with Google Search grounding is a later extension, not v1.

The contrast card answers:

- What did the document claim?
- What did the best source actually say?
- Is the source narrower, broader, contradictory, or not checkable?
- What is the safest defensible rewrite?

Final report layout should have two layers:

1. `Evidence Contrast`: the demo-facing side-by-side card that explains the claim/reference delta in one glance.
2. `Sources Checked`: expandable reference URLs, snippets, and mismatch notes underneath for auditability.

Example card shape:

```text
Claim says:
"Our method generalizes across real-world domains."

Best source says:
"Evaluated on three curated benchmark datasets."

Delta:
The claim generalizes benchmark evidence into real-world deployment language.

Verdict:
overstated / missing_context

Defensible rewrite:
"The method improved performance on three curated benchmarks; real-world deployment was not tested."
```

### Schema

Add schemas similar to:

```json
{
  "claim_id": "string",
  "claim_text": "string",
  "reference_sources": [
    {
      "url": "string",
      "title": "string",
      "source_type": "official_doc|paper|standard|dataset|benchmark|government|academic|vendor_doc|blog|unknown",
      "why_relevant": "string",
      "authority_score": 0
    }
  ],
  "contrast": {
    "best_sources": [
      {
        "url": "string",
        "title": "string",
        "stance": "supports|narrows|contradicts|irrelevant|unclear",
        "evidence_summary": "string",
        "key_qualification": "string"
      }
    ],
    "delta_type": "same|narrower_than_claim|broader_than_claim|missing_context|contradicted|not_checkable",
    "delta_explanation": "string",
    "suggested_rewrite": "string",
    "recommended_verdict": "supported|overstated|missing_context|contradicted|not_checkable",
    "confidence": "low|medium|high"
  }
}
```

Keep the schema shallow. Do not model full source graphs in this phase.

### Prompt Contract

Contrast prompt:

```text
Compare the exact claim wording against the provided reference URLs.
Focus on scope, quantity, causality, benchmark conditions, dates/versioning, uncertainty language, and missing qualifiers.
The task is not to prove universal truth. The task is to decide whether the selected sources support this claim as written.
Return JSON only.
```

### Verdict Rules

- The reader-facing report should show one final formal verdict per claim.
- Internally, raw JSON may preserve pre-contrast audit metadata for debugging, but the UI should not show `audit verdict -> contrast verdict` as the main story.
- If contrast is `not_checkable`, do not worsen the final verdict unless the existing audit was also weak.
- If delta is `narrower_than_claim`, map contrast verdict to `overstated` or `missing_context`.
- If delta is `contradicted`, map contrast verdict to `contradicted`.
- Do not hide uncertainty.

### Rendering Requirements

In Markdown and HTML, each contrasted claim should show an `Evidence Contrast` section before the raw evidence lists:

- Claim
- Best reference says
- Delta type and explanation
- Final formal verdict
- Defensible rewrite

The raw `Sources Checked` section should remain underneath and show:

- Reference URLs/titles
- Relevant snippets
- What each reference supports, narrows, contradicts, or leaves unchecked

The report must remain static. No hosted app.

## Implementation Order

### Phase 0: Preserve The Baseline

Before changes:

```bash
source .venv/bin/activate
python -m compileall cappincheck
cappincheck audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
python scripts/verify_numeric.py
```

Done when all commands exit `0`.

### Phase 1: Branding/Demo Posture Fix

Tasks:

- Update report ordering so formal verdict/confidence/reason are the primary reader-facing source of truth.
- Remove playful labels from the main demo view and generated JSON.
- Update README copy if it currently leads with informal terminology.

Verification:

```bash
cappincheck audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
open examples/demo_report.html
```

Manual check: selected claim view reads as a serious audit report.

### Phase 2: Contrast Schemas And Mock Fixture

Tasks:

- Add contrast-related schema classes.
- Add `--contrast`, `--contrast-top`, and repeatable `--reference`.
- Add deterministic mock contrast output.
- Add `examples/evidence_contrast_demo.md` if useful.

Verification:

```bash
cappincheck audit examples/demo_document.md --mock --contrast --contrast-top 2 --out examples/contrast_demo.md --json examples/contrast_demo.json --html examples/contrast_demo.html
```

Done when JSON includes contrast results and HTML renders contrast cards.

### Phase 3: Live Evidence Contrast

Tasks:

- Add contrast verification pass using URL Context over provided `--reference` URLs.
- Degrade gracefully when no reference URL is supplied or a reference cannot be read.
- Keep Search-based `--discover-references` as a documented v2 deferral unless the explicit-reference path is finished early.

Verification:

```bash
CAPPINCHECK_TIMEOUT_SECONDS=90 cappincheck audit examples/demo_document.md --contrast --reference https://example.com/reference --contrast-top 1 --out examples/contrast_live.md --json examples/contrast_live.json --html examples/contrast_live.html
```

Done when the command exits `0` and the report includes at least one live contrast card.

### Phase 4: Real Public Example

Tasks:

- Pick a public source with a strong, easily explainable claim stretch.
- Prefer URL-based input or public-safe excerpts/notes.
- Generate a stable report.
- Commit only public-safe artifacts.

Verification:

- The report has one row that can be explained in under 15 seconds.
- The row includes claim, evidence/source, delta, and rewrite.
- The deterministic mock remains available as fallback.

### Phase 5: Demo Rehearsal

Prepare three paths:

- Primary: real public contrast report.
- Fallback 1: live or pre-generated audit report.
- Fallback 2: deterministic synthetic numeric report.

Verification:

```bash
cappincheck audit examples/demo_document.md --mock --contrast --contrast-top 2 --out examples/contrast_demo.md --json examples/contrast_demo.json --html examples/contrast_demo.html
open examples/contrast_demo.html
```

Demo can be completed in 90 seconds.

## Explicit Deferrals

Do not spend this phase on:

- `--discover-references` source discovery.
- Search-discovered hype maps.
- Full Claim Drift mode across multiple downstream pages.
- Citation bibliography parsing.
- File Search.
- Hosted deployment.
- Authentication.
- Database persistence.
- Broad UI rewrite.
- Full Managed Agents migration beyond the existing experimental runtime.

## Demo Framing

Use this claim:

> CappinCheck does not prove papers true or false. It turns overclaim detection into an inspectable, grounded source-comparison workflow.

Core demo sentence:

> URL Context reads the references, Code Execution or local calibration checks numbers, and structured outputs turn it into a reusable claim ledger.

Keep the serious artifact first. The playful language is garnish.
