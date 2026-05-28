# Evidence Contrast Execution Plan

This is the coding-agent handoff for implementing Evidence Contrast Mode with concurrent work where safe.

Goal: add an optional `--contrast` mode to `honestlaunch audit` that compares selected claims against explicit reference URLs and renders a clear `Evidence Contrast` card plus `Sources Checked` details. V1 should not auto-discover references.

## Product Contract

Target demo domain: AI model reports and launch claims.

Reader-facing source of truth:

- One final formal verdict per claim.
- No playful verdict labels in the report or JSON schema.
- Evidence Contrast is the main demo card.
- Sources Checked is the expandable/detail layer.

V1 input model:

```bash
honestlaunch audit TARGET \
  --contrast \
  --reference REF_URL \
  --reference REF_URL \
  --contrast-top 2 \
  --out examples/contrast_live.md \
  --json examples/contrast_live.json \
  --html examples/contrast_live.html
```

V1 mock/demo model:

```bash
honestlaunch audit examples/demo_document.md \
  --mock \
  --contrast \
  --contrast-top 2 \
  --out examples/contrast_demo.md \
  --json examples/contrast_demo.json \
  --html examples/contrast_demo.html
```

Explicit deferrals:

- No `--discover-references` implementation.
- No File Search.
- No hosted UI.
- No auth/database.
- No broad Managed Agents migration.

## Dependency Graph

Serial gates:

1. Baseline smoke verification.
2. Schema/CLI contract.
3. Mock contrast generation.
4. Rendering.
5. Live contrast.
6. Real public example and demo rehearsal.

Parallel lanes after Gate 2:

- Lane A: mock fixture and gold expectations.
- Lane B: report rendering.
- Lane C: live contrast prompt/client.
- Lane D: public AI model report example research.

Merge point:

- Lanes A/B/C merge when `honestlaunch audit ... --mock --contrast ...` writes JSON/Markdown/HTML and the HTML visibly shows `Evidence Contrast` plus `Sources Checked`.

## Work Unit 0: Baseline Verification

Owner: first agent touching implementation.

Files likely touched: none.

Tasks:

- Verify current baseline before editing.
- Record failures before changing behavior.

Commands:

```bash
source .venv/bin/activate
python -m compileall honestlaunch
honestlaunch audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
python scripts/verify_numeric.py
```

Success criteria:

- All commands exit `0`.
- `examples/demo_report.html` still opens locally.
- No tracked files change unless generated report output is intentionally refreshed.

## Work Unit 1: Schema Contract

Can run concurrently with Work Unit 4 after file ownership is agreed.

Files likely touched:

- `honestlaunch/schemas.py`

Tasks:

- Add contrast schemas.
- Attach optional contrast result to `ClaimAudit`.
- Keep existing report JSON backward-compatible by making contrast optional.

Suggested model names:

- `ReferenceSource`
- `ContrastSource`
- `EvidenceContrast`

Required fields:

```text
ReferenceSource:
  url
  title
  source_type
  why_relevant
  authority_score

ContrastSource:
  url
  title
  stance
  evidence_summary
  key_qualification

EvidenceContrast:
  claim_id
  claim_text
  reference_sources
  best_sources
  delta_type
  delta_explanation
  suggested_rewrite
  recommended_verdict
  confidence
```

Enums should match `DEMO_EXTENSION_PLAN.md`:

- source type: `official_doc`, `paper`, `standard`, `dataset`, `benchmark`, `government`, `academic`, `vendor_doc`, `blog`, `unknown`
- stance: `supports`, `narrows`, `contradicts`, `irrelevant`, `unclear`
- delta type: `same`, `narrower_than_claim`, `broader_than_claim`, `missing_context`, `contradicted`, `not_checkable`

Success criteria:

- `python -m compileall honestlaunch` exits `0`.
- Existing `examples/demo_report.json` can still be generated.
- JSON output for non-contrast audits either omits contrast or has `null` contrast.

## Work Unit 2: CLI Contract

Depends on Work Unit 1.

Files likely touched:

- `honestlaunch/cli.py`
- `honestlaunch/audit.py`

Tasks:

- Add flags:
  - `--contrast`
  - repeatable `--reference`
  - `--contrast-top`, default `2`
- Pass these options into the audit pipeline.
- Do not add `--live`; non-mock means live.
- Do not add `--discover-references` in v1.

Behavior:

- If `--contrast` is absent, current behavior is unchanged.
- If `--contrast` is present with `--mock`, deterministic contrast results are attached.
- If `--contrast` is present without references in live mode, fail fast with a clear message or produce `not_checkable` contrast entries. Prefer fail-fast for CLI clarity.

Success criteria:

```bash
honestlaunch audit examples/demo_document.md --mock --contrast --contrast-top 2 --out examples/contrast_demo.md --json examples/contrast_demo.json --html examples/contrast_demo.html
```

- Command exits `0`.
- Existing command without `--contrast` still exits `0`.
- Invalid reference usage has a clear CLI error.

## Work Unit 3: Mock Contrast Fixture

Can run after Work Unit 1; can proceed in parallel with Work Unit 4.

Files likely touched:

- `honestlaunch/audit.py` or new `honestlaunch/contrast.py`
- `examples/evidence_contrast_demo.md` optional
- generated `examples/contrast_demo.*`

Tasks:

- Add deterministic contrast for at least two demo claims.
- First demo claim should use the numeric-stretch case:
  - Claim says: `30% improvement over prior work on real-world tasks`
  - Reference says: `84.1% -> 87.3% on Benchmark X`
  - Delta: numeric/scope mismatch
  - Final verdict: `overstated`
  - Suggested rewrite includes `3.2 percentage points` and `3.8% relative`
- Second demo claim should cover generalization:
  - Claim says: `robustly generalizes across domains`
  - Reference says: curated benchmark only or no deployment setting
  - Final verdict: `missing_context` or `overstated`

Success criteria:

- `examples/contrast_demo.json` includes `contrast` for selected claims.
- At least one contrast item has `recommended_verdict: "overstated"`.
- At least one contrast item has `delta_type: "narrower_than_claim"` or `missing_context`.
- Deterministic mock does not require `GEMINI_API_KEY`.

## Work Unit 4: Report Rendering

Can begin after Work Unit 1 with stub/mock contrast data.

Files likely touched:

- `honestlaunch/report.py`
- generated `examples/contrast_demo.html`
- generated `examples/contrast_demo.md`

Tasks:

- Remove playful labels from main HTML/Markdown/JSON output.
- Make formal verdict, confidence, reason, and rewrite primary.
- Add `Evidence Contrast` above raw evidence.
- Add `Sources Checked` below contrast card.
- Keep report static and embedded-data only.

HTML layout target:

```text
Selected Claim
  Formal Verdict
  Confidence
  Why
  Defensible Rewrite

Evidence Contrast
  Claim says
  Best reference says
  Delta
  Final verdict
  Defensible rewrite

Sources Checked
  URL/title
  Relevant snippet
  Supports/narrows/contradicts/unclear
```

Markdown layout target:

```markdown
## claim_id: overstated

**Confidence:** high
**Original:** ...
**Why:** ...
**Defensible rewrite:** ...

### Evidence Contrast
...

### Sources Checked
...
```

Success criteria:

- HTML visibly shows Evidence Contrast before Sources Checked.
- Main report view has no playful verdict labels.
- Markdown has no informal-label heading for claim sections.
- Existing support/counter/missing-context details remain inspectable.
- Narrow viewport does not visibly overlap text.

## Work Unit 5: Live Contrast

Depends on Work Units 1 and 2. Can run in parallel with Work Unit 4 if schemas are stable.

Files likely touched:

- new `honestlaunch/contrast.py`
- `honestlaunch/audit.py`
- `honestlaunch/gemini.py` only if a helper is needed

Tasks:

- Implement live contrast prompt using provided `--reference` URLs.
- Use URL Context via existing Gemini tool configuration.
- For each selected claim, ask Gemini to compare claim wording to the provided references.
- Return `EvidenceContrast` schema.
- Gracefully handle unreadable references:
  - mark source stance as `unclear` or contrast as `not_checkable`
  - do not crash the whole audit unless every reference fails before model call

Prompt constraints:

- The task is fidelity to the provided references, not universal truth.
- Focus on scope, benchmark conditions, causality, numeric framing, uncertainty, dates/versioning, and missing qualifiers.
- Return JSON only.

Success criteria:

```bash
HONESTLAUNCH_TIMEOUT_SECONDS=90 honestlaunch audit examples/demo_document.md \
  --contrast \
  --reference https://example.com/reference \
  --contrast-top 1 \
  --out examples/contrast_live.md \
  --json examples/contrast_live.json \
  --html examples/contrast_live.html
```

- Command exits `0` or fails with a clear reference/model error.
- Successful run includes at least one contrast result.
- `--mock --contrast` still works.
- Non-contrast live audit still works.

## Work Unit 6: Verdict Merge

Depends on Work Units 1, 3 or 5.

Files likely touched:

- `honestlaunch/audit.py`
- `honestlaunch/report.py`

Tasks:

- Produce one final reader-facing verdict.
- Internally preserve raw pre-contrast audit data if useful, but do not display `audit verdict -> contrast verdict`.
- If contrast is strong, use `recommended_verdict` as the final verdict.
- If contrast is `not_checkable`, preserve existing verdict unless existing verdict is weak.
- Preserve uncertainty in `why` and `confidence`.

Success criteria:

- HTML selected claim shows one final formal verdict.
- JSON has enough metadata to inspect what contrast recommended.
- The reader never has to choose between two competing verdicts.

## Work Unit 7: Real AI Model Report Example

Can run concurrently from the start; no code dependency until report generation.

Files likely touched:

- `examples/real_public_example.md`
- generated `examples/real_contrast_report.*` if public-safe
- README if a good example is found

Tasks:

- Find a public AI model report / model card / benchmark page and a reference URL pair.
- Prioritize examples with:
  - broad claim in target
  - narrower official reference
  - visible benchmark or scope limitation
  - no licensing issue for storing URLs/notes
- Do not paste copyrighted full text unless license permits.
- Store source title, URLs, why it is useful, and command.

Success criteria:

- At least one candidate example is documented.
- If time/API allows, generated real contrast report exists.
- The selected row can be explained in under 15 seconds.

## Work Unit 8: Verification Script

Can run after Work Units 1 and 3.

Files likely touched:

- `scripts/verify_contrast.py`
- optional `examples/gold_claims.json`

Tasks:

- Add a lightweight verifier for deterministic contrast output.
- Verify:
  - contrast exists for selected claims
  - final verdict includes expected `overstated`
  - numeric rewrite includes `3.2` and `3.8%`
  - no informal verdict label is required for the main result

Suggested command:

```bash
python scripts/verify_contrast.py examples/contrast_demo.json
```

Success criteria:

- Script exits `0` on generated mock contrast report.
- Script fails with a clear message if contrast is missing or verdict is wrong.

## Work Unit 9: README And Demo Script

Can run near the end; depends on final CLI shape.

Files likely touched:

- `README.md`
- `DEMO_EXTENSION_PLAN.md` only if decisions change

Tasks:

- Add contrast quickstart command.
- Add one paragraph explaining explicit references.
- Add demo flow:
  - run mock contrast
  - open HTML
  - click the numeric/generalization claim
  - show Evidence Contrast then Sources Checked
- Keep limitations honest:
  - reference fidelity, not universal truth
  - live URL reads can vary
  - explicit references are v1
  - auto-discovery is future work

Success criteria:

- Fresh reader can run the mock contrast demo from README.
- README does not claim auto-discovery is implemented.
- README does not claim File Search or full Managed Agents are required.

## Work Unit 10: Final Demo Rehearsal

Depends on Work Units 3, 4, and optionally 5/7.

Commands:

```bash
source .venv/bin/activate
python -m compileall honestlaunch
honestlaunch audit examples/demo_document.md --mock --contrast --contrast-top 2 --out examples/contrast_demo.md --json examples/contrast_demo.json --html examples/contrast_demo.html
python scripts/verify_numeric.py
python scripts/verify_contrast.py examples/contrast_demo.json
open examples/contrast_demo.html
```

Success criteria:

- Full mock contrast demo runs in under 90 seconds.
- HTML opens locally.
- Evidence Contrast is visible without scrolling deep into raw JSON.
- The demo can be explained as:

```text
HonestLaunch compares a risky claim against explicit reference sources. The reference supports a narrower statement, so the final verdict is overstated and the report gives a defensible rewrite.
```

## Suggested Concurrent Execution

Use one coordinator and up to four workers.

Coordinator:

- Owns Work Units 0, 2, 6, and final merge.
- Prevents conflicting edits to `audit.py` and `cli.py`.

Worker A: schema/mock

- Work Units 1 and 3.
- Owns `schemas.py` and mock contrast fixtures.

Worker B: renderer

- Work Unit 4.
- Owns `report.py`.
- Can start once Worker A has stub schema names or a sample JSON shape.

Worker C: live contrast

- Work Unit 5.
- Owns new `contrast.py` and minimal `audit.py` integration patch.
- Should coordinate with Coordinator before editing `audit.py`.

Worker D: examples/docs

- Work Units 7 and 9.
- Owns `examples/real_public_example.md` and README after CLI shape is stable.

Worker E: verification

- Work Unit 8.
- Owns `scripts/verify_contrast.py`.
- Can start after Worker A produces expected mock JSON shape.

Recommended order:

1. Coordinator runs Work Unit 0.
2. Worker A does schema + mock shape.
3. Coordinator adds CLI flags and connects mock contrast.
4. Worker B renders contrast from mock JSON.
5. Worker E adds verifier.
6. Worker C adds live contrast.
7. Worker D adds real example and README.
8. Coordinator runs Work Unit 10 and commits/pushes.

## Merge Checklist

Before final commit/push:

```bash
git status --short
source .venv/bin/activate
python -m compileall honestlaunch
honestlaunch audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
honestlaunch audit examples/demo_document.md --mock --contrast --contrast-top 2 --out examples/contrast_demo.md --json examples/contrast_demo.json --html examples/contrast_demo.html
python scripts/verify_numeric.py
python scripts/verify_contrast.py examples/contrast_demo.json
rg -n "AIza[0-9A-Za-z_-]+|gho_[0-9A-Za-z_]+" . --glob '!/.env' --glob '!/.venv/**' --glob '!/.git/**'
```

Pass criteria:

- All commands exit `0`.
- `.env` remains ignored and untracked.
- Existing non-contrast demo still works.
- Contrast demo works without API/network.
- Public docs match implemented behavior.
