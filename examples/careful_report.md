# CappinCheck Report: Careful Scientific Claim Demo

Source: `examples/careful_document.md`

| Claim | Formal Verdict | Confidence | Vibe | Cap Score |
| --- | --- | --- | --- | ---: |
| CappinCheck improved from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain under the benchmark conditions. | supported | high | no cap | 8 |
| The evaluation does not establish real-world deployment performance. | supported | high | no cap | 14 |
| The result is limited to the curated Benchmark X dataset. | supported | high | no cap | 14 |

## careful_1: supported

**Confidence:** high

**Vibe:** no cap

**Original:** CappinCheck improved from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain under the benchmark conditions.

**Cap Score:** 8/100

**Why:** The claim is narrow, scoped, and supported by the document's own evidence and caveats.

**Defensible rewrite:** CappinCheck improved from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain under the benchmark conditions.

**Numeric findings:**
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- The document uses percentage-point wording, so the numeric claim is properly scoped.

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.


## careful_2: supported

**Confidence:** high

**Vibe:** no cap

**Original:** The evaluation does not establish real-world deployment performance.

**Cap Score:** 14/100

**Why:** The claim is narrow, scoped, and supported by the document's own evidence and caveats.

**Defensible rewrite:** The evaluation does not establish real-world deployment performance.

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.


## careful_3: supported

**Confidence:** high

**Vibe:** no cap

**Original:** The result is limited to the curated Benchmark X dataset.

**Cap Score:** 14/100

**Why:** The claim is narrow, scoped, and supported by the document's own evidence and caveats.

**Defensible rewrite:** The result is limited to the curated Benchmark X dataset.

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. The document calls this a 3.2 percentage-point gain. (Careful document benchmark table). Relevance: The source wording matches the table and keeps the scope limited to Benchmark X.

