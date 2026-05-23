# CappinCheck Report: Careful Scientific Claim Demo

Source: `examples/careful_document.md`

## Provenance

- Mode: `deterministic_fallback`
- Runtime: `local`
- Model: `none`
- Evidence Contrast: `disabled`
- Provided reference URLs: `none`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| CappinCheck improved from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain under the benchmark conditions. | supported | high | 8 |
| The evaluation does not establish real-world deployment performance. | supported | high | 14 |
| The result is limited to the curated Benchmark X dataset. | supported | high | 14 |

## careful_1: supported

**Confidence:** high

**Original:** CappinCheck improved from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain under the benchmark conditions.

**Stretch Score:** 8/100

**Why:** The claim is narrow, scoped, and supported by the document's own evidence and caveats.

**Defensible rewrite:** CappinCheck improved from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain under the benchmark conditions.

### Agent Steps

<details><summary>verifier: Found direct benchmark support for the narrower table values.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

</details>

<details><summary>contradiction-finder: No contradictions were found for the scoped claim.</summary>

</details>

<details><summary>numeric-calibrator: Computed the absolute and relative difference from the benchmark values.</summary>

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- The document uses percentage-point wording, so the numeric claim is properly scoped.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `supported` with `high` confidence.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- The document uses percentage-point wording, so the numeric claim is properly scoped.

</details>

**Computed checks:**
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- The document uses percentage-point wording, so the numeric claim is properly scoped.

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.


## careful_2: supported

**Confidence:** high

**Original:** The evaluation does not establish real-world deployment performance.

**Stretch Score:** 14/100

**Why:** The claim is narrow, scoped, and supported by the document's own evidence and caveats.

**Defensible rewrite:** The evaluation does not establish real-world deployment performance.

### Agent Steps

<details><summary>verifier: Found direct benchmark support for the narrower table values.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

</details>

<details><summary>contradiction-finder: No contradictions were found for the scoped claim.</summary>

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `supported` with `high` confidence.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

</details>

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.


## careful_3: supported

**Confidence:** high

**Original:** The result is limited to the curated Benchmark X dataset.

**Stretch Score:** 14/100

**Why:** The claim is narrow, scoped, and supported by the document's own evidence and caveats.

**Defensible rewrite:** The result is limited to the curated Benchmark X dataset.

### Agent Steps

<details><summary>verifier: Found direct benchmark support for the narrower table values.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

</details>

<details><summary>contradiction-finder: No contradictions were found for the scoped claim.</summary>

</details>

<details><summary>numeric-calibrator: No numeric calibration was applicable.</summary>

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `supported` with `high` confidence.</summary>

**Supporting evidence:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

</details>

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

