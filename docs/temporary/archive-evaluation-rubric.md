# Archive Evaluation Rubric

Status: active working rubric for judging whether the audited launch archive is becoming a durable public artifact rather than just a strong demo.

## Goal

Judge HonestLaunch the way a skeptical technical visitor would judge it:

- Is the product legible immediately?
- Does the judgment feel fair?
- Can every visible edit be inspected?
- Does the page experience feel coherent and intentional?
- Does the archive teach something a normal benchmark site does not?

## Excellence Bar

An excellent version of the archive would make a strong technical visitor say:

> I may disagree with some calls, but this is clearly thoughtful, fair, inspectable, and worth checking every time a major lab launches something.

## Scoring Model

Overall score: `100`

- `20` First-glance legibility and wow
- `25` Trust and inspectability
- `25` Judgment quality
- `15` Page fidelity and polish
- `15` Archive usefulness and coherence

## Category Definitions

### 1. First-Glance Legibility And Wow

Questions:

- Can a new visitor explain the product in `10 seconds`?
- Is the modified launch-page concept obvious?
- Are the edited claims discoverable without instruction?
- Is the original source reachable immediately?

Current measurement proxies:

- archive landing page exists and loads
- methodology page exists and loads
- all featured reports expose:
  - modified-version notice
  - original-source link
  - `Audited Launch Page`
  - `Audit Ledger`

### 2. Trust And Inspectability

Questions:

- Does every meaningful visible edit have receipts?
- Is the page honest about being modified?
- Is the source path clear when a proxy or PDF is used?
- Are citations concrete and explicit?

Current measurement proxies:

- tooltip-citation coverage on rewritten claims
- anchor coverage on rewritten claims
- evidence-packet coverage
- publication-gate pass rate

### 3. Judgment Quality

Questions:

- Would a strong technical reviewer call the verdict fair?
- Does the rewrite preserve strength without overclaiming?
- Are the same standards being applied across labs?

Current measurement proxies:

- reviewed gold-set verdict agreement
- reviewed gold-set rewrite expectation coverage

Important:

- this category is not credible without a reviewed gold set
- the current `seed-v1` set is only a starter signal

### 4. Page Fidelity And Polish

Questions:

- Does the audited page still feel like the source on first glance?
- Are edits placed correctly?
- Does the interface feel intentional instead of patched together?

Current measurement proxies:

- preserved-block coverage
- anchor coverage
- source-note coverage for proxies and PDFs
- report-surface coverage

### 5. Archive Usefulness And Coherence

Questions:

- Does the archive feel like a destination?
- Are the canonical pages coherent as a set?
- Can a visitor move between archive, artifact, and methodology naturally?

Current measurement proxies:

- featured-page count
- evidence-packet coverage
- methodology presence
- archive landing presence
- publication-gate pass rate

## Publication Gate

Every featured page should pass all of these checks before it is treated as fully publishable:

- visible modified-version notice
- original-source link
- evidence-packet sidecar exists
- every rewritten claim has an anchor
- every rewritten claim has at least one tooltip citation
- preserved source blocks exist

This is intentionally strict. The goal is to stop the archive from feeling half-reviewed.

## Gold Set Policy

The archive should eventually be judged against a reviewed gold set of at least `30-50` claims across:

- Google
- Anthropic
- OpenAI
- xAI

Current state:

- `evaluations/gold_set_seed.json` exists as a starter set
- it is useful for early pressure, not enough for benchmark-grade confidence

## Evaluation Workflow

1. Rebuild archive HTML artifacts.
2. Refresh archive manifest metadata and evidence-packet sidecars.
3. Run the archive-quality evaluation script.
4. Inspect category scores and failing proxies.
5. Fix the archive before expanding the corpus.

Current commands:

```bash
cd /Users/rupert/engineering/honestlaunch
source .venv/bin/activate
python scripts/rebuild_archive.py
python scripts/evaluate_archive.py
```

## Current Priority

Do not spend effort on a benchmark UI until the archive consistently scores well on:

- trust and inspectability
- judgment quality
- archive usefulness and coherence
