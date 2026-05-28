# Landscape Research Handoff

Status: handoff brief for a deep research agent to investigate whether a disclosure-quality benchmark/archive for AI model launches already exists, and what adjacent resources could support or compete with this direction.

## One-Sentence Project Summary

We are exploring a product that audits AI model launch disclosures for **support quality**, not absolute truth: it would freeze a dated evidence packet for each launch, assign claim-level verdicts such as `supported`, `overstated`, and `missing_context`, publish a reviewed artifact, and aggregate those audits into a recurring benchmark of **how stretched, comparable, and well-supported model-provider announcements are**.

## What Exists Today

Current internal prototype:

- repo: `/Users/rupert/engineering/honestlaunch`
- current artifact direction:
  - audited launch-page regeneration
  - claim ledger with verdicts, evidence, and rewrites
- current product thinking is shifting from:
  - “paste any launch URL and generate live”
  - toward
  - “curated, reviewed archive of major launches plus benchmark”

Relevant internal context docs:

- [docs/temporary/audited-launch-page-plan.md](/Users/rupert/engineering/honestlaunch/docs/temporary/audited-launch-page-plan.md:1)
- [docs/temporary/hosted-beta-implementation-spec.md](/Users/rupert/engineering/honestlaunch/docs/temporary/hosted-beta-implementation-spec.md:1)
- [docs/temporary/disclosure-benchmark-plan.md](/Users/rupert/engineering/honestlaunch/docs/temporary/disclosure-benchmark-plan.md:1)

## What We Need To Learn

We need a strong landscape layer on questions like:

1. Does a direct analogue already exist?
2. If not, what adjacent products, datasets, benchmarks, and standards already cover parts of the problem?
3. What data sources or APIs could support a serious version of this benchmark?
4. What methodology precedents exist for scoring disclosure quality, transparency, claim support, or benchmark comparability?
5. Is the better product a live auditing tool, or a curated archive/benchmark destination?

## Core Product Idea To Evaluate

### Product Thesis

The public product is not primarily a “truth engine.”

It is a **disclosure-quality audit** and **benchmark archive** for frontier AI launches.

For each major launch:

- freeze a dated evidence packet
- identify benchmarkable claims
- judge support relative to evidence
- publish a reviewed artifact
- aggregate scores across labs over time

### Core Claim

This product would answer:

- “How well supported was this launch language?”
- “How stretched was this announcement?”
- “How comparable were the benchmark claims?”
- “How much methodology and caveat context was disclosed?”

It would **not** try to answer:

- “Which model is objectively the best overall?”
- “Which lab is the most truthful in a moral sense?”

## Working Taxonomy

### Primary Verdicts

These are intended to be mutually exclusive at the claim level:

- `supported`
- `overstated`
- `missing_context`
- `contradicted`
- `not_checkable`

### Secondary Dimensions

These likely sit underneath the verdict:

- stretch severity
- evidence confidence
- comparability risk
- disclosure completeness
- numeric integrity

Research should evaluate whether this structure matches best practice or whether there are stronger alternatives.

## What Counts As “Evidence”

Preferred evidence stack:

### Primary Sources

- launch post
- model card / system card
- eval appendix
- benchmark-native official docs or papers
- pricing / availability docs

### Secondary Sources

- third-party benchmark aggregators
- public leaderboards
- benchmark datasets

### Deterministic/Internal Checks

- percent and percentage-point math
- benchmark rank claims
- pricing / tokens-per-second claims
- dates and availability claims

Research should specifically test whether any of the secondary sources are accepted as sufficiently authoritative to support recurring publication.

## Main Research Questions

### A. Direct Analogues

Find any products, archives, or research projects that already do something close to this:

- audit AI launch-post language
- measure overstatement/stretch in AI vendor announcements
- benchmark disclosure quality across AI labs
- compare model launch claims to model cards / eval reports / leaderboards

Important:

- direct analogue means more than “general fact-checking”
- direct analogue means more than “capability leaderboard”

### B. Adjacent Categories

Map strong adjacent categories:

1. AI capability benchmark aggregators
2. AI transparency and documentation benchmarks
3. fact-checking / claim-verification tools
4. model-card / system-card ecosystems
5. disclosure-quality scoring systems outside AI

### C. Data And API Availability

For each promising resource, determine:

- API or dataset access
- stability
- licensing
- update frequency
- whether it can be cited in a reviewed benchmark

### D. Methodology Precedents

Find serious precedents for scoring:

- disclosure completeness
- comparability
- evidence support
- marketing claim substantiation
- model transparency

### E. Product Positioning

Assess whether the strongest opportunity is:

- live generation tool
- curated reviewed archive
- benchmark destination
- analyst workflow tool
- compliance / comms workflow tool

## Initial Landscape Snapshot

This is not the final answer. It is a quick initial map to help the deep research agent start from non-zero context.

### 1. Transparency / Disclosure Benchmarks

Most relevant current analogue:

- **Stanford Foundation Model Transparency Index (FMTI)**  
  Measures foundation-model developer transparency across many indicators. This is the closest benchmark-like precedent on the **transparency/disclosure** side, but it is broader than launch-post claim support and not specifically about announcement language.  
  Sources:
  - [FMTI home](https://crfm.stanford.edu/fmti/)
  - [FMTI 2025 index](https://crfm.stanford.edu/fmti/December-2025/index.html)
  - [Stanford HAI summary](https://hai.stanford.edu/news/transparency-in-ai-is-on-the-decline)

### 2. Capability Benchmark Aggregators

These are likely supporting evidence sources, not the benchmark itself:

- **Artificial Analysis**  
  Independent benchmark aggregator with API access and published methodology. Strong candidate as a structured secondary source, but should not be treated as sole truth.  
  Sources:
  - [API reference](https://artificialanalysis.ai/documentation)
  - [FAQ / methodology overview](https://artificialanalysis.ai/faq)
  - [Main site](https://artificialanalysis.ai/)

- **Arena / LM Arena**  
  Important as a public preference-based leaderboard and source of historical leaderboard snapshots. Useful for “ranked #1” or Elo-style claims, but should be treated carefully because it measures a specific construct.  
  Sources:
  - [leaderboard dataset on Hugging Face](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
  - [dataset list](https://huggingface.co/lmarena-ai/datasets)

- **LiveBench**  
  Strong candidate for contamination-aware objective evaluation references and a methodology precedent for living benchmarks.  
  Sources:
  - [paper](https://arxiv.org/abs/2406.19314)
  - [project PDF / site reference](https://livebench.ai/livebench.pdf)

- **HELM / Stanford CRFM**  
  Strong methodology precedent for holistic, reproducible benchmarking; less directly about launch disclosure.  
  Sources:
  - [HELM GitHub](https://github.com/stanford-crfm/helm)
  - [HELM Instruct writeup](https://crfm.stanford.edu/2024/02/18/helm-instruct.html)

- **Epoch AI benchmarking**  
  Relevant as a public example of aggregating results from many benchmarks and external sources with explicit methodology.  
  Source:
  - [Epoch AI benchmarking overview](https://epoch.ai/benchmarks/about)

### 3. Fact-Checking / Claim-Verification Infrastructure

These are adjacent because they help with claim spotting and evidence retrieval, but are not obviously the same product:

- **Factiverse**  
  Offers claim detection, stance detection, fact-checking, and APIs. Potentially relevant as workflow or technical precedent.  
  Sources:
  - [Products](https://www.factiverse.ai/products)
  - [API overview](https://www.factiverse.ai/api)
  - [API docs](https://api.factiverse.ai/v1/redoc)

- **ClaimBuster**  
  Longstanding academic / applied claim-detection and fact-checking infrastructure with an API. Likely relevant for methodology, especially around “check-worthy claim” detection.  
  Sources:
  - [API docs](https://idir.uta.edu/claimbuster-dev/api/)
  - [benchmark dataset of check-worthy factual claims](https://arxiv.org/abs/2004.14425)

- **AVeriTeC**  
  Important dataset/research precedent for real-world claim verification with web evidence.  
  Source:
  - [AVeriTeC paper](https://arxiv.org/abs/2305.13117)

### 4. Model Card / System Card / Documentation Ecosystem

These matter because the proposed benchmark depends heavily on frozen evidence packets and disclosure artifacts:

- **Google DeepMind model cards**  
  Important source type; also evidence that model-card ecosystems are already standardized enough to use as benchmark inputs.  
  Source:
  - [DeepMind model cards](https://deepmind.google/models/model-cards/)

- **Hugging Face model cards**  
  Important precedent for documentation standards and potential indexing infrastructure.  
  Sources:
  - [Hub model cards docs](https://huggingface.co/docs/hub/main/model-cards)
  - [Model card creation guide](https://huggingface.co/docs/huggingface_hub/guides/model-cards)

- **Google Model Card Toolkit**  
  Useful documentation and tooling precedent.  
  Sources:
  - [Google blog intro](https://research.google/blog/introducing-the-model-card-toolkit-for-easier-model-transparency-reporting/?m=1)
  - [Toolkit guide](https://tensorflow.google.cn/responsible_ai/model_card_toolkit/guide?hl=en)

- **Machine-readable system-card work**  
  Relevant for structured evidence packets and canonical schemas.  
  Source:
  - [Red Hat AI system card repo](https://github.com/RedHatProductSecurity/ai-system-card)

- **OpenAI system cards**  
  Important evidence source type and precedent for dated public safety/eval documents.  
  Sources:
  - [GPT-4o system card](https://openai.com/index/gpt-4o-system-card/)
  - [o1 system card](https://openai.com/index/openai-o1-system-card/)

- **Anthropic system cards / Responsible Scaling Policy**  
  Important evidence source type and transparency precedent.  
  Sources:
  - [Responsible Scaling Policy updates](https://www.anthropic.com/responsible-scaling-policy)
  - [Claude 4 system card PDF](https://assets.anthropic.com/m/6c940a1b69ed6a1c/original/Claude-4-System-Card.pdf)

- **STREAM (Standard for Transparently Reporting Evaluations in AI Model Reports)**  
  Especially relevant as a precedent for how model reports should disclose evaluation evidence, methodology, caveats, and reporting quality. This is closer to the “how well was this announcement/report supported?” question than generic capability leaderboards.  
  Sources:
  - [STREAM site](https://streamevals.com/)
  - [STREAM paper](https://arxiv.org/abs/2508.09853)
  - [Follow-on comparison of real model reports against STREAM](https://arxiv.org/abs/2510.20927)

### 5. Benchmark Critique / Methodology Caution

These are important because this project must avoid reproducing shallow leaderboard logic:

- **Can We Trust AI Benchmarks?**  
  Relevant meta-methodology literature on benchmark validity, gaming, and construct mismatch.  
  Sources:
  - [arXiv abstract](https://arxiv.org/abs/2502.06559)
  - [AAAI / AIES paper download](https://ojs.aaai.org/index.php/AIES/article/download/36595/38733/40670)

- **AI Index / responsible AI reporting references**  
  Useful for broader framing and transparency context.  
  Source:
  - [Stanford AI Index responsible AI chapter](https://hai.stanford.edu/ai-index/2025-ai-index-report/responsible-ai)

- **Audit Cards: Contextualizing AI Evaluations**  
  Useful precedent for making audits inspectable and reporting context such as auditor identity, scope, methodology, resource access, process integrity, and review mechanisms.  
  Source:
  - [Audit Cards paper](https://arxiv.org/abs/2504.13839)

- **Unsteady Metrics and Benchmarking Cultures of AI Model Builders**  
  Important recent critique of how labs selectively highlight different benchmarks across releases, which is directly relevant to a benchmark about announcement comparability and stretch.  
  Sources:
  - [paper](https://arxiv.org/abs/2605.14164)
  - [Benchmarking-Cultures-25 dataset](https://huggingface.co/datasets/matybohacek/benchmarking-cultures-25)

## Initial Hypotheses

These should be tested, not assumed.

1. **No direct public benchmark currently dominates this exact niche.**  
   Initial scan found strong adjacent projects, but no obvious widely known product focused specifically on **AI launch-post disclosure stretch/support quality**.

2. **The closest serious precedent is FMTI, not Artificial Analysis.**  
   FMTI is closer on “transparency/disclosure” while Artificial Analysis is closer on “capability leaderboard data.”

3. **The strongest public product direction is likely a curated archive plus benchmark, not arbitrary live generation.**  
   Trust, cost, and latency all favor publication of reviewed artifacts over open live generation.

4. **The evidence stack will likely need multiple classes of sources.**  
   No single benchmark aggregator will be sufficient as “the” source of truth.

5. **The novelty may lie more in synthesis and methodology than raw technology.**  
   The gap appears to be a reviewed disclosure benchmark built from evidence packets, not a new model capability benchmark.

## What The Deep Research Agent Should Produce

Please return:

### 1. Direct Analogues Table

For any product / project that seems close:

- name
- category
- what it does
- target user
- business model if knowable
- how close it is to this idea
- why it matters

### 2. Adjacent Resource Map

Organize by:

- transparency benchmarks
- capability benchmark aggregators
- fact-checking / claim verification tools
- documentation / model-card ecosystems
- disclosure / compliance scoring systems outside AI

### 3. Data / API Source Table

For each relevant source:

- source name
- official URL
- API or dataset availability
- pricing / access constraints
- update cadence
- citation suitability
- likely role in our evidence packet

### 4. Methodology Precedents

Summarize the strongest precedents for:

- claim selection
- check-worthiness
- evidence-grounded verdicts
- transparency/disclosure scoring
- benchmark aggregation

### 5. White-Space Assessment

Conclude with:

- what already exists
- what is crowded
- what seems underbuilt
- where this project would be differentiated

### 6. Recommendation

Answer directly:

- Should this be a live generation tool, curated archive, benchmark, or workflow product?
- What is the most defensible first wedge?

## Suggested Search Directions

### Direct search themes

- AI launch post audit
- model announcement fact check
- AI model transparency benchmark
- system card archive
- model card database
- claim substantiation software
- marketing claim verification
- disclosure quality benchmark
- vendor benchmark comparability

### Outside-AI analogue themes

- advertising claim substantiation software
- investor disclosure quality scoring
- earnings-call claim verification
- ESG disclosure benchmark
- policy transparency scorecards

## What To Be Skeptical Of

- generic AI benchmark dashboards that only compare capability scores
- generic fact-checking tools with no product fit to launch disclosures
- one-off journalism pieces criticizing a specific announcement without a reusable methodology
- startup marketing pages that overclaim fact-checking capability without clear evidence workflows

## Research Guardrails

- Prefer primary sources and official docs when possible.
- For products, find pricing, API, or workflow details rather than relying only on home-page claims.
- Distinguish carefully between:
  - capability benchmarking
  - transparency benchmarking
  - claim detection / fact checking
  - documentation tooling
- If no direct analogue exists, say that explicitly rather than forcing a comparison.
