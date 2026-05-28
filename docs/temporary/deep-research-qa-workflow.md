# Deep Research QA Workflow

Status: recommended lighter-weight QA layer for the archive. This is not the full benchmark evaluation system.

## Goal

Use deep-research models as **independent editorial readers** before publication.

The point is not to replace HonestLaunch.
The point is to sanity-check that:

- HonestLaunch surfaced the right suspicious claims
- the verdicts are directionally fair
- the archive did not miss the most important stretch or caveat

## What This Is

This is a `QA layer`, not a new source of truth.

Production still works like this:

1. HonestLaunch ingests the launch and picks the risky claims.
2. HonestLaunch audits those claims and renders the artifact.
3. Deep-research runs act as second readers.
4. You decide whether to publish.

## Why This Layer Exists

Citations alone are enough for a publishable inspectable artifact.

They are **not** enough to tell you:

- whether HonestLaunch picked the most important claims
- whether it missed a better caveat
- whether another strong reader would have reached a very different conclusion

This workflow is meant to answer that without pretending we have a benchmark-grade gold set yet.

## Recommended Model Setup

Use two independent research systems:

- `Anthropic deep research`
- `OpenAI deep research`

Run them separately.

Do **not** ask one model to do discovery and adjudication in the same prompt if you want useful QA. Split the work:

1. `Discovery`
2. `Adjudication`

This makes it easier to detect where models converge or diverge.

## Workflow

### Step 1: Initialize a QA packet

```bash
cd /Users/rupert/engineering/honestlaunch
source .venv/bin/activate
python scripts/init_qa_packet.py gemini-35-flash
```

This creates:

- `evaluations/packets/gemini-35-flash.json`

The packet contains:

- launch metadata
- archive artifact pointers
- explicit reference URLs
- slots for discovery and adjudication outputs
- final human publish decision

### Step 2: Run discovery prompts independently

Use:

- `evaluations/prompts/discovery_prompt.md`

Run it once in Anthropic deep research and once in OpenAI deep research.

Inputs to provide:

- launch title
- launch URL
- source note
- explicit references

Output to capture in the packet:

- `discovery.providers[*].suspectClaims`
- `discovery.providers[*].notes`

### Step 3: Do a human merge on discovery

You review:

- HonestLaunch's selected claims
- Anthropic-discovered suspect claims
- OpenAI-discovered suspect claims

Then fill:

- `discovery.mergedReview.mustCatchClaims`
- `discovery.mergedReview.niceToCatchClaims`
- `discovery.mergedReview.nonIssues`

This is the key step.

The point is **not** to make deep research the source of truth.
The point is to get an independent read on what a good audit should probably look at.

### Step 4: Run adjudication prompts on the merged claims

Use:

- `evaluations/prompts/adjudication_prompt.md`

Feed in only the merged claims you actually want checked.

Run it once in Anthropic deep research and once in OpenAI deep research.

Capture:

- expected verdict
- rationale
- must-have caveat
- rewrite must-contain
- rewrite must-avoid
- approved primary sources

### Step 5: Compare QA outputs to HonestLaunch

For each merged claim, compare:

- Did HonestLaunch catch it?
- Did it choose a similar verdict?
- Did it cite similar primary sources?
- Did its rewrite preserve the right meaning?

This is the lightweight QA question:

> If two strong independent readers and HonestLaunch all look at this launch, do they roughly agree on what the risky claims are and how they should be narrowed?

### Step 6: Human publication decision

Fill:

- `humanDecision.publishStatus`
- `humanDecision.decisionNotes`
- `humanDecision.reviewer`
- `humanDecision.reviewedAt`

Possible statuses:

- `publish`
- `publish_with_note`
- `hold`

## Packet Shape

The packet is initialized by:

- `scripts/init_qa_packet.py`

Backed by:

- `honestlaunch/research_qa.py`

The packet is intentionally minimal.

It is **not** the full gold set.
It is a launch-specific QA record.

## What This Gives You

This workflow helps answer:

- did HonestLaunch pick the right suspicious claims?
- did it miss a major stretch?
- do independent readers agree with the archive directionally?

It does **not** yet prove:

- benchmark-grade methodological rigor
- version-to-version eval confidence
- lab-level comparative scoring quality

That is what the larger gold set and benchmark layer are for later.

## Recommended Near-Term Use

Use this on the 4 canonical archive pages:

- Google
- Anthropic
- OpenAI
- xAI

Do not block publishing on perfect agreement.
Use it as editorial QA:

- if HonestLaunch and both research readers roughly converge, publish with confidence
- if they diverge sharply, inspect the claim selection or evidence before publish

## Practical Rule

If you are choosing between:

- building a full benchmark eval now
- or getting strong independent QA on the 4 featured pages

choose the QA layer first.
