# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

| Claim | Formal Verdict | Confidence | Vibe | Cap Score |
| --- | --- | --- | --- | ---: |
| Our method improves performance by 30% over prior work on real-world tasks. | overstated | high | cap | 88 |
| The system robustly generalizes across domains. | missing_context | medium | sus | 64 |
| This is the first agentic workflow for scientific claim auditing. | missing_context | medium | sus | 64 |

## c1: overstated

**Confidence:** high

**Vibe:** cap

**Original:** Our method improves performance by 30% over prior work on real-world tasks.

**Cap Score:** 88/100

**Why:** The reported benchmark numbers show improvement, but the stated 30% improvement does not match the arithmetic and the evidence is a curated benchmark, not real-world tasks.

**Defensible rewrite:** Our method improves performance from 84.1% to 87.3% on Benchmark X, a 3.2-point absolute gain and 3.8% relative improvement.

**Numeric findings:**
- Absolute gain: 87.3 - 84.1 = 3.2 points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.

**Supporting evidence found:**
- Baseline: 84.1%. CappinCheck: 87.3%. (Demo document benchmark table). Relevance: The table supports a 3.2-point absolute gain, not a 30% relative improvement.

**Missing context:**
- No real-world deployment task is reported in the demo document.


## c2: missing_context

**Confidence:** medium

**Vibe:** sus

**Original:** The system robustly generalizes across domains.

**Cap Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Missing context:**
- Additional external grounding would be needed for a production verdict.


## c3: missing_context

**Confidence:** medium

**Vibe:** sus

**Original:** This is the first agentic workflow for scientific claim auditing.

**Cap Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Missing context:**
- Additional external grounding would be needed for a production verdict.

