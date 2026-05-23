# CappinCheck Report: Unauditable Fixture Demo

Source: `examples/needs_receipts_document.md`

## Provenance

- Mode: `deterministic_fallback`
- Model: `none`
- Pipeline wall: `2ms`
- Load / Extract / Audit / Contrast: `1ms` / `1ms` / `1ms` / `0ms`
- Claims extracted / audited: `3` / `3`
- Specialist passes / unique sources: `9` / `0`

- Evidence Contrast: `disabled`
- Provided reference URLs: `none`

## Scorecard

- Claims audited: `3`
- Verdict counts: `supported=0` · `overstated=0` · `missing_context=0` · `contradicted=0` · `not_checkable=3`
- Average stretch score: `63/100`
- Provided reference URL count: `0`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| Users strongly prefer CappinCheck over existing review tools. | not_checkable | medium | 58 |
| CappinCheck is safe for production use in regulated environments. | not_checkable | medium | 72 |
| CappinCheck is the first tool to audit scientific claims with agents. | not_checkable | medium | 58 |

## receipts_1: not_checkable

**Confidence:** medium

**Original:** Users strongly prefer CappinCheck over existing review tools.

**Stretch Score:** 58/100

**Why:** The claim may be true, but the document does not provide the evidence needed to audit it.

**Defensible rewrite:** The document presents this as an aspiration or positioning claim, not an evidenced result.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 0ms / 0ms / 0ms / 0ms / 0ms / 0ms

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

**Duration:** 0ms

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Duration:** 0ms

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

**Duration:** 0ms

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `not_checkable` with `medium` confidence.</summary>

**Duration:** 0ms

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

</details>

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.


## receipts_2: not_checkable

**Confidence:** medium

**Original:** CappinCheck is safe for production use in regulated environments.

**Stretch Score:** 72/100

**Why:** The claim may be true, but the document does not provide the evidence needed to audit it.

**Defensible rewrite:** The document presents this as an aspiration or positioning claim, not an evidenced result.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 0ms / 0ms / 0ms / 0ms / 0ms / 0ms

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

**Duration:** 0ms

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Duration:** 0ms

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

**Duration:** 0ms

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `not_checkable` with `medium` confidence.</summary>

**Duration:** 0ms

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

</details>

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.


## receipts_3: not_checkable

**Confidence:** medium

**Original:** CappinCheck is the first tool to audit scientific claims with agents.

**Stretch Score:** 58/100

**Why:** The claim may be true, but the document does not provide the evidence needed to audit it.

**Defensible rewrite:** The document presents this as an aspiration or positioning claim, not an evidenced result.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 0ms / 0ms / 0ms / 0ms / 0ms / 0ms

### Agent Steps

<details><summary>verifier: No direct supporting evidence was available in the deterministic fixture.</summary>

**Duration:** 0ms

</details>

<details><summary>contradiction-finder: Found scope limitations, missing deployment evidence, or wording that narrows the claim.</summary>

**Duration:** 0ms

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

**Duration:** 0ms

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `not_checkable` with `medium` confidence.</summary>

**Duration:** 0ms

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

</details>

**Missing context:**
- No measurement method is reported.
- No sample size, benchmark, user study, or external validation is attached to the claim.

