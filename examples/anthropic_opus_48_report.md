# CappinCheck Report: Anthropic Claude Opus 4.8

Source: `https://www.anthropic.com/news/claude-opus-4-8`

## Provenance

- Mode: `curated_manual`
- Model: `none`
- Evidence Contrast: `enabled`
- Provided reference URLs: `https://www.anthropic.com/claude-opus-4-8-system-card`, `https://www.anthropic.com/news/claude-opus-4-8`, `https://platform.claude.com/docs/en/about-claude/models/overview`, `https://claude.com/pricing#api`, `https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy`

## Scorecard

- Claims audited: `6`
- Verdict counts: `supported=2` · `overstated=0` · `missing_context=3` · `contradicted=0` · `not_checkable=1`
- Average stretch score: `46/100`
- Provided reference URL count: `5`

| Claim | Formal Verdict | Confidence | Stretch Score |
| --- | --- | --- | ---: |
| It builds on Opus 4.7 with improvements across benchmarks, and is a more effective collaborator. | missing_context | high | 57 |
| Early testers have found Claude Opus 4.8 to be more reliable and sharper in its judgement when it’s performing agentic tasks. | missing_context | high | 63 |
| On our Super-Agent benchmark, Claude Opus 4.8 is the only model to complete every case end-to-end, beating prior Opus models and GPT-5.5 at parity on cost. | not_checkable | medium | 74 |
| This is borne out in our evaluations, which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked. | missing_context | high | 49 |
| The assessment also showed Opus 4.8 to have rates of misaligned behavior (such as deception or cooperation with misuse) that are substantially lower than Opus 4.7, and similar to our best-aligned model, Claude Mythos Preview. | supported | high | 24 |
| Claude Opus 4.8 is available everywhere today. Pricing for regular usage is unchanged from Opus 4.7: $5 per million input tokens and $25 per million output tokens. Pricing for fast mode is $10 per million input tokens and $50 per million output tokens. Developers can use claude-opus-4-8 via the Claude API. | supported | high | 10 |

## claim_benchmark_collaboration: missing_context

**Confidence:** high

**Original:** It builds on Opus 4.7 with improvements across benchmarks, and is a more effective collaborator.

**Stretch Score:** 57/100

**Why:** The launch and system card support meaningful benchmark improvements, but "more effective collaborator" is a broader qualitative framing than the public materials measure directly.

**Defensible rewrite:** It builds on Opus 4.7 with stronger results on several published evaluations and a launch narrative centered on improved collaboration.

### Agent Steps

<details><summary>manual-curation: Reviewed the launch headline against Anthropic's Opus 4.8 system card and developer model overview.</summary>

**Supporting evidence:**
- Anthropic's most capable model for complex reasoning and high-autonomy work. ([Models overview - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/overview)). Relevance: Developer-doc positioning.

**Contradictions / narrowing evidence:**
- Anthropic itself calls the upgrade modest but tangible later in the launch. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Narrows the top-line framing.

**Missing context:**
- The collaboration claim is qualitative rather than directly benchmarked.

</details>

### Evidence Contrast

**Claim says:** It builds on Opus 4.7 with improvements across benchmarks, and is a more effective collaborator.

**Best reference says:** The system card reports broad capability sections across coding, reasoning, multimodal, and professional tasks and describes Opus 4.8 as an improvement over Opus 4.7 on many measures.

**Key qualification:** The public materials support benchmark gains, but not a single quantified collaborator score.

**Delta:** missing_context — The public sources support benchmark gains, but the broader collaborator framing is qualitative and not directly measured.

**Final verdict:** missing_context

**Defensible rewrite:** It builds on Opus 4.7 with stronger results on several published evaluations and a launch narrative centered on improved collaboration.

### Claim-Level Contrast References

- Claude Opus 4.8 System Card - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/claude-opus-4-8-system-card. Primary capability and safety evaluation reference.
- Models overview - Claude API Docs (official_doc, authority 90/100): https://platform.claude.com/docs/en/about-claude/models/overview. Developer-facing model positioning and comparison table.

**Reference snippets / mismatches:**
- The system card reports broad capability sections across coding, reasoning, multimodal, and professional tasks and describes Opus 4.8 as an improvement over Opus 4.7 on many measures. (Claude Opus 4.8 System Card - Anthropic, supports, https://www.anthropic.com/claude-opus-4-8-system-card). The public materials support benchmark gains, but not a single quantified collaborator score.
- Later in the launch Anthropic calls Opus 4.8 a modest but tangible improvement on its predecessor. (Introducing Claude Opus 4.8 - Anthropic, narrows, https://www.anthropic.com/news/claude-opus-4-8). That wording is narrower than the opening claim.

**Gemini-discovered supporting sources:**
- Anthropic positions Opus 4.8 as an upgrade over Opus 4.7 with benchmark gains and collaboration improvements. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Primary launch framing for the benchmark and collaboration claim.
- Anthropic documents Opus 4.8 as its most capable model for complex reasoning, long-horizon agentic coding, and high-autonomy work. ([Models overview - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/overview)). Relevance: Shows how Anthropic positions the model in developer-facing docs.

**Gemini-discovered caveat / counter sources:**
- Anthropic later describes Opus 4.8 as a modest but tangible improvement on its predecessor rather than a wholesale leap. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Narrows the breadth of the opening headline.

**Missing context:**
- The public materials do not define a single collaboration metric or a benchmark summary score that directly maps to "more effective collaborator."
- Benchmark gains are distributed across many tasks rather than expressed as a single across-the-board improvement.


## claim_agentic_reliability: missing_context

**Confidence:** high

**Original:** Early testers have found Claude Opus 4.8 to be more reliable and sharper in its judgement when it’s performing agentic tasks.

**Stretch Score:** 63/100

**Why:** The launch offers consistent positive tester quotes, but it does not publish a standardized operational reliability rate, intervention threshold, or failure distribution for agentic tasks.

**Defensible rewrite:** Early testers report that Claude Opus 4.8 feels more reliable and sharper in judgment on agentic tasks, though the launch does not publish standardized reliability rates or intervention thresholds.

### Agent Steps

<details><summary>manual-curation: Compared the early-tester reliability framing to the launch evidence and the Opus 4.8 system card.</summary>

**Supporting evidence:**
- The system card reports improved honesty in agentic settings and lower rates of some misaligned actions. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Supports the direction of the claim.

**Missing context:**
- No public operational reliability rate or intervention policy is provided.

</details>

### Evidence Contrast

**Claim says:** Early testers have found Claude Opus 4.8 to be more reliable and sharper in its judgement when it’s performing agentic tasks.

**Best reference says:** The system card describes broad improvements in honesty and alignment behavior, but it does not present one standardized reliability rate for agentic tasks.

**Key qualification:** The evidence is directional rather than a single operational benchmark for reliability.

**Delta:** missing_context — The launch uses strong reliability language, but the public materials do not publish a standardized agentic reliability metric or supervision policy.

**Final verdict:** missing_context

**Defensible rewrite:** Early testers report that Claude Opus 4.8 feels more reliable and sharper in judgment on agentic tasks, though the launch does not publish standardized reliability rates or intervention thresholds.

### Claim-Level Contrast References

- Claude Opus 4.8 System Card - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/claude-opus-4-8-system-card. Primary evaluation reference for agentic behavior and alignment outcomes.
- Introducing Claude Opus 4.8 - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/news/claude-opus-4-8. Contains the testimonial-driven reliability framing.

**Reference snippets / mismatches:**
- The system card describes broad improvements in honesty and alignment behavior, but it does not present one standardized reliability rate for agentic tasks. (Claude Opus 4.8 System Card - Anthropic, narrows, https://www.anthropic.com/claude-opus-4-8-system-card). The evidence is directional rather than a single operational benchmark for reliability.

**Gemini-discovered supporting sources:**
- The launch introduces a section of tester quotes describing sharper judgment and reliability on agentic work. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Primary source for the early-tester framing.
- The system card reports improvements on many alignment and capability measures and notes improved honesty in agentic settings. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Directionally supports better model behavior on long-horizon tasks.

**Gemini-discovered caveat / counter sources:**
- The launch surfaces testimonials and benchmark snapshots, but not a single published reliability rate for production agentic workflows. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Shows the evidence gap behind the reliability phrasing.

**Missing context:**
- No standardized public success-rate threshold is attached to the claim.
- The launch does not say how much human supervision or intervention the quoted workflows required.


## claim_super_agent_quote: not_checkable

**Confidence:** medium

**Original:** On our Super-Agent benchmark, Claude Opus 4.8 is the only model to complete every case end-to-end, beating prior Opus models and GPT-5.5 at parity on cost.

**Stretch Score:** 74/100

**Why:** The launch quote is concrete, but the public materials reviewed here do not disclose enough methodology, scoring details, or cost accounting to independently verify the result.

**Defensible rewrite:** Anthropic quotes an early tester saying Opus 4.8 completed every case end-to-end on that internal Super-Agent benchmark and matched GPT-5.5 at comparable cost, but the public launch does not disclose enough methodology to independently verify the claim.

### Agent Steps

<details><summary>manual-curation: Treated the partner benchmark quote as a separate audit target and checked whether the reviewed public materials make it independently verifiable.</summary>

**Supporting evidence:**
- The claim appears verbatim in the launch as a customer benchmark statement. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Shows the source of the benchmark quote.

**Contradictions / narrowing evidence:**
- The reviewed public packet does not surface a matching public methodology for this exact quote. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Explains the independent-verification gap.

</details>

### Evidence Contrast

**Claim says:** On our Super-Agent benchmark, Claude Opus 4.8 is the only model to complete every case end-to-end, beating prior Opus models and GPT-5.5 at parity on cost.

**Best reference says:** The claim is presented as an early tester quote, not as a benchmark result fully unpacked in the launch itself.

**Key qualification:** The quote is real, but the methodology remains opaque.

**Delta:** not_checkable — The quote may be directionally accurate, but the reviewed public materials do not expose enough benchmark and cost methodology to verify it independently.

**Final verdict:** not_checkable

**Defensible rewrite:** Anthropic quotes an early tester saying Opus 4.8 completed every case end-to-end on that internal Super-Agent benchmark and matched GPT-5.5 at comparable cost, but the public launch does not disclose enough methodology to independently verify the claim.

### Claim-Level Contrast References

- Introducing Claude Opus 4.8 - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/news/claude-opus-4-8. Contains the customer benchmark quote as published.
- Claude Opus 4.8 System Card - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/claude-opus-4-8-system-card. Public evaluation packet reviewed for verification.
- Plans & Pricing - Claude by Anthropic (official_doc, authority 90/100): https://claude.com/pricing#api. Relevant to the cost-comparison part of the quote.

**Reference snippets / mismatches:**
- The claim is presented as an early tester quote, not as a benchmark result fully unpacked in the launch itself. (Introducing Claude Opus 4.8 - Anthropic, supports, https://www.anthropic.com/news/claude-opus-4-8). The quote is real, but the methodology remains opaque.
- The public evaluation packet reviewed here does not provide enough methodological detail to independently validate the specific Super-Agent result and parity-on-cost comparison. (Claude Opus 4.8 System Card - Anthropic, narrows, https://www.anthropic.com/claude-opus-4-8-system-card). Independent verification is limited by missing benchmark-method detail.

**Gemini-discovered supporting sources:**
- The Super-Agent result appears as a customer quote inside the launch page. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Primary source for the quoted benchmark claim.

**Gemini-discovered caveat / counter sources:**
- The public system card covers many benchmark families, but the launch quote does not come with a public methodology packet here for the quoted Super-Agent result. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Why the claim is not independently checkable from the reviewed public packet.

**Missing context:**
- The public launch does not disclose the full Super-Agent benchmark methodology or dataset.
- The cost-comparison method behind the GPT-5.5 parity claim is not public in the reviewed materials.


## claim_honesty_flawed_code: missing_context

**Confidence:** high

**Original:** This is borne out in our evaluations, which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked.

**Stretch Score:** 49/100

**Why:** The reviewed public materials clearly support a strong directional improvement in honesty around reporting flawed code, but they surface that directional result more clearly than the exact four-times ratio.

**Defensible rewrite:** Anthropic’s evaluations indicate that Opus 4.8 is materially less likely than prior Opus models to leave flawed code unflagged, though the public materials here emphasize the directional improvement more clearly than the exact ratio.

### Agent Steps

<details><summary>manual-curation: Compared the launch's exact honesty ratio to the system-card summary language about failing to report flawed code.</summary>

**Supporting evidence:**
- The system card describes markedly improved honesty in agentic settings and a much lower tendency to miss flawed code. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Directional support for the claim.

**Contradictions / narrowing evidence:**
- The card also flags evaluation-awareness trends worth monitoring. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Why the exact ratio deserves caveat.

**Computed checks:**
- Public supporting material reviewed here clearly supports the direction of the improvement; the exact ratio is less directly surfaced.

</details>

### Evidence Contrast

**Claim says:** This is borne out in our evaluations, which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked.

**Best reference says:** The system card says honesty in agentic settings is markedly improved and that Opus 4.8 is much less likely than prior models to fail to report flawed code.

**Key qualification:** The direction is clear, but the exact ratio is less front-and-center in the reviewed supporting material.

**Delta:** missing_context — The public evidence reviewed here strongly supports the direction of the honesty improvement, but the exact ratio and its evaluation context still need caveat.

**Final verdict:** missing_context

**Defensible rewrite:** Anthropic’s evaluations indicate that Opus 4.8 is materially less likely than prior Opus models to leave flawed code unflagged, though the public materials here emphasize the directional improvement more clearly than the exact ratio.

### Claim-Level Contrast References

- Claude Opus 4.8 System Card - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/claude-opus-4-8-system-card. Primary evidence packet for honesty and alignment evaluations.
- Introducing Claude Opus 4.8 - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/news/claude-opus-4-8. Contains the exact ratio language.

**Reference snippets / mismatches:**
- The system card says honesty in agentic settings is markedly improved and that Opus 4.8 is much less likely than prior models to fail to report flawed code. (Claude Opus 4.8 System Card - Anthropic, narrows, https://www.anthropic.com/claude-opus-4-8-system-card). The direction is clear, but the exact ratio is less front-and-center in the reviewed supporting material.
- The same section notes hints of evaluation awareness that Anthropic considers worth watching. (Claude Opus 4.8 System Card - Anthropic, narrows, https://www.anthropic.com/claude-opus-4-8-system-card). That caveat belongs alongside the headline honesty claim.

**Computed checks:**
- Launch claim uses a relative ratio (around 4x); the supporting system-card language reviewed here is stronger on direction than on the exact multiple.

**Gemini-discovered supporting sources:**
- The launch says Anthropic's evaluations show Opus 4.8 is around four times less likely than its predecessor to let flawed code pass unremarked. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Primary source for the exact claim.
- The system card says honesty in agentic settings is markedly improved and that Opus 4.8 has a much lower tendency than previous models to fail to report flawed code. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Supports the direction of the honesty improvement.

**Gemini-discovered caveat / counter sources:**
- The same system card notes hints of evaluation awareness and treats them as trends worth watching. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: A relevant caveat on how these evaluation results should be read.

**Missing context:**
- The public materials reviewed here make the direction of the improvement clearer than the exact four-times ratio.
- The launch does not spell out the exact evaluation setup in the same paragraph as the headline honesty claim.


## claim_alignment_assessment: supported

**Confidence:** high

**Original:** The assessment also showed Opus 4.8 to have rates of misaligned behavior (such as deception or cooperation with misuse) that are substantially lower than Opus 4.7, and similar to our best-aligned model, Claude Mythos Preview.

**Stretch Score:** 24/100

**Why:** The reviewed system-card summary directly says Opus 4.8 shows a large improvement over Opus 4.7 on susceptibility to misuse and misaligned actions and brings the model broadly in line with Mythos Preview on these measures.

**Defensible rewrite:** The system card says Opus 4.8 shows substantially lower rates of several misaligned behaviors than Opus 4.7 and is broadly in line with Claude Mythos Preview on Anthropic’s primary behavioral evaluations.

### Agent Steps

<details><summary>manual-curation: Checked the launch's alignment comparison against the corresponding system-card summary language.</summary>

**Supporting evidence:**
- System-card summary language closely matches the launch comparison. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Direct support.

</details>

### Evidence Contrast

**Claim says:** The assessment also showed Opus 4.8 to have rates of misaligned behavior (such as deception or cooperation with misuse) that are substantially lower than Opus 4.7, and similar to our best-aligned model, Claude Mythos Preview.

**Best reference says:** The system-card summary says Opus 4.8 shows a large improvement over Opus 4.7 on susceptibility to misuse and misaligned actions and is broadly in line with Mythos Preview.

**Key qualification:** The launch claim is closely aligned to the reviewed supporting source.

**Delta:** same — The reviewed system-card summary materially supports the comparative alignment claim as written.

**Final verdict:** supported

**Defensible rewrite:** The system card says Opus 4.8 shows substantially lower rates of several misaligned behaviors than Opus 4.7 and is broadly in line with Claude Mythos Preview on Anthropic’s primary behavioral evaluations.

### Claim-Level Contrast References

- Claude Opus 4.8 System Card - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/claude-opus-4-8-system-card. Primary alignment and safety evidence packet.
- Announcing our updated Responsible Scaling Policy - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy. Safety-governance context for Anthropic's release process.

**Reference snippets / mismatches:**
- The system-card summary says Opus 4.8 shows a large improvement over Opus 4.7 on susceptibility to misuse and misaligned actions and is broadly in line with Mythos Preview. (Claude Opus 4.8 System Card - Anthropic, supports, https://www.anthropic.com/claude-opus-4-8-system-card). The launch claim is closely aligned to the reviewed supporting source.

**Gemini-discovered supporting sources:**
- The system card says Opus 4.8 reaches new highs on prosocial traits and shows a large improvement over Opus 4.7 on susceptibility to misuse and misaligned actions, broadly in line with Mythos Preview. ([Claude Opus 4.8 System Card - Anthropic](https://www.anthropic.com/claude-opus-4-8-system-card)). Relevance: Direct support for the launch's alignment comparison.
- The launch explicitly points readers to the Opus 4.8 system card for the full alignment assessment and safety tests. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Connects the claim to the underlying evaluation packet.


## claim_availability_pricing: supported

**Confidence:** high

**Original:** Claude Opus 4.8 is available everywhere today. Pricing for regular usage is unchanged from Opus 4.7: $5 per million input tokens and $25 per million output tokens. Pricing for fast mode is $10 per million input tokens and $50 per million output tokens. Developers can use claude-opus-4-8 via the Claude API.

**Stretch Score:** 10/100

**Why:** The launch, models overview, and pricing materials reviewed here align on the API name and the regular/fast mode price structure for Opus 4.8.

**Defensible rewrite:** Claude Opus 4.8 is available through Anthropic’s surfaces and cloud partners, with regular usage priced at $5 per million input tokens and $25 per million output tokens, and fast mode at $10 and $50 respectively.

### Agent Steps

<details><summary>manual-curation: Checked Anthropic's launch availability paragraph against the current model-overview and pricing docs.</summary>

**Supporting evidence:**
- Model overview lists Claude Opus 4.8 and the standard API pricing. ([Models overview - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/overview)). Relevance: Docs confirmation.
- Pricing page describes fast mode at 2x standard pricing for Opus 4.8. ([Plans & Pricing - Claude by Anthropic](https://claude.com/pricing#api)). Relevance: Pricing confirmation.

**Computed checks:**
- The launch pricing block matches the reviewed docs for standard and fast mode pricing.

</details>

### Evidence Contrast

**Claim says:** Claude Opus 4.8 is available everywhere today. Pricing for regular usage is unchanged from Opus 4.7: $5 per million input tokens and $25 per million output tokens. Pricing for fast mode is $10 per million input tokens and $50 per million output tokens. Developers can use claude-opus-4-8 via the Claude API.

**Best reference says:** The models overview lists Claude Opus 4.8 with the claude-opus-4-8 API alias and a $5 input / $25 output pricing row.

**Key qualification:** Direct support for the standard pricing and API identifier.

**Delta:** same — The reviewed docs support the availability, API identifier, and price structure described in the launch.

**Final verdict:** supported

**Defensible rewrite:** Claude Opus 4.8 is available through Anthropic’s surfaces and cloud partners, with regular usage priced at $5 per million input tokens and $25 per million output tokens, and fast mode at $10 and $50 respectively.

### Claim-Level Contrast References

- Models overview - Claude API Docs (official_doc, authority 90/100): https://platform.claude.com/docs/en/about-claude/models/overview. Lists the model IDs, pricing, and context window for Claude Opus 4.8.
- Plans & Pricing - Claude by Anthropic (official_doc, authority 90/100): https://claude.com/pricing#api. Current pricing page for standard and fast mode.
- Introducing Claude Opus 4.8 - Anthropic (vendor_doc, authority 90/100): https://www.anthropic.com/news/claude-opus-4-8. Launch availability paragraph and model identifier.

**Reference snippets / mismatches:**
- The models overview lists Claude Opus 4.8 with the claude-opus-4-8 API alias and a $5 input / $25 output pricing row. (Models overview - Claude API Docs, supports, https://platform.claude.com/docs/en/about-claude/models/overview). Direct support for the standard pricing and API identifier.
- Anthropic’s pricing page describes fast mode for Opus 4.8 at 2x standard pricing. (Plans & Pricing - Claude by Anthropic, supports, https://claude.com/pricing#api). Supports the fast-mode prices stated in the launch.

**Computed checks:**
- Regular usage: $5/M input and $25/M output. Fast mode: $10/M input and $50/M output. Claude API identifier: claude-opus-4-8.

**Gemini-discovered supporting sources:**
- The availability section says Opus 4.8 is available everywhere today and gives the regular and fast-mode prices plus the Claude API model name. ([Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)). Relevance: Primary source for the launch availability block.
- Anthropic's models overview lists Claude Opus 4.8, the claude-opus-4-8 API alias, and the $5 input / $25 output pricing. ([Models overview - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/overview)). Relevance: Developer-doc confirmation of model name and base pricing.
- Anthropic's pricing page describes Opus 4.8 pricing, fast mode at 2x standard pricing, and related prompt-caching / batch details. ([Plans & Pricing - Claude by Anthropic](https://claude.com/pricing#api)). Relevance: Supports the pricing structure beyond the launch post.

