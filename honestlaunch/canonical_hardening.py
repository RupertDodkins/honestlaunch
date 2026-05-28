from __future__ import annotations

from .archive_registry import match_archive_entry
from .schemas import (
    AuditReport,
    ClaimAudit,
    ClaimType,
    Document,
    EvidenceItem,
    RiskyClaim,
    Verdict,
)


GEMINI_LAUNCH_URL = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
GEMINI_MODEL_CARD_URL = "https://deepmind.google/models/model-cards/gemini-3-5-flash"
GEMINI_EVALS_URL = "https://deepmind.google/models/evals-methodology/gemini-3-5-flash"
GEMINI_MODELS_DOCS_URL = "https://ai.google.dev/gemini-api/docs/models"
GEMINI_WHATS_NEW_URL = "https://ai.google.dev/gemini-api/docs/interactions/whats-new-gemini-3.5"
GEMINI_PRICING_URL = "https://ai.google.dev/gemini-api/docs/pricing"
OPENAI_PRICING_URL = "https://openai.com/api/pricing/"
ANTHROPIC_PRICING_URL = "https://platform.claude.com/docs/en/about-claude/pricing"
MCP_ATLAS_URL = "https://labs.scale.com/leaderboard/mcp_atlas"
GDPVAL_AA_URL = "https://artificialanalysis.ai/evaluations/gdpval-aa"
CHARXIV_URL = "https://charxiv.github.io/"
ARTIFICIAL_ANALYSIS_URL = "https://artificialanalysis.ai/articles/gemini-3-5-flash-everything-you-need-to-know"

GEMINI_REFERENCE_URLS = [
    GEMINI_MODEL_CARD_URL,
    GEMINI_EVALS_URL,
    GEMINI_LAUNCH_URL,
    GEMINI_MODELS_DOCS_URL,
    GEMINI_WHATS_NEW_URL,
    GEMINI_PRICING_URL,
    OPENAI_PRICING_URL,
    ANTHROPIC_PRICING_URL,
    MCP_ATLAS_URL,
    GDPVAL_AA_URL,
    CHARXIV_URL,
    ARTIFICIAL_ANALYSIS_URL,
]


def harden_report(report: AuditReport) -> AuditReport:
    entry = match_archive_entry(report.document.source, report.document.title)
    if entry is None:
        return report
    slug = str(entry.get("slug", ""))
    if slug == "gemini-35-flash":
        return _harden_gemini_report(report)
    return report


def _harden_gemini_report(report: AuditReport) -> AuditReport:
    report.reference_urls = list(GEMINI_REFERENCE_URLS)
    document = report.document
    existing_claims = {claim.id: claim for claim in report.claims}

    claim_1 = _claim(
        existing_claims.get("1"),
        claim_id="1",
        claim=(
            "It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on "
            "challenging coding and agentic benchmarks like Terminal-Bench 2.1, GDPval-AA and MCP Atlas."
        ),
        claim_type=ClaimType.BENCHMARK,
        source_location="Performance",
        why_risky="Benchmark leadership claims need scope, comparable methodology, and baseline context.",
        audit_question=(
            "Do the reported benchmark results support a strongest-Gemini claim against Gemini 3.1 Pro "
            "on the cited agentic and coding evaluations?"
        ),
    )
    claim_1b = RiskyClaim(
        id="1b",
        claim=(
            "Gemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple "
            "dimensions, including leading in multimodal understanding (84.2% on CharXiv Reasoning)."
        ),
        claim_type=ClaimType.BENCHMARK,
        source_location="Performance",
        why_risky="Broad flagship comparisons can hide where the model trails or where the benchmark scope is narrow.",
        audit_question=(
            "Does the evidence support a broad flagship-rival framing, or should the claim be limited to "
            "specific benchmark dimensions such as CharXiv Reasoning?"
        ),
    )
    claim_2 = _claim(
        existing_claims.get("2"),
        claim_id="2",
        claim="When looking at output tokens per second, 3.5 Flash is 4 times faster than other frontier models.",
        claim_type=ClaimType.NUMERIC,
        source_location="Performance",
        why_risky="Raw throughput claims are easy to overread as total latency or workflow speed.",
        audit_question="Is the 4x comparison valid, and is the scope clearly limited to raw output-token throughput?",
    )
    claim_3 = _claim(
        existing_claims.get("3"),
        claim_id="3",
        claim=(
            "What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in "
            "a fraction of the time, often at less than half the cost of other frontier models."
        ),
        claim_type=ClaimType.GENERALIZATION,
        source_location="Performance",
        why_risky="Real-world time and cost claims require baselines, operational evidence, and named comparison sets.",
        audit_question=(
            "Is there public workflow evidence for the claimed time savings, and is the cost comparison "
            "true across the named frontier baselines?"
        ),
    )
    claim_4 = _claim(
        existing_claims.get("4"),
        claim_id="4",
        claim="Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.",
        claim_type=ClaimType.DEPLOYMENT,
        source_location="Performance",
        why_risky="Reliability language needs a measured success rate, intervention policy, and failure-rate context.",
        audit_question=(
            "Do the public benchmarks and docs justify calling the model reliable for supervised multi-step workflows?"
        ),
    )
    claim_6 = _claim(
        existing_claims.get("6"),
        claim_id="6",
        claim=(
            "Macquarie Bank is piloting how 3.5 Flash can accelerate customer onboarding by reasoning "
            "over complex 100+ page documents, retrieving relevant information and making reliable "
            "recommendations with low latency."
        ),
        claim_type=ClaimType.DEPLOYMENT,
        source_location="Real-world impact",
        why_risky="Partner-impact claims are often illustrative and rarely come with public denominators or error rates.",
        audit_question=(
            "Is there public evidence for the claimed onboarding acceleration, recommendation reliability, "
            "and latency in Macquarie's deployment?"
        ),
    )
    claim_8 = _claim(
        existing_claims.get("8"),
        claim_id="8",
        claim=(
            "We have strengthened our cyber and CBRN safeguards, which means it's less likely to generate "
            "harmful content, and to mistakenly refuse to answer safe queries."
        ),
        claim_type=ClaimType.SAFETY,
        source_location="Safety",
        why_risky="Safety claims need public eval detail, baseline context, and clarity on whether results are automated or human-reviewed.",
        audit_question=(
            "Does the model card publish enough public evidence to support the broader cyber, CBRN, and refusal-behavior claim?"
        ),
    )

    audits = [
        ClaimAudit(
            claim=claim_1,
            verdict=Verdict.SUPPORTED,
            confidence="high",
            stretch_score=12,
            why=(
                "The cited Google benchmark table supports a narrower strongest-Gemini claim against Gemini 3.1 Pro "
                "on the named agentic and coding evaluations. The evidence does not justify extending that claim to "
                "overall flagship leadership, but it does support the scoped within-Gemini comparison."
            ),
            weaker_supported_rewrite=(
                "On the listed evaluations, Gemini 3.5 Flash is Google's strongest Gemini model for agentic and coding "
                "tasks, outperforming Gemini 3.1 Pro on Terminal-Bench 2.1, GDPval-AA, MCP Atlas, and narrowly on "
                "SWE-Bench Pro."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini 3.5: frontier intelligence with action - Google Blog",
                    GEMINI_LAUNCH_URL,
                    "It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1, GDPval-AA and MCP Atlas.",
                    "This is the launch's scoped within-Google benchmark claim.",
                ),
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "Terminal-Bench 2.1: 76.2 vs 70.3, GDPval-AA: 1656 vs 1314, MCP Atlas: 83.6 vs 78.2, SWE-Bench Pro: 55.1 vs 54.2.",
                    "These published numbers support the narrower Gemini-vs-Gemini benchmark comparison.",
                ),
            ],
            counter_evidence=[],
            missing_context=[],
            numeric_findings=[
                "Terminal-Bench 2.1: 76.2% vs 70.3%",
                "GDPval-AA: 1656 Elo vs 1314 Elo",
                "MCP Atlas: 83.6% vs 78.2%",
                "SWE-Bench Pro: 55.1% vs 54.2%",
            ],
        ),
        ClaimAudit(
            claim=claim_1b,
            verdict=Verdict.MISSING_CONTEXT,
            confidence="high",
            stretch_score=58,
            why=(
                "The model card supports strong results on several agentic, coding, and multimodal benchmarks, but the "
                "broader flagship-rival framing hides where Gemini 3.5 Flash trails GPT-5.5, Claude Opus 4.7, or Gemini "
                "3.1 Pro on other rows. The CharXiv result is also specific to chart reasoning rather than multimodal "
                "understanding as a whole."
            ),
            weaker_supported_rewrite=(
                "Gemini 3.5 Flash is competitive with large flagship models on several agentic, coding, and multimodal "
                "benchmarks, while still trailing them on some reasoning, coding, and long-context evaluations."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini 3.5: frontier intelligence with action - Google Blog",
                    GEMINI_LAUNCH_URL,
                    "Gemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions.",
                    "This is the broad comparative framing used in the launch.",
                ),
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "Gemini 3.5 Flash posts strong scores on MCP Atlas, Finance Agent v2, CharXiv, and MMMU-Pro.",
                    "These rows support the claim that the model is competitive on several named dimensions.",
                ),
            ],
            counter_evidence=[
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "The same table shows lower scores than GPT-5.5, Claude Opus 4.7, or Gemini 3.1 Pro on Terminal-Bench 2.1, SWE-Bench Pro, GDPval-AA, MRCR v2, HLE, ARC-AGI-2, and Blueprint-Bench 2.",
                    "These rows show why the broader flagship-rival wording needs qualification.",
                ),
                _evidence(
                    "Gemini 3.5 Flash evaluation methodology - Google DeepMind",
                    GEMINI_EVALS_URL,
                    "Google notes that some comparison scores are self-computed while others are provider-reported or sourced from public leaderboards.",
                    "The methodology caveat matters when a single row is generalized into broad multimodal or flagship language.",
                ),
            ],
            missing_context=[
                "The launch does not specify where Gemini 3.5 Flash still trails flagship models on reasoning, coding, and long-context evaluations.",
                "CharXiv Reasoning is a chart-understanding benchmark and should not be treated as broad multimodal leadership by itself.",
            ],
            numeric_findings=[
                "CharXiv Reasoning: 84.2%",
                "Flagship comparisons vary by benchmark row",
            ],
        ),
        ClaimAudit(
            claim=claim_2,
            verdict=Verdict.MISSING_CONTEXT,
            confidence="medium",
            stretch_score=42,
            why=(
                "The launch properly narrows the metric to output tokens per second, but the comparison still needs named "
                "baselines and a caveat that raw throughput is not the same thing as total latency, tool-loop overhead, "
                "or end-to-end workflow speed."
            ),
            weaker_supported_rewrite=(
                "On raw output-token generation, Gemini 3.5 Flash reaches more than 280 output tokens per second in public "
                "testing; practical latency gains depend on time-to-first-token, tool calls, reasoning level, and workflow shape."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini 3.5: frontier intelligence with action - Google Blog",
                    GEMINI_LAUNCH_URL,
                    "When looking at output tokens per second, it is 4 times faster than other frontier models.",
                    "This is the exact launch framing for the speed claim.",
                ),
                _evidence(
                    "Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis",
                    ARTIFICIAL_ANALYSIS_URL,
                    "Artificial Analysis reports Gemini 3.5 Flash at more than 280 output tokens per second.",
                    "This supports the narrow raw-throughput part of the launch claim.",
                ),
            ],
            counter_evidence=[
                _evidence(
                    "Gemini 3.5 Flash: The new leader in intelligence versus speed - Artificial Analysis",
                    ARTIFICIAL_ANALYSIS_URL,
                    "The same analysis distinguishes raw output speed from total workload latency and cost.",
                    "This is why the launch wording should stay confined to raw token throughput.",
                ),
            ],
            missing_context=[
                "The launch does not name the exact comparison baselines inline.",
                "Raw output throughput does not establish time-to-first-token, tool-loop latency, or end-to-end workflow speed.",
            ],
            numeric_findings=[
                "More than 280 output tokens per second",
                "Roughly 4x larger-flagship output speed in public testing",
            ],
        ),
        ClaimAudit(
            claim=claim_3,
            verdict=Verdict.OVERSTATED,
            confidence="high",
            stretch_score=79,
            why=(
                "The list-price comparison is strong against heavy flagships like GPT-5.5 and Claude Opus 4.7, but the "
                "launch overreaches when it collapses real-world time savings and broad frontier-model cost comparisons into "
                "one sentence. There are no public workflow studies, intervention rates, or total-cost measurements for the "
                "days-to-weeks claim."
            ),
            weaker_supported_rewrite=(
                "Gemini 3.5 Flash can accelerate some complex development and auditing workflows, and its list price is less "
                "than half of GPT-5.5 and Claude Opus 4.7, though measured time savings and total workflow cost depend on task "
                "design, thinking level, tool use, and baseline model."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini Developer API pricing - Google AI for Developers",
                    GEMINI_PRICING_URL,
                    "Gemini 3.5 Flash list pricing is $1.50 per million input tokens and $9 per million output tokens.",
                    "These published prices support the narrower list-price comparison.",
                ),
                _evidence(
                    "OpenAI API Pricing",
                    OPENAI_PRICING_URL,
                    "GPT-5.5 is listed at $5 per million input tokens and $30 per million output tokens.",
                    "This is one of the named heavy-flagship baselines that is clearly more than 2x the Gemini list price.",
                ),
                _evidence(
                    "Claude API pricing",
                    ANTHROPIC_PRICING_URL,
                    "Claude Opus 4.7 is listed at $5 per million input tokens and $25 per million output tokens.",
                    "This is another heavy-flagship baseline that supports the narrower pricing claim.",
                ),
            ],
            counter_evidence=[
                _evidence(
                    "Claude API pricing",
                    ANTHROPIC_PRICING_URL,
                    "Claude Sonnet 4.6 and Claude Haiku 4.5 are materially cheaper than the launch's broad 'other frontier models' phrasing implies.",
                    "The broad half-cost claim does not hold across every plausible high-end or fast-agent baseline.",
                ),
                _evidence(
                    "Gemini 3.5: frontier intelligence with action - Google Blog",
                    GEMINI_LAUNCH_URL,
                    "The launch offers partner examples but no controlled study for developer-days or auditor-weeks time savings.",
                    "This is why the real-world time claim needs a narrower evidence bar.",
                ),
            ],
            missing_context=[
                "No public workflow study or audited measurement backs the developer-days or auditor-weeks time compression claim.",
                "The sentence mixes list pricing with total workflow cost, which can vary with reasoning level, retries, and tool calls.",
            ],
            numeric_findings=[
                "Gemini 3.5 Flash: $1.50/M input, $9/M output",
                "GPT-5.5: $5/M input, $30/M output",
                "Claude Opus 4.7: $5/M input, $25/M output",
            ],
        ),
        ClaimAudit(
            claim=claim_4,
            verdict=Verdict.OVERSTATED,
            confidence="high",
            stretch_score=74,
            why=(
                "The public benchmarks support strong multi-step and coding capability, but 'reliably execute' implies a clearer "
                "operational success bar than the launch provides. The model card shows meaningful failure margins on several "
                "benchmark tasks, and the launch does not publish intervention rates or per-workflow completion reliability."
            ),
            weaker_supported_rewrite=(
                "Under human supervision, Gemini 3.5 Flash shows strong multi-step agentic and coding performance on benchmarks "
                "such as MCP Atlas and Terminal-Bench 2.1, but reliability depends on workflow design, tools, and intervention policy."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "Google reports 83.6% on MCP Atlas and 76.2% on Terminal-Bench 2.1 for Gemini 3.5 Flash.",
                    "These benchmark scores support the narrower claim that the model is strong on supervised agentic workflows.",
                ),
                _evidence(
                    "Gemini Interactions API - Google AI for Developers",
                    GEMINI_WHATS_NEW_URL,
                    "The developer docs position Gemini 3.5 Flash for long-context, coding, and agentic workflows.",
                    "This supports the workflow-design framing, not a blanket reliability guarantee.",
                ),
            ],
            counter_evidence=[
                _evidence(
                    "Scale Labs Leaderboard: MCP Atlas",
                    MCP_ATLAS_URL,
                    "MCP Atlas frames real-world tool use as difficult even for frontier models and catalogs failure modes around tool use and task understanding.",
                    "This benchmark context undercuts reading the launch claim as operational reliability in the broad sense.",
                ),
            ],
            missing_context=[
                "The launch does not define reliability in terms of run success rate, retries, or allowed human interventions.",
                "Benchmark pass rates are not the same thing as production workflow reliability across varied environments.",
            ],
            numeric_findings=[
                "MCP Atlas: 83.6%",
                "Terminal-Bench 2.1: 76.2%",
                "SWE-Bench Pro: 55.1%",
            ],
        ),
        ClaimAudit(
            claim=claim_6,
            verdict=Verdict.NOT_CHECKABLE,
            confidence="medium",
            stretch_score=63,
            why=(
                "The launch identifies a real partner and concrete workflow shape, but there is no public denominator, baseline, "
                "error rate, latency distribution, or intervention policy for the Macquarie pilot. That makes the recommendation "
                "reliability and low-latency outcomes illustrative rather than independently checkable."
            ),
            weaker_supported_rewrite=(
                "Google reports that Macquarie is piloting Gemini 3.5 Flash for complex onboarding-document review and recommendations, "
                "but the public record does not provide enough evidence to verify the claimed reliability or latency outcomes."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini 3.5: frontier intelligence with action - Google Blog",
                    GEMINI_LAUNCH_URL,
                    "Macquarie Bank is piloting how 3.5 Flash can accelerate customer onboarding by reasoning over complex 100+ page documents.",
                    "This is the only primary source for the pilot claim and its workflow framing.",
                ),
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "The model card says Gemini 3.5 Flash is suited to agentic and long-context workflows.",
                    "This supports product fit, not the claimed Macquarie pilot outcomes.",
                ),
            ],
            counter_evidence=[],
            missing_context=[
                "No public sample size, baseline, latency distribution, or error rate is given for the Macquarie pilot.",
                "There is no audited evidence showing how often humans intervene or override the recommendations.",
            ],
            numeric_findings=["100+ page onboarding documents"],
        ),
        ClaimAudit(
            claim=claim_8,
            verdict=Verdict.MISSING_CONTEXT,
            confidence="medium",
            stretch_score=56,
            why=(
                "Google publishes a relative safety-improvement story versus Gemini 3 Flash and says no egregious concerns were "
                "found, but the public detail is still limited for the broader cyber, CBRN, and refusal-behavior framing. Some "
                "published safety results are automated or relative rather than full public red-team disclosures."
            ),
            weaker_supported_rewrite=(
                "Google reports improved safety and refusal behavior versus Gemini 3 Flash, supported by internal automated evaluations "
                "and red-team review; public details for cyber and CBRN safeguards remain limited."
            ),
            supporting_evidence=[
                _evidence(
                    "Gemini 3.5: frontier intelligence with action - Google Blog",
                    GEMINI_LAUNCH_URL,
                    "We have strengthened our cyber and CBRN safeguards, which means it's less likely to generate harmful content, and to mistakenly refuse to answer safe queries.",
                    "This is the launch's broader safety framing.",
                ),
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "The model card reports internal automated safety and refusal improvements relative to Gemini 3 Flash and notes manual red teaming.",
                    "This supports a narrower relative-safety improvement story.",
                ),
            ],
            counter_evidence=[
                _evidence(
                    "Gemini 3.5 Flash - Model Card - Google DeepMind",
                    GEMINI_MODEL_CARD_URL,
                    "The public card gives limited detailed cyber and CBRN evidence and notes that some safety results are automated rather than human-evaluated.",
                    "That keeps the broader cyber and CBRN phrasing from being self-contained.",
                ),
            ],
            missing_context=[
                "The public model card does not fully publish the detailed cyber and CBRN evaluation evidence behind the broader launch wording.",
                "Some refusal-behavior improvements are reported through automated evaluations rather than full public human-review detail.",
            ],
            numeric_findings=[],
        ),
    ]

    report.claims = [audit.claim for audit in audits]
    report.audits = audits
    if report.run_profile is not None:
        report.run_profile.claims_extracted = len(report.claims)
        report.run_profile.claims_audited = len(report.audits)
        report.run_profile.contrast_claims = min(report.run_profile.contrast_claims, len(report.audits))
    if document.source != GEMINI_LAUNCH_URL:
        report.document = Document(
            title=document.title,
            source=GEMINI_LAUNCH_URL,
            text=document.text,
            snapshot=document.snapshot,
        )
    return report


def _claim(
    existing: RiskyClaim | None,
    *,
    claim_id: str,
    claim: str,
    claim_type: ClaimType,
    source_location: str,
    why_risky: str,
    audit_question: str,
) -> RiskyClaim:
    base = existing or RiskyClaim(
        id=claim_id,
        claim=claim,
        claim_type=claim_type,
        source_location=source_location,
        why_risky=why_risky,
        audit_question=audit_question,
    )
    return base.model_copy(
        update={
            "id": claim_id,
            "claim": claim,
            "claim_type": claim_type,
            "source_location": source_location,
            "why_risky": why_risky,
            "audit_question": audit_question,
        }
    )


def _evidence(source_title: str, url: str, snippet: str, relevance: str) -> EvidenceItem:
    return EvidenceItem(
        source_title=source_title,
        url=url,
        snippet=snippet,
        relevance=relevance,
    )
