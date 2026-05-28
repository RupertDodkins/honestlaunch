# Audited Launch Page Plan

Status: temporary implementation plan for the next HonestLaunch phase.

## Goal

Turn the primary HonestLaunch surface into a high-fidelity modified version of the source launch page, with audited claim substitutions rendered inline.

Product contract for v1:

- The first-glance surface should look like the original page.
- Where technically feasible, preserve the original page structure and feel very closely.
- Rewritten claims should be subtly underlined.
- Hover or tap on a rewritten span should reveal:
  - original wording
  - formal verdict
  - concise reason for the rewrite
  - citations supporting the correction
- Tooltip citations should come from explicit reference URLs only.
- The existing claim ledger should remain available as a secondary inspection/debug surface.
- The first real target should be the Gemini launch page.
- xAI should follow after the Gemini path is stable; current xAI fetch constraints make it a worse first target.
- Published pages should include a visible notice that the page is an audited modified version of the original source, plus a prominent link back to the original.

## Resolved Decisions

- Primary surface: near-clone of the source page
- Main goal: demo wow + credible proof + reusable serious interface
- Rewrite policy: rewrite every non-`supported` claim
- Source fidelity: preserve original layout and feel as much as practical, including exact-clone fidelity where technically feasible
- Evidence placement: inline hover/tap tooltip
- Tooltip nuance for `missing_context`: keep the visible replacement clean; put the caveat/context in the tooltip
- Branding: subtle HonestLaunch wrapper for now; rename can happen later
- Mobile interaction: tap popover
- Publishing posture: show that the page is a modified audited version, not the original source

## Current State

Relevant files:

- `honestlaunch/ingest.py`
- `honestlaunch/report.py`
- `honestlaunch/schemas.py`
- `honestlaunch/cli.py`
- `examples/index.html`
- `README.md`

Current implementation reality:

- `ingest.py` now preserves more HTML block structure than before, but still flattens the page into text.
- `report.py` now contains:
  - the existing claim-ledger HTML renderer
  - a prototype "Launch Rewrite" tab
  - text-block and clause-level rewrite mapping
- The current rewrite view is useful as a proof of direction, but it is not source-page-aware enough to satisfy the product target.

Main gap:

- The current renderer rewrites reconstructed text blocks, not a preserved source-page structure with exact inline spans.

## Current Product Sequencing

This work is now the immediate public-facing priority.

Current sequence:

1. Ship a small static archive of reviewed audited launch pages.
2. Use those pages as the public-facing artifact archive.
3. Build the disclosure benchmark later on top of that archive.

The first archive should center on:

- Google
- Anthropic
- OpenAI
- xAI

The benchmark is no longer the next implementation milestone for this repo. The next milestone is making those pages solid, legible, and publishable.

## Recommended Module Shape

Do not keep expanding `report.py` as one file. Use it as the public orchestration layer and split the audited-page work into focused modules.

Target module split:

- `honestlaunch/report.py`
  - keep `write_markdown`, `write_json`, and top-level `write_html`
  - delegate HTML generation to sub-renderers
- `honestlaunch/ingest.py`
  - preserve source text and produce a sanitized source snapshot
- `honestlaunch/schemas.py`
  - add snapshot, anchor, and tooltip citation models
- `honestlaunch/source_snapshot.py`
  - sanitize and normalize fetched HTML into a stable article snapshot
- `honestlaunch/anchor_map.py`
  - map audited claims onto exact source spans
- `honestlaunch/citations.py`
  - normalize explicit reference URLs into canonical source titles for UI
- `honestlaunch/report_dashboard.py`
  - current claim-ledger HTML surface
- `honestlaunch/report_launch_page.py`
  - audited launch-page renderer with inline replacements and tooltips

This split is not required all at once, but it should be the direction of travel.

## Data Model Additions

Add models that support exact substitution and tooltip rendering.

Suggested additions in `schemas.py`:

- `SourceSnapshot`
  - `title`
  - `source_url`
  - `blocks: list[SnapshotBlock]`
  - optional preserved metadata for canonical page title / description
- `SnapshotBlock`
  - `block_id`
  - `kind` such as `heading`, `paragraph`, `list_item`, `table_row`, `quote`
  - `text`
  - `html`
  - optional source order / parent section metadata
- `ClaimAnchor`
  - `claim_id`
  - `block_id`
  - `matched_text`
  - `start_char`
  - `end_char`
  - `match_type`
  - `match_confidence`
- `TooltipCitation`
  - `title`
  - `url`
  - `snippet`
  - `why_relevant`
- `RewriteDecoration`
  - `claim_id`
  - `verdict`
  - `original_text`
  - `rewritten_text`
  - `reason`
  - `citations: list[TooltipCitation]`
  - `anchor: ClaimAnchor`

## Phase Plan

### Phase 0: Freeze The Product Contract

Objective:

- Record the target interaction and lock the Gemini page as the first real target.

Deliverables:

- This plan
- One explicit target page and one explicit reference packet

Verification criteria:

- Team can answer, in one sentence, what the primary surface is
- Gemini is confirmed as the v1 anchor page

Can be done concurrently:

- Nothing meaningful; this is the dependency lock for the phases below

### Phase 1: Preserve A Real Source Snapshot

Objective:

- Stop treating launch pages as plain text only.
- Preserve enough sanitized source structure to rebuild the original page credibly.

Files:

- `honestlaunch/ingest.py`
- `honestlaunch/schemas.py`
- new `honestlaunch/source_snapshot.py`

Scope:

- Fetch page HTML
- Extract the main article/content region
- Sanitize it
- Preserve block structure and source order
- Keep `Document.text` for backward compatibility
- Add `Document.snapshot` or parallel snapshot output for the new renderer path

Non-goals:

- Do not preserve full site chrome
- Do not build a browser runtime
- Do not aim for perfect CSS fidelity yet

Verification criteria:

- Local fixture still works
- A real Gemini page produces:
  - stable title
  - article-like ordered blocks
  - preserved headings, paragraphs, and lists
- `python -m compileall honestlaunch` passes
- Existing `--mock` report generation still works

Suggested verification:

```bash
source .venv/bin/activate
python -m compileall honestlaunch
honestlaunch audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
```

Can be done concurrently:

- Citation normalization design work
- README/demo-surface notes

Should not be done concurrently with:

- Final audited-page UI implementation, because the snapshot contract needs to stabilize first

### Phase 2: Build Exact Claim Anchoring

Objective:

- Map audited claims onto exact source spans within the preserved snapshot.

Files:

- `honestlaunch/schemas.py`
- new `honestlaunch/anchor_map.py`
- possibly `honestlaunch/audit.py` if anchors are computed during audit finalization

Scope:

- Prefer exact or near-exact span mapping against preserved source blocks
- Support sentence and clause anchors
- Record confidence and fallback type
- Preserve the currently useful fuzzy fallback as a last resort only

Key rule:

- The audited-page renderer should consume `ClaimAnchor` data, not rediscover matches on the fly

Verification criteria:

- Demo fixture maps all non-`supported` claims to explicit source spans
- Gemini target page maps most audited claims to exact or clause-level anchors
- Low-confidence matches are visible in the debug surface
- Anchor metadata is serializable in the JSON report

Suggested verification:

```bash
source .venv/bin/activate
honestlaunch audit examples/demo_document.md --mock --json examples/demo_report.json --html examples/demo_report.html
```

Manual checks:

- Confirm that each edited claim has a `block_id`, `matched_text`, and confidence score

Can be done concurrently:

- Citation normalization implementation

Should not be done concurrently with:

- Final tooltip UI, because the tooltip contract should depend on stable anchor data

### Phase 3: Canonical Citation And Tooltip Packet Cleanup

Objective:

- Make inline tooltip receipts feel authoritative instead of noisy.

Files:

- new `honestlaunch/citations.py`
- `honestlaunch/report_launch_page.py`
- possibly `honestlaunch/contrast.py`

Scope:

- Use explicit reference URLs only for audited-page tooltip citations
- Resolve ugly grounding redirects into canonical source titles
- Produce short, clean citation packets:
  - source title
  - url
  - one relevant snippet
  - one-line relevance

Non-goals:

- Do not include every Gemini-discovered source inline
- Do not overload the tooltip with long reasoning text

Verification criteria:

- No visible `vertexaisearch.cloud.google.com/grounding-api-redirect/...` URLs in the tooltip UI
- Tooltip citation titles read like actual sources
- The citation packet for the Gemini page is concise and legible

Suggested verification:

- Generate a real Gemini report and inspect the rendered tooltip citations

Can be done concurrently:

- Phase 2 after the anchor data shape is mostly known
- Dashboard/ledger cleanup

### Phase 4: Build The Audited Launch Page Renderer

Objective:

- Render the source launch page as the primary audited surface.

Files:

- new `honestlaunch/report_launch_page.py`
- `honestlaunch/report.py`

Scope:

- Start from the preserved `SourceSnapshot`
- Render blocks in source order
- Substitute rewritten spans inline using `ClaimAnchor`
- Wrap rewritten spans with a subtle audit decoration:
  - underline or dotted underline
  - accessible focus style
  - hover/tap target
- Keep the page visually close to the original content hierarchy

Key UI rule:

- The page should look normal on first glance
- Audit styling should be discoverable, not loud

Verification criteria:

- The primary view reads like the original launch page
- Edited spans are visible but subtle
- Rewrites do not destroy sentence flow
- The page renders on desktop and mobile widths

Suggested verification:

```bash
source .venv/bin/activate
honestlaunch audit <gemini-url-or-local-snapshot> --contrast --reference <canonical-ref-url> --out examples/gemini_35_flash_report.md --json examples/gemini_35_flash_report.json --html examples/gemini_35_flash_report.html
```

Can be done concurrently:

- Tooltip component work after anchor and citation contracts are stable
- README/gallery updates can start late in this phase

Should not be done concurrently with:

- Phase 1 snapshot redesign

### Phase 5: Add Hover / Tap Tooltips

Objective:

- Reveal the audit proof inline without changing the visible page copy.

Files:

- `honestlaunch/report_launch_page.py`
- optional shared UI helpers if extracted from `report.py`

Scope:

- Desktop hover and keyboard focus tooltip
- Mobile tap popover
- Tooltip contents:
  - original wording
  - formal verdict
  - concise rewrite reason
  - explicit reference citations

Important product rule:

- `missing_context` nuance belongs in the tooltip, not inline

Verification criteria:

- Hover works on desktop
- Focus works with keyboard navigation
- Tap works on mobile-sized viewport
- Tooltip stays compact and readable
- Tooltip never exposes raw redirect URLs

Manual verification checklist:

- Hover on at least 3 rewritten claims
- Focus through rewritten claims with keyboard
- Check mobile-width behavior

Can be done concurrently:

- Phase 4 late-stage styling and polish

### Phase 6: Reframe The Existing Surface Hierarchy

Objective:

- Make the audited launch page the default product surface and demote the claim ledger to secondary.

Files:

- `honestlaunch/report.py`
- `honestlaunch/report_dashboard.py` if split
- `README.md`
- `examples/index.html`

Scope:

- Default to the audited launch page view
- Keep the ledger as:
  - `Audit Ledger`
  - `Receipts`
  - or similar secondary tab
- Update the demo gallery to present the audited page as the hero
- Update README copy and demo script

Verification criteria:

- A first-time viewer lands on the audited launch page, not the ledger
- The ledger is still one click away
- README and demo gallery match the new primary surface

Can be done concurrently:

- README hygiene pass
- demo video planning

### Phase 7: Real-Page Hardening On Gemini

Objective:

- Prove the audited-page interaction on one real launch page before generalizing.

Files:

- likely no new core modules; mostly iteration across phases 1-6
- example outputs in `examples/`

Scope:

- Run the full flow against the Gemini page
- Fix layout, match quality, tooltip tone, and citation packet quality
- Decide whether any source-specific exceptions belong in generic code or in a source adapter layer

Verification criteria:

- The Gemini page is recognizably the original at first glance
- Most audited claims land on the correct source spans
- Tooltip citations feel trustworthy
- The audited page is the obvious demo surface

Can be done concurrently:

- xAI feasibility review
- README/demo-gallery framing

### Phase 8: xAI And Gallery Generalization

Objective:

- Extend the audited launch-page path beyond Gemini.

Files:

- `examples/index.html`
- source-specific ingestion helpers only if strictly needed

Scope:

- Apply the same renderer to xAI using the proxy/local source if needed
- Decide whether per-source adapters are necessary
- Roll the primary audited-page surface into the gallery

Verification criteria:

- xAI output uses the same audited-page UI contract
- Gallery links remain stable
- Different sources do not require hand-editing the renderer

## Concurrency Summary

Workstreams that can run in parallel after Phase 0:

- Workstream A: source snapshot preservation
- Workstream B: citation/title normalization
- Workstream C: README/demo-gallery copy planning

Workstreams that can run in parallel after Phase 1:

- Workstream D: exact anchor mapping
- Workstream B: citation packet cleanup

Workstreams that can run in parallel after Phase 2:

- Workstream E: audited-page renderer
- Workstream F: tooltip interaction layer

Workstreams that should stay mostly sequential:

- Snapshot contract -> anchor contract -> audited-page renderer
- Do not let the renderer invent its own matching logic after the anchor model exists

## Recommended Execution Order

If one person is doing the work sequentially:

1. Phase 1
2. Phase 2
3. Phase 3
4. Phase 4
5. Phase 5
6. Phase 6
7. Phase 7
8. Phase 8

If multiple people or agents are available:

1. One person on source snapshot preservation
2. One person on citation normalization and tooltip packet shape
3. Once snapshot shape stabilizes, one person on anchor mapping
4. Once anchor and citation contracts stabilize, one person on audited-page rendering
5. In parallel, one person updates README/gallery/demo script

## Minimum Success Criteria For This Phase

The phase is a success when all of these are true:

- The primary surface is the audited launch page
- Rewritten claims appear inline on a page that still looks like the original
- Hover/tap reveals original wording and explicit-reference citations
- The claim ledger remains available for debugging and trust
- The Gemini page works end to end
- Raw redirect URLs are gone from the primary UI

## Explicit Non-Goals For V1

- Perfect full-site cloning
- A hosted frontend/backend split
- Rich WYSIWYG author tooling
- Automatic source discovery in tooltips
- Perfect xAI fidelity before Gemini is solid

## Verification Commands To Keep Running

Compile and mock regression:

```bash
source .venv/bin/activate
python -m compileall honestlaunch
honestlaunch audit examples/demo_document.md --mock --out examples/demo_report.md --json examples/demo_report.json --html examples/demo_report.html
```

Real Gemini page:

```bash
source .venv/bin/activate
honestlaunch audit https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/ \
  --contrast \
  --reference https://deepmind.google/models/model-cards/gemini-3-5-flash \
  --contrast-top 2 \
  --limit 4 \
  --out examples/gemini_35_flash_report.md \
  --json examples/gemini_35_flash_report.json \
  --html examples/gemini_35_flash_report.html
```

## Notes

- The current prototype rewrite view is still useful as a stepping stone and should not be discarded blindly.
- The biggest technical risk is exact span anchoring on real launch pages.
- The biggest product risk is shipping a page that looks clever but not trustworthy; citation cleanup is therefore a core dependency, not polish.
