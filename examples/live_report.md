# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

| Claim | Vibe | Formal Verdict | Cap Score | Confidence |
| --- | --- | --- | ---: | --- |
| improves performance by 30% over prior work | cap | contradicted | 90 | high |

## claim_1: cap / contradicted

**Original:** improves performance by 30% over prior work

**Cap Score:** 90/100

**Why:** The claim of a 30% performance improvement over prior work is mathematically contradicted by the paper's own empirical results. The actual data presented on Benchmark X shows CappinCheck achieving 87.3% accuracy compared to a baseline of 84.1%, which translates to a 3.2 percentage point absolute increase, a 3.8% relative accuracy improvement, or a 20.1% relative error rate reduction. None of these calculations yield 30%. Furthermore, the authors state they did not conduct an external literature search, meaning the claim of beating 'prior work' lacks foundational evidence.

**Defensible rewrite:** improves relative performance accuracy by 3.8% (or reduces the error rate by 20.1%) on Benchmark X compared to a baseline claim-review pipeline

**Numeric findings:**
- Claimed performance improvement: 30%
- Baseline Benchmark X accuracy: 84.1%
- CappinCheck Benchmark X accuracy: 87.3%
- Absolute difference: 3.2 percentage points (87.3% - 84.1%)
- Relative accuracy improvement: 3.8% (3.2 / 84.1)
- Baseline error rate: 15.9%
- CappinCheck error rate: 12.7%
- Relative error rate reduction: 20.1% (3.2 / 15.9)
- Detected benchmark rows: Baseline = 84.1%, CappinCheck = 87.3%.
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- Claimed improvement is 30.0%; computed relative improvement is 3.8% (difference 26.2 points).

**Counter-evidence:**
- We compare CappinCheck against a baseline claim-review pipeline on Benchmark X. The baseline system achieves 84.1% on the benchmark. CappinCheck achieves 87.3% on the same benchmark. | System | Benchmark X accuracy | | --- | ---: | | Baseline | 84.1% | | CappinCheck | 87.3% | (Demo Paper: CappinCheck for Agentic Claim Audits)
- We did not run an external literature search for prior scientific fact-checking or claim-audit systems. (Demo Paper: CappinCheck for Agentic Claim Audits)

**Missing context:**
- The specific baseline, task, or metric that shows a 30% improvement over prior work is completely missing from the paper.
- The paper does not provide the formula, metric, or justification used to calculate the 30% performance improvement figure.
- The exact specifications, architecture, and source of the 'baseline claim-review pipeline' are not documented.
- The paper lacks any other performance evaluations or external comparisons besides the Benchmark X comparison.

