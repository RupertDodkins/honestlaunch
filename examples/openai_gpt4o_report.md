# CappinCheck Report: GPT-4o System Card

Source: `https://cdn.openai.com/gpt-4o-system-card.pdf`

## Provenance

- Mode: `live_gemini`
- Model: `gemini-3.5-flash`
- Pipeline wall: `93.26s`
- Load / Extract / Audit / Contrast: `9.79s` / `27.60s` / `55.87s` / `0ms`
- Claims extracted / audited: `8` / `1`
- Specialist passes / unique sources: `3` / `1`

- Evidence Contrast: `disabled`
- Provided reference URLs: `none`

## Scorecard

- Claims audited: `1`
- Verdict counts: `supported=0` · `overstated=0` · `missing_context=1` · `contradicted=0` · `not_checkable=0`
- Average stretch score: `35/100`
- Provided reference URL count: `0`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in a conversation. | missing_context | high | 35 |

## claim_1: missing_context

**Confidence:** high

**Original:** GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in a conversation.

**Stretch Score:** 35/100

**Why:** While the claimed response times (232 ms minimum, 320 ms average) are directly cited from the official GPT-4o System Card, the document completely omits the operational context under which these metrics were achieved. Crucial parameters—such as host GPU models, server cluster configurations, concurrent traffic loads, and whether these figures incorporate client-to-server network round-trip time (RTT)—are not disclosed. Independent benchmarks in production environments show that real-world end-to-end conversational latency averages around 1.2 seconds, which is about four times slower than the model's server-side processing average and fails to match 'human-like' conversational speeds in standard deployment.

**Defensible rewrite:** Under optimal, local server-side benchmark conditions, GPT-4o is capable of processing and generating audio responses in as little as 232 milliseconds (with a 320 millisecond average), though typical real-world end-to-end conversational latencies are higher due to network transit and routing overhead.

**Claim timing:**
- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: 55.87s / 27.12s / 29.74s / 25.66s / 26.11s / 0ms

### Agent Steps

<details><summary>grounded_verifier: The GPT-4o System Card supports the claim that GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds. However, neither the system card nor OpenAI's official launch documentation discloses the exact hardware configuration, network latency, or server load conditions under which these benchmarks were measured. Furthermore, it is not explicitly stated whether these figures include end-to-end network round-trip time (RTT), though external technical reports suggest they represent server-side processing/inference latency rather than real-world end-to-end WAN transit times.</summary>

**Duration:** 27.12s

**Supporting evidence:**
- GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time[2] in a conversation. ([GPT-4o System Card](https://cdn.openai.com/gpt-4o-system-card.pdf)). Relevance: Provides direct primary source support for the claimed minimum and average response times.
- Source returned by Gemini grounding metadata. ([openai.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYmSrmESR8Z-1HVNDN8eukQl8lNF4jR4BLdXMjZjHxmWS3hgYOVLSALDYozL_sBhUIDUa8PKZ5Ol-As3-fJ7j8kptjZ45sfxTWj17zBb2U2PLLfFG_XB5xSn0_KJpF_bGcmA==)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([agora.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4aUm7WvxcK_n9BmFzqMC0JdLDxI5zh02kWDN5dCF_5oHdXyHk-Bvc4X5M9wRJN-CeK9hSP0rlHDTIYeYBGUjlrf8Zb4gPApF4eO02kvD43wpWxdyrnb9HybTmSGAFAU_0-qBrgvWHgVEexBq8JXyMpQwxKSeori9tJh3QwA8pRc9piFW-7ZWL86fUCIgYMo8fiMsV4tfO_N0=)). Relevance: Grounding source used during specialist audit.

**Missing context:**
- The exact hardware configuration (such as host GPU models and cluster setup) used during the latency benchmarks.
- The network conditions, routing protocols, and whether WAN or local network latency was factored into the figures.
- The server load and concurrency levels (requests per second) active during the evaluation.
- An explicit breakdown of whether the figures measure server-side time-to-first-token (TTFT) or true end-to-end mouth-to-ear latency.

**Computed checks:**
- Minimum audio response time of 232 milliseconds
- Average audio response time of 320 milliseconds

</details>

<details><summary>skeptical_contradiction_finder: While the GPT-4o System Card states that the model can respond to audio inputs in as little as 232 milliseconds (with a 320ms average), the claim completely omits any description of the testing environment or conditions under which these numbers were obtained. There is no disclosure of server load, GPU hardware configurations, physical server locations, or network variables. Furthermore, the document does not clarify if these metrics include end-to-end network round-trip time (RTT) or are merely server-side Time to First Token (TTFT) measurements. Independent real-world benchmarks show that end-to-end conversational latency in production is significantly higher.</summary>

**Duration:** 29.74s

**Supporting evidence:**
- Source returned by Gemini grounding metadata. ([openai.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDHaldqOZrwU4zGU45uyhsHpnrXXDRW6InPfi3w_k02_FMGufyDYNlZX8_XFniYmvE_ShXwPER8wmXaUfwaea42xWcCrlDvLt1Zu4PRoTUJyHY7pCas5w_9IXrPHHhLysIiOQ=)). Relevance: Grounding source used during specialist audit.
- Source returned by Gemini grounding metadata. ([ailatency.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMgAH7kikYU_60bJtShP0Nmr5HhrMXYBcf31q2uDwqMNuwgztie68ZA7AgFa9rSD-0Vba_vr7lJS07SzuK_36UKIjssY3dL1-xLxBm2aGjBEC1ejaSMibVBMmOEBwsQAI4h3PdaVx5xcA=)). Relevance: Grounding source used during specialist audit.

**Contradictions / narrowing evidence:**
- Total Latency 1.2s Grade C . Average. Time to First Token 1.2s Initial Response Time. (GPT-4o Response Time, TTFT & Throughput - AILatency). Relevance: Independent production-level API performance benchmarks indicate that the actual end-to-end response time (including network and routing overhead) for GPT-4o averages around 1.2 seconds, which is roughly 4 times slower than the ideal 320ms average presented by OpenAI.

**Missing context:**
- The document does not disclose the specific hardware configuration (e.g., GPU specifications or cluster sizes) used to run the low-latency tests.
- The claim fails to clarify whether the 232ms minimum and 320ms average latencies include end-to-end network round-trip time (RTT) or represent solely server-side inference (Time to First Token/Audio Packet) times.
- No information is provided regarding the server load conditions (e.g., isolated testing environment vs. live public traffic) during these latency benchmarks.
- The claim omits geographic and connectivity constraints; standard mobile or residential network transit times alone can introduce 50ms to 200ms+ of latency, preventing real-world interactions from matching 'human response times' under typical network paths.

**Computed checks:**
- Reported minimum audio response latency: 232 ms
- Reported average audio response latency: 320 ms
- Observed real-world production average response latency (TTFT): 1.2 seconds

</details>

<details><summary>numeric_calibrator: The claim states that GPT-4o can respond to audio inputs in as little as 232 ms (minimum) and 320 ms (average), which is comparable to human response times in conversation. While the document mentions these numbers, it lacks any specified network latency conditions, hardware configurations, concurrent server load environments, or explicit numeric thresholds used for the human baseline comparison.</summary>

**Duration:** 25.66s

**Supporting evidence:**
- GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time[2] in a conversation. ([GPT-4o System Card](https://cdn.openai.com/gpt-4o-system-card.pdf)). Relevance: Provides the specific minimum (232 ms) and average (320 ms) response times for GPT-4o's audio input capabilities.

**Missing context:**
- The specific hardware configuration (e.g., CPU/GPU model specifications, memory capacity, and clustering architecture) utilized during the benchmark.
- The network conditions under which the testing took place, specifically clarifying whether these figures are local/model execution latencies or if they include client-to-server end-to-end network round-trip time (RTT).
- The server load environment (such as concurrent requests, queries per second, and overall system load) present during the latency measurement.
- The exact numeric benchmark value used for the 'human response time in a conversation' (which is referenced via citation [2] but not quantified in the text).

**Computed checks:**
- Absolute delta between the average and minimum response times: 320 ms - 232 ms = 88 ms.
- Relative increase from the minimum response time to the average response time: (320 ms - 232 ms) / 232 ms = 37.93%.
- Relative decrease from the average response time to the minimum response time: (320 ms - 232 ms) / 320 ms = 27.50%.
- Unit conversion of minimum response time to seconds: 232 ms = 0.232 seconds.
- Unit conversion of average response time to seconds: 320 ms = 0.320 seconds.

</details>

<details><summary>claim-aggregator: Combined specialist outputs into final verdict `missing_context` with `high` confidence.</summary>

**Duration:** 26.11s

**Supporting evidence:**
- GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time[2] in a conversation. ([GPT-4o System Card](https://cdn.openai.com/gpt-4o-system-card.pdf)). Relevance: Provides direct primary source support for the claimed minimum and average response times.

**Contradictions / narrowing evidence:**
- Total Latency 1.2s Grade C . Average. Time to First Token 1.2s Initial Response Time. (GPT-4o Response Time, TTFT & Throughput - AILatency). Relevance: Independent production-level API performance benchmarks indicate that the actual end-to-end response time (including network and routing overhead) for GPT-4o averages around 1.2 seconds, which is roughly 4 times slower than the ideal 320ms average presented by OpenAI.

**Missing context:**
- The specific hardware configuration (such as CPU/GPU model specifications, memory capacity, and clustering architecture) utilized during the benchmark.
- The network conditions under which testing took place, specifically clarifying whether these figures are local/model execution latencies or if they include client-to-server end-to-end network round-trip time (RTT).
- The server load environment (such as concurrent requests, queries per second, and overall system load) present during the latency measurement.
- The exact numeric benchmark value used for the 'human response time in a conversation' (which is referenced via citation but not quantified in the text).

**Computed checks:**
- Reported minimum audio response latency: 232 ms (0.232 seconds)
- Reported average audio response latency: 320 ms (0.320 seconds)
- Observed real-world production average response latency (TTFT): 1.2 seconds
- Absolute delta between the average and minimum response times: 88 ms
- Relative increase from the minimum response time to the average response time: 37.93%

</details>

**Computed checks:**
- Reported minimum audio response latency: 232 ms (0.232 seconds)
- Reported average audio response latency: 320 ms (0.320 seconds)
- Observed real-world production average response latency (TTFT): 1.2 seconds
- Absolute delta between the average and minimum response times: 88 ms
- Relative increase from the minimum response time to the average response time: 37.93%

**Gemini-discovered supporting sources:**
- GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time[2] in a conversation. ([GPT-4o System Card](https://cdn.openai.com/gpt-4o-system-card.pdf)). Relevance: Provides direct primary source support for the claimed minimum and average response times.

**Gemini-discovered caveat / counter sources:**
- Total Latency 1.2s Grade C . Average. Time to First Token 1.2s Initial Response Time. (GPT-4o Response Time, TTFT & Throughput - AILatency). Relevance: Independent production-level API performance benchmarks indicate that the actual end-to-end response time (including network and routing overhead) for GPT-4o averages around 1.2 seconds, which is roughly 4 times slower than the ideal 320ms average presented by OpenAI.

**Missing context:**
- The specific hardware configuration (such as CPU/GPU model specifications, memory capacity, and clustering architecture) utilized during the benchmark.
- The network conditions under which testing took place, specifically clarifying whether these figures are local/model execution latencies or if they include client-to-server end-to-end network round-trip time (RTT).
- The server load environment (such as concurrent requests, queries per second, and overall system load) present during the latency measurement.
- The exact numeric benchmark value used for the 'human response time in a conversation' (which is referenced via citation but not quantified in the text).

