# Disclosure Benchmark Plan

Status: proposed work plan for turning `honestlaunch` from a one-off hackathon audit tool into a recurring disclosure-quality benchmark and artifact archive.

## Sequencing Update

This is now explicitly a `V2` plan.

`V1` is not the benchmark. `V1` is a publishable archive of reviewed audited launch pages that people can browse.

Current intended sequence:

1. Finish and publish a small static archive of audited launch pages.
2. Use that archive as the durable public artifact.
3. Add disclosure-benchmark scoring and cross-lab comparison on top of that archive.

The current canonical `V1` corpus is:

- Google
- Anthropic
- OpenAI
- xAI

The benchmark should not be treated as the next shipping milestone. It should be treated as the layer that comes after the pages themselves are solid.

## Goal

Build a trusted, repeatable system for auditing major AI launch disclosures and publishing:

- a reviewed per-launch artifact
- a frozen evidence packet
- a benchmark scorecard over time

The benchmark should measure:

- how stretched the launch language is
- how well supported the claims are
- how comparable the evidence is
- how clearly the lab disclosed methodology and caveats

It should **not** try to become a universal model-capability benchmark or a grand moral score for “truthfulness.”

## Product Direction

Recommendation:

- prioritize a **curated archive of pre-generated audits**
- deprioritize “paste any URL and generate live” as the public product
- treat the benchmark as a second-layer product built on top of that archive

Why:

- reviewed artifacts are more trustworthy than live unreviewed generation
- public expectations around “instant generation” will be miscalibrated
- costs are much easier to control
- benchmark consistency is far better when runs are frozen and dated
- the product becomes a durable reference destination rather than a toy

## Product Contract

Public site should eventually provide:

1. `Latest Audits`
Recently reviewed launch audits.

2. `Artifacts`
Per-launch audited page, ledger, and frozen evidence packet.

3. `Methodology`
Clear explanation of claim selection, verdicts, evidence policy, and review standards.

4. `Benchmark`
Cross-lab disclosure-quality comparisons over time.

For the current release sequence:

- `Latest Audits`, `Artifacts`, and `Methodology` come first
- `Benchmark` comes after the archive is real and stable

## Core Benchmark Principle

The benchmark should score **support quality**, not abstract truth.

Correct framing:

- “How well supported is this disclosure language?”
- “How stretched is this launch narrative relative to the evidence packet?”

Incorrect framing:

- “Which lab is objectively the most truthful?”
- “Which model is actually the best overall?”

## Source Of Truth Hierarchy

### Primary Sources

Use as the first-class evidence packet:

- launch post
- model card / system card
- eval appendix
- benchmark-specific official references
- pricing and availability docs when relevant

### Secondary Structured Sources

Use as challenge/reference sources, not sole truth:

- Artificial Analysis
- Arena leaderboard snapshots
- LiveBench
- benchmark-native repos or papers

### Internal Checks

Use deterministic or rule-based checks where possible:

- percentages
- percentage-point vs percent confusion
- table deltas
- rank claims
- pricing claims
- availability claims

## Verdict Model

### Primary Verdict

Keep one mutually exclusive label per claim:

- `supported`
- `overstated`
- `missing_context`
- `contradicted`
- `not_checkable`

### Secondary Dimensions

Add orthogonal scores instead of overloading the primary label:

- `stretch_severity`: `0-100`
- `evidence_confidence`: `0-100`
- `comparability_risk`: `0-100`
- `disclosure_completeness`: `0-100`
- `numeric_integrity`: `pass | fail | n/a`

This keeps the top-level verdict legible while preserving nuance.

## Benchmark Output

### Per-Launch Metrics

- `supported_claim_rate`
- `overstatement_rate`
- `missing_context_rate`
- `contradiction_rate`
- `average_stretch_severity`
- `average_evidence_confidence`
- `average_comparability_risk`
- `evidence_packet_coverage`

### Per-Lab Rollups

Aggregate over time:

- last `3` launches
- trailing `12` months
- all tracked launches

Suggested lab-level summaries:

- average stretch
- median comparability risk
- methodology clarity trend
- evidence transparency trend
- launch-to-launch volatility

## Current Capability Verification

Per-launch audit artifact generation: `Partial`

- existing audit engine: `Yes`
- audited launch-page view: `Yes`
- frozen evidence packet model: `Partial`
- manual generation and manual publish decision by repo owner: `Yes`
- in-product publication states and workflow: `No`

Cross-launch benchmark scoring: `No`

- no launch registry
- no score aggregation model
- no benchmark UI

Review workflow: `Partial`

- current workflow is manual generation followed by a manual publish decision
- there is no automated async review system in scope for `V1`
- there are no first-class publication states or reviewer notes yet

Artifact archive: `Partial`

- generated examples exist locally
- demo gallery exists
- there is no final canonical corpus, index, or publication lifecycle yet

## V1 Archive Preconditions

Before benchmark work becomes the active priority, the archive should meet these conditions:

- four canonical launch pages exist and are shareable
- each page has a clear original-source link
- each page clearly signals that it is an audited modified version of the source
- each page has stable citations and a usable ledger
- the gallery feels coherent as a destination, not just a pile of examples

Only after those conditions are true should benchmark implementation become the main workstream.

## Work Units

## Work Unit 1: Benchmark Schema

Objective:

- define the canonical data model for launches, claims, evidence packets, and benchmark scores

Deliverables:

- benchmark schema doc
- updates to `honestlaunch/schemas.py`
- launch-level score packet shape

Files likely involved:

- `honestlaunch/schemas.py`
- new `honestlaunch/benchmark_schema.py`
- `docs/temporary/disclosure-benchmark-plan.md`

Verification:

- one launch can serialize:
  - evidence packet
  - claim packets
  - final verdicts
  - benchmark summary metrics

## Work Unit 2: Launch Registry

Objective:

- define the curated set of launches to audit and revisit

Deliverables:

- launch registry file
- inclusion criteria
- supported-domain metadata
- reference preset mapping

Suggested scope for v1 registry:

- Google
- Anthropic
- OpenAI
- xAI

Files likely involved:

- new `data/launch_registry.yaml`
- new `honestlaunch/reference_presets.py`

Verification:

- every registry item has:
  - launch URL
  - canonical lab name
  - model name
  - launch date
  - reference URLs

## Work Unit 3: Frozen Evidence Packets

Objective:

- make every published audit reproducible and dated

Deliverables:

- evidence packet schema
- fetched and normalized source snapshots
- frozen reference packet storage layout

Files likely involved:

- `honestlaunch/ingest.py`
- `honestlaunch/source_snapshot.py`
- new `honestlaunch/evidence_packet.py`
- new `artifacts/launches/<slug>/`

Stored packet contents:

- launch URL
- launch snapshot
- reference URLs
- fetched reference metadata
- benchmark snapshot notes
- run date

Verification:

- rerendering a published launch does not depend on unstable live fetch alone

## Work Unit 4: Claim Taxonomy And Selection Policy

Objective:

- define which claims count toward the benchmark and which do not

Claim categories:

- benchmark/performance
- speed/latency
- price/cost-efficiency
- multimodal capability
- safety/disclosure
- deployment/availability
- enterprise impact
- general marketing / frontier framing

Needed policy:

- what qualifies as a “benchmarkable claim”
- what gets excluded from scoring
- how to treat broad qualitative language

Deliverables:

- claim-selection policy doc
- taxonomy updates
- benchmark-eligibility flag per claim

Files likely involved:

- `honestlaunch/schemas.py`
- `honestlaunch/claims.py`
- new `docs/methodology_claim_selection.md`

Verification:

- two reviewers can independently label whether a claim counts toward the benchmark

## Work Unit 5: Deterministic Checks

Objective:

- increase trust by replacing soft model judgment with direct computation where possible

Checks to add:

- percentage math
- percentage-point math
- pricing and token-rate comparisons
- rank and leaderboard claims
- date / availability consistency

Files likely involved:

- current numeric helpers
- new `honestlaunch/deterministic_checks.py`

Verification:

- benchmark/performance claims with explicit numbers produce deterministic evidence notes

## Work Unit 6: Evidence Contrast Hardening

Objective:

- strengthen claim-vs-source comparison beyond general-purpose model prose

Needed changes:

- distinguish identical vs non-identical evaluation setups
- explicitly record missing comparability conditions
- better benchmark-source normalization

Deliverables:

- comparability checklist per claim
- comparability risk score

Files likely involved:

- `honestlaunch/contrast.py`
- `honestlaunch/citations.py`
- `honestlaunch/anchor_map.py`

Verification:

- benchmark claims clearly state whether comparisons are apples-to-apples, self-reported, or mixed-source

## Work Unit 7: Review Workflow

Objective:

- move from machine-generated artifact to trusted published artifact

Proposed publication states:

- `draft_machine`
- `review_in_progress`
- `reviewed`
- `published`
- `superseded`

Reviewer tasks:

- confirm claim selection
- confirm evidence packet
- confirm verdicts on high-impact claims
- edit rewrite/tooltip language if needed
- approve benchmark publication

Files likely involved:

- new `data/reviews/`
- new `docs/review_workflow.md`
- eventual hosted admin UI or local review scripts

Verification:

- every published artifact can show whether it is machine draft or reviewed

## Work Unit 8: Benchmark Aggregation

Objective:

- roll reviewed launch artifacts into lab-level and global benchmark views

Deliverables:

- aggregation module
- per-lab score summaries
- historical trend data

Files likely involved:

- new `honestlaunch/benchmark_aggregate.py`
- new `data/benchmark/`

Verification:

- benchmark table can be rebuilt deterministically from reviewed launch packets

## Work Unit 9: Archive And Site Presentation

Objective:

- publish the benchmark as a destination, not just a report dump

Pages to build:

- latest launches
- benchmark rankings
- methodology
- per-launch artifact pages

Design requirement:

- the audited launch page remains the hero artifact
- the benchmark context is visible but secondary on the launch page

Files likely involved:

- current static reports
- new index-generation layer
- eventual hosted frontend

Verification:

- a visitor can understand:
  - what the benchmark measures
  - what one launch scored
  - how that compares across labs

## Work Unit 10: Corpus Expansion

Objective:

- grow from a few demos to a real, recurring benchmark set

Initial target corpus:

- 10-20 major launches

Ongoing process:

- add each meaningful new lab launch
- refresh benchmark tables on a fixed cadence
- never silently overwrite prior evidence packets

Verification:

- each published launch is versioned and dated

## Execution Plan

### Phase 0: Freeze The Benchmark Product Contract

Objective:

- commit to the curated archive / reviewed benchmark direction

Tasks:

- define the benchmark statement in one sentence
- define what is in-scope vs out-of-scope
- define v1 publication standard

Exit criteria:

- team agrees the public product is not primarily “live arbitrary URL generation”

### Phase 1: Data Model And Methodology

Work units:

- Work Unit 1: Benchmark Schema
- Work Unit 4: Claim Taxonomy And Selection Policy

Reason:

- benchmark credibility depends on a stable methodological frame before more code is added

Exit criteria:

- one canonical score packet exists
- one canonical claim-selection policy exists

### Phase 2: Launch Registry And Evidence Packets

Work units:

- Work Unit 2: Launch Registry
- Work Unit 3: Frozen Evidence Packets

Reason:

- benchmark outputs must be reproducible and tied to a dated corpus

Exit criteria:

- at least 5 curated launches can be represented as frozen packets

### Phase 3: Trust Hardening In The Audit Engine

Work units:

- Work Unit 5: Deterministic Checks
- Work Unit 6: Evidence Contrast Hardening

Reason:

- this is where the prototype becomes defensible

Exit criteria:

- high-impact numeric and comparability claims are substantially grounded by deterministic or structured evidence checks

### Phase 4: Review Workflow

Work units:

- Work Unit 7: Review Workflow

Reason:

- benchmark publication should not be raw model output

Exit criteria:

- one launch can move from machine draft to reviewed artifact with explicit state tracking

### Phase 5: Benchmark Aggregation

Work units:

- Work Unit 8: Benchmark Aggregation

Reason:

- only reviewed launches should feed the public benchmark

Exit criteria:

- lab-level benchmark summaries can be rebuilt from reviewed artifacts

### Phase 6: Site Archive And Public Presentation

Work units:

- Work Unit 9: Archive And Site Presentation

Reason:

- the archive is the product surface people will return to

Exit criteria:

- public site can show latest launches, benchmark table, methodology, and artifact pages

### Phase 7: Corpus Expansion

Work units:

- Work Unit 10: Corpus Expansion

Reason:

- benchmark value comes from repeated, comparable coverage over time

Exit criteria:

- there is enough breadth for meaningful cross-lab comparisons

## Concurrency Notes

Can be done concurrently:

- Work Unit 2 and Work Unit 4 after Phase 1 is stable
- Work Unit 5 and Work Unit 6 after evidence packet shape is stable
- Work Unit 7 can begin in parallel with late Work Unit 6 once draft packets are available

Should stay sequential:

- benchmark schema before benchmark aggregation
- frozen evidence packets before public benchmark publication
- review workflow before public benchmark rollup

## Recommended First Shipping Slice

The smallest serious version of this benchmark is:

- 5 reviewed launch audits
- frozen evidence packets for each
- benchmark methodology page
- one benchmark table with:
  - supported rate
  - overstated rate
  - missing-context rate
  - average stretch
- audited launch page + ledger for each launch

That is enough to make the product feel real without pretending the system is broader or more automated than it is.

## Verification Checklist

The benchmark direction is ready when:

- published launches use frozen evidence packets
- each published claim has one exclusive verdict plus secondary dimensions
- high-impact numeric claims have deterministic evidence where possible
- reviewed artifacts are clearly distinguished from machine drafts
- cross-lab benchmark tables are derived from reviewed artifacts only
- the public methodology page makes the scope and limits obvious
