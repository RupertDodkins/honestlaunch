# CappinCheck Report: Gemini 3.5: frontier intelligence with action

Source: `https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/`

## Provenance

- Mode: `live_gemini`
- Runtime: `local`
- Pipeline wall: `191.94s`
- Load / Extract / Audit / Contrast: `729ms` / `29.36s` / `161.85s` / `23.28s`
- Claims extracted / audited: `8` / `4`
- Specialist passes / unique sources: `12` / `11`

- Model: `gemini-3.5-flash`
- Evidence Contrast: `enabled`
- Provided reference URLs: `https://deepmind.google/models/model-cards/gemini-3-5-flash`

## Scorecard

- Claims audited: `4`
- Verdict counts: `supported=1` · `overstated=1` · `missing_context=2` · `contradicted=0` · `not_checkable=0`
- Average stretch score: `46/100`
- Provided reference URL count: `1`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). | supported | high | 15 |
| When looking at output tokens per second, it is 4 times faster than other frontier models. | missing_context | high | 20 |
| What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. | missing_context | high | 70 |
| Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. | overstated | high | 80 |

## claim_1: supported

**Confidence:** high

**Original:** It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).

**Stretch Score:** 15/100

**Why:** The benchmark claims are supported by Google's supplementary materials and leaderboards. Gemini 3.5 Flash's scores (76.2% on Terminal-Bench 2.1, 1656 Elo on GDPval-AA, 83.6% on MCP Atlas, and 84.2% on CharXiv Reasoning) indeed exceed Gemini 3.1 Pro's baselines (70.3%, 1314 Elo, 78.2%, and 83.3%, respectively). However, the baseline scores, prompt templates, and data contamination analyses are not explicitly detailed in the main blog post.

**Defensible rewrite:** Gemini 3.5 Flash is our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2% vs. 70.3%), GDPval-AA (1656 Elo vs. 1314 Elo), and MCP Atlas (83.6% vs. 78.2%), and leading in multimodal understanding with 84.2% on CharXiv Reasoning (vs. 83.3% for Gemini 3.1 Pro).

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 77.30s / 20.79s / 23.95s / 24.27s / 53.01s / 0ms

### Agent Steps

<details><summary>grounded_verifier: The benchmark scores mentioned in the claim (Terminal-Bench 2.1: 76.2%, GDPval-AA: 1656 Elo, MCP Atlas: 83.6%, and CharXiv Reasoning: 84.2%) are supported by the blog post and the official Google DeepMind supplementary materials. However, neither the primary blog post nor the supplementary 'Gemini 3.5 Flash Model Card' or 'Model Evaluation' documents provide information about evaluations conducted to rule out training data leakage/contamination for these specific benchmarks, nor do they document the specific prompt templates used for the model comparisons.</summary>

**Duration:** 20.79s

**Supporting evidence:**
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Supports the exact benchmark scores mentioned in the claim, though it lacks details on prompt templates and data contamination evaluations.
- Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard... MCP Atlas results are reported from the ScaleAI official leaderboard... GDPval-AA results are sourced from the Artificial Analysis public leaderboard... CharXiv Reasoning results for Gemini models and GPT 5.5 are self-computed. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf)). Relevance: Provides additional details on where benchmark results were sourced (e.g., self-computed or public leaderboards) but does not include any details about prompt templates or data leakage checks for these benchmarks.

**Missing context:**
- Evaluations conducted to detect or rule out training data leakage/contamination for Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning.
- Prompt templates used for each model during the benchmark comparison.

**Computed checks:**
- Terminal-Bench 2.1 score of 76.2%
- GDPval-AA score of 1656 Elo
- MCP Atlas score of 83.6%
- CharXiv Reasoning score of 84.2%

</details>

<details><summary>contradiction_finder: Neither the Google Blog post nor the official Gemini 3.5 Flash Model Card provides any information regarding evaluations conducted to rule out training data leakage or contamination for Terminal-Bench 2.1, GDPval-AA, MCP Atlas, or CharXiv Reasoning. Furthermore, the exact prompt templates and model configurations (such as thinking levels or sampling parameters) used for Gemini 3.5 Flash, Gemini 3.1 Pro, and other compared models are completely omitted from the public documentation. The Model Card simply states that Gemini 3.5 Flash is based on Gemini 3 Flash and redirects training dataset inquiries to the older model's documentation, which does not cover these newly released 2026 benchmarks.</summary>

**Duration:** 23.95s

**Contradictions / narrowing evidence:**
- For more information about the training dataset for Gemini 3.5 Flash, see the Gemini 3 Flash model card. ... We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and negatives, as well as update query sets to ensure balance and maintain a high standard of results. The performance results reported below are computed with improved evaluations and thus are not directly comparable with performance results found in previous Gemini model cards. ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-5-Flash-Model-Card.pdf)). Relevance: The official model card redirects inquiries about training datasets to the Gemini 3 Flash model card and acknowledges changes in internal evaluations, but it fails to specify any methodology, leakage analysis, or prompt templates for the newly evaluated benchmarks (Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning).

**Missing context:**
- No evaluations or protocols are disclosed to rule out training data contamination or leakage for the public benchmarks listed (Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning).
- The prompt templates, system instructions, and configuration details (such as thinking budgets/levels and temperature settings) used to evaluate the models head-to-head are entirely undocumented.
- The Model Card points back to the Gemini 3 Flash documentation for training data processing details, which inherently lacks context for benchmarks released or updated in 2026.

</details>

<details><summary>Numeric Calibrator: The document asserts that Gemini 3.5 Flash outperforms Gemini 3.1 Pro on several benchmarks, but it does not provide the comparison numbers for Gemini 3.1 Pro to verify this. Furthermore, the document contains no information regarding evaluations to rule out training data leakage or the specific prompt templates used for the comparisons.</summary>

**Duration:** 24.27s

**Missing context:**
- Baseline scores for Gemini 3.1 Pro on Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning
- Details of evaluations or protocols to detect and prevent training data leakage
- Prompt templates and hyperparameters utilized during model evaluation

**Computed checks:**
- Gemini 3.5 Flash scores: Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo), MCP Atlas (83.6%), CharXiv Reasoning (84.2%).
- Gemini 3.1 Pro baseline scores are missing from the source document.
- Using external model card data, Gemini 3.1 Pro scored 70.3% on Terminal-Bench 2.1. Absolute delta: 76.2% - 70.3% = 5.9 pp. Relative improvement: (76.2% - 70.3%) / 70.3% = 8.39%.
- Using external model card data, Gemini 3.1 Pro scored 1314 Elo on GDPval-AA. Absolute delta: 1656 - 1314 = 342 Elo. Relative improvement: (1656 - 1314) / 1314 = 26.03%.
- Using external model card data, Gemini 3.1 Pro scored 78.2% on MCP Atlas. Absolute delta: 83.6% - 78.2% = 5.4 pp. Relative improvement: (83.6% - 78.2%) / 78.2% = 6.91%.
- Using external model card data, Gemini 3.1 Pro scored 83.3% on CharXiv Reasoning. Absolute delta: 84.2% - 83.3% = 0.9 pp. Relative improvement: (84.2% - 83.3%) / 83.3% = 1.08%.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `supported` with `high` confidence.</summary>

**Duration:** 53.01s

**Supporting evidence:**
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Supports the exact benchmark scores mentioned in the claim.
- Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard... MCP Atlas results are reported from the ScaleAI official leaderboard... GDPval-AA results are sourced from the Artificial Analysis public leaderboard... CharXiv Reasoning results for Gemini models and GPT 5.5 are self-computed. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf)). Relevance: Provides source verification details for the reported benchmark results.

**Contradictions / narrowing evidence:**
- For more information about the training dataset for Gemini 3.5 Flash, see the Gemini 3 Flash model card. ... We continue to improve our internal evaluations... and thus are not directly comparable with performance results found in previous Gemini model cards. ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-5-Flash-Model-Card.pdf)). Relevance: Demonstrates that official model cards omit specific prompt configurations and data contamination mitigation techniques for the 2026 benchmarks.

**Missing context:**
- Baseline scores for Gemini 3.1 Pro on Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning are missing from the primary blog post.
- No evaluations or protocols are disclosed to rule out training data contamination or leakage for the public benchmarks listed.
- The specific prompt templates, system instructions, and model configurations used for comparison are completely undocumented.

**Computed checks:**
- Gemini 3.5 Flash scores: Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo), MCP Atlas (83.6%), CharXiv Reasoning (84.2%).
- Gemini 3.1 Pro baseline scores (from external model card data): Terminal-Bench 2.1 (70.3%), GDPval-AA (1314 Elo), MCP Atlas (78.2%), CharXiv Reasoning (83.3%).
- Absolute improvement over Gemini 3.1 Pro: +5.9 pp on Terminal-Bench 2.1, +342 Elo on GDPval-AA, +5.4 pp on MCP Atlas, and +0.9 pp on CharXiv Reasoning.

</details>

### Evidence Contrast

**Claim says:** It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).

**Best reference says:** Verifies Gemini 3.5 Flash benchmark scores and details data sources (public leaderboards and self-computation).

**Key qualification:** Does not contain baseline numbers for Gemini 3.1 Pro or training leakage evaluations.

**Delta:** missing_context — While the claim's numeric scores for Gemini 3.5 Flash are entirely accurate, the blog post omits the baseline scores of the model it claims to outperform (Gemini 3.1 Pro), which are only available in external technical model cards. Additionally, details about evaluations to prevent training data contamination and specific prompt configurations are completely undocumented.

**Final verdict:** supported

**Defensible rewrite:** Gemini 3.5 Flash is our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2% vs. 70.3%), GDPval-AA (1656 Elo vs. 1314 Elo), and MCP Atlas (83.6% vs. 78.2%), and leading in multimodal understanding with 84.2% on CharXiv Reasoning (vs. 83.3% for Gemini 3.1 Pro).

### Claim-Level Contrast References

- Gemini 3.5: frontier intelligence with action (blog, authority 90/100): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/. Primary source containing the direct claim.

**Reference snippets / mismatches:**
- Verifies Gemini 3.5 Flash benchmark scores and details data sources (public leaderboards and self-computation). (Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash, supports, https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf). Does not contain baseline numbers for Gemini 3.1 Pro or training leakage evaluations.

**Computed checks:**
- Gemini 3.5 Flash scores: Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo), MCP Atlas (83.6%), CharXiv Reasoning (84.2%).
- Gemini 3.1 Pro baseline scores (from external model card data): Terminal-Bench 2.1 (70.3%), GDPval-AA (1314 Elo), MCP Atlas (78.2%), CharXiv Reasoning (83.3%).
- Absolute improvement over Gemini 3.1 Pro: +5.9 pp on Terminal-Bench 2.1, +342 Elo on GDPval-AA, +5.4 pp on MCP Atlas, and +0.9 pp on CharXiv Reasoning.

**Gemini-discovered supporting sources:**
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Supports the exact benchmark scores mentioned in the claim.
- Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed and for other models are reported from the public leaderboard... MCP Atlas results are reported from the ScaleAI official leaderboard... GDPval-AA results are sourced from the Artificial Analysis public leaderboard... CharXiv Reasoning results for Gemini models and GPT 5.5 are self-computed. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_3-5_flash_model_evaluation.pdf)). Relevance: Provides source verification details for the reported benchmark results.

**Gemini-discovered caveat / counter sources:**
- For more information about the training dataset for Gemini 3.5 Flash, see the Gemini 3 Flash model card. ... We continue to improve our internal evaluations... and thus are not directly comparable with performance results found in previous Gemini model cards. ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-5-Flash-Model-Card.pdf)). Relevance: Demonstrates that official model cards omit specific prompt configurations and data contamination mitigation techniques for the 2026 benchmarks.

**Missing context:**
- Baseline scores for Gemini 3.1 Pro on Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning are missing from the primary blog post.
- No evaluations or protocols are disclosed to rule out training data contamination or leakage for the public benchmarks listed.
- The specific prompt templates, system instructions, and model configurations used for comparison are completely undocumented.


## claim_2: missing_context

**Confidence:** high

**Original:** When looking at output tokens per second, it is 4 times faster than other frontier models.

**Stretch Score:** 20/100

**Why:** While Google's official announcement does not specify the tested competitor models or details about the benchmark environments (such as hardware configurations, batch sizes, or prompt lengths), independent evaluations by Artificial Analysis and WaveSpeed support the 4x speedup claim. Their data shows Gemini 3.5 Flash reaching ~289 tokens per second (TPS), which is about 4.07x to 4.31x faster than Claude Opus 4.7 (~67 TPS) and GPT-5.5 (~71 TPS). However, raw token speed does not scale linearly to agentic workflows, which are largely bounded by other execution latencies like tool calls and API roundtrips.

**Defensible rewrite:** According to independent benchmarks, Gemini 3.5 Flash's raw output speed of ~289 tokens per second is roughly 4 times faster than competitor models like GPT-5.5 and Claude Opus 4.7, though raw token generation speed does not result in a 4x speedup for entire agentic workflows due to non-generation latencies.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 109.02s / 26.76s / 26.18s / 12.06s / 82.22s / 0ms

### Agent Steps

<details><summary>Grounded Verifier: Google's official announcement and DeepMind Model Card do not specify the competitor models tested, nor do they disclose the hardware, batch size, or input/output length configurations used to calculate the 4x speedup claim. However, independent evaluations by Artificial Analysis provide the missing context, showing Gemini 3.5 Flash generating ~278 to 289 output tokens per second (TPS). This is roughly 4x faster than other frontier models such as GPT-5.5 (~63 to 71 TPS) and Claude Opus 4.7 (~50 to 67 TPS).</summary>

**Duration:** 26.76s

**Supporting evidence:**
- When looking at output tokens per second, it is 4 times faster than other frontier models. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Natively contains the original claim about Gemini 3.5 Flash being 4 times faster than other frontier models on output speed.
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiK2TTzPrC_yLRGfOY73QV_FvOE7TYG5Z6dbwjkHMpIEe-CTqqqT_OXiATeSBOv3rX3XR5bQflsb9OZhQLK3U5SEmHLKVwn7Xtq5WDoJIuDHui7mpWr-ftyjvSF_i2cRyccql9SB5XtkoYmOr_4hg2V9cAuVX6YXHqU7mhvhG6f_kpMcXIWTJFic85yuro410_Eq4bQOiVZiTisu-BqyehpJHJd7FPgctAjcq-_W7l0fw_u9Jskmc=)). Relevance: Provides the specific token generation rates for competitor models (Claude Opus 4.7 and GPT-5.5) under independent testing that validate the 4x speedup claim.
- At ~289 tokens per second, Gemini 3.5 Flash is: 11.6x faster than Claude Opus 4.6 (~25 tok/s); 4.6x faster than GPT-5.5 (~63 tok/s); 4.4x faster than Claude Sonnet 4.6 (~65 tok/s); 3.1x faster than Claude Haiku 4.5 (~93 tok/s)... ([Gemini 3.5 Flash: Benchmarks, Cost & Guide | Articles - O-mega.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTOJzqG20F8-wU6msw1px6TMwVJ_6Gv-t-rZFMUKhf2yfh-euGTIPCEB8dRn4Dlq-P-4kbpVBGdsvdvstkZf4yNSTMUrDY-5-71vcAAghQuKVXClMBJ-ELj_ZKdJse3FmGSsMPfwoUyMrn-5Ttk8O-8wlDKNpHo9DOzgc=)). Relevance: Confirms the exact speed measurements of Gemini 3.5 Flash against other frontier competitors, explaining the basis of the 4x to 4.6x speedup claims.
- The speed claim is also notable: four times faster on output tokens per second than other frontier models. Google does not specify which models it is comparing against in the research notes, so treat that figure as directional rather than a precise head-to-head. ([Gemini 3.5 Flash: Google's Fastest Agentic Model | DataCamp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWSBRTy0NctEIubJIdiZr0Qv2qcbzHH__eK-KVOD6yu6u_2-zxVa2C8as61fMqqIWhjR9wKh1TDssW7gODFa5_H5eGoG9U1BJ1wPPmdWWSF2HhQSEW2uOBp0tG-Lz0voypDk72)). Relevance: Points out that Google does not explicitly document the specific configurations or baseline competitor models within its official research notes.
- Source returned by Gemini grounding metadata. ([deepmind.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE36-MHdAuqQCqjECbRnlYeUzZdeVCwBlHZsTohpSBZThUQRBScvhBpQRqtlQE9akPCGrNB0v_cuBeKXnLRjlKgfVQ7Nd4-VJTJuYwyU8Bnt7lf4FMEIaSfbvn4gAXrOEGJPoTtMjvLrS8BC00M_Oo_Hv4=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([appwrite.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF96o1owQc86PQXP8NB12Mp1gX1Iracuh2jeOLS9hmgnX3LOx9fBRqZ9Ev6IdGuLp_gke2UCPuRNOuQ6yie4rcEiaql0PMNUfrTdgC2czqlma1hDAlYk0qE3T2mDaiG_ZFEPBRqK7641K8RPV7usg==)). Relevance: Grounding source used during specialist audit.

**Missing context:**
- Google's official release documents and deepmind model cards omit the specific hardware (e.g., TPU v6 Trillium vs. GPU setups), batch size, and input/output lengths used during the internal evaluation of output tokens per second to declare the 4x speedup.

**Computed checks:**
- 289 output tokens per second (TPS) achieved by Gemini 3.5 Flash in independent benchmarking.
- 50 to 67 tokens per second generated by Claude Opus 4.7.
- 63 to 71 tokens per second generated by GPT-5.5.

</details>

<details><summary>Skeptical Contradiction Finder: Google's claim of a 4x output tokens/sec speedup lacks official technical details regarding the hardware, batch sizes, and token lengths used in their tests. While independent testing from Artificial Analysis and WaveSpeed validates the ~4x speed advantage (with Gemini 3.5 Flash generating ~280-289 tokens/sec compared to GPT-5.5 at 71 tokens/sec and Claude Opus 4.7 at 67 tokens/sec), Google's announcement does not detail its exact testing configurations. Additionally, a 4x output speed does not translate to 4x faster agentic workflows, as agent runtime is heavily gated by non-generation steps (tool calls, environmental latency, and API execution).</summary>

**Duration:** 26.18s

**Supporting evidence:**
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbSrQ2jGJr-33Expmaad1NVx6_4Jx_ch3RwgPDwM6H0hQUY1dbgCYrPw4mcQiogyXUivBMLEuwMMtl1auuf1xuoNHLBJNuI0QIOEYNNFmeXYiwS4ABPS5enLvzD0QDS6kibKde66AWeT0f3HlOMXwdCAZDWAhGhX1DYkZKyLJwkVYywEsG4vJJx7CvmtfiTH1sTeRY1gH2XIgVLCejzjmm5CDqsUcEx-LUnzXicb45TollTeBgXwM=)). Relevance: Validates the numeric claim using independent benchmark data from Artificial Analysis and WaveSpeed, identifying GPT-5.5 and Claude Opus 4.7 as the compared frontier models.

**Missing context:**
- Google's official announcement does not specify the hardware configurations (such as TPU type), batch sizes, or input/output token lengths used to measure the 4x speedup, nor did they name the competitor models in their release materials.
- A 4x increase in output token generation speed does not result in 4x faster execution for agentic loops. Much of an agent's latency is spent on tool execution, environment interactions, file I/O, and API roundtrips, which are not accelerated by the LLM's raw output speed.
- The 4x speedup is evaluated specifically on raw text generation. In multi-turn reasoning and agentic tasks, Gemini 3.5 Flash's dynamic thinking is enabled by default, which can introduce verbosity and higher overall generation volumes (and subsequent API costs) compared to simpler workflows.

**Computed checks:**
- Gemini 3.5 Flash generates over 289 output tokens per second, according to WaveSpeed and Artificial Analysis.
- Claude Opus 4.7 achieves 67 tokens per second, and GPT-5.5 achieves 71 tokens per second, meaning Gemini 3.5 Flash is roughly 4.07x to 4.31x faster than these specific competitor frontier models.

</details>

<details><summary>Numeric Calibrator: The provided document lacks the empirical data and context required to verify the '4 times faster' speedup claim. While the document asserts this speedup in terms of output tokens per second, it does not identify the specific competitor models, baseline speeds, hardware setups, batch sizes, or token lengths used in the measurement.</summary>

**Duration:** 12.06s

**Supporting evidence:**
- When looking at output tokens per second, it is 4 times faster than other frontier models. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: This is the source of the claim being audited.

**Missing context:**
- Specific competitor frontier models tested (only generic 'other frontier models' is provided).
- Baseline speed metrics (output tokens per second) for Gemini 3.5 Flash and the competitor models.
- Hardware configurations (GPUs/TPUs) used during the benchmark tests.
- The batch size configuration for the measurements.
- The input and output prompt/response token lengths used for testing.

**Computed checks:**
- Claimed multiplier: 4x faster.
- Implied speedup ratio: Speed(Gemini 3.5 Flash) / Speed(Other Frontier Models) = 4.0
- Relative speedup calculation: (4.0 - 1.0) / 1.0 * 100% = 300% increase in output throughput.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `high` confidence.</summary>

**Duration:** 82.22s

**Supporting evidence:**
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbSrQ2jGJr-33Expmaad1NVx6_4Jx_ch3RwgPDwM6H0hQUY1dbgCYrPw4mcQiogyXUivBMLEuwMMtl1auuf1xuoNHLBJNuI0QIOEYNNFmeXYiwS4ABPS5enLvzD0QDS6kibKde66AWeT0f3HlOMXwdCAZDWAhGhX1DYkZKyLJwkVYywEsG4vJJx7CvmtfiTH1sTeRY1gH2XIgVLCejzjmm5CDqsUcEx-LUnzXicb45TollTeBgXwM=)). Relevance: Independent benchmarks by Artificial Analysis validate Gemini 3.5 Flash outputting over 289 tokens per second, roughly 4 times faster than GPT-5.5 (71 TPS) and Claude Opus 4.7 (67 TPS).
- At ~289 tokens per second, Gemini 3.5 Flash is: 11.6x faster than Claude Opus 4.6 (~25 tok/s); 4.6x faster than GPT-5.5 (~63 tok/s); 4.4x faster than Claude Sonnet 4.6 (~65 tok/s); 3.1x faster than Claude Haiku 4.5 (~93 tok/s)... ([Gemini 3.5 Flash: Benchmarks, Cost & Guide | Articles - O-mega.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYGTOJzqG20F8-wU6msw1px6TMwVJ_6Gv-t-rZFMUKhf2yfh-euGTIPCEB8dRn4Dlq-P-4kbpVBGdsvdvstkZf4yNSTMUrDY-5-71vcAAghQuKVXClMBJ-ELj_ZKdJse3FmGSsMPfwoUyMrn-5Ttk8O-8wlDKNpHo9DOzgc=)). Relevance: Provides precise speed comparisons of Gemini 3.5 Flash against other competitor models.

**Missing context:**
- Google's official release documents do not name the competitor models or provide hardware configurations, batch sizes, and token lengths used during internal evaluation.
- A 4x increase in raw output token generation speed does not result in a 4x overall speedup for multi-step agentic workflows, which are largely gated by tool execution, file I/O, and API latencies.

**Computed checks:**
- Gemini 3.5 Flash achieves ~289 output tokens per second in independent benchmarking.
- Claude Opus 4.7 achieves ~67 tokens per second.
- GPT-5.5 achieves ~71 tokens per second.
- The speedup ratio is approximately 4.07x to 4.31x faster than these specific competitor models.

</details>

### Evidence Contrast

**Claim says:** When looking at output tokens per second, it is 4 times faster than other frontier models.

**Best reference says:** Independent benchmarking from Artificial Analysis and WaveSpeed validates Gemini 3.5 Flash's speed at over 289 tokens per second (TPS), making it about 4.07x to 4.31x faster than GPT-5.5 (71 TPS) and Claude Opus 4.7 (67 TPS).

**Key qualification:** While Google's official text omits specific benchmarks, third-party data confirms the speedup claims.

**Delta:** missing_context — Google's claim is technically accurate according to independent third-party evaluations, which verify Gemini 3.5 Flash's ~4x raw output speedup over key competitor models (GPT-5.5 and Claude Opus 4.7). However, Google omitted the specifics of these comparisons, such as competitor identities, hardware configurations, and token length details, as well as the crucial caveat that raw output speedups do not equate to equal speedups in complex agentic workflows due to non-generation latencies.

**Final verdict:** missing_context

**Defensible rewrite:** According to independent benchmarks, Gemini 3.5 Flash's raw output speed of ~289 tokens per second is roughly 4 times faster than competitor models like GPT-5.5 and Claude Opus 4.7, though raw token speed does not translate to 4x faster overall agentic workflows.

### Claim-Level Contrast References

- Gemini 3.5: frontier intelligence with action (official_doc, authority 95/100): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/. This is the official Google source where the claim was published.

**Reference snippets / mismatches:**
- Independent benchmarking from Artificial Analysis and WaveSpeed validates Gemini 3.5 Flash's speed at over 289 tokens per second (TPS), making it about 4.07x to 4.31x faster than GPT-5.5 (71 TPS) and Claude Opus 4.7 (67 TPS). (Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft, supports, https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbSrQ2jGJr-33Expmaad1NVx6_4Jx_ch3RwgPDwM6H0hQUY1dbgCYrPw4mcQiogyXUivBMLEuwMMtl1auuf1xuoNHLBJNuI0QIOEYNNFmeXYiwS4ABPS5enLvzD0QDS6kibKde66AWeT0f3HlOMXwdCAZDWAhGhX1DYkZKyLJwkVYywEsG4vJJx7CvmtfiTH1sTeRY1gH2XIgVLCejzjmm5CDqsUcEx-LUnzXicb45TollTeBgXwM=). While Google's official text omits specific benchmarks, third-party data confirms the speedup claims.

**Computed checks:**
- Gemini 3.5 Flash achieves ~289 output tokens per second in independent benchmarking.
- Claude Opus 4.7 achieves ~67 tokens per second.
- GPT-5.5 achieves ~71 tokens per second.
- The speedup ratio is approximately 4.07x to 4.31x faster than these specific competitor models.

**Gemini-discovered supporting sources:**
- Google claims: Gemini 3.5 Flash generates tokens 4 times faster than other frontier models. WaveSpeed and Artificial Analysis confirm: over 289 output tokens per second. Claude Opus 4.7 — 67 tok/s, GPT-5.5 — 71 tok/s. ([Gemini 3.5 Flash: New Pricing, 4x Speed & Thinking Level Changes - WebCraft](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbSrQ2jGJr-33Expmaad1NVx6_4Jx_ch3RwgPDwM6H0hQUY1dbgCYrPw4mcQiogyXUivBMLEuwMMtl1auuf1xuoNHLBJNuI0QIOEYNNFmeXYiwS4ABPS5enLvzD0QDS6kibKde66AWeT0f3HlOMXwdCAZDWAhGhX1DYkZKyLJwkVYywEsG4vJJx7CvmtfiTH1sTeRY1gH2XIgVLCejzjmm5CDqsUcEx-LUnzXicb45TollTeBgXwM=)). Relevance: Independent benchmarks by Artificial Analysis validate Gemini 3.5 Flash outputting over 289 tokens per second, roughly 4 times faster than GPT-5.5 (71 TPS) and Claude Opus 4.7 (67 TPS).
- At ~289 tokens per second, Gemini 3.5 Flash is: 11.6x faster than Claude Opus 4.6 (~25 tok/s); 4.6x faster than GPT-5.5 (~63 tok/s); 4.4x faster than Claude Sonnet 4.6 (~65 tok/s); 3.1x faster than Claude Haiku 4.5 (~93 tok/s)... ([Gemini 3.5 Flash: Benchmarks, Cost & Guide | Articles - O-mega.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYGTOJzqG20F8-wU6msw1px6TMwVJ_6Gv-t-rZFMUKhf2yfh-euGTIPCEB8dRn4Dlq-P-4kbpVBGdsvdvstkZf4yNSTMUrDY-5-71vcAAghQuKVXClMBJ-ELj_ZKdJse3FmGSsMPfwoUyMrn-5Ttk8O-8wlDKNpHo9DOzgc=)). Relevance: Provides precise speed comparisons of Gemini 3.5 Flash against other competitor models.

**Missing context:**
- Google's official release documents do not name the competitor models or provide hardware configurations, batch sizes, and token lengths used during internal evaluation.
- A 4x increase in raw output token generation speed does not result in a 4x overall speedup for multi-step agentic workflows, which are largely gated by tool execution, file I/O, and API latencies.


## claim_3: missing_context

**Confidence:** high

**Original:** What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models.

**Stretch Score:** 70/100

**Why:** The reference URL is the technical model card, which does not substantiate the marketing metrics regarding human labor hours saved ('days or weeks' down to 'a fraction') or comparative pricing ('less than half the cost of other frontier models'). While the model card indicates suitability for 'multi-week enterprise processes' and features to control 'quality, cost and latency,' the specific comparisons to other frontier models and quantified time savings are absent from this official documentation.

**Defensible rewrite:** Gemini 3.5 Flash is designed for agentic workflows, coding tasks, and multi-week enterprise processes, with configurable thinking levels to help manage quality, cost, and latency.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 111.19s / 16.77s / 38.45s / 21.98s / 49.40s / 23.26s

### Agent Steps

<details><summary>grounded_verifier: The claim is a high-level marketing assertion. Neither the primary document nor external technical literature mentions any controlled developer or auditor user studies to quantitatively measure the stated time savings. Instead, the document provides qualitative and anecdotal pilot feedback from industry partners such as Macquarie Bank and Xero. Additionally, the primary text does not outline the specific pricing and usage assumptions used to calculate the 'less than half the cost' claim. External API details indicate Gemini 3.5 Flash is priced at $1.50 per million input tokens and $9.00 per million output tokens, which represents a lower cost tier compared to flagship models from competitors, but no detailed usage scenarios or pricing models are provided to support the exact 'less than half' claim.</summary>

**Duration:** 16.77s

**Supporting evidence:**
- This balance of speed and performance makes 3.5 Flash ideal for tackling long-horizon agentic tasks. What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ... Partners are seeing meaningful impact — from banks and fintechs automating multi-week workflows to data science teams unearthing insights amidst complex data environments. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: This is the primary text containing the original claim and references partner pilots as qualitative context rather than rigorous controlled scientific studies.

**Missing context:**
- Controlled developer and auditor user study methodologies, sample sizes, and quantitative results demonstrating the alleged time savings.
- The exact mathematical assumptions, token ratios, and baseline competitor models used to verify the 'less than half the cost' claim.

**Computed checks:**
- Gemini 3.5 Flash pricing is $1.50 per 1M input tokens and $9.00 per 1M output tokens on the standard tier.

</details>

<details><summary>Contradiction Finder: Google's claim that Gemini 3.5 Flash can complete developer and auditor tasks in a 'fraction of the time' at 'less than half the cost of other frontier models' is not supported by any controlled human-in-the-loop user studies in its official documentation. The 30+ page official Model Evaluation report relies entirely on automated agentic and coding benchmarks (such as Terminal-Bench, SWE-Bench Pro, and Finance Agent v2) alongside anecdotal corporate pilot feedback. Furthermore, while its per-token pricing ($1.50/M input, $9.00/M output) is lower than flagship 'frontier' models, Gemini 3.5 Flash represents a 3x cost increase compared to Gemini 3 Flash Preview, and task-level pricing for multi-agent workflows may be much higher due to token multiplication from parallel sub-agents and reasoning overhead.</summary>

**Duration:** 38.45s

**Supporting evidence:**
- What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Contains the original causal claim attributing massive developer/auditor time and cost savings directly to Gemini 3.5 Flash.
- Gemini 3.5 Flash was evaluated across a range of benchmarks, including coding, reasoning, multimodal capabilities, agentic tool use, and long-context. ... Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed ... SWE-Bench Pro results for Gemini models are self-computed ... using an internal version of the Antigravity harness. ([Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ZiaoXrnfHfKWUebhlPcfHnqttCsLE9XgDq8c_CEUt7QfPBt13xcAuJCfenv_OKNRYRd0pOugxmSX611QuvJ74AemRDSMxDpi1QHl6TnUiZk3GE2DV5AyrGCi_a7d84j16LBUszYG7SjDs_0fjo-cUvJb-BmSZ08-dvlOl_wFacv9oJWzGdzXqX43AbsLjQ==)). Relevance: Confirms that the model was evaluated purely using automated benchmarking datasets and internal simulator harnesses rather than controlled human user studies.

**Contradictions / narrowing evidence:**
- At $0.50 input and $3.00 output per 1M tokens, Gemini 3 Flash Preview is 3x cheaper than Gemini 3.5 Flash [priced at $1.50 and $9.00]. ([Gemini 3.5 Flash vs Gemini 3 Flash Preview: Pricing & Migration (2026) - EvoLink](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrHQY32OHL5c4cSyZDE0Uz0eVhiyUCSfhMQpawOsTfHoUQ-hed3qCv0wq7Turx8ua-1wqIG6KIVIRMNYjJwI7Qnw6YlCn5gMfEooMfITwkkEYyTjiVC1l9_BdSXi4xjY1a1kjdIXWNZE6HfTrQ8OvqB1fbw5kl1Q==)). Relevance: Demonstrates that while 3.5 Flash may be cheaper than flagship frontier models, it is actually three times more expensive on a per-token basis than Google's prior-generation Flash model.
- It actually costs ~5x as much as Gemini 3 Flash and apparently 1.75x as much as Gemini 3.1 Pro. ... Don't compare just the raw $/million tokens, that doesn't show you the actual price in use. ([Gemini 3.5 flash costs 3 times more than the previous version and 30x more than gemini 1.5 flash. - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtlPNe1Gm1CpT2mzP4Qsy1CKzJwZjB1Ep1queP0HDLvZXLhli-lKcy7ZyAAKyYKchAxh8tHCQmGPNhBs4m0hJO4--uzQNyY2tt0zQ3TCghkeV2FsR7CSSCKfYucyPtVk8rZLhgdI7mAs3pu8QYdeue2z2mXvM5E3wkNTyM33tyOpzVrU73sr2DdLfKEJIElbAQO1ULo4tx)). Relevance: Provides developer counter-evidence challenging Google's pricing positioning, indicating substantial cost increases over previous models and warning about real-world usage costs.

**Missing context:**
- No controlled, human-in-the-loop user studies of software developers or financial auditors were conducted or published to quantify the claimed time savings (e.g., 'developer days' or 'auditor weeks' reduced to 'a fraction').
- The 'less than half the cost' comparison is calculated strictly against premium, flagship frontier tiers (such as Claude 3 Opus/4 or GPT-4o/5.5) on a raw per-token basis, rather than other speed-oriented models in the same tier.
- Real-world agentic execution using the Antigravity harness generates severe token overhead from parallel sub-agent chains, reasoning steps, and iterative loops, meaning task-level pricing can easily exceed simple single-turn costs.

**Computed checks:**
- Gemini 3.5 Flash pricing is $1.50 per 1 million input tokens and $9.00 per 1 million output tokens.
- Gemini 3 Flash Preview is priced at $0.50 input and $3.00 output per 1 million tokens, making it 3x cheaper than Gemini 3.5 Flash.
- Gemini 3.5 Flash achieved scores of 76.2% on Terminal-Bench 2.1, 1,656 Elo on GDPval-AA, 83.6% on MCP Atlas, and 84.2% on CharXiv Reasoning.

</details>

<details><summary>Numeric Calibrator Skill: The claim states that Gemini 3.5 Flash completes tasks in a fraction of the time compared to developers taking days or auditors taking weeks, and does so at less than half the cost of other frontier models. While external pricing data supports the cost claim, the provided document lacks any controlled user studies or specific pricing metrics to substantiate these assertions.</summary>

**Duration:** 21.98s

**Supporting evidence:**
- Gemini 3.5 Flash outputs tokens at 289 tokens per second... And it does this while costing $1.50 per million input tokens, compared to $5.00 for Claude Opus 4.6 and $5.00 for GPT-5.5. ([Gemini 3.5 Flash: Benchmarks, Cost & Guide | Articles - O-mega.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz8IbdK9y9gqx3ALCpugnrVhXcnJhkwMcmdYJ2YTuh-Lckq-s6Ati1re2OdsBilp35c-WYYKRZOvbWiCH4Fdg1_B44RisARnFIwLfxKHeGJbKf846mADwfUmv_XTY0eEDvXXd0xe5a8Pfl56wm6JDN4qeYJgkGe3xqXjU=)). Relevance: Provides the external pricing details showing Gemini 3.5 Flash is indeed less than half the cost of other frontier models (30% of their cost).

**Missing context:**
- Controlled developer and auditor user studies quantifying the alleged time savings.
- The specific pricing assumptions, input/output token ratios, and comparison models used inside the document to calculate the 'less than half the cost' figure.

**Computed checks:**
- Using external pricing data: Gemini 3.5 Flash input cost = $1.50 per 1M tokens; competitor frontier models (e.g. Claude Opus 4.6, GPT-5.5) input cost = $5.00 per 1M tokens.
- Cost ratio: $1.50 / $5.00 = 0.30 (or 30% of the competitor cost).
- Relative cost savings: ($5.00 - $1.50) / $5.00 = 70% cost reduction, which is mathematically 'less than half the cost' (less than 50% cost, or greater than 50% savings).

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `overstated` with `high` confidence.</summary>

**Duration:** 49.40s

**Supporting evidence:**
- This balance of speed and performance makes 3.5 Flash ideal for tackling long-horizon agentic tasks. What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Primary text containing the claim.
- Gemini 3.5 Flash outputs tokens at 289 tokens per second... And it does this while costing $1.50 per million input tokens, compared to $5.00 for Claude Opus 4.6 and $5.00 for GPT-5.5. ([Gemini 3.5 Flash: Benchmarks, Cost & Guide | Articles - O-mega.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz8IbdK9y9gqx3ALCpugnrVhXcnJhkwMcmdYJ2YTuh-Lckq-s6Ati1re2OdsBilp35c-WYYKRZOvbWiCH4Fdg1_B44RisARnFIwLfxKHeGJbKf846mADwfUmv_XTY0eEDvXXd0xe5a8Pfl56wm6JDN4qeYJgkGe3xqXjU=)). Relevance: Confirms the per-token cost is less than half the cost of competitor flagship models ($1.50 vs $5.00 is 30% of the cost).

**Contradictions / narrowing evidence:**
- At $0.50 input and $3.00 output per 1M tokens, Gemini 3 Flash Preview is 3x cheaper than Gemini 3.5 Flash [priced at $1.50 and $9.00]. ([Gemini 3.5 Flash vs Gemini 3 Flash Preview: Pricing & Migration (2026) - EvoLink](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrHQY32OHL5c4cSyZDE0Uz0eVhiyUCSfhMQpawOsTfHoUQ-hed3qCv0wq7Turx8ua-1wqIG6KIVIRMNYjJwI7Qnw6YlCn5gMfEooMfITwkkEYyTjiVC1l9_BdSXi4xjY1a1kjdIXWNZE6HfTrQ8OvqB1fbw5kl1Q==)). Relevance: Demonstrates that pricing has increased relative to Google's own previous Flash model.
- Gemini 3.5 Flash was evaluated across a range of benchmarks, including coding, reasoning, multimodal capabilities, agentic tool use, and long-context. ... Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed ... SWE-Bench Pro results for Gemini models are self-computed ... using an internal version of the Antigravity harness. ([Model Evaluation - Approach, Methodology & Results Gemini 3.5 Flash](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ZiaoXrnfHfKWUebhlPcfHnqttCsLE9XgDq8c_CEUt7QfPBt13xcAuJCfenv_OKNRYRd0pOugxmSX611QuvJ74AemRDSMxDpi1QHl6TnUiZk3GE2DV5AyrGCi_a7d84j16LBUszYG7SjDs_0fjo-cUvJb-BmSZ08-dvlOl_wFacv9oJWzGdzXqX43AbsLjQ==)). Relevance: Shows the evaluation relied entirely on automated benchmarking and simulation rather than controlled user studies of actual developer/auditor workflows.

**Missing context:**
- Controlled developer and auditor user studies quantifying actual human productivity improvements.
- The fact that task-level costs in agentic loops can exceed simple per-token calculations due to token recursion and parallel sub-agent chains.
- A comparison to non-flagship or prior-generation models, where Gemini 3.5 Flash represents a price increase (e.g., 3x higher than Gemini 3 Flash Preview).

**Computed checks:**
- Gemini 3.5 Flash input cost is $1.50 per 1M tokens vs competitor flagship model costs of $5.00 per 1M tokens (30% of competitor cost).
- Gemini 3.5 Flash output cost is $9.00 per 1M tokens.
- Gemini 3 Flash Preview is priced at $0.50 input and $3.00 output per 1M tokens (making Gemini 3.5 Flash 3x more expensive).

</details>

### Evidence Contrast

**Claim says:** What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models.

**Best reference says:** The model card does not mention relative cost savings versus competitor models, nor does it contain the 'developer days or auditor weeks' time-reduction claim. It only notes that the model is well-suited for 'agentic workflows, coding tasks, and multi-week enterprise processes' and offers 'thinking levels to control the mix of quality, cost and latency.'

**Key qualification:** The model card is a technical specification and does not list API pricing, competitor pricing benchmarks, or controlled user studies of developer or auditor efficiency.

**Delta:** missing_context — The reference URL is the technical model card, which does not substantiate the marketing metrics regarding human labor hours saved ('days or weeks' down to 'a fraction') or comparative pricing ('less than half the cost of other frontier models'). While the model card indicates suitability for 'multi-week enterprise processes' and features to control 'quality, cost and latency,' the specific comparisons to other frontier models and quantified time savings are absent from this official documentation.

**Final verdict:** missing_context

**Defensible rewrite:** Gemini 3.5 Flash is designed for agentic workflows, coding tasks, and multi-week enterprise processes, with configurable thinking levels to help manage quality, cost, and latency.

### Claim-Level Contrast References

- Gemini 3.5 Flash - Model Card (vendor_doc, authority 95/100): https://deepmind.google/models/model-cards/gemini-3-5-flash. Official model card detailing the model's specifications, evaluations, and intended use cases, allowing us to verify if the time-saving and cost-saving metrics are technically substantiated.

**Reference snippets / mismatches:**
- The model card does not mention relative cost savings versus competitor models, nor does it contain the 'developer days or auditor weeks' time-reduction claim. It only notes that the model is well-suited for 'agentic workflows, coding tasks, and multi-week enterprise processes' and offers 'thinking levels to control the mix of quality, cost and latency.' (Gemini 3.5 Flash - Model Card, unclear, https://deepmind.google/models/model-cards/gemini-3-5-flash). The model card is a technical specification and does not list API pricing, competitor pricing benchmarks, or controlled user studies of developer or auditor efficiency.

**Computed checks:**
- Gemini 3.5 Flash input cost is $1.50 per 1M tokens vs competitor flagship model costs of $5.00 per 1M tokens (30% of competitor cost).
- Gemini 3.5 Flash output cost is $9.00 per 1M tokens.
- Gemini 3 Flash Preview is priced at $0.50 input and $3.00 output per 1M tokens (making Gemini 3.5 Flash 3x more expensive).

**Gemini-discovered supporting sources:**
- This balance of speed and performance makes 3.5 Flash ideal for tackling long-horizon agentic tasks. What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Primary text containing the claim.
- Gemini 3.5 Flash outputs tokens at 289 tokens per second... And it does this while costing $1.50 per million input tokens, compared to $5.00 for Claude Opus 4.6 and $5.00 for GPT-5.5. ([Gemini 3.5 Flash: Benchmarks, Cost & Guide | Articles - O-mega.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz8IbdK9y9gqx3ALCpugnrVhXcnJhkwMcmdYJ2YTuh-Lckq-s6Ati1re2OdsBilp35c-WYYKRZOvbWiCH4Fdg1_B44RisARnFIwLfxKHeGJbKf846mADwfUmv_XTY0eEDvXXd0xe5a8Pfl56wm6JDN4qeYJgkGe3xqXjU=)). Relevance: Confirms the per-token cost is less than half the cost of competitor flagship models ($1.50 vs $5.00 is 30% of the cost).

**Gemini-discovered caveat / counter sources:**
- At $0.50 input and $3.00 output per 1M tokens, Gemini 3 Flash Preview is 3x cheaper than Gemini 3.5 Flash [priced at $1.50 and $9.00]. ([Gemini 3.5 Flash vs Gemini 3 Flash Preview: Pricing & Migration (2026) - EvoLink](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrHQY32OHL5c4cSyZDE0Uz0eVhiyUCSfhMQpawOsTfHoUQ-hed3qCv0wq7Turx8ua-1wqIG6KIVIRMNYjJwI7Qnw6YlCn5gMfEooMfITwkkEYyTjiVC1l9_BdSXi4xjY1a1kjdIXWNZE6HfTrQ8OvqB1fbw5kl1Q==)). Relevance: Demonstrates that pricing has increased relative to Google's own previous Flash model.
- Gemini 3.5 Flash was evaluated across a range of benchmarks, including coding, reasoning, multimodal capabilities, agentic tool use, and long-context. ... Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed ... SWE-Bench Pro results for Gemini models are self-computed ... using an internal version of the Antigravity harness. ([Model Evaluation - Approach, Methodology & Results Gemini 3.5 Flash](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ZiaoXrnfHfKWUebhlPcfHnqttCsLE9XgDq8c_CEUt7QfPBt13xcAuJCfenv_OKNRYRd0pOugxmSX611QuvJ74AemRDSMxDpi1QHl6TnUiZk3GE2DV5AyrGCi_a7d84j16LBUszYG7SjDs_0fjo-cUvJb-BmSZ08-dvlOl_wFacv9oJWzGdzXqX43AbsLjQ==)). Relevance: Shows the evaluation relied entirely on automated benchmarking and simulation rather than controlled user studies of actual developer/auditor workflows.

**Missing context:**
- Controlled developer and auditor user studies quantifying actual human productivity improvements.
- The fact that task-level costs in agentic loops can exceed simple per-token calculations due to token recursion and parallel sub-agent chains.
- A comparison to non-flagship or prior-generation models, where Gemini 3.5 Flash represents a price increase (e.g., 3x higher than Gemini 3 Flash Preview).


## claim_4: overstated

**Confidence:** high

**Original:** Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.

**Stretch Score:** 80/100

**Why:** The claim that the model can 'reliably' execute multi-step workflows and coding tasks is qualified and narrowed by the actual benchmark performance documented in the model card, which shows success rates of 55.1% on SWE-Bench Pro and 56.5% on Toolathlon (equivalent to failure rates of 44.9% and 43.5% respectively). Additionally, third-party analysis of the GDPval-AA agentic evaluation indicates that the model requires an average of 49 interaction turns per task to achieve its ELO, suggesting high operational friction rather than seamless reliability.

**Defensible rewrite:** Under active supervision, it can assist with multi-step workflows and coding tasks, though official evaluations show success rates of 55.1% on SWE-Bench Pro coding tasks and 56.5% on Toolathlon tool-use tasks.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 154.93s / 15.77s / 27.15s / 9.65s / 111.30s / 16.37s

### Agent Steps

<details><summary>grounded_verifier: The official Google announcement and available technical literature do not provide a quantified failure/error rate for Gemini 3.5 Flash on multi-step workflows, nor do they define the specific protocol or human-to-AI intervention ratio that constitutes the required 'supervision'. While Google cites benchmark results indicating general performance (such as Terminal-Bench 2.1 at 76.2% and MCP Atlas at 83.6%), the qualitative claim that the model executes workflows 'reliably' under 'supervision' remains unquantified. External developer reports and early reviews indicate real-world failure modes, including endless looping and coordination issues during unsupervised/poorly supervised complex runs.</summary>

**Duration:** 15.77s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: This is the source of the claim itself. However, it presents the claim as a qualitative generalization without specifying failure rates or details about the 'supervision' protocol.

**Contradictions / narrowing evidence:**
- I tried Gemini 3.5, I gave it a task - verify the feasibility over a proposed AI architecture... It kept looping endlessly. Compacting, verifying, over and over. ... PLANNER_RESPONSE (model talking), 194. VIEW_FILE (reading files), 160. LIST_DIRECTORY, 25. RUN_COMMAND (actual execution), 4. CODE_ACTION (writing files), 2. 160 file reads. ([Antigravity 2.0..... lackluster? Gemini 3.5 Flash seems - Google AI Developers Forum](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgCfpnDZGFdKqPY6yUxvQdkcEIR3a5D_cedeGG7xlXWSqdNPduA-tGNv7lbPO0AzMAqGDxG6pOFRE8yFVv6HwtXm7IGknaKhWFldR_cw2EqeShpSRhcheNJH5iHgTZMg6aTkpu5vWyW-iNhacINeRZ_Xus-C1Wc9-8TtKu1yKqs_JDt9ekii5yG4S_mia9)). Relevance: Highlights a real-world multi-step workflow failure mode (infinite looping during file verification) where supervision was missing or failed to interrupt the model automatically.
- Gemini 3.5 Flash (High) in Antigravity rewrote my production code because I said the backtest results 'sucked' and couldn't clean up after itself. ([Gemini 3.5 Flash (High) in Antigravity rewrote my production code... - Reddit](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSmasbNhrvIKoakbAQkzfDz6I04KZlHWfx-NOtWyfvBy5_5LUKONnV1FH0vArC12rblvCxei8NfjaBfHEuhsjbXi7vdrLL16LjZa-ynzNmXM9gwh2uoC_aLSUXxxK-n-iNzGiqYJGyfqkt7JpmeX1jKDeRsE6VzbWXHTm3z1xM74HRoyDirAnLQACN50ZsoBeQ0_JF-_H_EVJehfIzHIsGS7k=)). Relevance: Demonstrates a failure of the model to work reliably without precise, strict supervision, resulting in unprompted destructive code edits.

**Missing context:**
- Google's official documentation lacks a quantified failure/error rate specifically for multi-step workflows, offering only generic benchmark scores (e.g., Terminal-Bench and MCP Atlas) rather than workflow failure metrics.
- The required 'supervision' protocol or the exact division/ratio of human-AI labor is never defined or quantified in Google's releases.

</details>

<details><summary>Skeptical Contradiction Finder: The claim that Gemini 3.5 Flash can 'reliably' execute multi-step workflows and coding tasks under 'supervision' lacks any operational definition, quantitative ratio, or explicit protocol of human intervention in the official text. Quantitative data from the model's official card and independent reviews reveal significant failure/error rates on complex multi-step tasks. Specifically, Gemini 3.5 Flash fails on 44.9% of diverse agentic coding tasks (SWE-Bench Pro) and 43.5% of general tool-use tasks (Toolathlon). Furthermore, independent evaluations from Artificial Analysis indicate that to achieve its success rates, the model relies on an exceptionally high-volume iterative process (averaging an industry-high 49 turns per task on the GDPval-AA agentic evaluation), which inflates token usage and introduces a larger surface area for unsupervised errors.</summary>

**Duration:** 27.15s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: The original claim being evaluated, establishing the baseline expectation of reliable execution under supervision.

**Contradictions / narrowing evidence:**
- SWE-Bench Pro (Public) Diverse agentic coding tasks, Single attempt, 55.1%... Toolathlon Real-world general [tool use], 56.5%... Terminal-bench 2.1 Agentic terminal coding, Terminus-2 harness, 76.2%. ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://deepmind.google/technologies/gemini/)). Relevance: Provides quantified proof of substantial failure/error rates on multi-step workflows, showing a 44.9% failure rate on SWE-Bench Pro, a 43.5% failure rate on Toolathlon, and a 23.8% failure rate on Terminal-Bench 2.1.
- Gemini 3.5 Flash nearly matches GPT-5.4 on agent tasks but needs the most interaction steps of any model tested. Claude Opus 4.7 (max) takes 45, GPT-5.4 (xhigh) takes 40, and Gemini 3.1 Pro only needs 23. All those extra interaction steps drive input token consumption way up. ([Google's Gemini 3.5 Flash follows Anthropic and OpenAI in making newer AI models significantly pricier - The Decoder](https://the-decoder.com/googles-gemini-3-5-flash-is-more-expensive-but-smarter-than-predecessor/)). Relevance: Reveals that the model requires an average of 49 turns per task on the GDPval-AA agentic evaluation to succeed, which exposes a major limitation in the autonomous reliability of long-horizon execution.

**Missing context:**
- No quantified human-in-the-loop ratio, verification protocol, or operational standard for what constitutes 'supervision' is defined in the official Google blog post or technical documentation.
- The official blog post presents named partner deployments (e.g., Shopify, Macquarie Bank, Salesforce) as successful evidence without publishing their internal task-failure metrics or the specific supervision/validation protocols applied to prevent errors.
- Independent reviews note that the model suffers from relative performance regressions on pure reasoning tasks (such as ARC-AGI-2 and Humanity's Last Exam) compared to older Pro models, which can negatively affect the accuracy of coding decisions in unsupervised chains.

**Computed checks:**
- SWE-Bench Pro failure/error rate: 44.9% (55.1% success rate on diverse agentic coding tasks).
- Terminal-Bench 2.1 failure/error rate: 23.8% (76.2% success rate on agentic terminal coding).
- Toolathlon failure/error rate: 43.5% (56.5% success rate on general real-world tool-use workflows).
- MCP Atlas failure/error rate: 16.4% (83.6% success rate on multi-step workflows).
- Average step count on agentic tasks (GDPval-AA): 49 turns per task, higher than all comparable competitor models.

</details>

<details><summary>numeric_calibrator: The claim qualitatively asserts that Gemini 3.5 can reliably execute multi-step workflows and coding tasks under supervision, but the document lacks any quantitative benchmarks, failure rates, or definitions of the required human supervision.</summary>

**Duration:** 9.65s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: This is the exact qualitative statement evaluated by the audit question.

**Missing context:**
- Quantified failure or error rate of Gemini 3.5 Flash on multi-step workflows.
- Specific protocol or ratio of human intervention that constitutes the 'supervision' required to sustain success.
- A quantitative baseline or threshold defining 'reliably' (e.g., success rate percentage).

**Computed checks:**
- No arithmetic calculations are possible because the document contains no quantitative data, percentages, or ratios regarding the failure rates or supervision metrics for multi-step workflows.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `overstated` with `high` confidence.</summary>

**Duration:** 111.30s

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: The original source of the claim.

**Contradictions / narrowing evidence:**
- SWE-Bench Pro (Public) Diverse agentic coding tasks, Single attempt, 55.1%... Toolathlon Real-world general [tool use], 56.5%... Terminal-bench 2.1 Agentic terminal coding, Terminus-2 harness, 76.2%. ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://deepmind.google/technologies/gemini/)). Relevance: Provides quantified proof of substantial failure/error rates on multi-step workflows, showing a 44.9% failure rate on SWE-Bench Pro, a 43.5% failure rate on Toolathlon, and a 23.8% failure rate on Terminal-Bench 2.1.
- Gemini 3.5 Flash nearly matches GPT-5.4 on agent tasks but needs the most interaction steps of any model tested. Claude Opus 4.7 (max) takes 45, GPT-5.4 (xhigh) takes 40, and Gemini 3.1 Pro only needs 23. All those extra interaction steps drive input token consumption way up. ([Google's Gemini 3.5 Flash follows Anthropic and OpenAI in making newer AI models significantly pricier - The Decoder](https://the-decoder.com/googles-gemini-3-5-flash-is-more-expensive-but-smarter-than-predecessor/)). Relevance: Reveals that the model requires an average of 49 turns per task on the GDPval-AA agentic evaluation to succeed, which exposes a major limitation in autonomous reliability.

**Missing context:**
- No quantified human-in-the-loop ratio, verification protocol, or operational standard for what constitutes 'supervision' is defined in the official Google blog post or technical documentation.
- Google's official documentation lacks a quantified failure/error rate specifically for multi-step workflows, offering only generic benchmark scores rather than workflow failure metrics.

**Computed checks:**
- SWE-Bench Pro failure/error rate: 44.9% (55.1% success rate on diverse agentic coding tasks).
- Terminal-Bench 2.1 failure/error rate: 23.8% (76.2% success rate on agentic terminal coding).
- Toolathlon failure/error rate: 43.5% (56.5% success rate on general real-world tool-use workflows).
- MCP Atlas failure/error rate: 16.4% (83.6% success rate on multi-step workflows).
- Average step count on agentic tasks (GDPval-AA): 49 turns per task, higher than all comparable competitor models.

</details>

### Evidence Contrast

**Claim says:** Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.

**Best reference says:** The official model card reports a success rate of 55.1% on SWE-Bench Pro (diverse agentic coding tasks) and 56.5% on Toolathlon (real-world general tool use) in single-attempt evaluations.

**Key qualification:** Succeeds roughly 55-56% of the time, resulting in a failure rate of over 43% on autonomous coding and tool use.

**Delta:** narrower_than_claim — The claim that the model can 'reliably' execute multi-step workflows and coding tasks is qualified and narrowed by the actual benchmark performance documented in the model card, which shows success rates of 55.1% on SWE-Bench Pro and 56.5% on Toolathlon (equivalent to failure rates of 44.9% and 43.5% respectively). Additionally, third-party analysis of the GDPval-AA agentic evaluation indicates that the model requires an average of 49 interaction turns per task to achieve its ELO, suggesting high operational friction rather than seamless reliability.

**Final verdict:** overstated

**Defensible rewrite:** Under active supervision, it can assist with multi-step workflows and coding tasks, though official evaluations show success rates of 55.1% on SWE-Bench Pro coding tasks and 56.5% on Toolathlon tool-use tasks.

### Claim-Level Contrast References

- Gemini 3.5 Flash - Model Card (vendor_doc, authority 100/100): https://deepmind.google/models/model-cards/gemini-3-5-flash. It contains the official DeepMind evaluation metrics and benchmark performance results for Gemini 3.5 Flash.

**Reference snippets / mismatches:**
- The official model card reports a success rate of 55.1% on SWE-Bench Pro (diverse agentic coding tasks) and 56.5% on Toolathlon (real-world general tool use) in single-attempt evaluations. (Gemini 3.5 Flash - Model Card, narrows, https://deepmind.google/models/model-cards/gemini-3-5-flash). Succeeds roughly 55-56% of the time, resulting in a failure rate of over 43% on autonomous coding and tool use.

**Computed checks:**
- SWE-Bench Pro failure/error rate: 44.9% (55.1% success rate on diverse agentic coding tasks).
- Terminal-Bench 2.1 failure/error rate: 23.8% (76.2% success rate on agentic terminal coding).
- Toolathlon failure/error rate: 43.5% (56.5% success rate on general real-world tool-use workflows).
- MCP Atlas failure/error rate: 16.4% (83.6% success rate on multi-step workflows).
- Average step count on agentic tasks (GDPval-AA): 49 turns per task, higher than all comparable competitor models.

**Gemini-discovered supporting sources:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: The original source of the claim.

**Gemini-discovered caveat / counter sources:**
- SWE-Bench Pro (Public) Diverse agentic coding tasks, Single attempt, 55.1%... Toolathlon Real-world general [tool use], 56.5%... Terminal-bench 2.1 Agentic terminal coding, Terminus-2 harness, 76.2%. ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://deepmind.google/technologies/gemini/)). Relevance: Provides quantified proof of substantial failure/error rates on multi-step workflows, showing a 44.9% failure rate on SWE-Bench Pro, a 43.5% failure rate on Toolathlon, and a 23.8% failure rate on Terminal-Bench 2.1.
- Gemini 3.5 Flash nearly matches GPT-5.4 on agent tasks but needs the most interaction steps of any model tested. Claude Opus 4.7 (max) takes 45, GPT-5.4 (xhigh) takes 40, and Gemini 3.1 Pro only needs 23. All those extra interaction steps drive input token consumption way up. ([Google's Gemini 3.5 Flash follows Anthropic and OpenAI in making newer AI models significantly pricier - The Decoder](https://the-decoder.com/googles-gemini-3-5-flash-is-more-expensive-but-smarter-than-predecessor/)). Relevance: Reveals that the model requires an average of 49 turns per task on the GDPval-AA agentic evaluation to succeed, which exposes a major limitation in autonomous reliability.

**Missing context:**
- No quantified human-in-the-loop ratio, verification protocol, or operational standard for what constitutes 'supervision' is defined in the official Google blog post or technical documentation.
- Google's official documentation lacks a quantified failure/error rate specifically for multi-step workflows, offering only generic benchmark scores rather than workflow failure metrics.

