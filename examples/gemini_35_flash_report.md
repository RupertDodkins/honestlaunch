# CappinCheck Report: Gemini 3.5: frontier intelligence with action

Source: `https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/`

## Provenance

- Mode: `live_gemini`
- Model: `gemini-3.5-flash`
- Pipeline wall: `130.80s`
- Load / Extract / Audit / Contrast: `386ms` / `23.03s` / `107.38s` / `27.03s`
- Claims extracted / audited: `8` / `4`
- Specialist passes / unique sources: `12` / `13`

- Evidence Contrast: `enabled`
- Provided reference URLs: `https://deepmind.google/models/model-cards/gemini-3-5-flash`

## Scorecard

- Claims audited: `4`
- Verdict counts: `supported=0` · `overstated=2` · `missing_context=2` · `contradicted=0` · `not_checkable=0`
- Average stretch score: `59/100`
- Provided reference URL count: `1`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| Gemini 3.5 Flash outperforms Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). | missing_context | high | 40 |
| When looking at output tokens per second, 3.5 Flash is 4 times faster than other frontier models. | missing_context | high | 35 |
| What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. | overstated | high | 80 |
| Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. | overstated | high | 80 |

## 1: missing_context

**Confidence:** high

**Original:** Gemini 3.5 Flash outperforms Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).

**Stretch Score:** 40/100

**Why:** The claim accurately reflects Google's self-reported benchmark figures for Gemini 3.5 Flash. However, it lacks critical context regarding the non-uniform evaluation conditions. Specifically, the compared Gemini 3.1 Pro baselines were sourced from public third-party leaderboards rather than evaluated under identical local configurations. Additionally, achieving these results required configuring Gemini 3.5 Flash in a non-default 'high' thinking mode (which increases token consumption and cost), there was no documented training data decontamination, and Gemini 3.5 Flash actually regresses compared to Gemini 3.1 Pro on long-context retrieval, abstract reasoning, and hard academic exams.

**Defensible rewrite:** Based on self-reported and public leaderboard data, Gemini 3.5 Flash (configured with high thinking settings) scores higher than Gemini 3.1 Pro on specific coding, agentic, and multimodal benchmarks, including Terminal-Bench 2.1 (76.2% vs 70.3%), GDPval-AA (1656 Elo vs 1314 Elo), MCP Atlas (83.6% vs 78.2%), and CharXiv Reasoning (84.2% vs 83.3%), though it does not outperform the Pro model across all domains.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 80.35s / 37.28s / 39.29s / 22.58s / 41.04s / 0ms

### Agent Steps

<details><summary>grounded_verifier: The claim accurately reflects the official benchmark numbers published by Google for Gemini 3.5 Flash. However, the audit reveals that the evaluation datasets were not documented as tested for training data contamination, and identical prompt structures, hardware configurations, or API settings were not uniformly used to compare the models. Google's Model Evaluation PDF outlines that several benchmark scores (such as GDPval-AA and MCP Atlas) were sourced directly from third-party public leaderboards (e.g., ScaleAI, Artificial Analysis) where testing environments vary. For self-computed evaluations, Google ran the tests using the Gemini API with default sampling settings, which differs from competitors' API configurations and local hardware setups.</summary>

**Duration:** 37.28s

**Supporting evidence:**
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Directly confirms the claimed performance metrics for Gemini 3.5 Flash and its outperformance over Gemini 3.1 Pro on the specific benchmarks.
- Methodology: All Gemini scores are pass @1 except where otherwise noted. All of the results are all run with the Gemini API for the model-id gemini-3.5-flash with default sampling settings unless indicated otherwise below. ... All the results for non-Gemini models are sourced from providers' self reported numbers unless otherwise mentioned below. ... Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard. ... MCP Atlas results are reported from the ScaleAI official leaderboard. ... GDPval-AA results are sourced from the Artificial Analysis public leaderboard. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf)). Relevance: Documents the evaluation methodology, showing that baseline comparisons were not evaluated in identical controlled environments but were instead compiled from external third-party leaderboards and default vendor APIs.

**Missing context:**
- There is no documentation or disclosure in the official Gemini 3.5 Flash release regarding training data contamination tests for the evaluated benchmarks.
- Prompt structures, hardware configurations, and API settings were not identical across compared models, as many baseline scores were sourced directly from external public leaderboards.

**Computed checks:**
- Terminal-Bench 2.1: 76.2%
- GDPval-AA: 1656 Elo
- MCP Atlas: 83.6%
- CharXiv Reasoning: 84.2%

</details>

<details><summary>Skeptical Contradiction Finder: Google's claim that Gemini 3.5 Flash outperforms Gemini 3.1 Pro on challenging coding and agentic benchmarks is subject to major context gaps and evaluation mismatches. First, there is no documented decontamination testing to filter training data for benchmarks like Terminal-Bench 2.1, GDPval-AA, MCP Atlas, or CharXiv Reasoning. Second, Google did not evaluate Gemini 3.1 Pro and Gemini 3.5 Flash under identical local execution environments; for Terminal-Bench 2.1, Gemini 3.5 Flash's score was self-computed, while Gemini 3.1 Pro's score was pulled from a public leaderboard. Third, achieving these benchmark results required manually setting Gemini 3.5 Flash to 'high' thinking mode (its API default is 'medium'), which consumes massive token overhead and can make Flash more expensive than Pro to run on identical tasks. Lastly, Gemini 3.5 Flash actually regresses compared to Gemini 3.1 Pro on long-context retrieval, hard academic reasoning, and abstract puzzles.</summary>

**Duration:** 39.29s

**Contradictions / narrowing evidence:**
- Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard. Results are reported for the default agent harness (Terminus 2) only. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash - Googleapis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU34bE3F1HrUEGlL9c7_iLja9eWD08TBxNK7cDUGKUtRjdSUORNf-JmOF34tiHChk5PnnCSUpWrTiSTIg89MzgWA3-PNaGdNe0lHFNxbjSuJQXBGX27MT7JdhxIhTn92rA-JVvITDRGf3k_z4SF08hHkjZIGCGEGptyDOvF2afIdMsj7I0zo1NCWZGY-LrOTg=)). Relevance: Confirms a methodology mismatch: Google did not locally evaluate Gemini 3.1 Pro under identical scaffolding, but instead compared their own self-computed Flash numbers to third-party leaderboard scores.
- Lower scores on long-context and academic reasoning are expected: 3.5 Flash trades raw knowledge for agentic capability. ... MRCR v2 128k: -7.6. Humanity's Last Exam: -4.2. ARC-AGI-2: -5.0. Gemini 3.1 Pro: 84.9%, 44.4%, 77.1%. Gemini 3.5 Flash: 77.3%, 40.2%, 72.1%. ([Gemini 3.5 Flash: Benchmarks, Pricing, and Complete Specs - LLM Stats](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWkYYgrGmzArT26xMMNADslIpPD8C7grVcGBS70u597mu8XnVT_KscnAapOy2-wBYCDogks5LBhrFTOaenEFXmbCwuQ9zrJ7Z9YJqaul1004_HFsZUgP5Fv0INV5mHwW0pTvNhDMLgVZrMgmLf9kCy9Q==)). Relevance: Demonstrates that the performance gains are not uniform across the board; Gemini 3.5 Flash underperforms Gemini 3.1 Pro on long-context, abstract reasoning, and expert academic knowledge benchmarks.
- So Gemini 3.5 Flash scores slightly lower than Gemini 3.1 Pro, 55 vs 57, but costs more in their benchmark, $1,552 vs $892. The per-token API price is lower than Pro, but the total benchmark cost ends up higher. ([Gemini 3.5 Flash looks worse than it seems on Artificial Analysis : r/singularity - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgdI8LIPIptm6xHS6EUUcjx5DKSFlkxx_RIAaeecqUhpCxj0sDOWjf9sYkf3w-sCSstdC6GTHUdSgRCxBLCM_7rPmrR6bl98_7jectq_B5ngQCUz8SxH31Dgimi2PlN4FvBexycqijzFAcPBTppYlTUMds0sAkWVP4-ESoc_guTI2T1F2qaIV0zohYsgvH7ZOUzjJ8jtqnqc8=)). Relevance: Exposes that the 'high' thinking levels required to match Pro-level agentic capabilities consume excessive reasoning tokens, offsetting Flash's raw token pricing advantages.

**Missing context:**
- No training data decontamination or contamination testing is documented by Google for Gemini 3.5 Flash against Terminal-Bench 2.1, GDPval-AA, MCP Atlas, or CharXiv Reasoning.
- For most benchmarks (such as Terminal-Bench 2.1, GDPval-AA, and MCP Atlas), Google compared self-computed scores directly to public leaderboard records of competitor models and Gemini 3.1 Pro rather than running identical prompts and local configurations.
- The benchmark numbers reflect a manually enabled non-default configuration ('high' thinking level) for Gemini 3.5 Flash, which has a standard API default of 'medium'. Standard settings yield higher hallucination rates and lower logic consistency in third-party testing.
- While Gemini 3.5 Flash leads on highlighted agentic tasks, it regresses compared to Gemini 3.1 Pro on multi-needle retrieval (77.3% vs 84.9%), abstract reasoning (72.1% vs 77.1%), and hard academic exams (40.2% vs 44.4%).

**Computed checks:**
- Terminal-Bench 2.1: Gemini 3.5 Flash (76.2%) vs Gemini 3.1 Pro (70.3%)
- MCP Atlas: Gemini 3.5 Flash (83.6%) vs Gemini 3.1 Pro (78.2%)
- CharXiv Reasoning: Gemini 3.5 Flash (84.2%) vs Gemini 3.1 Pro (83.3%)
- GDPval-AA: Gemini 3.5 Flash (1656 Elo) vs Gemini 3.1 Pro (1314 Elo)
- Long-Context Retrieval (MRCR v2 128k average): Gemini 3.5 Flash (77.3%) vs Gemini 3.1 Pro (84.9%)
- Humanity's Last Exam: Gemini 3.5 Flash (40.2%) vs Gemini 3.1 Pro (44.4%)
- ARC-AGI-2: Gemini 3.5 Flash (72.1%) vs Gemini 3.1 Pro (77.1%)

</details>

<details><summary>numeric_calibrator: The claim states that Gemini 3.5 Flash outperforms Gemini 3.1 Pro on challenging coding, agentic, and multimodal benchmarks. However, the provided document lacks the comparative benchmark scores for Gemini 3.1 Pro, as well as crucial methodology details regarding training data contamination testing, prompt structures, hardware configurations, and API settings used to compare the models. External sources, such as the Gemini 3.5 Flash Model Card, provide the necessary comparative scores: Terminal-Bench 2.1 (Gemini 3.1 Pro: 70.3%), GDPval-AA (Gemini 3.1 Pro: 1314 Elo), MCP Atlas (Gemini 3.1 Pro: 78.2%), and CharXiv Reasoning (Gemini 3.1 Pro: 83.3%). Calculating the deltas shows that Gemini 3.5 Flash improves over Gemini 3.1 Pro by 5.9 percentage points (8.39% relative) on Terminal-Bench 2.1, 342 Elo points (26.03% relative) on GDPval-AA, 5.4 percentage points (6.91% relative) on MCP Atlas, and 0.9 percentage points (1.08% relative) on CharXiv Reasoning.</summary>

**Duration:** 22.58s

**Supporting evidence:**
- Coding, Terminal-bench 2.1 Agentic terminal coding, Terminus-2 harness, 76.2%, 58.0%, 70.3%... Agentic, MCP Atlas Multi-step workflows... 83.6%, 62.0%, 78.2% ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBFrdLzoAQGusiKkJUUUHlbNGoA9lthfyVuawcYmFQi9kBZEj7ZwUspnuHd1b7bRLc_8HNbgSTkwLJCloX4qF5ZVrEtCCYn3IJiOOAQRch-_3M9vmq7xFnHHnN00Nvf3iL7eBiafbBRT93dw-wIo1G8S0=)). Relevance: Provides the baseline comparison scores for Gemini 3.1 Pro on Terminal-Bench 2.1 and MCP Atlas, allowing the calculation of performance improvements.
- Expert Tasks, GDPval-AA (economically valuable knowledge work, Elo), 1656, 1204, 1314... Multimodal, CharXiv Reasoning (information synthesis from complex charts), 84.2%, 80.3%, 83.3% ([Gemini 3.5 Flash Is Impressive. Here's What We Actually Found. - Truefoundry](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9emqiQBARa-bcwlQmHs5s3V8AamcF__mtLqwkFBKn6huzKUXZFx_lOqBJKATPsdMbLAnhbUqjgUdVFkFs6bCtLn6YAGRfXIUPg9Q8Nb_I2WEDs-ak0ggkM6uYPvdMmaj-O1Nd_kG2UHZ9qJy7suuL9Jp6VEXCTAQ1gGZcNeUMaotn00HRdLhavzr4qfQiAKIu8snffo0=)). Relevance: Provides the baseline comparison scores for Gemini 3.1 Pro on GDPval-AA and CharXiv Reasoning, allowing the calculation of performance improvements.

**Missing context:**
- The benchmark scores for Gemini 3.1 Pro (Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning) are missing from the original document.
- Any discussion or reporting of contamination testing for evaluation datasets is missing.
- Details about identical prompt structures, hardware configurations, and API settings used during benchmarking are missing.

**Computed checks:**
- Terminal-Bench 2.1: Gemini 3.5 Flash (76.2%) vs Gemini 3.1 Pro (70.3%). Absolute Delta = 76.2% - 70.3% = 5.9 percentage points. Relative Delta = (76.2% - 70.3%) / 70.3% = 8.39% relative improvement.
- GDPval-AA: Gemini 3.5 Flash (1656 Elo) vs Gemini 3.1 Pro (1314 Elo). Absolute Delta = 1656 - 1314 = 342 Elo points. Relative Delta = (1656 - 1314) / 1314 = 26.03% relative improvement.
- MCP Atlas: Gemini 3.5 Flash (83.6%) vs Gemini 3.1 Pro (78.2%). Absolute Delta = 83.6% - 78.2% = 5.4 percentage points. Relative Delta = (83.6% - 78.2%) / 78.2% = 6.91% relative improvement.
- CharXiv Reasoning: Gemini 3.5 Flash (84.2%) vs Gemini 3.1 Pro (83.3%). Absolute Delta = 84.2% - 83.3% = 0.9 percentage points. Relative Delta = (84.2% - 83.3%) / 83.3% = 1.08% relative improvement.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `high` confidence.</summary>

**Duration:** 41.04s

**Supporting evidence:**
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Directly confirms the claimed performance metrics for Gemini 3.5 Flash.
- Coding, Terminal-bench 2.1 Agentic terminal coding, Terminus-2 harness, 76.2%, 58.0%, 70.3%... Agentic, MCP Atlas Multi-step workflows... 83.6%, 62.0%, 78.2% ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBFrdLzoAQGusiKkJUUUHlbNGoA9lthfyVuawcYmFQi9kBZEj7ZwUspnuHd1b7bRLc_8HNbgSTkwLJCloX4qF5ZVrEtCCYn3IJiOOAQRch-_3M9vmq7xFnHHnN00Nvf3iL7eBiafbBRT93dw-wIo1G8S0=)). Relevance: Provides the comparative benchmark scores for Gemini 3.1 Pro on Terminal-Bench 2.1 and MCP Atlas.
- Expert Tasks, GDPval-AA (economically valuable knowledge work, Elo), 1656, 1204, 1314... Multimodal, CharXiv Reasoning (information synthesis from complex charts), 84.2%, 80.3%, 83.3% ([Gemini 3.5 Flash Is Impressive. Here's What We Actually Found. - Truefoundry](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9emqiQBARa-bcwlQmHs5s3V8AamcF__mtLqwkFBKn6huzKUXZFx_lOqBJKATPsdMbLAnhbUqjgUdVFkFs6bCtLn6YAGRfXIUPg9Q8Nb_I2WEDs-ak0ggkM6uYPvdMmaj-O1Nd_kG2UHZ9qJy7suuL9Jp6VEXCTAQ1gGZcNeUMaotn00HRdLhavzr4qfQiAKIu8snffo0=)). Relevance: Provides comparative baseline scores for Gemini 3.1 Pro on GDPval-AA and CharXiv Reasoning.

**Contradictions / narrowing evidence:**
- Methodology: All Gemini scores are pass @1 except where otherwise noted. All of the results are all run with the Gemini API for the model-id gemini-3.5-flash with default sampling settings unless indicated otherwise below. ... Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard. ... MCP Atlas results are reported from the ScaleAI official leaderboard. ... GDPval-AA results are sourced from the Artificial Analysis public leaderboard. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf)). Relevance: Confirms that comparative scores were pulled from external leaderboards rather than evaluated under identical local setups.
- Lower scores on long-context and academic reasoning are expected: 3.5 Flash trades raw knowledge for agentic capability. ... MRCR v2 128k: -7.6. Humanity's Last Exam: -4.2. ARC-AGI-2: -5.0. Gemini 3.1 Pro: 84.9%, 44.4%, 77.1%. Gemini 3.5 Flash: 77.3%, 40.2%, 72.1%. ([Gemini 3.5 Flash: Benchmarks, Pricing, and Complete Specs - LLM Stats](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWkYYgrGmzArT26xMMNADslIpPD8C7grVcGBS70u597mu8XnVT_KscnAapOy2-wBYCDogks5LBhrFTOaenEFXmbCwuQ9zrJ7Z9YJqaul1004_HFsZUgP5Fv0INV5mHwW0pTvNhDMLgVZrMgmLf9kCy9Q==)). Relevance: Shows performance regressions of Gemini 3.5 Flash relative to Gemini 3.1 Pro in academic and abstract reasoning tasks.
- So Gemini 3.5 Flash scores slightly lower than Gemini 3.1 Pro, 55 vs 57, but costs more in their benchmark, $1,552 vs $892. The per-token API price is lower than Pro, but the total benchmark cost ends up higher. ([Gemini 3.5 Flash looks worse than it seems on Artificial Analysis : r/singularity - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgdI8LIPIptm6xHS6EUUcjx5DKSFlkxx_RIAaeecqUhpCxj0sDOWjf9sYkf3w-sCSstdC6GTHUdSgRCxBLCM_7rPmrR6bl98_7jectq_B5ngQCUz8SxH31Dgimi2PlN4FvBexycqijzFAcPBTppYlTUMds0sAkWVP4-ESoc_guTI2T1F2qaIV0zohYsgvH7ZOUzjJ8jtqnqc8=)). Relevance: Details the trade-offs of the high thinking level required to achieve these scores, noting higher token consumption and total cost compared to Pro.

**Missing context:**
- The baseline comparative scores for Gemini 3.1 Pro are omitted from the main blog post.
- The evaluation was not conducted under identical prompt, API, or local hardware configurations, with several baseline scores sourced directly from third-party public leaderboards.
- No training data decontamination or contamination testing was documented for any of the evaluated benchmarks.
- To reach these top scores, Gemini 3.5 Flash requires a non-default 'high' thinking configuration which consumes significantly more tokens and increases operational cost.
- Gemini 3.5 Flash exhibits performance regressions compared to Gemini 3.1 Pro on long-context retrieval, abstract reasoning, and advanced academic exams.

**Computed checks:**
- Terminal-Bench 2.1: Gemini 3.5 Flash (76.2%) vs Gemini 3.1 Pro (70.3%) - Absolute Delta of +5.9 percentage points (+8.39% relative improvement)
- GDPval-AA: Gemini 3.5 Flash (1656 Elo) vs Gemini 3.1 Pro (1314 Elo) - Absolute Delta of +342 Elo points (+26.03% relative improvement)
- MCP Atlas: Gemini 3.5 Flash (83.6%) vs Gemini 3.1 Pro (78.2%) - Absolute Delta of +5.4 percentage points (+6.91% relative improvement)
- CharXiv Reasoning: Gemini 3.5 Flash (84.2%) vs Gemini 3.1 Pro (83.3%) - Absolute Delta of +0.9 percentage points (+1.08% relative improvement)
- Long-Context Retrieval (MRCR v2 128k average): Gemini 3.5 Flash (77.3%) vs Gemini 3.1 Pro (84.9%)
- Humanity's Last Exam: Gemini 3.5 Flash (40.2%) vs Gemini 3.1 Pro (44.4%)
- ARC-AGI-2: Gemini 3.5 Flash (72.1%) vs Gemini 3.1 Pro (77.1%)

</details>

### Evidence Contrast

**Claim says:** Gemini 3.5 Flash outperforms Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).

**Best reference says:** Shows baseline scores for Gemini 3.1 Pro, indicating performance gains are specific to these benchmarks and not uniform across the board.

**Key qualification:** Scores for Gemini 3.1 Pro are provided, but lack identical-environment testing data.

**Delta:** missing_context — The claim omits the fact that the comparison relies on non-uniform test setups (self-computed vs public leaderboard) and non-default configurations (high-thinking mode), and ignores regressions in long-context and academic domains.

**Final verdict:** missing_context

**Defensible rewrite:** Based on self-reported and public leaderboard data, Gemini 3.5 Flash (configured with high thinking settings) scores higher than Gemini 3.1 Pro on specific coding, agentic, and multimodal benchmarks, including Terminal-Bench 2.1 (76.2% vs 70.3%), GDPval-AA (1656 Elo vs 1314 Elo), MCP Atlas (83.6% vs 78.2%), and CharXiv Reasoning (84.2% vs 83.3%), though it does not outperform the Pro model across all domains.

### Claim-Level Contrast References

- Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash (official_doc, authority 95/100): https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf. Provides details on evaluation methodologies and public leaderboard comparisons.

**Reference snippets / mismatches:**
- Shows baseline scores for Gemini 3.1 Pro, indicating performance gains are specific to these benchmarks and not uniform across the board. (Gemini 3.5 Flash - Model Card - Google DeepMind, narrows, https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBFrdLzoAQGusiKkJUUUHlbNGoA9lthfyVuawcYmFQi9kBZEj7ZwUspnuHd1b7bRLc_8HNbgSTkwLJCloX4qF5ZVrEtCCYn3IJiOOAQRch-_3M9vmq7xFnHHnN00Nvf3iL7eBiafbBRT93dw-wIo1G8S0=). Scores for Gemini 3.1 Pro are provided, but lack identical-environment testing data.

**Computed checks:**
- Terminal-Bench 2.1: Gemini 3.5 Flash (76.2%) vs Gemini 3.1 Pro (70.3%) - Absolute Delta of +5.9 percentage points (+8.39% relative improvement)
- GDPval-AA: Gemini 3.5 Flash (1656 Elo) vs Gemini 3.1 Pro (1314 Elo) - Absolute Delta of +342 Elo points (+26.03% relative improvement)
- MCP Atlas: Gemini 3.5 Flash (83.6%) vs Gemini 3.1 Pro (78.2%) - Absolute Delta of +5.4 percentage points (+6.91% relative improvement)
- CharXiv Reasoning: Gemini 3.5 Flash (84.2%) vs Gemini 3.1 Pro (83.3%) - Absolute Delta of +0.9 percentage points (+1.08% relative improvement)
- Long-Context Retrieval (MRCR v2 128k average): Gemini 3.5 Flash (77.3%) vs Gemini 3.1 Pro (84.9%)
- Humanity's Last Exam: Gemini 3.5 Flash (40.2%) vs Gemini 3.1 Pro (44.4%)
- ARC-AGI-2: Gemini 3.5 Flash (72.1%) vs Gemini 3.1 Pro (77.1%)

**Gemini-discovered supporting sources:**
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Directly confirms the claimed performance metrics for Gemini 3.5 Flash.
- Coding, Terminal-bench 2.1 Agentic terminal coding, Terminus-2 harness, 76.2%, 58.0%, 70.3%... Agentic, MCP Atlas Multi-step workflows... 83.6%, 62.0%, 78.2% ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBFrdLzoAQGusiKkJUUUHlbNGoA9lthfyVuawcYmFQi9kBZEj7ZwUspnuHd1b7bRLc_8HNbgSTkwLJCloX4qF5ZVrEtCCYn3IJiOOAQRch-_3M9vmq7xFnHHnN00Nvf3iL7eBiafbBRT93dw-wIo1G8S0=)). Relevance: Provides the comparative benchmark scores for Gemini 3.1 Pro on Terminal-Bench 2.1 and MCP Atlas.
- Expert Tasks, GDPval-AA (economically valuable knowledge work, Elo), 1656, 1204, 1314... Multimodal, CharXiv Reasoning (information synthesis from complex charts), 84.2%, 80.3%, 83.3% ([Gemini 3.5 Flash Is Impressive. Here's What We Actually Found. - Truefoundry](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9emqiQBARa-bcwlQmHs5s3V8AamcF__mtLqwkFBKn6huzKUXZFx_lOqBJKATPsdMbLAnhbUqjgUdVFkFs6bCtLn6YAGRfXIUPg9Q8Nb_I2WEDs-ak0ggkM6uYPvdMmaj-O1Nd_kG2UHZ9qJy7suuL9Jp6VEXCTAQ1gGZcNeUMaotn00HRdLhavzr4qfQiAKIu8snffo0=)). Relevance: Provides comparative baseline scores for Gemini 3.1 Pro on GDPval-AA and CharXiv Reasoning.

**Gemini-discovered caveat / counter sources:**
- Methodology: All Gemini scores are pass @1 except where otherwise noted. All of the results are all run with the Gemini API for the model-id gemini-3.5-flash with default sampling settings unless indicated otherwise below. ... Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard. ... MCP Atlas results are reported from the ScaleAI official leaderboard. ... GDPval-AA results are sourced from the Artificial Analysis public leaderboard. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf)). Relevance: Confirms that comparative scores were pulled from external leaderboards rather than evaluated under identical local setups.
- Lower scores on long-context and academic reasoning are expected: 3.5 Flash trades raw knowledge for agentic capability. ... MRCR v2 128k: -7.6. Humanity's Last Exam: -4.2. ARC-AGI-2: -5.0. Gemini 3.1 Pro: 84.9%, 44.4%, 77.1%. Gemini 3.5 Flash: 77.3%, 40.2%, 72.1%. ([Gemini 3.5 Flash: Benchmarks, Pricing, and Complete Specs - LLM Stats](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWkYYgrGmzArT26xMMNADslIpPD8C7grVcGBS70u597mu8XnVT_KscnAapOy2-wBYCDogks5LBhrFTOaenEFXmbCwuQ9zrJ7Z9YJqaul1004_HFsZUgP5Fv0INV5mHwW0pTvNhDMLgVZrMgmLf9kCy9Q==)). Relevance: Shows performance regressions of Gemini 3.5 Flash relative to Gemini 3.1 Pro in academic and abstract reasoning tasks.
- So Gemini 3.5 Flash scores slightly lower than Gemini 3.1 Pro, 55 vs 57, but costs more in their benchmark, $1,552 vs $892. The per-token API price is lower than Pro, but the total benchmark cost ends up higher. ([Gemini 3.5 Flash looks worse than it seems on Artificial Analysis : r/singularity - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgdI8LIPIptm6xHS6EUUcjx5DKSFlkxx_RIAaeecqUhpCxj0sDOWjf9sYkf3w-sCSstdC6GTHUdSgRCxBLCM_7rPmrR6bl98_7jectq_B5ngQCUz8SxH31Dgimi2PlN4FvBexycqijzFAcPBTppYlTUMds0sAkWVP4-ESoc_guTI2T1F2qaIV0zohYsgvH7ZOUzjJ8jtqnqc8=)). Relevance: Details the trade-offs of the high thinking level required to achieve these scores, noting higher token consumption and total cost compared to Pro.

**Missing context:**
- The baseline comparative scores for Gemini 3.1 Pro are omitted from the main blog post.
- The evaluation was not conducted under identical prompt, API, or local hardware configurations, with several baseline scores sourced directly from third-party public leaderboards.
- No training data decontamination or contamination testing was documented for any of the evaluated benchmarks.
- To reach these top scores, Gemini 3.5 Flash requires a non-default 'high' thinking configuration which consumes significantly more tokens and increases operational cost.
- Gemini 3.5 Flash exhibits performance regressions compared to Gemini 3.1 Pro on long-context retrieval, abstract reasoning, and advanced academic exams.


## 2: missing_context

**Confidence:** high

**Original:** When looking at output tokens per second, 3.5 Flash is 4 times faster than other frontier models.

**Stretch Score:** 35/100

**Why:** While independent benchmarks confirm that Gemini 3.5 Flash's raw output throughput (~280-289 tokens/sec) is roughly 4 times faster than heavy flagship models like GPT-5.5 (~65-71 tokens/sec) and Claude Opus 4.7 (~50-67 tokens/sec), the claim lacks critical context. First, the 4x comparison evaluates a lightweight, speed-optimized model against premium flagship models rather than its direct peers. Second, it omits Gemini 3.5 Flash's high Time to First Token (TTFT) of 18.55 seconds. Third, raw output token speed does not translate to a 4x speedup in practical, end-to-end agentic workflows due to reasoning and tool-calling overheads.

**Defensible rewrite:** In terms of raw output throughput, Gemini 3.5 Flash generates over 280 tokens per second, making it roughly 4 times faster than larger flagship models like GPT-5.5 and Claude Opus 4.7, though total workflow speedups will vary due to latency overheads.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 53.39s / 33.64s / 31.01s / 18.09s / 19.70s / 0ms

### Agent Steps

<details><summary>Grounded Verifier: The claim that Gemini 3.5 Flash is 4 times faster than other frontier models is supported by independent benchmarking data from Artificial Analysis (as of May 2026). Artificial Analysis measured Gemini 3.5 Flash at 289 tokens per second, compared to competitors like GPT-5.5 (xhigh) at 71 tokens/second and Claude Opus 4.7 (max) at 67 tokens/second (roughly 4 times faster). These serverless API measurements are conducted using a standard 10k input token workload with at least 1,500 answer tokens under a single-prompt scenario (concurrency of 1) or parallel prompt scenario (concurrency of 10 with 1k input/output tokens). Hardware environments and server-side batch sizes are not disclosed since the endpoints are serverless and managed by the providers (Google AI Studio, OpenAI, Anthropic).</summary>

**Duration:** 33.64s

**Supporting evidence:**
- Speed: The 4x Number. Google's headline performance claim is that Gemini 3.5 Flash is roughly 4x faster in output tokens per second than other frontier models. The supporting data comes from Artificial Analysis (as of May 13, 2026): Gemini 3.5 Flash: 289 tokens/sec; Gemini 3.1 Pro: 135 tokens/sec; GPT-5.5 (xhigh): 71 tokens/sec; Claude Opus 4.7 (max): 67 tokens/sec. ([How to Use Gemini 3.5 Flash: Complete Guide to Google's Fastest AI Model (2026)](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBnMRELXP9QWyK4ypPWNeHKdJxDIY0EmiQkc7bknDJgwJP7sxdOm8gvGB_ymhFkNFjec1KovzLobHwxjRgcKF4mvpz36c5w7WBCuAnQbdfEsPFyvMeVRmFpQiS_TB7Nw_VpvFvZUz6uJXQLG0cBKsS)). Relevance: Identifies the exact output speeds (in tokens per second) and specific competitor frontier models (GPT-5.5 xhigh and Claude Opus 4.7 max) used in the 4x speed comparison.
- Workload type, Description. 10k input token, Approximately 10,000 input tokens, at least 1,500 answer tokens (default benchmark on our website). ... Load Scenarios. Single prompt, One prompt is sent to the model's API at a time. Parallel prompts, 10 prompts are sent to the model's API simultaneously. For our multiple or parallel workload test, we send 10 concurrent requests of our standard 1k input token workload once per day. ([Artificial Analysis Language Model API Performance Benchmarking Methodology](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6X-6k1UXMla8oOFLdtm2HEiEZwfrNNahSwYP6rYQO6rwBLeJYtZGicLhAHFaEHB9Wvc1UQC8c0ho95khGaKqnes3tQ_fRlg1wSygubLPEJe8BWSLO0DP2AQKv_3g4Lpn7Vz_Wkw37sBljleGmjpSEMvHWI8kKrJ8=)). Relevance: Documents the exact input/output token lengths (10k input / 1.5k answer tokens) and concurrency rates (1 for single prompt, 10 for parallel prompts) used in the throughput measurements.
- Gemini 3.5 Flash achieves speeds of over 280 output tokens per second, ~70% faster than Gemini 3 Flash and models such as gpt-oss-120b and GPT-5.4 mini (xhigh). ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIyJF2E6B6m1tmKc46opNDezsUg_VLRDaeK_QOac5HHVdPjQtUY3LwayqEN7D3A16_OAfmyHTy-rhUwbUSgLZwe4fS96HWfvgXdpatwNju5uLqv_ila5FpCOzitb0KF6RB3ZD8C-cT_kTEy6SGxzSlYJjapjJzlrXURJHQQSqaAxPdX9E619tAWg==)). Relevance: Provides third-party verification that Gemini 3.5 Flash achieves more than 280 output tokens per second.

**Missing context:**
- The exact hardware environments (such as specific TPU or GPU configurations) are not disclosed in serverless API benchmarks since they are proprietary and managed internally by the model providers (Google, OpenAI, Anthropic).
- The internal server-side batch sizes are abstracted away and not disclosed by the serverless hosting APIs.

**Computed checks:**
- Gemini 3.5 Flash output speed: 289 tokens per second (or over 280 tokens per second)
- Gemini 3.1 Pro output speed: 135 tokens per second
- GPT-5.5 (xhigh) output speed: 71 tokens per second
- Claude Opus 4.7 (max) output speed: 67 tokens per second
- Default benchmark workload length: Approximately 10,000 input tokens and at least 1,500 answer tokens
- Parallel workload concurrency: 10 concurrent requests using a 1,000 input/output token shape

</details>

<details><summary>Contradiction Finder Skill: Google claims that Gemini 3.5 Flash is 4x faster than other frontier models in output tokens per second, which maps to ~280-289 tokens/sec compared to competitors like GPT-5.5 (~71 tps) and Claude Opus 4.7 (~67 tps). However, Google's documentation omits critical hardware, concurrency, batch size, and prompt-length parameters used to establish this comparison. While raw output generation is fast, third-party benchmarks show the model suffers from high Time to First Token (TTFT) latency of 18.55 seconds and extreme verbosity (generating 73M tokens vs. a 36M average), inflating the benchmark evaluation cost to $1,551.60 (a 5.5x jump from Gemini 3 Flash). Furthermore, practitioners note that raw 4x token generation does not yield 4x speedups in agentic loops due to multi-turn reasoning and tool call overheads.</summary>

**Duration:** 31.01s

**Supporting evidence:**
- When looking at output tokens per second, it is 4 times faster than other frontier models. Landing in the top-right quadrant of the Artificial Analysis index, 3.5 Flash delivers frontier-level intelligence at exceptional speed — proving you no longer have to trade quality for latency. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: States the original speed claim of being 4x faster on output throughput.

**Contradictions / narrowing evidence:**
- According to Google, 3.5 Flash 'outperforms Gemini 3.1 Pro' on most benchmarks and generates tokens '4 times faster than other frontier models.' Faster token generation reduces the part of an agent's time spent generating text, and for agentic coding that text portion is often large (long plans, lots of code output, multi-turn reasoning). So agents get faster, but not 4x. ([Google Launched Antigravity 2.0 with Gemini 3.5 Flash. Will Agents Be 4x Faster? | Belitsoft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4c2946iGq8_9aK24fntNfENtTWxgWlHI5KutLowV2zY8jAlslhHqFDlnmm2EGYcto5kxcDvh3WZcL17iExdx_EJAX1y5pjw-CDbXzdBg_4iPZTlmwDSAaLn8bAQE1F2Sl6jTPRfaIb1EGJeQ==)). Relevance: Directly contradicts the implication that the 4x token generation rate yields a 4x overall speedup in agentic workflows, identifying text generation as only a partial slice of total wall-clock execution time.

**Missing context:**
- Neither Google's announcement nor the official Model Evaluation Methodology document specifies the exact hardware environments, batch sizes, quantization levels, concurrency rates, or input/output token lengths used to measure the claimed 4x throughput improvement.
- The comparison evaluates Gemini 3.5 Flash—a lightweight, speed-optimized model—against much larger, premium flagship models (such as GPT-5.5 and Claude Opus 4.7), which naturally prioritize complex reasoning depth over raw generation speed.
- The model exhibits an exceptionally high Time to First Token (TTFT) latency of 18.55 seconds on Google's API, compared to a median of 2.70 seconds for models in its price class.
- While the output speed is high, Gemini 3.5 Flash has a major verbosity issue, generating 73 million tokens in the Artificial Analysis Index compared to a 35-36 million token average. This high volume of output drives up total benchmark operational costs to $1,551.60—which is 5.5x higher than Gemini 3 Flash and 75% more costly than evaluating Gemini 3.1 Pro.

**Computed checks:**
- 280 to 289 tokens per second
- 18.55 seconds Time to First Token (TTFT)
- 73 million output tokens generated vs 36 million average
- 5.5x increase in operational benchmark cost
- $1,551.60 cost to run the Artificial Analysis Intelligence Index

</details>

<details><summary>numeric_calibrator: The claim that Gemini 3.5 Flash is 4 times faster than other frontier models is directionally validated by independent external benchmarks (such as Artificial Analysis), which show Flash generating ~284 to 289 output tokens per second compared to ~67 to 71 tokens per second for comparable frontier models like Claude Opus 4.7 and GPT-5.5. However, the original document lacks the necessary absolute numbers and technical benchmarks to verify this claim directly.</summary>

**Duration:** 18.09s

**Supporting evidence:**
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2A7W3_2jE5CxmJ0eJTyV0g95XLna4SftONI3XjgLLJ3L5nBI6HTx4mSpvd9DNt5mMmbCpGzYMPdVUzk-YTX6uraropKWTinbo31LZ0ESUfNhZP5JeivzwINy5DqWgC_erJCuRkhKMfHxf3gpNVbHsMAEQp9c-XpNHIRJQ55mvxbwpluYkxNsK9YJGAB-JWXQosku33_NZbPGsMAzOa8USaoi1GKa5fFfHHhSfqLK0qj9JLZWDtg==)). Relevance: Provides the specific token-per-second values for Gemini 3.5 Flash and competitor models, allowing calculation of the 4x speed multiplier.
- Speed: 278 output tokens per second (rank #2 of 147 in its AA price class)... Other frontier-class models are well behind: Gemini 3.1 Pro Preview at 123, GPT-5.5 (xhigh) at 65, Claude Opus 4.7 (max) at 50. ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbehuFiT79IeuiDX2g50utbBOL5geep0aVbHqrriij-ZfQbDtJRwxp6m4Phwo5grp3Z7S3JlDYQ_7c8BYoN8BVaJR_8vpkqdoJto_b6MyJQgbV0AnkQPAOwilJ1mF51Wcp7Buz_T9AAthrEJ2q)). Relevance: Provides additional independent speed metrics showing Claude Opus 4.7 (max) at 50 output tokens/sec and GPT-5.5 (xhigh) at 65 output tokens/sec compared to Gemini 3.5 Flash.

**Missing context:**
- The original document does not provide the absolute throughput (output tokens per second) for Gemini 3.5 Flash.
- The document fails to specify which competitor frontier models are used in the 'other frontier models' baseline comparison.
- The document lacks description of the testing parameters, such as the hardware environment (e.g., TPU cluster configurations), concurrent request rates, batch sizes, and average prompt/response token lengths.

**Computed checks:**
- Gemini 3.5 Flash average throughput: 284 to 289 tokens per second (based on Artificial Analysis and keynote claims).
- Claude Opus 4.7 baseline throughput: 67 tokens per second.
- GPT-5.5 baseline throughput: 71 tokens per second.
- Relative speed ratio against Claude Opus 4.7: 284 / 67 = 4.24x (or 289 / 67 = 4.31x) faster throughput.
- Relative speed ratio against GPT-5.5: 284 / 71 = 4.00x (or 289 / 71 = 4.07x) faster throughput.
- Relative speed ratio against GPT-5.5 (xhigh tier at 65 tokens/sec): 284 / 65 = 4.37x faster throughput.
- Relative speed ratio against Claude Opus 4.7 (max tier at 50 tokens/sec): 284 / 50 = 5.68x faster throughput.
- Relative speed ratio against Gemini 3.1 Pro Preview (123 tokens/sec): 284 / 123 = 2.31x faster throughput.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `high` confidence.</summary>

**Duration:** 19.70s

**Supporting evidence:**
- Speed: The 4x Number. Google's headline performance claim is that Gemini 3.5 Flash is roughly 4x faster in output tokens per second than other frontier models. The supporting data comes from Artificial Analysis (as of May 13, 2026): Gemini 3.5 Flash: 289 tokens/sec; Gemini 3.1 Pro: 135 tokens/sec; GPT-5.5 (xhigh): 71 tokens/sec; Claude Opus 4.7 (max): 67 tokens/sec. ([How to Use Gemini 3.5 Flash: Complete Guide to Google's Fastest AI Model (2026)](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBnMRELXP9QWyK4ypPWNeHKdJxDIY0EmiQkc7bknDJgwJP7sxdOm8gvGB_ymhFkNFjec1KovzLobHwxjRgcKF4mvpz36c5w7WBCuAnQbdfEsPFyvMeVRmFpQiS_TB7Nw_VpvFvZUz6uJXQLG0cBKsS)). Relevance: Identifies the exact output speeds and competitor models (GPT-5.5 xhigh and Claude Opus 4.7 max) used in the 4x speed comparison.
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2A7W3_2jE5CxmJ0eJTyV0g95XLna4SftONI3XjgLLJ3L5nBI6HTx4mSpvd9DNt5mMmbCpGzYMPdVUzk-YTX6uraropKWTinbo31LZ0ESUfNhZP5JeivzwINy5DqWgC_erJCuRkhKMfHxf3gpNVbHsMAEQp9c-XpNHIRJQ55mvxbwpluYkxNsK9YJGAB-JWXQosku33_NZbPGsMAzOa8USaoi1GKa5fFfHHhSfqLK0qj9JLZWDtg==)). Relevance: Confirms the specific token-per-second throughput metrics that yield the 4x multiplier.

**Contradictions / narrowing evidence:**
- According to Google, 3.5 Flash 'outperforms Gemini 3.1 Pro' on most benchmarks and generates tokens '4 times faster than other frontier models.' Faster token generation reduces the part of an agent's time spent generating text... So agents get faster, but not 4x. ([Google Launched Antigravity 2.0 with Gemini 3.5 Flash. Will Agents Be 4x Faster? | Belitsoft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4c2946iGq8_9aK24fntNfENtTWxgWlHI5KutLowV2zY8jAlslhHqFDlnmm2EGYcto5kxcDvh3WZcL17iExdx_EJAX1y5pjw-CDbXzdBg_4iPZTlmwDSAaLn8bAQE1F2Sl6jTPRfaIb1EGJeQ==)). Relevance: Directly counters the implication that 4x raw token throughput equals a 4x overall speedup in agentic loops.

**Missing context:**
- The compared 'other frontier models' (GPT-5.5, Claude Opus 4.7) are heavy, flagship reasoning models rather than comparable lightweight peers.
- The comparison fails to account for Gemini 3.5 Flash's high Time to First Token (TTFT) latency of 18.55 seconds on Google's API.
- Raw output token generation speed does not yield equivalent 4x wall-clock speed improvements in real-world multi-turn agentic workflows.

**Computed checks:**
- Gemini 3.5 Flash output speed: 284 to 289 tokens per second
- GPT-5.5 output speed: 65 to 71 tokens per second
- Claude Opus 4.7 output speed: 50 to 67 tokens per second
- Gemini 3.5 Flash Time to First Token (TTFT): 18.55 seconds
- Evaluated output speed ratio: 289 / 71 = 4.07x faster than GPT-5.5 and 289 / 67 = 4.31x faster than Claude Opus 4.7

</details>

### Evidence Contrast

**Claim says:** When looking at output tokens per second, 3.5 Flash is 4 times faster than other frontier models.

**Best reference says:** Confirms Artificial Analysis measured Gemini 3.5 Flash at 289 tps compared to GPT-5.5 at 71 tps and Claude Opus 4.7 at 67 tps, making the 4x claim mathematically correct for raw output tokens, but revealing that the comparison baselines are premium heavyweights.

**Key qualification:** Applies strictly to raw output token throughput, not end-to-end latency.

**Delta:** missing_context — While the 4x multiplier is mathematically verified by independent benchmarks of raw token-per-second generation, the original claim omits that this compares Gemini 3.5 Flash (a lightweight model) against much larger heavyweight flagships (GPT-5.5 and Claude Opus 4.7). Furthermore, it omits a high TTFT of 18.55s and the fact that raw throughput does not equate to a 4x overall agent speedup.

**Final verdict:** missing_context

**Defensible rewrite:** In terms of raw output token generation, Gemini 3.5 Flash achieves over 280 tokens per second, which is approximately four times faster than premium flagship models like GPT-5.5 and Claude Opus 4.7, though practical application speedups will vary.

### Claim-Level Contrast References

- Gemini 3.5: frontier intelligence with action (blog, authority 90/100): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/. Original announcement containing the claim.

**Reference snippets / mismatches:**
- Confirms Artificial Analysis measured Gemini 3.5 Flash at 289 tps compared to GPT-5.5 at 71 tps and Claude Opus 4.7 at 67 tps, making the 4x claim mathematically correct for raw output tokens, but revealing that the comparison baselines are premium heavyweights. (How to Use Gemini 3.5 Flash: Complete Guide to Google's Fastest AI Model (2026), narrows, https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBnMRELXP9QWyK4ypPWNeHKdJxDIY0EmiQkc7bknDJgwJP7sxdOm8gvGB_ymhFkNFjec1KovzLobHwxjRgcKF4mvpz36c5w7WBCuAnQbdfEsPFyvMeVRmFpQiS_TB7Nw_VpvFvZUz6uJXQLG0cBKsS). Applies strictly to raw output token throughput, not end-to-end latency.

**Computed checks:**
- Gemini 3.5 Flash output speed: 284 to 289 tokens per second
- GPT-5.5 output speed: 65 to 71 tokens per second
- Claude Opus 4.7 output speed: 50 to 67 tokens per second
- Gemini 3.5 Flash Time to First Token (TTFT): 18.55 seconds
- Evaluated output speed ratio: 289 / 71 = 4.07x faster than GPT-5.5 and 289 / 67 = 4.31x faster than Claude Opus 4.7

**Gemini-discovered supporting sources:**
- Speed: The 4x Number. Google's headline performance claim is that Gemini 3.5 Flash is roughly 4x faster in output tokens per second than other frontier models. The supporting data comes from Artificial Analysis (as of May 13, 2026): Gemini 3.5 Flash: 289 tokens/sec; Gemini 3.1 Pro: 135 tokens/sec; GPT-5.5 (xhigh): 71 tokens/sec; Claude Opus 4.7 (max): 67 tokens/sec. ([How to Use Gemini 3.5 Flash: Complete Guide to Google's Fastest AI Model (2026)](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBnMRELXP9QWyK4ypPWNeHKdJxDIY0EmiQkc7bknDJgwJP7sxdOm8gvGB_ymhFkNFjec1KovzLobHwxjRgcKF4mvpz36c5w7WBCuAnQbdfEsPFyvMeVRmFpQiS_TB7Nw_VpvFvZUz6uJXQLG0cBKsS)). Relevance: Identifies the exact output speeds and competitor models (GPT-5.5 xhigh and Claude Opus 4.7 max) used in the 4x speed comparison.
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2A7W3_2jE5CxmJ0eJTyV0g95XLna4SftONI3XjgLLJ3L5nBI6HTx4mSpvd9DNt5mMmbCpGzYMPdVUzk-YTX6uraropKWTinbo31LZ0ESUfNhZP5JeivzwINy5DqWgC_erJCuRkhKMfHxf3gpNVbHsMAEQp9c-XpNHIRJQ55mvxbwpluYkxNsK9YJGAB-JWXQosku33_NZbPGsMAzOa8USaoi1GKa5fFfHHhSfqLK0qj9JLZWDtg==)). Relevance: Confirms the specific token-per-second throughput metrics that yield the 4x multiplier.

**Gemini-discovered caveat / counter sources:**
- According to Google, 3.5 Flash 'outperforms Gemini 3.1 Pro' on most benchmarks and generates tokens '4 times faster than other frontier models.' Faster token generation reduces the part of an agent's time spent generating text... So agents get faster, but not 4x. ([Google Launched Antigravity 2.0 with Gemini 3.5 Flash. Will Agents Be 4x Faster? | Belitsoft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4c2946iGq8_9aK24fntNfENtTWxgWlHI5KutLowV2zY8jAlslhHqFDlnmm2EGYcto5kxcDvh3WZcL17iExdx_EJAX1y5pjw-CDbXzdBg_4iPZTlmwDSAaLn8bAQE1F2Sl6jTPRfaIb1EGJeQ==)). Relevance: Directly counters the implication that 4x raw token throughput equals a 4x overall speedup in agentic loops.

**Missing context:**
- The compared 'other frontier models' (GPT-5.5, Claude Opus 4.7) are heavy, flagship reasoning models rather than comparable lightweight peers.
- The comparison fails to account for Gemini 3.5 Flash's high Time to First Token (TTFT) latency of 18.55 seconds on Google's API.
- Raw output token generation speed does not yield equivalent 4x wall-clock speed improvements in real-world multi-turn agentic workflows.


## 3: overstated

**Confidence:** high

**Original:** What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models.

**Stretch Score:** 80/100

**Why:** The reference source (the model card) has a much narrower scope than the claim. It reports performance on structured synthetic benchmarks and details variable pricing mechanics ('thinking levels'), rather than verifying the claim's broad real-world timeline reductions (days/weeks) or providing a comparative economic study demonstrating half-cost operation against all comparable frontier models.

**Defensible rewrite:** Gemini 3.5 Flash is designed to help accelerate complex development and auditing tasks, offering a highly cost-efficient alternative compared to heavy flagship frontier models.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 100.27s / 27.57s / 32.95s / 27.92s / 40.20s / 27.03s

### Agent Steps

<details><summary>grounded_verifier: The claim is supported by general benchmark comparisons (Terminal-Bench 2.1, GDPval-AA, MCP Atlas), illustrative partner pilots (Macquarie Bank, Xero, Shopify, Databricks), and API pricing ($1.50/$9.00 per 1M tokens), though no controlled user studies or audited evaluations measuring exact developer/auditor time reductions are publicly documented.</summary>

**Duration:** 27.57s

**Supporting evidence:**
- Gemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions, at the speeds you have come to expect from the Flash series. It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).... What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: This is the primary source document containing the specific claim and framing of capabilities.
- Pichai put the performance gap in blunt terms: '3.5 Flash is better than 3.1 Pro, which was just four months ago, and it's at the almost, I would say, 90% of the performance of frontier models, 4x faster, much faster in Antigravity, maybe 12x, and about 1/3 to one half the cost.' ([Google says Gemini 3.5 Flash can slash enterprise AI costs by more than $1 billion a year](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGVWir65BHuscHIuHOWJtTJnzPTeDGN8WQ0euzqSr_3BEXZENo3kauN1qqR25dBbMpKuR2kVoAyj2hybJGr0sZXgrWbEtWEtAi8wV5i4_NsjvghwXdjps6mBTehqglFsdc3h3ASXuN1HwAkHgw9QOz96QvdVWK03m6NjHYLIqIr-gNifWhYsbFs4-SoxmLOvUzZPSu-e9eX3stkgO4yPudr31bLr9Crphzm2Ud-Q7DPPw=)). Relevance: Provides Pichai's explanation of the pricing framework justifying the 'less than half' cost claim compared to other frontier models.
- 'What's amazing about Flash is how it delivers frontier-level capabilities at less than half the price, in some cases almost a third of the price of comparable frontier models,' Pichai noted. ([Google's Gemini 3.5 Flash beats the frontier models](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjib2pL9gHsxzYdvy5e0z8vK7YPChN9i_BwCoK2Dk1FYOKHDQQJOqzxvszrwDUgv1BGGmYysEORE-6Fkla7IDTyd58mWKVwSNsR_qb2h8g_WSSu7UX9X8Gct0Gyq_paltLwLlhApM4HAYFi-wCz1TIaiQFipSHxp70z5FNjeHDdg==)). Relevance: Corroborates the cost framework comparing Gemini 3.5 Flash against larger competing frontier models.

**Missing context:**
- No formal controlled user studies or audited workflow evaluations are publicly available to systematically quantify the claimed time reductions for developers or auditors; the claim is backed primarily by anecdotal partner pilots (e.g., Xero's multi-week tax workflows or Macquarie Bank's customer onboarding documents) and general benchmark statistics.

**Computed checks:**
- Gemini 3.5 Flash API is priced at $1.50 per million input tokens and $9.00 per million output tokens.
- The model delivers near-frontier performance (~90% of frontier model levels) at 1/3 to 1/2 of the cost of comparable frontier models.

</details>

<details><summary>contradiction_finder: While Google claims Gemini 3.5 Flash reduces developer and auditor workloads from days/weeks to a fraction of the time at 'less than half the cost' of other frontier models, independent benchmarks and pricing analyses contradict and limit this claim. First, there are no published controlled user studies or audited workflow evaluations proving the 'days-to-weeks' reduction; Google relies on automated coding benchmarks and anecdotal partner pilots. Second, the 'half the cost' claim is a highly selective comparison against premium models (like GPT-5.5 or Claude Opus). It ignores highly capable, cost-efficient frontier competitors like Claude Haiku 4.5, which is cheaper at $1.00/$5.00 per million tokens. Finally, due to 3.5 Flash's high token verbosity in reasoning modes, real-world benchmark evaluations show it is actually 75% more expensive to run than Gemini 3.1 Pro and over 5 times more expensive than Gemini 3 Flash.</summary>

**Duration:** 32.95s

**Supporting evidence:**
- What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: States the original marketing claim that Gemini 3.5 Flash drastically compresses professional workloads and operates at less than half the cost of other frontier models.

**Contradictions / narrowing evidence:**
- Gemini 3.5 Flash scores 55 on the Artificial Analysis Intelligence Index, up 9 points from Gemini 3 Flash... but higher token usage and token pricing make it over 5x more costly to run the Intelligence Index than Gemini 3 Flash, and 75% more costly than Gemini 3.1 Pro. ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Directly contradicts the general 'less than half the cost' narrative by demonstrating that high token verbosity and pricing adjustments make Gemini 3.5 Flash significantly more expensive in practice than previous Pro models.
- Running the benchmark for 3.5 Flash (high) cost significantly more than 3.1 Pro Preview! Here are some numbers from other vendors... Gemini 3.5 Flash (high): $1,551.60; Gemini 3.1 Pro Preview: $892.28; Gemini 3 Flash Preview (Reasoning): $278.26. ([Gemini 3.5 Flash: more expensive, but Google plan to use it for everything](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8C2J7DzRwe81gY9HXf-kjCdfw19SgqRLK1cj0gVCJNq0_6O6nzm7qCLHVmz-NgWXj_NjTuattB3oZhRuwyeVkoa1hTtLEQscpXVxBh8eYawlRxujSggpjYrdiTTDSPyMixh-tlf5ZhhnYyc4=)). Relevance: Provides concrete evaluation figures showing that running 3.5 Flash in high-thinking agentic configurations actually costs $1,551.60 on standard benchmarks—nearly double the cost of Gemini 3.1 Pro Preview.
- Claude Haiku 4.5 is cheaper on output tokens ($5 vs $9 per 1M)... Input pricing: $1.50 / 1M tokens (Gemini) vs $1.00 / 1M tokens (Haiku). ([Gemini 3.5 Flash vs Claude Haiku 4.5: Pricing & Production Fit (2026) - EvoLink](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtagWPnsnip1NvGcBIliDTDXl_lqv96FapF9kc9ZWQExkLeAWcxlZJ8gCoA4Ui5Dt5B9xBfmtAYvB_AQ73om1dPuN-5k-9IKw2--nssFQx4Vaunn9-q9Lq61ALe3uSigGbv1xNd1t3ecaZkoqoxnNIe60=)). Relevance: Shows that Gemini 3.5 Flash ($1.50 input / $9.00 output per 1M) is more expensive than Claude Haiku 4.5 ($1.00 input / $5.00 output per 1M), which is a direct frontier competitor on coding and agentic benchmarks.

**Missing context:**
- No controlled user studies, randomized trials, or independent audits have been published to validate that professional developers or financial auditors complete workflows in a 'fraction of the time.' The claim relies on synthetic automation benchmarks (e.g., Terminal-Bench 2.1) and subjective partner pilots.
- The 'less than half the cost' claim only holds true when compared to premium, high-latency flagship models (such as GPT-5.5 at $5.00/$30.00 or Claude Opus 4.7 at $5.00/$25.00), while omitting comparisons to fast frontier competitors like Claude Haiku 4.5.
- The cost framework ignores token verbosity (such as reasoning and thinking tokens). Standard pricing lists Gemini 3.5 Flash at a 3x premium over Gemini 3 Flash ($1.50/$9.00 per 1M vs $0.50/$3.00), and its high token output can balloon live API expenses beyond expected Pro-tier levels.

**Computed checks:**
- Gemini 3.5 Flash API pricing is set at $1.50 per million input tokens and $9.00 per million output tokens, a 3x increase over Gemini 3 Flash ($0.50/$3.00).
- On the Artificial Analysis Intelligence Index benchmark, Gemini 3.5 Flash (high) cost $1,551.60 to run, which is 75% more expensive than Gemini 3.1 Pro Preview ($892.28).
- Under high thinking modes, Gemini 3.5 Flash is highly verbose, generating 73 million tokens on the Intelligence Index compared to an average of 35 million tokens for other models.
- Claude Haiku 4.5 provides a cheaper alternative with $1.00 per million input and $5.00 per million output tokens, matching major coding evaluations.

</details>

<details><summary>numeric_calibrator: The claim that Gemini 3.5 Flash reduces developer or auditor tasks to a fraction of the time at less than half the cost is unsupported by quantitative data within the source document itself. The document lacks structured baseline metrics or controlled study results to define what constitutes 'days' of developer work or 'weeks' of auditor work, though it highlights a specific six-hour coding project. Externally retrieved API pricing reveals Gemini 3.5 Flash costs $1.50 per million input tokens and $9.00 per million output tokens. This is indeed less than half the cost of other major frontier models like GPT-5.5 ($5.00 input / $30.00 output) and Claude Opus 4.7 ($5.00 input / $25.00 output), representing 30% to 36% of their costs (a 64% to 70% saving). However, this pricing is also a 3x increase over previous Gemini Flash models, which some developers argue offsets its cost-effectiveness in high-volume routing workflows.</summary>

**Duration:** 27.92s

**Supporting evidence:**
- What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Contains the core claim regarding reduced workload duration and cost metrics.
- Leveraging Antigravity, 3.5 Flash uses two agents to synthesize the AlphaZero paper and code a fully playable game in six hours. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides a specific timeline of six hours for a major coding project to anchor developer timeframes.
- The headline framing from Google is that 3.5 Flash is 'cheaper than the frontier models it now beats.' And yeah, technically, that's true: GPT-5.5 launched at $5.00 / $30.00, and Claude Opus 4.7 is $5.00 / $25.00. ([Gemini 3.5 Flash hits Frontier performance... and pricing - AI World](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHff3k4BftNM-z6TiLaipFqxqI8JznnLb58g5tZsDJD1kFbcDICnN1xRBWKspnDRrgnxJnYvImkIP1B5RhoCbk1tzTlC4pHmzQjkb7fatC5lY768HXvNNtmG1Mk5HvnuSiF_6fiAQk8GZ5gY7L7Otr0mrXFGGMt8v3QmhbrECLmGpgw34c=)). Relevance: Provides the pricing framework of competing frontier models to verify the 'less than half the cost' estimate.

**Contradictions / narrowing evidence:**
- In context, though, there's a number that sits a bit awkwardly in the announcement: $1.50 input / $9.00 output per million tokens. For reference, Gemini 3 Flash launched at $0.50 / $3.00. That's a 3x price increase, 6x if you were on Flash-Lite... Running the Artificial Analysis benchmark against 3.5 Flash costed ~$1,500, 75% more than doing the same against 3.1 Pro Preview. ([Gemini 3.5 Flash hits Frontier performance... and pricing - AI World](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHff3k4BftNM-z6TiLaipFqxqI8JznnLb58g5tZsDJD1kFbcDICnN1xRBWKspnDRrgnxJnYvImkIP1B5RhoCbk1tzTlC4pHmzQjkb7fatC5lY768HXvNNtmG1Mk5HvnuSiF_6fiAQk8GZ5gY7L7Otr0mrXFGGMt8v3QmhbrECLmGpgw34c=)). Relevance: Demonstrates that while 3.5 Flash is cheaper than larger models, its pricing represents a 3x to 6x increase over its predecessor class, meaning its relative cost-savings depend heavily on the baseline model compared.

**Missing context:**
- Baseline developer hours representing 'days' or baseline auditor hours representing 'weeks' to calculate the exact fraction of time saved.
- The precise API pricing of Gemini 3.5 Flash (input and output token costs) and those of competing 'other frontier models' (like GPT-5.5 or Claude Opus 4.7) to mathematically justify the 'less than half the cost' assertion.
- Data from controlled user studies, audited workflow evaluations, or systematic benchmarks quantifying the speedups and costs under real-world conditions.

**Computed checks:**
- Input token cost ratio comparison: Gemini 3.5 Flash ($1.50 / 1M) vs GPT-5.5 ($5.00 / 1M) = 1.50 / 5.00 = 0.30 (30% of GPT-5.5 cost, representing a 70% cost saving).
- Output token cost ratio comparison vs GPT-5.5: Gemini 3.5 Flash ($9.00 / 1M) vs GPT-5.5 ($30.00 / 1M) = 9.00 / 30.00 = 0.30 (30% of GPT-5.5 cost, representing a 70% cost saving).
- Output token cost ratio comparison vs Claude Opus 4.7: Gemini 3.5 Flash ($9.00 / 1M) vs Claude Opus 4.7 ($25.00 / 1M) = 9.00 / 25.00 = 0.36 (36% of Claude Opus 4.7 cost, representing a 64% cost saving).
- Time savings ratio based on 6 hours vs typical 3-day (72 hours) developer baseline: 6 / 72 = 0.0833 (completing the task in approximately 8.3% of the time, or a 12x speedup).
- Time savings ratio based on 6 hours vs typical 2-week (336 hours / including off-hours, or 80 business hours) auditor baseline: 6 / 80 = 0.075 (completing the task in 7.5% of working hours, or a 13.3x speedup).

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `overstated` with `high` confidence.</summary>

**Duration:** 40.20s

**Supporting evidence:**
- Gemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions... What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides the original context, benchmarks, and pricing framework framing Gemini 3.5 Flash's value proposition.
- The headline framing from Google is that 3.5 Flash is 'cheaper than the frontier models it now beats.' And yeah, technically, that's true: GPT-5.5 launched at $5.00 / $30.00, and Claude Opus 4.7 is $5.00 / $25.00. (Gemini 3.5 Flash hits Frontier performance... and pricing - AI World). Relevance: Confirms that Gemini 3.5 Flash's token list price represents a 64% to 70% savings over the heaviest premium flagship competitors.

**Contradictions / narrowing evidence:**
- Gemini 3.5 Flash scores 55 on the Artificial Analysis Intelligence Index, up 9 points from Gemini 3 Flash... but higher token usage and token pricing make it over 5x more costly to run the Intelligence Index than Gemini 3 Flash, and 75% more costly than Gemini 3.1 Pro. ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Directly refutes the idea of generic 'half the cost' operation, showing that higher token verbosity under thinking configurations makes it costlier to run than Pro-tier alternatives.
- Claude Haiku 4.5 is cheaper on output tokens ($5 vs $9 per 1M)... Input pricing: $1.50 / 1M tokens (Gemini) vs $1.00 / 1M tokens (Haiku). (Gemini 3.5 Flash vs Claude Haiku 4.5: Pricing & Production Fit (2026) - EvoLink). Relevance: Demonstrates that there are other fast-frontier models that are cheaper than Gemini 3.5 Flash, contradicting the blanket cost claim.

**Missing context:**
- No formal controlled user studies or audited evaluations have been published to systematically quantify the hours saved by developers or auditors.
- The cost comparison omits other budget-friendly fast-frontier competitors like Claude Haiku 4.5.
- Real-world agentic execution costs are heavily influenced by high token output verbosity in thinking modes, which can significantly drive up total bills compared to static list-price comparisons.

**Computed checks:**
- Gemini 3.5 Flash list price: $1.50 per 1M input tokens and $9.00 per 1M output tokens.
- GPT-5.5 list price: $5.00 input and $30.00 output per 1M tokens (Gemini 3.5 Flash is 30% of this cost, representing a 70% saving).
- Claude Opus 4.7 list price: $5.00 input and $25.00 output per 1M tokens (Gemini 3.5 Flash is 30% to 36% of this cost, representing a 64% to 70% saving).
- Claude Haiku 4.5 list price: $1.00 input and $5.00 output per 1M tokens (cheaper than Gemini 3.5 Flash).
- Running the Artificial Analysis benchmark on Gemini 3.5 Flash (high reasoning configuration) cost $1,551.60, which is 75% more expensive than Gemini 3.1 Pro Preview ($892.28).

</details>

### Evidence Contrast

**Claim says:** What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models.

**Best reference says:** The model card evaluates Gemini 3.5 Flash on standardized coding and agentic benchmarks (such as Terminal-Bench) and explains that the model relies on user-controlled 'thinking levels' to manage the trade-offs of quality, cost, and latency. It does not provide empirical data or user studies backing the claim of reducing human developer or auditor labor from 'days or weeks' to a 'fraction of the time', nor does it validate the cost-halving comparison against other frontier-class models.

**Key qualification:** The workflow acceleration and cost-reduction assertions represent high-level marketing generalizations rather than verified technical findings in the official model documentation. Actual cost-efficiency is highly dependent on selected competitors and active thinking-level configurations.

**Delta:** narrower_than_claim — The reference source (the model card) has a much narrower scope than the claim. It reports performance on structured synthetic benchmarks and details variable pricing mechanics ('thinking levels'), rather than verifying the claim's broad real-world timeline reductions (days/weeks) or providing a comparative economic study demonstrating half-cost operation against all comparable frontier models.

**Final verdict:** overstated

**Defensible rewrite:** Gemini 3.5 Flash is designed to help accelerate complex development and auditing tasks, offering a highly cost-efficient alternative compared to heavy flagship frontier models.

### Claim-Level Contrast References

- Gemini 3.5 Flash - Model Card - Google DeepMind (vendor_doc, authority 95/100): https://deepmind.google/models/model-cards/gemini-3-5-flash. This is the official technical model card for Gemini 3.5 Flash, providing the authoritative benchmarks, architecture details, and parameters regarding cost and latency controls.

**Reference snippets / mismatches:**
- The model card evaluates Gemini 3.5 Flash on standardized coding and agentic benchmarks (such as Terminal-Bench) and explains that the model relies on user-controlled 'thinking levels' to manage the trade-offs of quality, cost, and latency. It does not provide empirical data or user studies backing the claim of reducing human developer or auditor labor from 'days or weeks' to a 'fraction of the time', nor does it validate the cost-halving comparison against other frontier-class models. (Gemini 3.5 Flash - Model Card - Google DeepMind, narrows, https://deepmind.google/models/model-cards/gemini-3-5-flash). The workflow acceleration and cost-reduction assertions represent high-level marketing generalizations rather than verified technical findings in the official model documentation. Actual cost-efficiency is highly dependent on selected competitors and active thinking-level configurations.

**Computed checks:**
- Gemini 3.5 Flash list price: $1.50 per 1M input tokens and $9.00 per 1M output tokens.
- GPT-5.5 list price: $5.00 input and $30.00 output per 1M tokens (Gemini 3.5 Flash is 30% of this cost, representing a 70% saving).
- Claude Opus 4.7 list price: $5.00 input and $25.00 output per 1M tokens (Gemini 3.5 Flash is 30% to 36% of this cost, representing a 64% to 70% saving).
- Claude Haiku 4.5 list price: $1.00 input and $5.00 output per 1M tokens (cheaper than Gemini 3.5 Flash).
- Running the Artificial Analysis benchmark on Gemini 3.5 Flash (high reasoning configuration) cost $1,551.60, which is 75% more expensive than Gemini 3.1 Pro Preview ($892.28).

**Gemini-discovered supporting sources:**
- Gemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions... What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides the original context, benchmarks, and pricing framework framing Gemini 3.5 Flash's value proposition.
- The headline framing from Google is that 3.5 Flash is 'cheaper than the frontier models it now beats.' And yeah, technically, that's true: GPT-5.5 launched at $5.00 / $30.00, and Claude Opus 4.7 is $5.00 / $25.00. (Gemini 3.5 Flash hits Frontier performance... and pricing - AI World). Relevance: Confirms that Gemini 3.5 Flash's token list price represents a 64% to 70% savings over the heaviest premium flagship competitors.

**Gemini-discovered caveat / counter sources:**
- Gemini 3.5 Flash scores 55 on the Artificial Analysis Intelligence Index, up 9 points from Gemini 3 Flash... but higher token usage and token pricing make it over 5x more costly to run the Intelligence Index than Gemini 3 Flash, and 75% more costly than Gemini 3.1 Pro. ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Directly refutes the idea of generic 'half the cost' operation, showing that higher token verbosity under thinking configurations makes it costlier to run than Pro-tier alternatives.
- Claude Haiku 4.5 is cheaper on output tokens ($5 vs $9 per 1M)... Input pricing: $1.50 / 1M tokens (Gemini) vs $1.00 / 1M tokens (Haiku). (Gemini 3.5 Flash vs Claude Haiku 4.5: Pricing & Production Fit (2026) - EvoLink). Relevance: Demonstrates that there are other fast-frontier models that are cheaper than Gemini 3.5 Flash, contradicting the blanket cost claim.

**Missing context:**
- No formal controlled user studies or audited evaluations have been published to systematically quantify the hours saved by developers or auditors.
- The cost comparison omits other budget-friendly fast-frontier competitors like Claude Haiku 4.5.
- Real-world agentic execution costs are heavily influenced by high token output verbosity in thinking modes, which can significantly drive up total bills compared to static list-price comparisons.


## 4: overstated

**Confidence:** high

**Original:** Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.

**Stretch Score:** 80/100

**Why:** The claim asserts that Gemini 3.5 can 'reliably execute' multi-step workflows and coding tasks. However, the official technical evaluations in the provided reference model card narrow this by revealing real success rates. The model achieves scores between 55.1% (on SWE-Bench Pro) and 83.6% (on MCP Atlas), leaving a substantial margin of failure (16.4% to 44.9%) that contradicts a claim of absolute reliability.

**Defensible rewrite:** Under human supervision, the model can execute complex multi-step workflows and coding tasks, demonstrating improved capabilities on challenging agentic benchmarks with success rates ranging from approximately 55% to 84%.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 97.03s / 22.50s / 35.80s / 9.55s / 37.31s / 23.80s

### Agent Steps

<details><summary>dense_verifier: The claim is directly asserted in the official Google blog post. However, the document does not provide a precise definition of 'reliability' in multi-step workflows, nor does it specify a general measured success rate per run or the frequency of required human interventions. Instead, it offers performance scores on standardized benchmarks like Terminal-Bench 2.1 (76.2%) and MCP Atlas (83.6%) to support its agentic capability claims.</summary>

**Duration:** 22.50s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Direct source of the verbatim claim within Google's launch announcement.
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides quantitative performance metrics on standard agentic and coding benchmarks, which serve as the only concrete indicators of execution success rates offered in the release.

**Missing context:**
- A formal definition of 'reliability' in the context of these multi-step workflows.
- The measured end-to-end success rate per run for the workflows described in the real-world impact section (outside of standardized academic benchmarks).
- Specific data on how frequently human supervisors are required to intervene to correct a workflow before it fails.

**Computed checks:**
- 76.2% success rate on Terminal-Bench 2.1 coding benchmark
- 83.6% success rate on MCP Atlas tool use benchmark
- 1656 Elo rating on GDPval-AA agentic evaluation
- 84.2% on CharXiv Reasoning multimodal understanding benchmark

</details>

<details><summary>skeptical_contradiction_finder: The claim that Gemini 3.5 Flash can 'reliably execute' multi-step workflows under supervision lacks a precise definition of reliability or intervention metrics. Official benchmarks show failure rates of 16.4% to 44.9% depending on the task. Real-world developer feedback indicates critical reliability failures, including infinite ingestion loops caused by 'Context Window Compaction Amnesia' and challenges in manual supervision due to rapid token generation rates.</summary>

**Duration:** 35.80s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance... outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: The official blog post presents these benchmark numbers to back up its claim of reliable execution, though it doesn't define 'reliability' or supervise intervention frequency.

**Contradictions / narrowing evidence:**
- When the context window fills up... the platform compacts the conversation to free space. After compaction, the model loses the specific details... Its next action is always: 'I will read the file to understand...' — re-reading the exact same files it just read before compaction... triggers another compaction -> amnesia -> re-read. This is the loop. The model never accumulates enough simultaneous context to actually synthesize the analysis. ([Antigravity 2.0..... lackluster? Gemini 3.5 Flash seems - Google AI Developers Forum](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUiHsXMatBgZTfgU57IWOe6jaGxOI57Oc8l4I9Cvmh40j0y3A0tf-yqHwqRIVapjB8i4HJPsDSgni-pBqdymUg8HL0NaHsBm18X64A0Zf3_8UYx3ivNcBMc3H8KVm_A06aTkr6iz28ge5Rq1TUQ8NQcTkZ28ofYD8XDOXafW42RgNMG5N8xbXBcgkjtK4=)). Relevance: Exposes a major technical loop failure ('compaction amnesia') that directly prevents the model from reliably executing multi-step workflows over a long horizon.
- Avoid Gemini 3.5 Flash (Medium). It's too fast to follow along to be able to intervene or correct course... And it makes syntactic and orthographic errors which makes me always wary of an AI. ([Antigravity 2 & Gemini 3.5 Flash Review : r/GoogleAntigravityIDE - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxWKp2XdVBBuMOkTKN2g6lYZmBFACB7uUS1VQ-rKzHSvEjmnK5GKUqiPR4tL8e5MizImtJxogrbGTGppm7JYSr0NY7RjjhNYjYAm9_7kcl0VTlUb5wrDp_1rMxSrHsMqpMczFoLm0T8GVf--n9rj-z9tjYZvCxPuQTGzZFbEe5IBXxmYtgyTVg50jadoMtXZe7nIojKKy8vec=)). Relevance: Shows that extreme speed and formatting errors make human supervision and timely correction of the workflow very difficult in practice.

**Missing context:**
- The blog post completely omits any definition of what 'under supervision' requires, nor does it quantify human intervention frequency or success rates for real-world automated tasks.
- Google's own cited benchmarks demonstrate that the model is not 100% reliable: it fails 23.8% of the time on Terminal-Bench 2.1 (scoring 76.2%) and 16.4% of the time on MCP Atlas (scoring 83.6%).
- On the more rigorous SWE-Bench Pro benchmark, Gemini 3.5 Flash scores only 55.1% on a single attempt, meaning nearly half of the software repository edits fail.

**Computed checks:**
- 76.2% success rate on Terminal-Bench 2.1
- 83.6% success rate on MCP Atlas
- 55.1% success rate on SWE-Bench Pro (single attempt)
- 1656 Elo on GDPval-AA

</details>

<details><summary>Numeric Calibrator: The claim asserts that Gemini 3.5 can 'reliably' execute multi-step workflows and coding tasks under supervision, but the source document provides no quantitative data, definitions, or metrics to support or define 'reliability', the measured success rate, or the necessary human intervention frequency.</summary>

**Duration:** 9.55s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: The source text containing the claim about reliable execution of multi-step workflows under supervision.

**Missing context:**
- The precise definition of 'reliability' in the context of multi-step workflows.
- The measured success rate per run (e.g., percentage of tasks completed without errors).
- The frequency of human supervisor intervention (e.g., rate of corrections needed per workflow or run).

**Computed checks:**
- No arithmetic calculations (absolute or relative deltas, denominators, or unit conversions) can be performed because the source document does not provide any numerical data, percentages, or statistics regarding the reliability or human intervention rates of these supervised workflows.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `overstated` with `high` confidence.</summary>

**Duration:** 37.31s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Direct source of the verbatim claim within Google's launch announcement.
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides quantitative performance metrics on standard agentic and coding benchmarks, which serve as the only concrete indicators of execution success rates offered in the release.

**Contradictions / narrowing evidence:**
- When the context window fills up... the platform compacts the conversation to free space. After compaction, the model loses the specific details... Its next action is always: 'I will read the file to understand...' — re-reading the exact same files it just read before compaction... triggers another compaction -> amnesia -> re-read. This is the loop. The model never accumulates enough simultaneous context to actually synthesize the analysis. ([Antigravity 2.0..... lackluster? Gemini 3.5 Flash seems - Google AI Developers Forum](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUiHsXMatBgZTfgU57IWOe6jaGxOI57Oc8l4I9Cvmh40j0y3A0tf-yqHwqRIVapjB8i4HJPsDSgni-pBqdymUg8HL0NaHsBm18X64A0Zf3_8UYx3ivNcBMc3H8KVm_A06aTkr6iz28ge5Rq1TUQ8NQcTkZ28ofYD8XDOXafW42RgNMG5N8xbXBcgkjtK4=)). Relevance: Exposes a major technical loop failure ('compaction amnesia') that directly prevents the model from reliably executing multi-step workflows over a long horizon.
- Avoid Gemini 3.5 Flash (Medium). It's too fast to follow along to be able to intervene or correct course... And it makes syntactic and orthographic errors which makes me always wary of an AI. ([Antigravity 2 & Gemini 3.5 Flash Review : r/GoogleAntigravityIDE - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxWKp2XdVBBuMOkTKN2g6lYZmBFACB7uUS1VQ-rKzHSvEjmnK5GKUqiPR4tL8e5MizImtJxogrbGTGppm7JYSr0NY7RjjhNYjYAm9_7kcl0VTlUb5wrDp_1rMxSrHsMqpMczFoLm0T8GVf--n9rj-z9tjYZvCxPuQTGzZFbEe5IBXxmYtgyTVg50jadoMtXZe7nIojKKy8vec=)). Relevance: Shows that extreme speed and formatting errors make human supervision and timely correction of the workflow very difficult in practice.

**Missing context:**
- A formal definition of 'reliability' in the context of these multi-step workflows is completely omitted.
- The blog post does not specify the measured end-to-end success rate per run for the workflows described outside of standardized academic benchmarks.
- There is no quantified data on how frequently human supervisors are required to intervene to correct a workflow before it fails.
- Google's own cited benchmarks demonstrate that the model is not 100% reliable: it fails 23.8% of the time on Terminal-Bench 2.1 (76.2% success) and 16.4% of the time on MCP Atlas (83.6% success).
- On the more rigorous SWE-Bench Pro benchmark, Gemini 3.5 Flash scores only 55.1% on a single attempt, meaning nearly half of the software repository edits fail.

**Computed checks:**
- 76.2% success rate on Terminal-Bench 2.1 coding benchmark
- 83.6% success rate on MCP Atlas tool use benchmark
- 55.1% success rate on SWE-Bench Pro (single attempt)
- 1656 Elo rating on GDPval-AA agentic evaluation
- 84.2% on CharXiv Reasoning multimodal understanding benchmark

</details>

### Evidence Contrast

**Claim says:** Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.

**Best reference says:** The model card presents benchmark scores for Gemini 3.5 Flash, showing a 55.1% success rate on SWE-Bench Pro, 76.2% on Terminal-Bench 2.1, and 83.6% on MCP Atlas. These metrics indicate that while the model has improved agentic capabilities, it exhibits failure rates ranging from approximately 16.4% to 44.9% on multi-step and coding workflows.

**Key qualification:** The term 'reliably execute' in the claim is qualified by actual technical benchmarks in the model card, which show the model does not achieve perfect or absolute reliability and fails on a substantial portion of complex tasks.

**Delta:** narrower_than_claim — The claim asserts that Gemini 3.5 can 'reliably execute' multi-step workflows and coding tasks. However, the official technical evaluations in the provided reference model card narrow this by revealing real success rates. The model achieves scores between 55.1% (on SWE-Bench Pro) and 83.6% (on MCP Atlas), leaving a substantial margin of failure (16.4% to 44.9%) that contradicts a claim of absolute reliability.

**Final verdict:** overstated

**Defensible rewrite:** Under human supervision, the model can execute complex multi-step workflows and coding tasks, demonstrating improved capabilities on challenging agentic benchmarks with success rates ranging from approximately 55% to 84%.

### Claim-Level Contrast References

- Gemini 3.5 Flash Model Card (vendor_doc, authority 100/100): https://deepmind.google/models/model-cards/gemini-3-5-flash. It provides the official technical benchmarks, evaluated success rates, and documented capabilities for Gemini 3.5 Flash.

**Reference snippets / mismatches:**
- The model card presents benchmark scores for Gemini 3.5 Flash, showing a 55.1% success rate on SWE-Bench Pro, 76.2% on Terminal-Bench 2.1, and 83.6% on MCP Atlas. These metrics indicate that while the model has improved agentic capabilities, it exhibits failure rates ranging from approximately 16.4% to 44.9% on multi-step and coding workflows. (Gemini 3.5 Flash Model Card, narrows, https://deepmind.google/models/model-cards/gemini-3-5-flash). The term 'reliably execute' in the claim is qualified by actual technical benchmarks in the model card, which show the model does not achieve perfect or absolute reliability and fails on a substantial portion of complex tasks.

**Computed checks:**
- 76.2% success rate on Terminal-Bench 2.1 coding benchmark
- 83.6% success rate on MCP Atlas tool use benchmark
- 55.1% success rate on SWE-Bench Pro (single attempt)
- 1656 Elo rating on GDPval-AA agentic evaluation
- 84.2% on CharXiv Reasoning multimodal understanding benchmark

**Gemini-discovered supporting sources:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Direct source of the verbatim claim within Google's launch announcement.
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides quantitative performance metrics on standard agentic and coding benchmarks, which serve as the only concrete indicators of execution success rates offered in the release.

**Gemini-discovered caveat / counter sources:**
- When the context window fills up... the platform compacts the conversation to free space. After compaction, the model loses the specific details... Its next action is always: 'I will read the file to understand...' — re-reading the exact same files it just read before compaction... triggers another compaction -> amnesia -> re-read. This is the loop. The model never accumulates enough simultaneous context to actually synthesize the analysis. ([Antigravity 2.0..... lackluster? Gemini 3.5 Flash seems - Google AI Developers Forum](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUiHsXMatBgZTfgU57IWOe6jaGxOI57Oc8l4I9Cvmh40j0y3A0tf-yqHwqRIVapjB8i4HJPsDSgni-pBqdymUg8HL0NaHsBm18X64A0Zf3_8UYx3ivNcBMc3H8KVm_A06aTkr6iz28ge5Rq1TUQ8NQcTkZ28ofYD8XDOXafW42RgNMG5N8xbXBcgkjtK4=)). Relevance: Exposes a major technical loop failure ('compaction amnesia') that directly prevents the model from reliably executing multi-step workflows over a long horizon.
- Avoid Gemini 3.5 Flash (Medium). It's too fast to follow along to be able to intervene or correct course... And it makes syntactic and orthographic errors which makes me always wary of an AI. ([Antigravity 2 & Gemini 3.5 Flash Review : r/GoogleAntigravityIDE - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxWKp2XdVBBuMOkTKN2g6lYZmBFACB7uUS1VQ-rKzHSvEjmnK5GKUqiPR4tL8e5MizImtJxogrbGTGppm7JYSr0NY7RjjhNYjYAm9_7kcl0VTlUb5wrDp_1rMxSrHsMqpMczFoLm0T8GVf--n9rj-z9tjYZvCxPuQTGzZFbEe5IBXxmYtgyTVg50jadoMtXZe7nIojKKy8vec=)). Relevance: Shows that extreme speed and formatting errors make human supervision and timely correction of the workflow very difficult in practice.

**Missing context:**
- A formal definition of 'reliability' in the context of these multi-step workflows is completely omitted.
- The blog post does not specify the measured end-to-end success rate per run for the workflows described outside of standardized academic benchmarks.
- There is no quantified data on how frequently human supervisors are required to intervene to correct a workflow before it fails.
- Google's own cited benchmarks demonstrate that the model is not 100% reliable: it fails 23.8% of the time on Terminal-Bench 2.1 (76.2% success) and 16.4% of the time on MCP Atlas (83.6% success).
- On the more rigorous SWE-Bench Pro benchmark, Gemini 3.5 Flash scores only 55.1% on a single attempt, meaning nearly half of the software repository edits fail.

