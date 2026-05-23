# CappinCheck Report: Demo Paper: CappinCheck for Agentic Claim Audits

Source: `examples/demo_document.md`

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

### Evidence Contrast

**Claim says:** Our method improves performance by 30% over prior work on real-world tasks.

**Best reference says:** The reference reports 84.1% for the baseline and 87.3% for CappinCheck on Benchmark X.

**Key qualification:** The evidence is one curated benchmark, not real-world tasks; the computed gain is 3.2 percentage points and 3.8% relative.

**Delta:** narrower_than_claim — The reference supports a narrower benchmark improvement, but not a 30% improvement on real-world tasks.

**Final verdict:** overstated

**Defensible rewrite:** CappinCheck improves from 84.1% to 87.3% on Benchmark X, a 3.2 percentage-point gain and 3.8% relative improvement under the benchmark conditions.

### Sources Checked

- Benchmark X Report (benchmark, authority 85/100): https://example.org/benchmark-x-report. Contains the baseline and CappinCheck benchmark scores used by the claim.

**Reference snippets / mismatches:**
- The reference reports 84.1% for the baseline and 87.3% for CappinCheck on Benchmark X. (Benchmark X Report, narrows, https://example.org/benchmark-x-report). The evidence is one curated benchmark, not real-world tasks; the computed gain is 3.2 percentage points and 3.8% relative.

**Numeric findings:**
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

### Evidence Contrast

**Claim says:** The system robustly generalizes across domains.

**Best reference says:** The reference describes curated technical claims from public documents.

**Key qualification:** It does not evaluate clinical, legal, private-enterprise, or real-world deployment settings.

**Delta:** missing_context — The claim generalizes beyond the reference, which only supports performance on curated Benchmark X.

**Final verdict:** missing_context

**Defensible rewrite:** CappinCheck generalizes across the curated domains represented in Benchmark X; real-world deployment performance was not evaluated.

### Sources Checked

- Benchmark X Report (benchmark, authority 85/100): https://example.org/benchmark-x-report. Defines the evaluation setting and its limitations.

**Reference snippets / mismatches:**
- The reference describes curated technical claims from public documents. (Benchmark X Report, narrows, https://example.org/benchmark-x-report). It does not evaluate clinical, legal, private-enterprise, or real-world deployment settings.

**Missing context:**
- Additional external grounding would be needed for a production verdict.


## c3: missing_context

**Confidence:** medium

**Original:** This is the first agentic workflow for scientific claim auditing.

**Stretch Score:** 64/100

**Why:** The claim may be plausible, but the demo document does not provide enough scope or external evidence.

**Defensible rewrite:** The document provides preliminary evidence for a narrower version of this claim.

**Missing context:**
- Additional external grounding would be needed for a production verdict.

