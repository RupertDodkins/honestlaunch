# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

| Claim | Vibe | Formal Verdict | Cap Score | Confidence |
| --- | --- | --- | ---: | --- |
| We introduce CappinCheck, an agentic workflow that improves performance by 30% over prior work on real-world tasks. | cap | contradicted | 95 | high |

## claim_1: cap / contradicted

**Original:** We introduce CappinCheck, an agentic workflow that improves performance by 30% over prior work on real-world tasks.

**Cap Score:** 95/100

**Why:** The claim of a 30% performance improvement is mathematically contradicted by the paper's results, which show only a 3.2% absolute (3.8% relative) improvement on Benchmark X (87.3% vs 84.1%). Furthermore, the assertion of evaluating on 'real-world tasks' and improving over 'prior work' is directly contradicted by the authors' admissions that they did not evaluate prospective real-world deployments and did not conduct an external literature search for prior work.

**Defensible rewrite:** We introduce CappinCheck, an agentic workflow that improves performance by 3.2% absolute (3.8% relative) over a baseline claim-review pipeline on Benchmark X.

**Numeric findings:**
- Baseline accuracy on Benchmark X: 84.1%
- CappinCheck accuracy on Benchmark X: 87.3%
- Absolute accuracy improvement: 3.2 percentage points
- Relative accuracy improvement: ~3.8%
- Relative error rate reduction: ~20.1%
- Claimed performance improvement: 30%

**Counter-evidence:**
- We compare CappinCheck against a baseline claim-review pipeline on Benchmark X. The baseline system achieves 84.1% on the benchmark. CappinCheck achieves 87.3% on the same benchmark. (Demo Paper: CappinCheck for Agentic Claim Audits)
- The benchmark contains curated technical claims from public documents. We did not evaluate prospective real-world deployment, clinical documents, legal documents, or private enterprise workflows. (Demo Paper: CappinCheck for Agentic Claim Audits - Discussion)
- We did not run an external literature search for prior scientific fact-checking or claim-audit systems. (Demo Paper: CappinCheck for Agentic Claim Audits - Discussion)

**Missing context:**
- The mathematical basis for the 30% improvement claim is completely absent from the text.
- No evaluation or metrics for real-world tasks other than Benchmark X are presented.
- The text lacks any explanation of what prior work was compared against, other than a single baseline pipeline.

