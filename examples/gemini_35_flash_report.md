# CappinCheck Report: Gemini 3.5: frontier intelligence with action

Source: `https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/`

## Provenance

- Mode: `live_gemini`
- Runtime: `local`
- Model: `gemini-3.5-flash`
- Evidence Contrast: `enabled`
- Provided reference URLs: `https://deepmind.google/models/model-cards/gemini-3-5-flash`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). | overstated | high | 45 |
| When looking at output tokens per second, it is 4 times faster than other frontier models. | overstated | high | 60 |
| What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. | overstated | high | 80 |
| Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. | overstated | high | 45 |

## claim_1: overstated

**Confidence:** high

**Original:** It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).

**Stretch Score:** 45/100

**Why:** While Gemini 3.5 (specifically Gemini 3.5 Flash) does achieve the cited benchmark numbers and outperforms Gemini 3.1 Pro on the specified tasks, framing it unconditionally as Google's 'strongest agentic and coding model yet' is overstated. Independent evaluations show that Gemini 3.5 Flash actually regresses against the older Gemini 3.1 Pro on pure reasoning and long-context benchmarks (such as ARC-AGI-2, Humanity's Last Exam, and MRCR v2 128k context). Furthermore, the peak performance listed depends on a 'high' thinking level configuration that is disabled by default in the API, and some of the benchmarks (Terminal-Bench 2.1 and CharXiv Reasoning) were self-computed internally by Google with potential risks of training set contamination.

**Defensible rewrite:** Gemini 3.5 Flash outperforms Gemini 3.1 Pro on several key coding and agentic benchmarks when configured with its 'high' thinking level, achieving 76.2% on Terminal-Bench 2.1, 1656 Elo on GDPval-AA, and 83.6% on MCP Atlas, despite experiencing some regressions on pure reasoning and long-context tasks.

### Agent Steps

<details><summary>grounded_verifier: The claim that Gemini 3.5 (specifically Gemini 3.5 Flash) outperforms Gemini 3.1 Pro on the specified benchmarks is partially validated by independent third-party evaluations. Specifically, the GDPval-AA score of 1656 Elo has been independently verified and published on the Artificial Analysis leaderboard, and the MCP Atlas score of 83.6% is sourced from Scale AI's official leaderboard. However, the Terminal-Bench 2.1 score of 76.2% and the CharXiv Reasoning score of 84.2% were self-computed by Google DeepMind and have not yet been independently validated under audited external test environments, leaving questions regarding potential training set contamination and reproducibility open for those specific tests.</summary>

**Supporting evidence:**
- Gemini 3.5 Flash scores 55 on the Artificial Analysis Intelligence Index, up 9 points from Gemini 3 Flash... Its GDPval-AA result is especially notable, achieving an Elo of 1656, well ahead of Gemini 3 Flash (1204) and Gemini 3.1 Pro (1314). ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://artificialanalysis.ai/evaluations/gdpval-aa)). Relevance: Provides independent verification of the GDPval-AA benchmark score of 1656 Elo, which was run by Artificial Analysis.
- Terminal-Bench 2.1 results for Gemini 3.5 Flash and 3 Flash are self computed... MCP Atlas results are reported from the ScaleAI official leaderboard... GDPval-AA results are sourced from the Artificial Analysis public leaderboard... CharXiv Reasoning results for Gemini models and GPT 5.5 are self-computed. (Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash). Relevance: The official evaluation details from Google DeepMind confirm that the GDPval-AA and MCP Atlas results are derived from external leaderboards, whereas Terminal-Bench 2.1 and CharXiv Reasoning are self-computed internally.

**Missing context:**
- Terminal-Bench 2.1 and CharXiv Reasoning scores were self-computed by Google rather than independently evaluated by the benchmark hosts, leaving their reproducibility and potential training set contamination unverified by external parties.

**Computed checks:**
- GDPval-AA Elo score of 1656
- MCP Atlas score of 83.6%
- Terminal-Bench 2.1 score of 76.2%
- CharXiv Reasoning score of 84.2%

</details>

<details><summary>Skeptical Contradiction Finder: While independent benchmarks (such as Artificial Analysis and Scale AI leaderboards) confirm that Gemini 3.5 Flash achieves the reported scores of 1656 Elo on GDPval-AA and 83.6% on MCP Atlas, the claim of it being 'our strongest agentic and coding model yet' hides significant caveats. First, the model actually regresses against the older Gemini 3.1 Pro on pure abstract reasoning and long-context benchmarks. Second, both Terminal-Bench and CharXiv datasets are vulnerable to pretraining data contamination due to their open public nature. Third, Google evaluated these benchmarks under self-computed, non-standard environments, and the peak performance metrics depend on a 'high' thinking level that is disabled by default in the API.</summary>

**Supporting evidence:**
- Its GDPval-AA result is especially notable, achieving an Elo of 1656, well ahead of Gemini 3 Flash (1204) and Gemini 3.1 Pro (1314) ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Independently verifies that Gemini 3.5 Flash achieves 1656 Elo on GDPval-AA and outperforms Gemini 3.1 Pro under external evaluation [2.2.8].
- MCP-Atlas evaluates how well AI agents can use tools to complete real-world tasks. The benchmark includes: 36 MCP servers... 500 evaluation prompts ([scaleapi/mcp-atlas - GitHub](https://github.com/scaleapi/mcp-atlas)). Relevance: Verifies the official structure of the MCP Atlas benchmark, matching the 83.6% tool-use performance claimed by Google.
- Source returned by Gemini grounding metadata. ([appwrite.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyV_zWmMunMgcGwZt2NcDPNh_7omIJ-m8DrWxxaCZp72Sy1Ox5RQAMWdQy1_ElkvrsgLaFB0ZcOyeXEhNu0YreoYe5joKhuGogIuBrQKZXh9lVSCbz-Gw6wa5E3pXWO2PyawaUcSMzzD9TYQq9wg==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([artificialanalysis.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHlRkbzh2r2ben8sC8tPiP--LgXMYW4m1YQRZrzCfqaQdCgjEK2j1rOxifawDNHjNlULHxq-0JTx5xFk6I_lGsPcHgNb9Qppq2d2OUFE8rTf_5dVHt6xBpZvheNgBP52OzMgY5V7RnbpE_DDCxQqVzXOTkLUasymdV7t5OsGOxKaeozYFH6BsK9Q==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([nxcode.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Eux_OW1E6uke2RPIRNn2PlpviiWB3Yl92yoNACBqOt1Au-tpn-vPXMBh2JL1Pz-zqFsGyUHp6QSdHGqDj5fyMKtPMPlmwwsq_IaUonhPGlkgVrDX7Bz3-vPnLQBH0X1oYl3ati5VJixDzy4GmiJuhqqF5QTaELum09WLgzts25CzDcAny7pvs1NvzLdM1rfRUBxTY_g=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM8aNGbTidSz9ZYp8u_UAeKlh3Pq5FuHwWPDESRBMCPrMYZ_5wazg2pFt1OgVAjomen76Fwin7qJFm2MNjDYVdyu7VjbOZ75ZoSmtbfhSKNiQNhBtH9BQrsg==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([anthropic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsa2yEHP8MDd0SpH1_5FH6ZDR07HuCpaB9tdMKKNlZVc3iEzIA-241VlHBKI6hC92fxcQBDxarN2CaU-cHToU8ySyTWupe7bIchbtavCqrnwtaOqsy8ivH_UdjAdUb3uE31Fz5CH2v7a7-VhJzKyQF6drFSltWiIwRmq0OGGAMwA==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([googleapis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhFmvHQ30j9tn54gWrVKNlZW2_1Ktq01uLEnOzo8Y0w39jvtYbBR8uGlPW0gE3f2nl35WS0CLIi71voCfGhPKov66f1gNWIIFmRCjesgyzlJmNIF4XHeidSeROnLg8S9cuqdmWSD-g7jCqcP8tf-a8eoYZ4D4jtyH6xvWUI-lH_iqXFNVRZQ31BMv2mq1h-1k=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrxzqD7TExRL9ekPGtzRr1_RLDDDLP3spRaUxiJ2_whxhkC929JC3iFA1JFcr5ElzaVS0NH9HakBPBb8NyxfKAeuDwxx0Z6qOL8beL2obFrwmbezgborTcKXzx)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([tosea.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFTR1ZigKjFDBY-95V5FLJfWyE9PzGxW1gnyUEYZn1JfIpllfxvrhfaNxzEpElJ3Nbm8vUh7_yUHPUln7WVj0dMSNtxiyLcobe1fUbo2SPR1Fj3NZsGiMbggf2QlqZ75LUBkAOqDMn25-nodSCcUwb)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([appwrite.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ2dTkVqhLU8-QEBBgoztU6zmKp0mVIoWNcBHD0nKSQx13pHIu5YUKE8aSK-XLMJdkuk13ElrJjXTFVcQL9ydiI5s_2dwMpx9WmyvvTsfJ_PZ4KqI4iFiU6aAIaZ2lK7qY-KZvFUDQFQQLAO4shQ==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([google.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEhZfnrcef2wl9C0VttY7xuo_tcklZxlMmABJ20XDImfvN86gYYgLitMmOjJ-HK2VVXPGeoIXylEq5smbWAJX_Oden5Yo6AbHky84DPYlBGiRPjvgxw3Vqy9VCiOOZnTErzHSN3KpluJtvlrBDpCab)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([wavespeed.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FdFXuiuwrqZcCtM_vC63SEU6RK_X9pYjQ6Ifn1os1pbYErE_L70lecK-eFSUbjTffcB2jSgpbqzJcl77q5s_SFVdhc2XlY3W92uwICalsNOrRVEjqXBFUYWLFXcz8qljeFnPHdZUHmv7aWh6BzGyLMrEgD2wnw==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([blog.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh8h1vYOrJoM6EFlTXAuJuw8-72Pn9fzV4wqmtS9yZeoBtndpN-aUZ0gxIJWD_f0msyHQOHpyGRbx5CEL3c4kk0buGjhmHA1k_gapuukvCS-UHpbH_Cl8R25mCtVTvYSsgjO8L7xWhCDHPGsxdVQCGv7IBOsZER0PW78zxlaxuzOujxkXnvxcmeg==)). Relevance: Grounding source used during specialist audit.

**Contradictions / narrowing evidence:**
- The cracks are in pure reasoning and long context: Gemini 3.1 Pro still wins Humanity's Last Exam (44.4% vs 40.2%), ARC-AGI-2 (77.1% vs 72.1%), and the 128k slice of MRCR v2 by 7.6 points. ([Gemini 3.5 Flash: The Flash That Beat Last Year's Pro (Complete 2026 Guide) | NxCode](https://nxcode.com/gemini-3-5-flash)). Relevance: Directly refutes the framing of 3.5 Flash as unconditionally 'stronger' than 3.1 Pro, demonstrating performance regression in pure reasoning and long-context tasks [1.4.7].
- Where it is honestly mid-pack: SWE-Bench Pro (Public): 55.1% — behind Claude Opus 4.7 (64.3%). ([How to Use Gemini 3.5 Flash: Complete Guide to Google's Fastest AI Model (2026)](https://towardsai.net/gemini-3-5-flash-guide)). Relevance: Highlights that Gemini 3.5 Flash is not the overall market leader on standard agentic coding tasks such as SWE-Bench Pro.

**Missing context:**
- The Terminal-Bench 2.1 dataset is public, and its creators explicitly state that contamination prevention relies on a symbolic 'canary' GUID string, meaning the open repository makes it highly feasible for models to overfit or experience data leakage during pretraining [3.2.2].
- CharXiv Reasoning relies on diagrams and data harvested from public arXiv papers, which are widely represented in web-scale pretraining datasets, making complete decontamination of the test set structurally challenging.
- Google's official evaluation methodology discloses that the Terminal-Bench 2.1 scores for Gemini models were self-computed, whereas the competitor scores were pulled directly from the public leaderboard. Additionally, Google self-computed SWE-Bench Pro scores using its proprietary 'internal version of the Antigravity harness'.
- To achieve the peak performance reported (such as 1656 Elo on GDPval-AA and 76.2% on Terminal-Bench 2.1), the model must run with the 'high' thinking level configuration. However, Google's API migration documentation states that the default thinking level for the general-release model dropped from high to medium, meaning real-world users will get reduced performance out-of-the-box unless they explicitly modify the API parameters.

**Computed checks:**
- Terminal-Bench 2.1: 76.2% for Gemini 3.5 Flash vs 70.3% for Gemini 3.1 Pro [2.1.8]
- GDPval-AA: 1656 Elo for Gemini 3.5 Flash vs 1314 Elo for Gemini 3.1 Pro
- MCP Atlas: 83.6% for Gemini 3.5 Flash vs 78.2% for Gemini 3.1 Pro
- CharXiv Reasoning: 84.2% for Gemini 3.5 Flash
- ARC-AGI-2: 72.1% for Gemini 3.5 Flash vs 77.1% for Gemini 3.1 Pro (Regression of 5.0%)
- Humanity's Last Exam: 40.2% for Gemini 3.5 Flash vs 44.4% for Gemini 3.1 Pro (Regression of 4.2%)
- MRCR v2 (128k context): 77.3% for Gemini 3.5 Flash vs 84.9% for Gemini 3.1 Pro (Regression of 7.6%)
- SWE-Bench Pro: 55.1% for Gemini 3.5 Flash vs 64.3% for Claude Opus 4.7

</details>

<details><summary>numeric_calibrator: The provided document asserts that Gemini 3.5 (Flash) outperforms Gemini 3.1 Pro on key benchmarks (Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and CharXiv Reasoning). However, it does not provide the baseline scores of Gemini 3.1 Pro, nor does it detail the evaluation conditions (such as contamination or zero-shot setups) needed to verify reproducibility. Using external model card data, Gemini 3.1 Pro's baselines were found to be 70.3% on Terminal-Bench 2.1, 1314 Elo on GDPval-AA, 78.2% on MCP Atlas, and 83.3% on CharXiv Reasoning. Comparing these yields absolute improvements ranging from 0.9 to 5.9 percentage points (and 342 Elo points), representing relative improvements of 1.08% to 26.03%.</summary>

**Supporting evidence:**
- Terminal-Bench 2.1 (agentic terminal coding): Gemini 3.5 Flash 76.2%, Gemini 3.1 Pro 70.3%. MCP Atlas: Gemini 3.5 Flash 83.6%, Gemini 3.1 Pro 78.2%. GDPval-AA (Elo): Gemini 3.5 Flash 1656, Gemini 3.1 Pro 1314. CharXiv Reasoning: Gemini 3.5 Flash 84.2%, Gemini 3.1 Pro 83.3%. ([Gemini 3.5 Flash Is Impressive. Here's What We Actually Found. - Truefoundry](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFySPXYFu9Qh5lBCIjXwLQTwlfgP4ToOHK2pFdpXbQyYIBxsVLOkbFrcvodISb0dybXV6UwJCUYCfFjfpplR1N-pnXxgLrAPok7GT2cAbfW6WqmaUNoHZ5a2us85DB3kvrotcjAI1GsGGFxAtumf1Wbm3dwyOgjkM6K3MZgkNZxyMqlFtmGedfMK219CTh6Dv0Fzjdu2Qc=)). Relevance: Provides the exact baseline scores of Gemini 3.1 Pro across all four benchmarks to enable the calculation of performance deltas.
- Terminal-bench 2.1: Gemini 3.5 Flash 76.2%, Gemini 3.1 Pro 70.3%. MCP Atlas: Gemini 3.5 Flash 83.6%, Gemini 3.1 Pro 78.2%. GDPval-AA: Gemini 3.5 Flash 1656, Gemini 3.1 Pro 1314. CharXiv Reasoning: Gemini 3.5 Flash 84.2%, Gemini 3.1 Pro 83.3%. ([Gemini 3.5 - Google DeepMind](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNNtEQWF_6WSM10AEuuZGyRQLwUZnyt7u1IhhL43ao8KcnFYrD1WcBFMpd1QTdzcFwq55bYktR62vsuj7z7LsthC0iF6iy_PBDgt2vQgKiX9dQ-AD9-UV-ulNkuw==)). Relevance: Confirms official DeepMind benchmark evaluation results for both Gemini 3.5 Flash and Gemini 3.1 Pro.
- Source returned by Gemini grounding metadata. ([blog.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSR2Oms4w3hKkhYUk1mtwYYoWv5vHDu3poLQoyIagRBGkfGPokbSPzkWsAYYmoq2WCNz8_etVo78hbe0vWPuRDphQcwDcSXY1fSp3do-yFI1CyVGMoGIiFwq6zlfNvoWANzPCSLnsdYysyP18YEDWcHbiK45bTK4zXzQFZsLbmvZa1JBA-znN2Pw==)). Relevance: Grounding source used during specialist audit.

**Missing context:**
- Gemini 3.1 Pro baseline performance score on Terminal-Bench 2.1
- Gemini 3.1 Pro baseline performance score on GDPval-AA
- Gemini 3.1 Pro baseline performance score on MCP Atlas
- Gemini 3.1 Pro baseline performance score on CharXiv Reasoning
- Methodology or details regarding zero-shot or few-shot evaluation environments
- Analysis or assurance regarding training set contamination and reproducibility

**Computed checks:**
- Terminal-Bench 2.1: Gemini 3.5 Flash (76.2%) vs Gemini 3.1 Pro (70.3%) -> Absolute delta = 5.90 percentage points; Relative delta = 8.39% improvement
- GDPval-AA: Gemini 3.5 Flash (1656 Elo) vs Gemini 3.1 Pro (1314 Elo) -> Absolute delta = 342.00 Elo points; Relative delta = 26.03% improvement
- MCP Atlas: Gemini 3.5 Flash (83.6%) vs Gemini 3.1 Pro (78.2%) -> Absolute delta = 5.40 percentage points; Relative delta = 6.91% improvement
- CharXiv Reasoning: Gemini 3.5 Flash (84.2%) vs Gemini 3.1 Pro (83.3%) -> Absolute delta = 0.90 percentage points; Relative delta = 1.08% improvement

</details>

### Evidence Contrast

**Claim says:** It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning).

**Best reference says:** Demonstrates performance regressions of Gemini 3.5 Flash compared to Gemini 3.1 Pro on ARC-AGI-2, Humanity's Last Exam, and long-context tasks.

**Key qualification:** Points out that the older Pro model remains superior on pure reasoning and long context, contradicting the claim of 3.5 Flash being unconditionally the 'strongest' yet.

**Delta:** narrower_than_claim — The claim of being the 'strongest agentic and coding model yet' is a broad overgeneralization. Evidence shows that while Gemini 3.5 Flash outperforms the older Pro on specific agentic benchmarks (when utilizing non-default configurations like high thinking levels), it loses in other core cognitive dimensions like abstract reasoning and long context.

**Final verdict:** overstated

**Defensible rewrite:** Gemini 3.5 Flash outperforms Gemini 3.1 Pro on several key coding and agentic benchmarks when configured with its 'high' thinking level, achieving 76.2% on Terminal-Bench 2.1, 1656 Elo on GDPval-AA, and 83.6% on MCP Atlas, despite experiencing some regressions on pure reasoning and long-context tasks.

### Claim-Level Contrast References

- Gemini 3.5: frontier intelligence with action (blog, authority 90/100): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/. The original source containing the claim.

**Reference snippets / mismatches:**
- Demonstrates performance regressions of Gemini 3.5 Flash compared to Gemini 3.1 Pro on ARC-AGI-2, Humanity's Last Exam, and long-context tasks. (Gemini 3.5 Flash: The Flash That Beat Last Year's Pro (Complete 2026 Guide) | NxCode, contradicts, https://nxcode.com/gemini-3-5-flash). Points out that the older Pro model remains superior on pure reasoning and long context, contradicting the claim of 3.5 Flash being unconditionally the 'strongest' yet.

**Computed checks:**
- Terminal-Bench 2.1: Gemini 3.5 Flash (76.2%) vs Gemini 3.1 Pro (70.3%)
- GDPval-AA: Gemini 3.5 Flash (1656 Elo) vs Gemini 3.1 Pro (1314 Elo)
- MCP Atlas: Gemini 3.5 Flash (83.6%) vs Gemini 3.1 Pro (78.2%)
- CharXiv Reasoning: Gemini 3.5 Flash (84.2%) vs Gemini 3.1 Pro (83.3%)
- ARC-AGI-2 Regression: Gemini 3.5 Flash (72.1%) vs Gemini 3.1 Pro (77.1%)
- Humanity's Last Exam Regression: Gemini 3.5 Flash (40.2%) vs Gemini 3.1 Pro (44.4%)

**Supporting evidence found:**
- Gemini 3.5 Flash scores 55 on the Artificial Analysis Intelligence Index, up 9 points from Gemini 3 Flash... Its GDPval-AA result is especially notable, achieving an Elo of 1656, well ahead of Gemini 3 Flash (1204) and Gemini 3.1 Pro (1314). ([Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis](https://artificialanalysis.ai/evaluations/gdpval-aa)). Relevance: Independently verifies the GDPval-AA Elo score of 1656 and that it outperforms Gemini 3.1 Pro on this benchmark.
- MCP Atlas results are reported from the ScaleAI official leaderboard... GDPval-AA results are sourced from the Artificial Analysis public leaderboard... (Model Evaluation – Approach, Methodology & Results Gemini 3.5 Flash). Relevance: Confirms that major benchmarks like GDPval-AA and MCP Atlas were derived from external leaderboards.

**Contradictions / narrowing evidence:**
- The cracks are in pure reasoning and long context: Gemini 3.1 Pro still wins Humanity's Last Exam (44.4% vs 40.2%), ARC-AGI-2 (77.1% vs 72.1%), and the 128k slice of MRCR v2 by 7.6 points. ([Gemini 3.5 Flash: The Flash That Beat Last Year's Pro (Complete 2026 Guide) | NxCode](https://nxcode.com/gemini-3-5-flash)). Relevance: Directly contradicts the framing of Gemini 3.5 Flash as unconditionally stronger than Gemini 3.1 Pro by showing clear regressions on pure reasoning and long context.

**Missing context:**
- To achieve the peak performance reported (such as 1656 Elo on GDPval-AA and 76.2% on Terminal-Bench 2.1), the model must run with the 'high' thinking level configuration, which has been lowered to 'medium' by default in the general-release API.
- Terminal-Bench 2.1 and CharXiv Reasoning scores were self-computed by Google internally and have not been independently validated by external hosts, leaving them vulnerable to pretraining data contamination.


## claim_2: overstated

**Confidence:** high

**Original:** When looking at output tokens per second, it is 4 times faster than other frontier models.

**Stretch Score:** 60/100

**Why:** The claim is overstated because Gemini 3.5 Flash's 4x output speed advantage only applies when comparing it against heavy, reasoning-focused flagship models like GPT-5.5 (xhigh) running at ~65 tokens/sec (4.28x) or Claude Opus 4.7 (max) running at ~50 tokens/sec (5.56x). When compared against standard, highly-used frontier-class models like GPT-4o (~110-154.5 tokens/sec) or Gemini 3.1 Pro Preview (~123 tokens/sec), the speed advantage drops to 1.8x-2.5x and 2.26x respectively. For closer peers like gpt-oss-120b (~246 tokens/sec), the advantage is only 1.13x. Additionally, the model exhibits extreme verbosity, generating double the tokens of competitor models to complete identical tasks, which significantly dilutes its end-to-end task completion speed benefits in practical workflows.

**Defensible rewrite:** When looking at output tokens per second, Gemini 3.5 Flash is up to 4 times faster than select heavyweight reasoning models, though its speed advantage over standard frontier models like GPT-4o narrows to between 1.8x and 2.5x.

### Agent Steps

<details><summary>Grounded Verifier: While Google officially claims that Gemini 3.5 Flash is 4 times faster than other frontier models in output tokens per second, the official documentation does not disclose any standardized hardware setups, concurrency levels, or input/output payload shapes used for this measurement. Third-party tests from Artificial Analysis and independent reviews confirm that Gemini 3.5 Flash achieves output speeds of approximately 278 to 289 tokens per second (and up to 455 tokens per second under certain tasks), which is roughly 4x to 5.5x faster than other frontier models like GPT-5.5 (running at ~65 tokens per second) and Claude Opus 4.7 (running at ~50 tokens per second). However, the specific hardware and query configurations to consistently achieve this 4x advantage remain unspecified in Google's official material.</summary>

**Supporting evidence:**
- When looking at output tokens per second, it is 4 times faster than other frontier models. Landing in the top-right quadrant of the Artificial Analysis index, 3.5 Flash delivers frontier-level intelligence at exceptional speed — proving you no longer have to trade quality for latency. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Directly contains the official claim that the model is 4 times faster than other frontier models on output tokens per second [1.1.1].
- The only axis where 3.5 Flash leads is speed: 278 tokens per second versus 3.1 Pro's 123... GPT-5.5 (xhigh) ... speed: 65... Claude Opus 4.7 (max) ... speed: 50. ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuyL1VSiJiCiRWfhKQ6Ox4Z5PKC9sLB6rvUv4v_e_jFxqf2LAm47c4DfRiVG-jgJvjKMjglEoqr4tJ8TE_fHFDNS_qiXivmHmDf5mHHteFH-O_4EbHLE_wHlzOicn0doC25SOJlFuXgSUeJQEQEA==)). Relevance: Provides independent benchmarking showing Gemini 3.5 Flash reaching 278 tokens per second, which is roughly 4.3x faster than GPT-5.5 (65 tokens/sec) and 5.5x faster than Claude Opus 4.7 (50 tokens/sec).
- the model does something that “Flash” models have never done before — it runs at roughly 280 to 455 output tokens per second, which Sundar Pichai claimed in the keynote is “nearly four times the speed of competing frontier systems.” ([I Tested Gemini 3.5 Flash on 18 Agent Tasks — Google's 6× Pricier “Flash” Just Crushed GPT-5.5 at 4× Output Speed - Towards AI](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhkNNJzk9amoG0aXwagBYVPgsP501S9s3IdZaN7A_WeUmR1MRQOzA5-Uf7b9_ASogm_VCVfWe_5N80klbVaac90BFNfJEquATaW8Qyx6-qeh3JqMJ08yMsz-v0Eax9zWn5pGkXwdnycor8jqmiMmqzAXDStn3BwtR6vgVVdsreiftBHpzIIGym_-9DT4helGF1qU4VChYBee_lUUnbgHWLCxUztjjbFM_T70PrZcHlxvHxw3ly5YLo)). Relevance: Provides third-party verification of the 4x speed advantage claim and notes measured speed ranges in real-world agent tasks.
- Source returned by Gemini grounding metadata. ([blog.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXTKzsKde1Ga7sADOlE1vyb4veJN8g3b2dcq6tlQ1o7VPTEATgkKrpjHiGUY698KIw5MB3X6h6ZH3APYTjwtB0abcURATcgHfqAXczg_evboE51JKY_k6Mj6gnOtuhSpjSEnmqeTR-yW35nBAWVC6SiZ3DBwNVeOJNYorRkGfiYokjatrgwySX)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([appwrite.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNaGAY6bS_fXOs4OPC5-9v8AXSBUmjwvOZuBtEGDNgDz6TUlDqvAnznz4uH22ZwE9h-yWFovMv7U7QqgaiAoUgaChO9RZba2xN1TiybFRi_2osWm6yhXaFYKqT5k4q6TX76BbTE4SQf6ZBWc6k)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([datacamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoY_jr2jJi1jwsU9Qebwbbi91ySNQkdB7rOxKrDJ1OTkU5ou_N89GcP-Um29e8D65x9tbN6SHnIkydQFS2xNL2KR-sOV6ACLUd2LNpMmJhrsIfYibBnRnn5-rMcYYjAnh9eUI=)). Relevance: Grounding source used during specialist audit.

**Missing context:**
- Google's official release notes, system cards, and research blog do not specify the hardware configuration, concurrency levels, or input/output payload shapes used to achieve the claimed 4x output speed advantage [1.1.6].
- The specific comparable frontier models referenced in Google's internal '4x' baseline comparison are not explicitly named in the official announcement notes.

**Computed checks:**
- Approximately 4x (to 5.5x) speed advantage over competing frontier systems like GPT-5.5 (which runs at ~65 tokens per second) and Claude Opus 4.7 (which runs at ~50 tokens per second).

</details>

<details><summary>Skeptical Contradiction Finder: Google's claim that Gemini 3.5 Flash is '4 times faster than other frontier models' is technically supported when compared to heavy, reasoning-focused flagship models (like GPT-5.5 xhigh and Claude Opus 4.7 max). However, this comparison is highly asymmetric, pitting a lightweight Flash-tier model against massive reasoning models. Furthermore, Gemini 3.5 Flash exhibits extreme verbosity, generating more than double the tokens of other models on identical benchmarks, which dilutes its real-world latency advantages and inflates its total operation cost by 5.5x compared to Gemini 3 Flash and 75% compared to Gemini 3.1 Pro.</summary>

**Supporting evidence:**
- Speed: 278 output tokens per second (rank #2 of 147 in its AA price class). The closest frontier peer is gpt-oss-120b (high) at 246. Other frontier-class models are well behind: Gemini 3.1 Pro Preview at 123, GPT-5.5 (xhigh) at 65, Claude Opus 4.7 (max) at 50. ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMDIpHqYfGQ6LN4f5JeUrzdy7QQ6g6t2GdZHNBRNJRJ7tuIS04J_cieJwdMe65UgmavXdbhKceDuBUWBorgNep0Hd3tDokUwGbI3xK-kXn-nKgpVaqZd8hHCvAYf2UIVQ-V27ECtd12ukqv9IUzQ==)). Relevance: Confirms that Gemini 3.5 Flash's speed of 278 tokens/sec is roughly 4 to 5 times faster than heavyweight frontier-class reasoning models like GPT-5.5 (65 tokens/sec) or Claude Opus 4.7 (50 tokens/sec).
- Source returned by Gemini grounding metadata. ([artificialanalysis.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELmKrnj0Z-BnwYq-UwCmWHBgapdqgMbtCC0Bu36wTMLbb3FATx763uFZz-PSRTnwpKmuvXYKXAtXx5IIkARfLmJiyx-NkJx_zgoBgQ_wYPQFRU93Dmv2VXbgt_W84ZenIp8UjNdmC2R6zFdWeXhKx0IxqVY2RmeRiEHU-qi7rTl9wtEGBXeQ-lkA==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([appwrite.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4Tn076msZuT7fJHO_2yEjieprdKpuFEEPFoaH2XPLNBVtmEbz9RmZBF-yAaRR1JLX3Xi0GaAW_SwmkW-Fg1whNujpiAfVZyTQd7_R-9Ae9HJW8yHeWQRgKEcPg1BWjzTnEZI-95U2a87sazo7Yg==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([belitsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh_ztVWJPGiVu4d_GmyD6N-kzwkwUBldk6t-NW71HU77DvTxROTqsY1rOAnnv0kUbNLGnq0GCEpDLfDJphuuIfvfipP56VF3M1VGjgE2_CTsSYZs8aV-oB81yTcBXVdYl_I3p97WCfCkfhZPw=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([tosea.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPXBaimg1JBT6dbqiLPb188V4ER3hkE-hP45DZgi2RPTnRaDlFoEDkd6PCAZ4LPDWskIXW7BcDWJ5QSqerVyMMhw9UAAxVXBLKC8LuuYYMihslNyTjh96qmJbbI4T8AfY-WuCwVVBXsOMR-h3Nscsa)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([artificialanalysis.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnLTQCWB90RBcnWmf1TJjZ9tYbMnzwCCcrEhsRGKn_s0PpmUnwDGhZiBWdC5j-K5OY0BlyiKwqBWLXskjXSl8WH3jYYEZZ90h9zTOrzR6OC4mp5ZHP59GZDjGETF2v7Of4-WESRpIkGcjFhGoHLLaxnsNCdMnwKw==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([artificialanalysis.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9kc87citZthggApBLUiBwuVmZscG_mn9lRpv32ekG-rsvlUNap-nJEyTNozDdkXWIbvT0rOCwLvGmL4EXa0pG4m_FrsahH1knyhPP0dwW13VRN37QjGQuxfBv1GtwiRTeywo4Sr2eiA==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([baseten.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLh0C9fKZ6ki4tDVPKjF1Cp5X4A9GLLwmkFmMAPfDbShq-evJVgyIMgiHkxm3xxU9uLFYus-KPOlZnPgRMpHCdZp7mK6LvoasydBTJ9spjMLzCuM_X6Ad9PBCLH8UiFwx-qNRcTQGaON9-fel-ecTJjwMt-Qz4tSc=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([epoch.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF1maFt_TCGLG8_GN9IZ5J9GAaySymDcCS7u107YYmndqmJQgQ3MCya2BRrJmbX8qSer77cvMvzAmMdPuqr2bpPSCA_i6h8JW1mp5kaUMzDWZIQ2JNnw7luRLYb5OS6-IODlV_iI2TrQHi5IJ9l2y8IXJhgQ0Ehw1xhJORREaOQrRsImdC1vSrQQ==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([artificialanalysis.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ISDoRg6jzSxeLQkxdbEbwDNsbQQpXgkTi05JpWr-PbhlYuS6mE3g7SeU6T_NBUXdQ9a0Uz1zFnfGA0TmfcnhaaZtiL-9ka05dFvMAORgz-k1O7zEZYVma0vycBUwE5I=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLMUr5md55QFs2G8JuUk0AqhvO-7qQOkE89QAlw9hJW9Ayrp7rLx2VRHJfrUkwofGDf6mCb-XdsRRhPyZhhgeRhE9YjtbIBjG_6l9YKiLPOT_wLC6I-krxM339Og==)). Relevance: Grounding source used during specialist audit.

**Contradictions / narrowing evidence:**
- GPT-4o (Nov '24) generates output at 154.5 tokens per second (based on OpenAI's API) ([GPT-4o (Nov '24) Intelligence, Performance & Price Analysis](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ISDoRg6jzSxeLQkxdbEbwDNsbQQpXgkTi05JpWr-PbhlYuS6mE3g7SeU6T_NBUXdQ9a0Uz1zFnfGA0TmfcnhaaZtiL-9ka05dFvMAORgz-k1O7zEZYVma0vycBUwE5I=)). Relevance: Demonstrates that compared to GPT-4o (which is often considered a standard frontier-class model), Gemini 3.5 Flash's output speed advantage is closer to 1.8x to 2.5x, rather than the claimed 4x.

**Missing context:**
- Verbosity Inflation: On the Artificial Analysis Intelligence Index, Gemini 3.5 Flash generated 73 million tokens compared to a leaderboard average of 35-36 million tokens. This double-verbosity means that the end-to-end task completion latency is not 4x faster because the model must output twice as many tokens to complete the same task.
- Operational Cost Increase: Despite having lower nominal per-token rates than Pro models, the high token usage (verbosity) makes Gemini 3.5 Flash cost $1,552 to evaluate on the Intelligence Index—a 5.5x increase over Gemini 3 Flash and 75% more expensive than Gemini 3.1 Pro ($892).
- Serverless Benchmarking vs. Sustained Concurrency: The 278-289 tokens/sec speed is measured under single-prompt or low concurrency (10 parallel prompts) serverless API load scenarios. It does not reflect peak user throughput under sustained high-concurrency enterprise workloads (like those measured in AA-AgentPerf benchmarks).
- Opaque Infrastructure: As a closed-source API model, developers have no control over the underlying TPU/GPU hardware clusters, scheduling optimizations, or speculative draft models. The 4x speed advantages are entirely dependent on first-party hosting conditions and cannot be consistently tuned or reproduced locally.

**Computed checks:**
- GPT-5.5 (xhigh) runs at 65 to 71 output tokens per second, and Claude Opus 4.7 (max) runs at 50 to 67 output tokens per second.
- GPT-4o operates at 110 to 154.5 output tokens per second, narrowing Gemini 3.5 Flash's multiplier to 1.8x-2.5x.
- Gemini 3.5 Flash generated 73 million tokens on the Intelligence Index benchmark, compared to a leaderboard average of 35-36 million tokens.
- Evaluating Gemini 3.5 Flash on the Intelligence Index cost $1,552, compared to $892 for Gemini 3.1 Pro and a 5.5x increase over Gemini 3 Flash.

</details>

<details><summary>numeric_claim_calibrator: The claim asserts that Gemini 3.5 Flash is 4 times faster in output tokens per second compared to other frontier models. Independent benchmarking from Artificial Analysis confirms that Gemini 3.5 Flash achieves speeds of approximately 278 output tokens per second, representing a 4.28x improvement over GPT-5.5 (xhigh) and a 5.56x improvement over Claude Opus 4.7 (max). However, compared to other peer models like gpt-oss-120b (246 tokens/sec) or Gemini 3.1 Pro Preview (123 tokens/sec), the speedup falls below 4x (at 1.13x and 2.26x respectively). The source document does not provide details on specific comparable models, hardware setups, concurrency levels, or payload sizes.</summary>

**Supporting evidence:**
- When looking at output tokens per second, it is 4 times faster than other frontier models. Landing in the top-right quadrant of the Artificial Analysis index, 3.5 Flash delivers frontier-level intelligence at exceptional speed — proving you no longer have to trade quality for latency. ([Gemini 3.5: frontier intelligence with action - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Contains the original claim stating that the model is 4 times faster than other frontier models based on the Artificial Analysis index.
- Gemini 3.5 Flash on Artificial Analysis... Speed: 278 output tokens per second (rank #2 of 147 in its AA price class). The closest frontier peer is gpt-oss-120b (high) at 246. Other frontier-class models are well behind: Gemini 3.1 Pro Preview at 123, GPT-5.5 (xhigh) at 65, Claude Opus 4.7 (max) at 50. ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Provides the exact benchmark metrics showing output tokens per second for Gemini 3.5 Flash and other frontier models.
- Source returned by Gemini grounding metadata. ([blog.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX1_py77taqpyca-B3EPzEyxIX9DBqH5M71KytjCaMnfIN5J0cxCnYztK2UGfDqFerkZZhGBaxcHMKrxAMe7pTzo4tsVoyBFCVTR9E_YcnqHIXnHIIozzGrzyneTselOomUOk1gpLi50bKBlxqij4h8QJzZMFPx-Q_cF8U3chYx-ajmlmel94EOA==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([appwrite.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI7aNSpDB0iUsQXf06jX-lElGzGh_kWvEATrD6BmiBxsqOqc-BWI6gzDM99CqIDULTmvgkMlUDTj1bTuC9SybiDJR346C3P6-6MSi0xFsYwjrM2kYoHPaf5mqGUx_wKkcnG7DXxM_cHYodomMZ)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([datacamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFimAjcoN_YEanecxh0P4cHRtgrJcZJPjJPv1Hx9uqVJQsXztmHXzbGXbpbtsax3fnyblot8AsBeAkl6RGCtB1QlflZzOAr7Fmh6RBWTSVlru63KGh2lENhfBK85VsjZtwWROA=)). Relevance: Grounding source used during specialist audit.

**Contradictions / narrowing evidence:**
- The closest frontier peer is gpt-oss-120b (high) at 246. Other frontier-class models are well behind: Gemini 3.1 Pro Preview at 123... ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Demonstrates that when compared against closer peer models such as gpt-oss-120b or Gemini 3.1 Pro Preview, the speedup is significantly less than 4x.

**Missing context:**
- Specific comparison models, such as GPT-4o or Claude 3.5 Sonnet, are not named or profiled in the blog post's speed claim.
- Standardized hardware setups, host platforms, and region constraints for the speed evaluations are omitted from the source text.
- Concurrency levels, such as the number of parallel requests or batch sizes, are not provided.
- Input and output payload shapes (e.g., prompt size vs. response generation length) used during testing are missing from the documentation.

**Computed checks:**
- Relative speed improvement over GPT-5.5 (xhigh): 278 output tokens per second / 65 output tokens per second = 4.28x (exceeds 4x claim)
- Relative speed improvement over Claude Opus 4.7 (max): 278 output tokens per second / 50 output tokens per second = 5.56x (exceeds 4x claim)
- Relative speed improvement over Gemini 3.1 Pro Preview: 278 output tokens per second / 123 output tokens per second = 2.26x (falls below 4x claim)
- Relative speed improvement over gpt-oss-120b (high): 278 output tokens per second / 246 output tokens per second = 1.13x (falls below 4x claim)

</details>

### Evidence Contrast

**Claim says:** When looking at output tokens per second, it is 4 times faster than other frontier models.

**Best reference says:** The model card lists scores across multiple benchmarks (such as coding, agentic workflows, multimodal reasoning, and academic exams) but contains no data, comparisons, or mention of token throughput, speed, latency, or output tokens per second.

**Key qualification:** The reference completely lacks performance data regarding output speed or token generation metrics.

**Delta:** not_checkable — The claim states that Gemini 3.5 Flash is 4 times faster than other frontier models when looking at output tokens per second. However, the provided reference URL—the Gemini 3.5 Flash Model Card—focuses strictly on accuracy/capability benchmarks and safety assessments, containing absolutely no metrics or claims regarding latency, throughput, or speed. Thus, the claim is not checkable against the provided reference.

**Final verdict:** not_checkable

**Defensible rewrite:** While Google's promotional materials assert that Gemini 3.5 Flash is 4 times faster than other frontier models in output tokens per second, the official model card does not publish speed or latency benchmarks to verify this claim.

### Claim-Level Contrast References

- Gemini 3.5 Flash - Model Card - Google DeepMind (official_doc, authority 95/100): https://deepmind.google/models/model-cards/gemini-3-5-flash. This is the official model card containing the comprehensive benchmark evaluations, safety reports, and model specifications for Gemini 3.5 Flash.

**Reference snippets / mismatches:**
- The model card lists scores across multiple benchmarks (such as coding, agentic workflows, multimodal reasoning, and academic exams) but contains no data, comparisons, or mention of token throughput, speed, latency, or output tokens per second. (Gemini 3.5 Flash - Model Card - Google DeepMind, unclear, https://deepmind.google/models/model-cards/gemini-3-5-flash). The reference completely lacks performance data regarding output speed or token generation metrics.

**Computed checks:**
- Relative speed improvement over GPT-5.5 (xhigh): 4.28x
- Relative speed improvement over Claude Opus 4.7 (max): 5.56x
- Relative speed improvement over Gemini 3.1 Pro Preview: 2.26x
- Relative speed improvement over gpt-oss-120b (high): 1.13x
- Relative speed improvement over GPT-4o: 1.8x to 2.5x
- Verbosity comparison: Gemini 3.5 Flash generated 73 million tokens on the Intelligence Index vs leaderboard average of 35-36 million.

**Supporting evidence found:**
- Speed: 278 output tokens per second (rank #2 of 147 in its AA price class). The closest frontier peer is gpt-oss-120b (high) at 246. Other frontier-class models are well behind: Gemini 3.1 Pro Preview at 123, GPT-5.5 (xhigh) at 65, Claude Opus 4.7 (max) at 50. ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Confirms Gemini 3.5 Flash's ~4.3x speed advantage over GPT-5.5 (xhigh) and ~5.5x over Claude Opus 4.7 (max).

**Contradictions / narrowing evidence:**
- GPT-4o (Nov '24) generates output at 154.5 tokens per second (based on OpenAI's API) ([GPT-4o (Nov '24) Intelligence, Performance & Price Analysis](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ISDoRg6jzSxeLQkxdbEbwDNsbQQpXgkTi05JpWr-PbhlYuS6mE3g7SeU6T_NBUXdQ9a0Uz1zFnfGA0TmfcnhaaZtiL-9ka05dFvMAORgz-k1O7zEZYVma0vycBUwE5I=)). Relevance: Demonstrates that compared to standard frontier-class models, Gemini 3.5 Flash's speed multiplier is closer to 1.8x to 2.5x rather than 4x.
- The closest frontier peer is gpt-oss-120b (high) at 246. Other frontier-class models are well behind: Gemini 3.1 Pro Preview at 123... ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://artificialanalysis.ai/models/gemini-3-5-flash)). Relevance: Demonstrates that when compared against closer peer models such as gpt-oss-120b or Gemini 3.1 Pro Preview, the speedup is significantly less than 4x (1.13x and 2.26x respectively).

**Missing context:**
- The comparison pits a lightweight Flash-tier model against heavy reasoning models (asymmetric comparison).
- Gemini 3.5 Flash generates double the tokens of other models on identical tasks (high verbosity), reducing actual latency advantages.
- No hardware configurations, concurrency levels, or input/output payload shapes are provided in official materials.


## claim_3: overstated

**Confidence:** high

**Original:** What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models.

**Stretch Score:** 80/100

**Why:** The reference source (the model card) is narrower than the claim because it only quantifies task accuracy on standard static benchmarks and lists intended applications. It contains no financial cost comparisons or concrete data to verify the claim of completing developer/auditor tasks in a fraction of the time or at less than half the cost. In fact, it lists 'multi-week enterprise processes' as an intended use case, which contradicts the absolute notion of shrinking all such workflows into a small fraction of the time.

**Defensible rewrite:** Gemini 3.5 Flash is designed to handle agentic coding, audit, and multi-week enterprise workflows, achieving near-Pro level performance on specialized technical benchmarks.

### Agent Steps

<details><summary>grounded_verifier: There are no empirical, controlled user studies publicly available or cited by Google that systematically quantify a reduction in developer or auditor workflows from days/weeks to a fraction of the time. The claim relies on qualitative pilot testimonials and early corporate partner integrations (such as Macquarie Bank piloting 100+ page document reasoning, and Xero deploying agents to manage multi-week tax workflows). However, the pricing aspect of the claim is strongly supported by official developer pricing schemas: Gemini 3.5 Flash API costs $1.50 per million input tokens and $9.00 per million output tokens, which is less than half the per-token cost of comparable competing frontier models like GPT-5.5 ($5.00/$30.00) or Claude Opus 4.7 ($6.25/$25.00).</summary>

**Supporting evidence:**
- Gemini 3.5 Flash. gemini-3.5-flash. ... Standard Batch Flex Priority More. Free Tier, Paid Tier, per 1M tokens in USD. Input price, Free of charge ... Paid Tier: $1.50 per 1M input tokens, $9.00 per 1M output tokens. ([Gemini Developer API pricing](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJqTvVa9FHZeaoNTa7Q36CdoO1Hx6PhvoOgHG9o1WUfnd2CFKu1NvFL-zZ7nnEJ0Eq7knQ01krJd5fW55LkPEa1XmwU_3UVcTgAxTK86TDsFTjV-wUijikG77UBuTZhM9dqzY=)). Relevance: Establishes the exact API pricing framework for Gemini 3.5 Flash showing it runs at $1.50/1M input and $9.00/1M output tokens.
- GPT-5.5 (xhigh) ... Input $/Mtok: $5.00, Output $/Mtok: $30.00. Claude Opus 4.7 (max) ... Input $/Mtok: $6.25, Output $/Mtok: $25.00. Gemini 3.5 Flash (high) ... Input $/Mtok: $1.50, Output $/Mtok: $9.00. ([Gemini 3.5 Flash: a detailed benchmark and capability review - Appwrite](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVuBd9XzyA24M5uz-8V-MHT_cQxNZ-6YOp6XnkHKwjes2raOTKgVSdy-BXG4YBcqgGLIwB2SEldCpbHXhYMqUJKaZCq7yVGSpR_fgPLkx8_57cEH184IiCyyoVMewH5ib9NnKgYVZ6s2e1hL35HQ==)). Relevance: Provides direct pricing comparison against competing frontier models, confirming that Gemini 3.5 Flash's per-token cost is less than half of GPT-5.5 and Claude Opus 4.7.

**Contradictions / narrowing evidence:**
- It costs roughly 75% more to run a task on 3.5 Flash than it does on 3.1 Pro... Forced 'Thinking' Tokens: Gemini 3.5 Flash generates internal 'thinking' tokens to reason through problems... you are footed the bill for all of that invisible output text at $9.00 per 1M tokens. ... The model tends to simulate multiple turns of internal tool-calling and validation. ([Gemini 3.5 Flash is actively penalizing developers who write good, efficient prompts](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQ0EOoBU_tOy1WTJ_WtxATDRIBIJKcbMrq7C9mt_aNyH8z1SJtz_Opsrjf5WTIjMIpL1PK1_kbB1Li995uAZS0QE_mY-_WqcotY6TnE9oDFazRy0wTDNuFTdpomaVgdi_91ghcAxRxMpiYkyshES5QbWn56q3qLD5DVun5oJfQ5zML9KjP7DntD_Ir8tzAvpLJ_FLN7CQZM-3o8InZG5VzetrlSSgi98H60WCn7fwAwyw==)). Relevance: Shows that despite lower per-token pricing, the actual cost of executing complex agentic tasks on 3.5 Flash can be higher than expected due to verbose, multi-turn reasoning loops and 'thinking' tokens.

**Missing context:**
- No structured, empirical user studies comparing workflows before and after using Gemini 3.5 Flash have been published. The claim that it reduces weeks/days of work to a fraction of the time is based on high-level corporate partner testimonials rather than peer-reviewed or controlled research.

**Computed checks:**
- Gemini 3.5 Flash API pricing: $1.50 per 1 million input tokens, $9.00 per 1 million output tokens.
- GPT-5.5 (xhigh) API pricing: $5.00 per 1 million input tokens, $30.00 per 1 million output tokens (meaning Gemini 3.5 Flash is 70% cheaper on input and 70% cheaper on output).
- Claude Opus 4.7 (max) API pricing: $6.25 per 1 million input tokens, $25.00 per 1 million output tokens (meaning Gemini 3.5 Flash is 76% cheaper on input and 64% cheaper on output).

</details>

<details><summary>Skeptical Contradiction Finder: While Gemini 3.5 Flash pricing ($1.50 input / $9.00 output per 1M tokens) is less than half the cost of premium frontier models like GPT-5.5 ($5/$30) and Claude Opus 4.7 ($5/$25), it is not 'less than half the cost' of mid-tier models like GPT-5.4 ($2.50/$15) or Claude Sonnet 4.6 ($3/$15). Additionally, it represents a substantial 3x price increase over Gemini 3 Flash Preview ($0.50/$3.00), and is dramatically outpriced by cost-performance leaders like DeepSeek-V4-Pro ($0.43/$0.87). There are no published, controlled empirical user studies to support the claims of workflow reduction from days/weeks to a fraction of the time; Google relies solely on selective partner pilot descriptions. Finally, benchmarks show that 3.5 Flash actually regresses compared to Gemini 3.1 Pro on deep reasoning and long-context retrieval.</summary>

**Supporting evidence:**
- Input Price. $5per 1M. Output Price. $30per 1M. ([GPT-5.5 - API Pricing & Benchmarks - OpenRouter](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ58QUeEgoalRCJ5m9XPZ3Lvu9bkvpEZ7kVR4o1CfIo2zd1oliGYLSGrTGVMCA3azGnNtm342L7eqy08aMbNNc2BxAKvmZvhhpJasPwzYLEQmR5tghAQr5PCs=)). Relevance: Verifies that GPT-5.5 API pricing is $5/$30 per million tokens, meaning Gemini 3.5 Flash ($1.50/$9) is indeed less than half of this specific premium model's cost.
- Claude Opus 4.7, $5.00, $25.00 ([Claude API Pricing 2026: Latest Anthropic Costs for Opus, Sonnet, Haiku - EvoLink.AI](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMGOSgEiZn72DEvDDlYQvSmb3lDTE5ni5Dp0baWVyFtYIelK_jOVdJCOFCRvmwve20BU-lmIw_0Zv04z96D1T-pZUbIv_e-1BfffmHOt4bpep2tcBhzI-Yz2Uri7rFoF0I-i93y60voQz4g==)). Relevance: Confirms Claude Opus 4.7 pricing is $5/$25 per million tokens, against which Gemini 3.5 Flash is less than half the cost.
- Source returned by Gemini grounding metadata. ([youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoqMsDTxskp6RjmexawAQNELZfDOB2b2O_1wMRQQgNS30vqOWPKtqmGehM8_boVqG5aRjQ28gg1HiDhrCEvImJknsuvk_c361JVb9Bp_Sr3IDntw4ByV5Rua6wxFg4Y2w=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([cloudzero.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeq64NwnCfBB5DYFCAn2ZY_K_k3dESpA1myI5LRXkrch2VYG6R_EzsytvhRmYm9ROKXT1ApEvU8M1XkU773lzi7MCNZzfYVukiUoKBREFrYh60aWwaIRAJ5XsKadE9kAkz2SGWcqCtF4qeOzAg)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([milvus.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPK1l4bBe3aeZVcTF4qKT1h_HEMcJ3x5fpTzx0h6UVj6L-MJhtfdDIhqbB724mUCdkS4_DiPGtSQykJeSm_Gh3Cll_0XoloNZWwHEUL7_mWpaTNvK-xk3P_Pswr0jd0bGeXR-uzKIYUER86t0hNhFBd9d8td58-NDTTe6bboMSZYv4fgxWWU=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([claude.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwFo9x8VjMlET1xEJKcs6nvAXummUgxRjFdeBNyK5geX0BnFqjaeGvml1Q_Rt1GD0DHqtnr8O-1mklyhWONrTro6XiJWiFKTJMujaoVAdgipM6yCQC6IENcy0b-PHS8j0j8ZSxb5IOgcy7WU9BZA==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([evolink.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIr0TUrnQaJA7QgSwAslX6RRbVpueUaTs55K4tzFGfDMTmb2Ihi0zmwlpAwz0lmmdSmjSupSxXBco2uvyKCKhI_SKFKfVH1aT_IT64pkd13JwEnPhsjWhrpx3mT-gOauPu2rLERL5tzrLpQQguAubTz9KTrmRpPOw=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([howaiworks.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW1P1PoQV0SeaRx8SoXqiru3_rDnSjiRHBdg1LgsBz2dld0CzVt2aDDfN_nCh9wdRZtcFzVU6tclHZk4p77KZU_qaZeJEwdjW2M3uRHrjywLIS05iJ-_kYLEY-Ng3ETEO4cll72_zEWGVueU6VtK6G)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([labellerr.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFiS6P-cqmg1c7CExw844KtIRKHShOLcBixL4BzlpayvG0XiBtdW1s788d-k9cWYi_N0eUBvIdDEoaz5B2Si7rIAOnRSStH6pgzGjRF_re5gHBr0v-0_acvflDJCgQEAB1DH-42ZEC6o3oCaAs)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([nxcode.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbXL2b3Yrdn_Al8wAYtUK8Iew8Pp48dcTsW7gjbLFqcIlw_PLo7NBifIa1x2QIGc-OD8cE82AoS96Cm9c8xvy7fEsDDU5ZCT9-Wg4972MB0VzK4iK4soeEBJLxiq5KoUmFsJ-2l9h2TK_FDjUY_PvXWQWeiTdbh7CwwN2wxFNZlhM7g8_bQXwbzcCMbuAFi_ZBKDNK_nnD74U=)). Relevance: Grounding source used during specialist audit.

**Contradictions / narrowing evidence:**
- For the standard GPT-5.4 model, the API pricing is $2.50 per 1 million input tokens and $15.00 per 1 million output tokens ([What are the basic pricing models for GPT 5.4? - Milvus](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPK1l4bBe3aeZVcTF4qKT1h_HEMcJ3x5fpTzx0h6UVj6L-MJhtfdDIhqbB724mUCdkS4_DiPGtSQykJeSm_Gh3Cll_0XoloNZWwHEUL7_mWpaTNvK-xk3P_Pswr0jd0bGeXR-uzKIYUER86t0hNhFBd9d8td58-NDTTe6bboMSZYv4fgxWWU=)). Relevance: Contradicts the claim that Gemini 3.5 Flash is 'often at less than half the cost of other frontier models' when compared to GPT-5.4 ($2.50/$15), since Gemini ($1.50/$9) is 60% of GPT-5.4's cost.
- Claude Sonnet 4.6, $3.00, $15.00 ([Claude API Pricing 2026: Latest Anthropic Costs for Opus, Sonnet, Haiku - EvoLink.AI](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMGOSgEiZn72DEvDDlYQvSmb3lDTE5ni5Dp0baWVyFtYIelK_jOVdJCOFCRvmwve20BU-lmIw_0Zv04z96D1T-pZUbIv_e-1BfffmHOt4bpep2tcBhzI-Yz2Uri7rFoF0I-i93y60voQz4g==)). Relevance: Gemini 3.5 Flash is 50% of the input cost but 60% of the output cost compared to Claude Sonnet 4.6, violating the 'less than half the cost' claim for output pricing.
- Gemini 3.5 Flash costs $1.50/$9.00 per 1M tokens but ships as a stable GA model... Gemini 3 Flash Preview remains the cheaper option at $0.50/$3.00 per 1M tokens... ([Gemini 3.5 Flash vs Gemini 3 Flash Preview: Pricing & Migration (2026) - EvoLink](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIr0TUrnQaJA7QgSwAslX6RRbVpueUaTs55K4tzFGfDMTmb2Ihi0zmwlpAwz0lmmdSmjSupSxXBco2uvyKCKhI_SKFKfVH1aT_IT64pkd13JwEnPhsjWhrpx3mT-gOauPu2rLERL5tzrLpQQguAubTz9KTrmRpPOw=)). Relevance: Highlights that Gemini 3.5 Flash introduces a severe 3x price markup compared to the Flash tier model it succeeds.
- DeepSeek-V4-Pro (New), $0.43, $0.87 ([DeepSeek Slashes V4-Pro Prices by up to 90% - HowAIWorks.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW1P1PoQV0SeaRx8SoXqiru3_rDnSjiRHBdg1LgsBz2dld0CzVt2aDDfN_nCh9wdRZtcFzVU6tclHZk4p77KZU_qaZeJEwdjW2M3uRHrjywLIS05iJ-_kYLEY-Ng3ETEO4cll72_zEWGVueU6VtK6G)). Relevance: Shows that competing frontier-level models like DeepSeek V4 Pro operate at a tiny fraction of the cost of Gemini 3.5 Flash, directly contradicting the cost advantage claim relative to other frontier models.

**Missing context:**
- No empirical, controlled, or peer-reviewed user studies are provided or referenced to support the assertion that workflows are compressed from days or weeks to a 'fraction of the time'. Google relies entirely on anecdotal corporate pilot partner testimonials.
- Gemini 3.5 Flash exhibits benchmark regressions on pure reasoning and long-context retrieval when compared to its predecessor Gemini 3.1 Pro, falling behind on Humanity's Last Exam (40.2% vs 44.4%), ARC-AGI-2 (72.1% vs 77.1%), and the 128k context slice of MRCR v2 (by 7.6 points).

**Computed checks:**
- Gemini 3.5 Flash API pricing: $1.50 per 1M input tokens, $9.00 per 1M output tokens.
- GPT-5.5 API pricing: $5.00 input, $30.00 output per 1M tokens.
- Claude Opus 4.7 API pricing: $5.00 input, $25.00 output per 1M tokens.
- GPT-5.4 API pricing: $2.50 input, $15.00 output per 1M tokens.
- Claude Sonnet 4.6 API pricing: $3.00 input, $15.00 output per 1M tokens.
- DeepSeek-V4-Pro API pricing: $0.43 input, $0.87 output per 1M tokens.
- Gemini 3.5 Flash is 3x more expensive than Gemini 3 Flash Preview ($0.50 input, $3.00 output).
- Humanity's Last Exam score regression: 40.2% (Gemini 3.5 Flash) vs 44.4% (Gemini 3.1 Pro).
- ARC-AGI-2 score regression: 72.1% (Gemini 3.5 Flash) vs 77.1% (Gemini 3.1 Pro).

</details>

<details><summary>numeric_calibrator: The claim states that Gemini 3.5 Flash completes in a fraction of the time what once took developers days or auditors weeks, and operates at less than half the cost of other frontier models. While external API pricing logs show Gemini 3.5 Flash is indeed cheaper than certain frontier models (such as Claude Opus 4.7, GPT-4 Turbo, and Claude 3 Opus), it is not 'less than half the cost' across all other frontier models like GPT-4o (where its output token cost of $9.00/1M is 90% of GPT-4o's $10.00/1M) or Claude 3.5 Sonnet (where its output cost of $9.00/1M is 60% of Sonnet's $15.00/1M). Furthermore, the source document completely lacks the empirical pricing frameworks, controlled user studies, or quantitative time metrics needed to verify the claims directly.</summary>

**Supporting evidence:**
- Gemini 3.5 Flash... Input price... $1.50 [per 1M tokens]. Output price... $9.00 [per 1M tokens]. ([Gemini Developer API pricing](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELxG7AXzPy10x1cmPsT6FTv1-eZ3eiotZTEM8rqQWhKkPm2yAFHfpyas-mtSJmQK7ccw99jFngtmK8PSRFmWcoKAg-wXtAGlcXv5qLEO9V-u46r-Te8XcZeIZg5tXN0RFst_k=)). Relevance: Provides official pricing for Gemini 3.5 Flash to compute relative cost comparisons against other frontier models.
- Claude Opus 4.7... $5.00 [input], $25.00 [output]... Claude Sonnet 4.6... $3.00 [input], $15.00 [output] ([Anthropic Claude API Pricing In 2026: Models, Token Rates, Costs - CloudZero](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9A8S4M_2IiIvY8xCo4Zt7CNcZwutXUI__JYEQh6qNJyT6eKZDqFExHLiYi46KsbOtwAAzvey4t7xfEra7Boekf1NAM9zr37_5B9e1fuEM4hT1ayP4GP1dl23bTT9NqAmAFoJ5DjfmUg==)). Relevance: Provides pricing for competing current-generation frontier models from Anthropic to assess the 'less than half the cost' claim.
- Pricing starts at $2.50 per million input tokens and $10.00 per million output tokens. ([GPT-4o API Pricing 2026 - Costs, Performance & Providers - Price Per Token](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZRzmi3U8AApZeBhi9CQCsfOjTVzS1Zr9nDktAP_iEvuNsKjkxMZUB5RPI0I3EF7sHZgZolevWT2O1GX0WT_Q7jQy6C1arkfVsPckDDvj7C7mRJzj_bCNyX3yhsQrS1mSd-I6ROWExWyeJzyHSiicF)). Relevance: Provides pricing for OpenAI's GPT-4o model to compare against Gemini 3.5 Flash.

**Contradictions / narrowing evidence:**
- Pricing starts at $2.50 per million input tokens and $10.00 per million output tokens. ([GPT-4o API Pricing 2026 - Costs, Performance & Providers - Price Per Token](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZRzmi3U8AApZeBhi9CQCsfOjTVzS1Zr9nDktAP_iEvuNsKjkxMZUB5RPI0I3EF7sHZgZolevWT2O1GX0WT_Q7jQy6C1arkfVsPckDDvj7C7mRJzj_bCNyX3yhsQrS1mSd-I6ROWExWyeJzyHSiicF)). Relevance: Shows that Gemini 3.5 Flash ($1.50 / $9.00) is not less than half the cost of GPT-4o, as $9.00 is 90% of GPT-4o's output token cost of $10.00.
- The model costs $3 per million input tokens and $15 per million output tokens ([Introducing Claude 3.5 Sonnet - Anthropic](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWOSfDvTRFEhXiFnxikUDVZ-PKNddkDEPafV09rwLjQ2y2oSZfmY9rb34oGVq18rppgSRBTEeFYqTPU6TtzpfP12ViUJEe5UbD-ihf7Qrp_PXGURV7z1yBcDOb4TKB1dCYtRAP_ec=)). Relevance: Shows that Gemini 3.5 Flash's output price of $9.00/1M tokens is 60% of Claude 3.5 Sonnet's output price ($15.00/1M tokens), which is greater than half (50%) of the cost.

**Missing context:**
- The source document lacks empirical, controlled developer or auditor user studies comparing time savings from days or weeks to fractions of time.
- The source document provides no pricing figures, rate tables, or formal comparisons to back up the assertion of operating at 'less than half the cost' of other frontier models.

**Computed checks:**
- Gemini 3.5 Flash standard API rate: Input = $1.50 / 1M tokens, Output = $9.00 / 1M tokens.
- GPT-4o standard API rate: Input = $2.50 / 1M tokens, Output = $10.00 / 1M tokens.
- Claude Sonnet 4.6 (and Claude 3.5 Sonnet) standard API rate: Input = $3.00 / 1M tokens, Output = $15.00 / 1M tokens.
- Claude Opus 4.7 standard API rate: Input = $5.00 / 1M tokens, Output = $25.00 / 1M tokens.
- Calculation 1 (vs GPT-4o input cost): $1.50 / $2.50 = 0.60 (60% of cost, which is not less than half).
- Calculation 2 (vs GPT-4o output cost): $9.00 / $10.00 = 0.90 (90% of cost, which is not less than half).
- Calculation 3 (vs Claude 3.5 Sonnet input cost): $1.50 / $3.00 = 0.50 (exactly 50% of cost, which is not strictly less than half).
- Calculation 4 (vs Claude 3.5 Sonnet output cost): $9.00 / $15.00 = 0.60 (60% of cost, which is not less than half).
- Calculation 5 (vs Claude Opus 4.7 input cost): $1.50 / $5.00 = 0.30 (30% of cost, which is less than half).
- Calculation 6 (vs Claude Opus 4.7 output cost): $9.00 / $25.00 = 0.36 (36% of cost, which is less than half).

</details>

### Evidence Contrast

**Claim says:** What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models.

**Best reference says:** The model card documents Gemini 3.5 Flash's performance on technical coding and reasoning benchmarks (such as Terminal-bench, SWE-Bench Pro, and Finance Agent v2) as percentage success rates or Elo scores. It does not mention specific API pricing, relative cost-efficiency metrics, or empirical measurements of developer and auditor time savings. It also lists 'multi-week enterprise processes' as an intended use case.

**Key qualification:** While the model card details the model's high benchmark scores and lists its applicability to agentic coding and auditing workflows, it does not provide any empirical studies or data regarding time-saved metrics, nor does it detail cost-savings compared to other frontier models.

**Delta:** narrower_than_claim — The reference source (the model card) is narrower than the claim because it only quantifies task accuracy on standard static benchmarks and lists intended applications. It contains no financial cost comparisons or concrete data to verify the claim of completing developer/auditor tasks in a fraction of the time or at less than half the cost. In fact, it lists 'multi-week enterprise processes' as an intended use case, which contradicts the absolute notion of shrinking all such workflows into a small fraction of the time.

**Final verdict:** overstated

**Defensible rewrite:** Gemini 3.5 Flash is designed to handle agentic coding, audit, and multi-week enterprise workflows, achieving near-Pro level performance on specialized technical benchmarks.

### Claim-Level Contrast References

- Gemini 3.5 Flash - Model Card (vendor_doc, authority 95/100): https://deepmind.google/models/model-cards/gemini-3-5-flash. It is the official technical documentation containing benchmarks, intended usage, and evaluation metrics for Gemini 3.5 Flash.

**Reference snippets / mismatches:**
- The model card documents Gemini 3.5 Flash's performance on technical coding and reasoning benchmarks (such as Terminal-bench, SWE-Bench Pro, and Finance Agent v2) as percentage success rates or Elo scores. It does not mention specific API pricing, relative cost-efficiency metrics, or empirical measurements of developer and auditor time savings. It also lists 'multi-week enterprise processes' as an intended use case. (Gemini 3.5 Flash - Model Card, narrows, https://deepmind.google/models/model-cards/gemini-3-5-flash). While the model card details the model's high benchmark scores and lists its applicability to agentic coding and auditing workflows, it does not provide any empirical studies or data regarding time-saved metrics, nor does it detail cost-savings compared to other frontier models.

**Computed checks:**
- Gemini 3.5 Flash API pricing: $1.50 per 1M input tokens, $9.00 per 1M output tokens.
- GPT-5.5 API pricing: $5.00 input, $30.00 output per 1M tokens.
- Claude Opus 4.7 API pricing: $5.00 input, $25.00 output per 1M tokens.
- GPT-4o standard API rate: Input = $2.50 / 1M tokens, Output = $10.00 / 1M tokens.
- Claude Sonnet 4.6 standard API rate: Input = $3.00 / 1M tokens, Output = $15.00 / 1M tokens.
- Calculation (vs GPT-4o output cost): $9.00 / $10.00 = 90% of cost, which is not less than half.
- Calculation (vs Claude Sonnet 4.6 output cost): $9.00 / $15.00 = 60% of cost, which is not less than half.

**Supporting evidence found:**
- Paid Tier: $1.50 per 1M input tokens, $9.00 per 1M output tokens. ([Gemini Developer API pricing](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJqTvVa9FHZeaoNTa7Q36CdoO1Hx6PhvoOgHG9o1WUfnd2CFKu1NvFL-zZ7nnEJ0Eq7knQ01krJd5fW55LkPEa1XmwU_3UVcTgAxTK86TDsFTjV-wUijikG77UBuTZhM9dqzY=)). Relevance: Establishes the exact API pricing framework for Gemini 3.5 Flash showing its per-token rates.
- Claude Opus 4.7, $5.00, $25.00 ([Claude API Pricing 2026: Latest Anthropic Costs for Opus, Sonnet, Haiku - EvoLink.AI](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMGOSgEiZn72DEvDDlYQvSmb3lDTE5ni5Dp0baWVyFtYIelK_jOVdJCOFCRvmwve20BU-lmIw_0Zv04z96D1T-pZUbIv_e-1BfffmHOt4bpep2tcBhzI-Yz2Uri7rFoF0I-i93y60voQz4g==)). Relevance: Confirms Claude Opus 4.7 pricing is $5/$25 per million tokens, against which Gemini 3.5 Flash is less than half the cost.

**Contradictions / narrowing evidence:**
- Pricing starts at $2.50 per million input tokens and $10.00 per million output tokens. ([GPT-4o API Pricing 2026 - Costs, Performance & Providers - Price Per Token](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZRzmi3U8AApZeBhi9CQCsfOjTVzS1Zr9nDktAP_iEvuNsKjkxMZUB5RPI0I3EF7sHZgZolevWT2O1GX0WT_Q7jQy6C1arkfVsPckDDvj7C7mRJzj_bCNyX3yhsQrS1mSd-I6ROWExWyeJzyHSiicF)). Relevance: Shows that Gemini 3.5 Flash ($1.50 / $9.00) is not less than half the cost of GPT-4o, as $9.00 is 90% of GPT-4o's output token cost of $10.00.
- It costs roughly 75% more to run a task on 3.5 Flash than it does on 3.1 Pro... Forced 'Thinking' Tokens: Gemini 3.5 Flash generates internal 'thinking' tokens... you are footed the bill for all of that invisible output text at $9.00 per 1M tokens. ([Gemini 3.5 Flash is actively penalizing developers who write good, efficient prompts](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQ0EOoBU_tOy1WTJ_WtxATDRIBIJKcbMrq7C9mt_aNyH8z1SJtz_Opsrjf5WTIjMIpL1PK1_kbB1Li995uAZS0QE_mY-_WqcotY6TnE9oDFazRy0wTDNuFTdpomaVgdi_91ghcAxRxMpiYkyshES5QbWn56q3qLD5DVun5oJfQ5zML9KjP7DntD_Ir8tzAvpLJ_FLN7CQZM-3o8InZG5VzetrlSSgi98H60WCn7fwAwyw==)). Relevance: Shows that actual execution costs can be higher due to verbose thinking tokens, challenging the cost savings claim in practice.

**Missing context:**
- The source document lacks empirical, controlled developer or auditor user studies comparing time savings from days or weeks to fractions of time.
- The cost advantage of 'less than half the cost' does not apply to popular mid-tier frontier models like GPT-4o or Claude Sonnet 4.6.


## claim_4: overstated

**Confidence:** high

**Original:** Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.

**Stretch Score:** 45/100

**Why:** The claim asserts that the model can 'reliably' execute multi-step workflows and coding tasks under supervision. However, official model card benchmarks show failure rates of 16.4% to 44.9% on agentic and coding benchmarks. Calling this 'reliable' is an overstatement of the model's autonomous capabilities, and the critical caveat 'under supervision' is left completely undefined without metrics on the frequency of required human intervention.

**Defensible rewrite:** Under human supervision, Gemini 3.5 Flash can execute multi-step workflows and coding tasks, outperforming prior models on agentic benchmarks while still exhibiting failure rates between 16% and 45% on complex tasks.

### Agent Steps

<details><summary>grounded_verifier: The claim that Gemini 3.5 Flash can reliably execute multi-step workflows and coding tasks under supervision while sustaining frontier performance is directly supported by the source document's text. However, the document does not define 'reliability' nor does it provide any specific quantitative metrics regarding the success rate or mean-time-to-failure (MTTF) for workflows exceeding 10 steps. These details represent missing context that is not addressed in either the announcement blog post or the official Gemini 3.5 model card.</summary>

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Directly states the claim verbatim.
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5 - Google DeepMind](https://deepmind.google)). Relevance: Provides the official evaluation benchmarks verifying the frontier performance in coding and agentic tasks.

**Missing context:**
- Measured success rate of Gemini 3.5 Flash when executing multi-step workflows exceeding 10 steps.
- Mean-time-to-failure (MTTF) of Gemini 3.5 Flash when executing workflows exceeding 10 steps.
- How reliability is defined and programmatically verified in these specific multi-step environments.

**Computed checks:**
- Terminal-Bench 2.1 benchmark score: 76.2%
- GDPval-AA Elo rating: 1656
- MCP Atlas benchmark score: 83.6%
- CharXiv Reasoning benchmark score: 84.2%
- Model speed: 4 times faster output tokens per second compared to other frontier models

</details>

<details><summary>contradiction_finder: While Google claims Gemini 3.5 Flash can 'reliably execute multi-step workflows' under supervision, it does not define 'reliability' nor provide any measured Mean-Time-to-Failure (MTTF) or success rate for workflows exceeding 10 steps. Empirical benchmarks in official model cards reveal significant failure rates on multi-step and agentic tasks, ranging from 16.4% to 44.9%. Furthermore, the qualifier 'under supervision' is a critical caveat indicating that the system is not fully autonomous and requires human oversight to ensure reliable execution.</summary>

**Supporting evidence:**
- Source returned by Gemini grounding metadata. ([deepmind.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm1rrT8oxyTR1JzWNSkPWGBMxJ-hGK0F1Z7WnUBvYPlEzthrgyomO4FYnCHk-cWyBc4igphdHzoGTRRsyikqqz0atjtz8ctZAdLpSiqV66sGffVIiWSy2K_wBhb9-SjWe9d3cqlYqyYWMv9PVzBWF4984=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([truefoundry.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMZ-x7F5PeAL_DnUgz0-irl-Rc4yUhwvf_7GNxrDmGcIDa2wUdo2XkrrHP-tzxjcUcR_HgAHgywEvnEUKf30259rSqO88EPHApbisjt6tF6II69aZNy1YF91gKwgAc5mdDxr7EGlpIRmjrVRKNI9YlVbvt53L063t4KacKdOJGb9rjCOAwHTVGmJ4e4X6JQw2cN_NJRNw=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([blog.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsHltF4wLUysijFD0l6kQpjRfDaF-Mj6pcLOZO7Wph6WofTEqKFthq-uB78ibJxRI5VkWQxqcejNR1DYyQTzvRKaqQo30qQGTkto_VHIkC1DTq1EcIsdBGOO2Y5DyzC7YpJ5ehgd5A5yaOR5C2lctbhKWc6XwcKSUA1NWY8vOUsneEyr_7LwRLsw==)). Relevance: Grounding source used during specialist audit.

**Contradictions / narrowing evidence:**
- Terminal-bench 2.1 Agentic terminal coding... 76.2% ... SWE-Bench Pro (Public) Diverse agentic coding tasks, Single attempt, 55.1% ... Agentic, MCP Atlas Multi-step workflows using MCP, 83.6%... Toolathlon Real-world general [tool use], 56.5% ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: These official benchmarks demonstrate that Gemini 3.5 Flash fails on 16.4% to 44.9% of multi-step and agentic tasks depending on the harness, directly showing that the model does not achieve flawless reliability in executing these tasks autonomously.

**Missing context:**
- No quantitative definition of 'reliability' is established, nor is any metric provided for Mean-Time-to-Failure (MTTF) or success rates specifically for agentic workflows exceeding 10 steps.
- The claim specifies 'Under supervision,' which functions as an unquantified caveat meaning the model's reliability is contingent on Human-in-the-Loop intervention to catch and correct failures.
- Enterprise customer references (such as Shopify, Macquarie Bank, and Salesforce) describe qualitative or early pilot applications without disclosing operational error rates, success thresholds, or concrete definitions of reliability in production.

**Computed checks:**
- Gemini 3.5 Flash scores 55.1% on SWE-Bench Pro (Public), reflecting a 44.9% failure rate on complex, multi-file agentic coding tasks.
- The model achieves a 56.5% success rate on the Toolathlon benchmark, meaning it fails 43.5% of real-world general tool use evaluations.
- The model scores 76.2% on Terminal-Bench 2.1 and 83.6% on MCP Atlas, demonstrating failure rates of 23.8% and 16.4% respectively on terminal and multi-step tool-use environments.

</details>

<details><summary>Numeric Calibrator: The claim states that Gemini 3.5 Flash can reliably execute multi-step workflows and coding tasks under supervision, but the document does not provide any quantitative success rates, mean-time-to-failure (MTTF) metrics, or empirical definitions of reliability to support this assertion.</summary>

**Supporting evidence:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: This is the qualitative assertion of the claim in the text, which lacks accompanying numeric metrics.

**Missing context:**
- The measured success rate of Gemini 3.5 Flash when executing multi-step workflows (specifically those exceeding 10 steps).
- The mean-time-to-failure (MTTF) or rate of required intervention for these workflows.
- A quantitative definition of how 'reliability' is defined, evaluated, and verified in these environments.

**Computed checks:**
- The qualitative claim contains 0 numeric parameters, error rates, or success thresholds.
- The text cites general benchmarks (Terminal-Bench 2.1: 76.2%, GDPval-AA: 1656 Elo, MCP Atlas: 83.6%, CharXiv Reasoning: 84.2%), but these do not measure workflow execution reliability or MTTF.
- No arithmetic calculations (such as absolute or relative deltas) can be performed because no baseline or operational reliability statistics are provided in the document.

</details>

### Evidence Contrast

**Claim says:** Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.

**Best reference says:** The model card establishes actual success rates on agentic benchmarks ranging from 55.1% to 83.6%, meaning autonomous failure rates are substantial (16.4% to 44.9%). This narrows the broad claim of 'reliably' executing such workflows.

**Key qualification:** Assumes active human monitoring and intervention to handle failures and maintain operational workflows.

**Delta:** narrower_than_claim — While the model demonstrates frontier-level performance compared to other models on agentic benchmarks, the claim of 'reliably' executing these workflows is overstated because the actual empirical success rates range from 55.1% to 83.6%, meaning failure rates are significant (16.4% to 44.9%). Human supervision is a critical, unquantified safeguard rather than an optional enhancement.

**Final verdict:** overstated

**Defensible rewrite:** Under human supervision, Gemini 3.5 Flash can execute multi-step workflows and coding tasks, achieving frontier-tier benchmark results while continuing to face typical agentic failure rates of 16% to 45%.

### Claim-Level Contrast References

- Gemini 3.5: frontier intelligence with action (official_doc, authority 90/100): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/. This is the primary blog post hosting the claim.

**Reference snippets / mismatches:**
- The model card establishes actual success rates on agentic benchmarks ranging from 55.1% to 83.6%, meaning autonomous failure rates are substantial (16.4% to 44.9%). This narrows the broad claim of 'reliably' executing such workflows. (Gemini 3.5: frontier intelligence with action / Gemini 3.5 Flash Model Card, narrows, https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/). Assumes active human monitoring and intervention to handle failures and maintain operational workflows.

**Computed checks:**
- Gemini 3.5 Flash has a 44.9% failure rate on complex agentic coding tasks (55.1% success on SWE-Bench Pro).
- The model fails 43.5% of real-world tool use evaluations (56.5% success on Toolathlon).
- Failure rates of 23.8% on Terminal-Bench 2.1 and 16.4% on MCP Atlas are observed.
- The qualitative claim contains no specific error rates, success thresholds, or operational reliability parameters.

**Supporting evidence found:**
- Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance. ([Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: Provides the exact verbatim statement of the claim in the promotional document.
- It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). ([Gemini 3.5 - Google DeepMind](https://deepmind.google)). Relevance: Verifies that the model achieves top-tier scores relative to previous versions, supporting the 'sustaining frontier performance' aspect.

**Contradictions / narrowing evidence:**
- Terminal-bench 2.1 Agentic terminal coding... 76.2% ... SWE-Bench Pro (Public) Diverse agentic coding tasks, Single attempt, 55.1% ... Agentic, MCP Atlas Multi-step workflows using MCP, 83.6%... Toolathlon Real-world general [tool use], 56.5% ([Gemini 3.5 Flash - Model Card - Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)). Relevance: These official benchmarks show failure rates ranging from 16.4% to 44.9% on complex multi-step and agentic tasks, demonstrating that the system does not achieve flawless reliability without significant human oversight.

**Missing context:**
- A quantitative definition of 'reliability' is missing, with no metrics provided for Mean-Time-to-Failure (MTTF) or success rates for workflows exceeding 10 steps.
- The rate and nature of human intervention required under the 'under supervision' constraint is not disclosed or quantified.
- Qualitative enterprise customer testimonials lack operational error rates or success thresholds in real-world environments.

