# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

| Claim | Vibe | Formal Verdict | Cap Score | Confidence |
| --- | --- | --- | ---: | --- |
| We introduce CappinCheck, an agentic workflow that improves performance by 30% over prior work on real-world tasks. | cap | contradicted | 90 | high |

## claim_01: cap / contradicted

**Original:** We introduce CappinCheck, an agentic workflow that improves performance by 30% over prior work on real-world tasks.

**Cap Score:** 90/100

**Why:** The claim of a 30% performance improvement over prior work on real-world tasks is contradicted by the evaluation. The paper reports only a 3.2% absolute (3.8% relative) accuracy improvement over a single local baseline on Benchmark X, with no evaluation of real-world tasks or comparison to prior established literature.

**Defensible rewrite:** We introduce CappinCheck, an agentic workflow that achieves a 3.2% absolute accuracy improvement (increasing performance from 84.1% to 87.3%) over a local baseline pipeline on Benchmark X.

**Numeric findings:**
- Baseline accuracy: 84.1%
- CappinCheck accuracy: 87.3%
- Actual absolute improvement: 3.2%
- Actual relative accuracy improvement: 3.8%
- Relative reduction in error rate: 20.13% (from 15.9% to 12.7%)
- Claimed performance improvement: 30%
- Detected benchmark rows: Baseline = 84.1%, CappinCheck = 87.3%.
- Absolute gain: 87.3 - 84.1 = 3.2 percentage points.
- Relative gain: (3.2 / 84.1) * 100 = 3.8%.
- Claimed improvement is 30.0%; computed relative improvement is 3.8% (difference 26.2 points).

**Counter-evidence:**
- We compare CappinCheck against a baseline claim-review pipeline on Benchmark X. The baseline system achieves 84.1% on the benchmark. CappinCheck achieves 87.3% on the same benchmark. (Demo Paper: CappinCheck for Agentic Claim Audits)
- We did not evaluate prospective real-world deployment, clinical documents, legal documents, or private enterprise workflows. (Demo Paper: CappinCheck for Agentic Claim Audits)
- We did not run an external literature search for prior scientific fact-checking or claim-audit systems. (Demo Paper: CappinCheck for Agentic Claim Audits)

**Missing context:**
- The evaluation was restricted entirely to public technical claims curated within a static dataset (Benchmark X) with no prospective, clinical, legal, or live real-world deployment.
- The baseline pipeline used for comparison is undefined, making it impossible to assess if it represents a strong modern competitor.

