# ClaimLens Report: Demo Paper: ClaimLens for Agentic Claim Audits

Source: `examples/demo_document.md`

| Claim | Vibe | Formal Verdict | Cap Score | Confidence |
| --- | --- | --- | ---: | --- |
| Our method improves performance by 30% over prior work on real-world tasks. | cap | overstated | 88 | high |
| The system robustly generalizes across domains. | sus | missing_context | 64 | medium |
| This is the first agentic workflow for scientific claim auditing. | sus | missing_context | 64 | medium |

## c1: cap / overstated

**Original:** Our method improves performance by 30% over prior work on real-world tasks.

**Cap Score:** 88/100

**Why:** The reported benchmark numbers show improvement, but the stated 30% improvement does not match the arithmetic and the evidence is a curated benchmark, not real-world tasks.

**Defensible rewrite:** Our method improves performance from 84.1% to 87.3% on Benchmark X, a 3.2-point absolute gain and 3.8% relative improvement.

**Numeric findings:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

**Supporting evidence:**
- Baseline: 84.1%. ClaimLens: 87.3%. (Demo document benchmark table)

**Missing context:**
- No real-world deployment task is reported in the demo document.


## c2: sus / missing_context

**Original:** The system robustly generalizes across domains.

**Cap Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Missing context:**
- Additional external grounding would be needed for a production verdict.


## c3: sus / missing_context

**Original:** This is the first agentic workflow for scientific claim auditing.

**Cap Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Missing context:**
- Additional external grounding would be needed for a production verdict.

