# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

| Claim | Vibe | Formal Verdict | Cap Score | Confidence |
| --- | --- | --- | ---: | --- |
| improves performance by 30% over prior work | cap | overstated | 87 | high |

## claim_1: cap / overstated

**Original:** improves performance by 30% over prior work

**Cap Score:** 87/100

**Why:** The claim of a 30% performance improvement is mathematically irreconcilable with the actual results presented in the paper. The baseline system achieves 84.1% accuracy and CappinCheck achieves 87.3% accuracy on Benchmark X. This represents a 3.2 percentage point absolute increase, a ~3.8% relative accuracy improvement, or a ~20.1% relative reduction in the error rate. No standard mathematical formulation supports the 30% figure.

**Defensible rewrite:** CappinCheck improves from 84.1% to 87.3% versus Baseline, a 3.2-point absolute gain and 3.8% relative improvement.

**Numeric findings:**
- Baseline system accuracy: 84.1%
- CappinCheck accuracy: 87.3%
- Absolute accuracy improvement: 3.2 percentage points (87.3% - 84.1%)
- Relative accuracy improvement: ~3.8% ((87.3 - 84.1) / 84.1)
- Relative error rate reduction: ~20.1% ((15.9 - 12.7) / 15.9)
- Detected benchmark rows: Baseline = 84.1%, CappinCheck = 87.3%.
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- Claimed improvement is 30.0%; computed relative improvement is 3.8% (difference 26.2 points).

**Counter-evidence:**
- We compare CappinCheck against a baseline claim-review pipeline on Benchmark X. The baseline system achieves 84.1% on the benchmark. CappinCheck achieves 87.3% on the same benchmark. (Demo Paper: CappinCheck for Agentic Claim Audits)

**Missing context:**
- There is no mathematical explanation, alternative metric definition, or prior baseline in the text that justifies how the 30% improvement figure was calculated.

