# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

## Provenance

- Mode: `deterministic_fallback`
- Runtime: `local`
- Model: `none`
- Evidence Contrast: `enabled`
- Provided reference URLs: `none`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| Our method improves performance by 30% over prior work on real-world tasks. | overstated | high | 88 |
| The system robustly generalizes across domains. | missing_context | high | 64 |
| This is the first agentic workflow for scientific claim auditing. | missing_context | medium | 64 |

## c1: overstated

**Confidence:** high

**Original:** Our method improves performance by 30% over prior work on real-world tasks.

**Stretch Score:** 88/100

**Why:** The reference supports a narrower benchmark improvement, but not a 30% improvement on real-world tasks.

**Defensible rewrite:** CappinCheck improves from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain and 3.8% relative improvement under the benchmark conditions.

### Agent Steps

<details><summary>verifier: Found direct benchmark support for the narrower table values.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Missing context:**
- No real-world deployment task is reported in the demo document.

</details>

<details><summary>numeric-calibrator: Computed the absolute and relative difference from the benchmark values.</summary>

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `overstated` with `high` confidence.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

**Missing context:**
- No real-world deployment task is reported in the demo document.

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

</details>

### Evidence Contrast

**Claim says:** Our method improves performance by 30% over prior work on real-world tasks.

**Best reference says:** The reference reports 84.1% for the baseline and 87.3% for CappinCheck on Benchmark X.

**Key qualification:** The evidence is one curated benchmark, not real-world tasks; the computed gain is 3.2 percentage points and 3.8% relative.

**Delta:** narrower_than_claim — The reference supports a narrower benchmark improvement, but not a 30% improvement on real-world tasks.

**Final verdict:** overstated

**Defensible rewrite:** CappinCheck improves from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain and 3.8% relative improvement under the benchmark conditions.

### Claim-Level Contrast References

- Internal Benchmark X fixture (benchmark, authority 85/100): internal fixture source. Deterministic offline fixture containing the baseline and CappinCheck benchmark scores.

**Reference snippets / mismatches:**
- The reference reports 84.1% for the baseline and 87.3% for CappinCheck on Benchmark X. (Internal Benchmark X fixture, narrows, internal fixture source). The evidence is one curated benchmark, not real-world tasks; the computed gain is 3.2 percentage points and 3.8% relative.

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

**Missing context:**
- No real-world deployment task is reported in the demo document.


## c2: missing_context

**Confidence:** high

**Original:** The system robustly generalizes across domains.

**Stretch Score:** 64/100

**Why:** The claim generalizes beyond the reference, which only supports performance on curated Benchmark X.

**Defensible rewrite:** CappinCheck generalizes across the curated domains represented in Benchmark X; real-world deployment performance was not evaluated.

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `medium` confidence.</summary>

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

### Evidence Contrast

**Claim says:** The system robustly generalizes across domains.

**Best reference says:** The reference describes curated technical claims from public documents.

**Key qualification:** It does not evaluate clinical, legal, private-enterprise, or real-world deployment settings.

**Delta:** missing_context — The claim generalizes beyond the reference, which only supports performance on curated Benchmark X.

**Final verdict:** missing_context

**Defensible rewrite:** CappinCheck generalizes across the curated domains represented in Benchmark X; real-world deployment performance was not evaluated.

### Claim-Level Contrast References

- Internal Benchmark X fixture (benchmark, authority 85/100): internal fixture source. Deterministic offline fixture defining the evaluation setting and limitations.

**Reference snippets / mismatches:**
- The reference describes curated technical claims from public documents. (Internal Benchmark X fixture, narrows, internal fixture source). It does not evaluate clinical, legal, private-enterprise, or real-world deployment settings.

**Missing context:**
- Additional external grounding would be needed for a production verdict.


## c3: missing_context

**Confidence:** medium

**Original:** This is the first agentic workflow for scientific claim auditing.

**Stretch Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `medium` confidence.</summary>

**Missing context:**
- Additional external grounding would be needed for a production verdict.

</details>

**Missing context:**
- Additional external grounding would be needed for a production verdict.

