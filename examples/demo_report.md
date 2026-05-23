# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

## Provenance

- Mode: `deterministic_fallback`
- Model: `none`
- Pipeline wall: `1ms`
- Load / Extract / Audit / Contrast: `1ms` / `1ms` / `1ms` / `0ms`
- Claims extracted / audited: `3` / `3`
- Specialist passes / unique sources: `9` / `0`

- Evidence Contrast: `disabled`
- Provided reference URLs: `none`

## Scorecard

- Claims audited: `3`
- Verdict counts: `supported=0` · `overstated=1` · `missing_context=2` · `contradicted=0` · `not_checkable=0`
- Average stretch score: `72/100`
- Provided reference URL count: `0`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| Our method improves performance by 30% over prior work on real-world tasks. | overstated | high | 88 |
| The system robustly generalizes across domains. | missing_context | medium | 64 |
| This is the first agentic workflow for scientific claim auditing. | missing_context | medium | 64 |

## c1: overstated

**Confidence:** high

**Original:** Our method improves performance by 30% over prior work on real-world tasks.

**Stretch Score:** 88/100

**Why:** The reported benchmark numbers show improvement, but the stated 30% improvement does not match the arithmetic and the evidence is a curated benchmark, not real-world tasks.

**Defensible rewrite:** Our method improves performance from 84.1% to 87.3% on Benchmark X, a 3.2-point absolute gain and 3.8% relative improvement.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 0ms / 0ms / 0ms / 0ms / 0ms / 0ms

### Agent Steps

<details><summary>verifier: Found direct benchmark support for the narrower table values.</summary>

**Duration:** 0ms

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Duration:** 0ms

**Missing context:**
- No real-world deployment task is reported in the demo document.

</details>

<details><summary>numeric-calibrator: Computed the absolute and relative difference from the benchmark values.</summary>

**Duration:** 0ms

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `overstated` with `high` confidence.</summary>

**Duration:** 0ms

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

**Missing context:**
- No real-world deployment task is reported in the demo document.

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

</details>

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

**Gemini-discovered supporting sources:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

**Missing context:**
- No real-world deployment task is reported in the demo document.


## c2: missing_context

**Confidence:** medium

**Original:** The system robustly generalizes across domains.

**Stretch Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 0ms / 0ms / 0ms / 0ms / 0ms / 0ms

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

**Duration:** 0ms

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Duration:** 0ms

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

**Duration:** 0ms

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `medium` confidence.</summary>

**Duration:** 0ms

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

**Missing context:**
- Additional external grounding would be needed for a production verdict.


## c3: missing_context

**Confidence:** medium

**Original:** This is the first agentic workflow for scientific claim auditing.

**Stretch Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 0ms / 0ms / 0ms / 0ms / 0ms / 0ms

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

**Duration:** 0ms

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Duration:** 0ms

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

**Duration:** 0ms

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `medium` confidence.</summary>

**Duration:** 0ms

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

**Missing context:**
- Additional external grounding would be needed for a production verdict.

