from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from honestlaunch.anchor_map import enrich_report_for_launch_page
from honestlaunch.archive_quality import publication_gate, report_metrics
from honestlaunch.archive_registry import publication_info_for_report
from honestlaunch.canonical_hardening import GEMINI_REFERENCE_URLS, harden_report
from honestlaunch.citations import build_tooltip_citations, canonical_source_title
from honestlaunch.report import write_html
from honestlaunch.schemas import (
    AuditReport,
    ClaimAudit,
    ClaimType,
    ContrastSource,
    Document,
    EvidenceItem,
    EvidenceContrast,
    ReferenceSource,
    RiskyClaim,
    RunTimingProfile,
    PublicationInfo,
    Verdict,
)
from honestlaunch.source_snapshot import build_snapshot_from_html, build_snapshot_from_text


class AuditedLaunchPageTests(unittest.TestCase):
    def test_build_snapshot_from_html_preserves_content_blocks(self) -> None:
        html = """
        <html>
          <body>
            <article>
              <h1>Gemini 3.5 Flash</h1>
              <p>Fast enough for multi-step claim audits.</p>
              <ul><li>Lower latency</li></ul>
            </article>
          </body>
        </html>
        """

        snapshot = build_snapshot_from_html(
            html,
            source_url="https://example.com/gemini",
            title="Gemini 3.5 Flash",
        )

        self.assertEqual(snapshot.source_kind, "html")
        self.assertEqual([block.kind for block in snapshot.blocks], ["h1", "p", "li"])
        self.assertEqual(snapshot.blocks[1].section_heading, "Gemini 3.5 Flash")
        self.assertEqual(snapshot.blocks[2].text, "Lower latency")

    def test_build_snapshot_from_html_trims_prelude_toc_duplicates_and_tail_boilerplate(self) -> None:
        html = """
        <html>
          <body>
            <article>
              <ul><li>Breadcrumb</li></ul>
              <h1>Gemini 3.5 Flash</h1>
              <p>May 19, 2026</p>
              <ul>
                <li>Section one</li>
                <li>Section two</li>
                <li>Section three</li>
                <li>Section four</li>
              </ul>
              <p>Lead paragraph with the real article body.</p>
              <h2>Real section</h2>
              <p>Gemini Spark uses 3.5 Flash to help accomplish these tasks</p>
              <p>Gemini Spark uses 3.5 Flash to help accomplish these tasks</p>
              <p>Check your inbox to confirm your subscription.</p>
              <li>AI</li>
            </article>
          </body>
        </html>
        """

        snapshot = build_snapshot_from_html(
            html,
            source_url="https://example.com/gemini",
            title="Gemini 3.5 Flash",
        )

        self.assertEqual([block.kind for block in snapshot.blocks], ["h1", "p", "p", "h2", "p"])
        self.assertEqual(snapshot.blocks[0].text, "Gemini 3.5 Flash")
        self.assertEqual(snapshot.blocks[-1].text, "Gemini Spark uses 3.5 Flash to help accomplish these tasks")

    def test_build_tooltip_citations_prefers_explicit_reference_sources(self) -> None:
        audit = _sample_audit()

        citations = build_tooltip_citations(audit, reference_urls=[])

        self.assertEqual(len(citations), 1)
        self.assertEqual(citations[0].title, "Gemini 3.5 Flash model card")
        self.assertIn("Text-only", citations[0].snippet)
        self.assertIn("launch setup", citations[0].why_relevant)

    def test_build_tooltip_citations_prefers_explicit_reference_url_when_supplied(self) -> None:
        audit = _sample_audit()

        citations = build_tooltip_citations(
            audit,
            reference_urls=["https://deepmind.google/models/model-cards/gemini-3-5-flash"],
        )

        self.assertEqual(len(citations), 1)
        self.assertEqual(
            citations[0].url,
            "https://deepmind.google/models/model-cards/gemini-3-5-flash",
        )
        self.assertEqual(citations[0].title, "Gemini 3.5 Flash - deepmind.google")
        self.assertIn("Text-only", citations[0].snippet)

    def test_build_tooltip_citations_selects_pricing_references_for_cost_claim(self) -> None:
        claim = RiskyClaim(
            id="c2",
            claim="Gemini 3.5 Flash often runs at less than half the cost of other frontier models.",
            claim_type=ClaimType.GENERALIZATION,
            source_location="Performance",
            why_risky="Cost comparisons need named baselines.",
            audit_question="Is the cost comparison true against the named baselines?",
        )
        audit = ClaimAudit(
            claim=claim,
            verdict=Verdict.OVERSTATED,
            confidence="high",
            stretch_score=80,
            why="The cost claim needs named comparison sets.",
            weaker_supported_rewrite="The list price is less than half of some heavy-flagship baselines.",
        )

        citations = build_tooltip_citations(audit, GEMINI_REFERENCE_URLS)

        urls = [citation.url for citation in citations]
        self.assertIn("https://ai.google.dev/gemini-api/docs/pricing", urls)
        self.assertTrue(any("pricing" in (url or "") and "openai.com" in (url or "") or "claude.com" in (url or "") for url in urls))

    def test_canonical_source_title_ignores_placeholder_grounding_title(self) -> None:
        title = canonical_source_title(
            "Source returned by Gemini grounding metadata.",
            "https://deepmind.google/models/model-cards/gemini-3-5-flash",
        )

        self.assertEqual(title, "Gemini 3.5 Flash - deepmind.google")

    def test_enrich_report_for_launch_page_attaches_anchor_and_primary_view(self) -> None:
        snapshot = build_snapshot_from_text(
            "# Gemini 3.5 Flash\n\nGemini 3.5 Flash is always best-in-class across every benchmark.\n",
            source_url="https://example.com/gemini",
            title="Gemini 3.5 Flash",
        )
        document = Document(
            title="Gemini 3.5 Flash",
            source="https://example.com/gemini",
            text="Gemini 3.5 Flash is always best-in-class across every benchmark.",
            snapshot=snapshot,
        )
        audit = _sample_audit()
        report = AuditReport(
            document=document,
            claims=[audit.claim],
            audits=[audit],
            runtime="mock",
            mode="deterministic_fallback",
            contrast_enabled=True,
            reference_urls=["https://deepmind.google/models/model-cards/gemini-3-5-flash"],
            run_profile=RunTimingProfile(),
        )

        enriched = enrich_report_for_launch_page(report)

        self.assertIsNotNone(enriched.launch_page)
        self.assertEqual(enriched.launch_page.primary_view, "audited_launch_page")
        self.assertEqual(enriched.launch_page.rewritten_claim_count, 1)
        self.assertEqual(enriched.launch_page.explicit_reference_count, 1)
        self.assertIsNotNone(enriched.audits[0].anchor)
        self.assertEqual(enriched.audits[0].anchor.claim_id, "c1")
        self.assertEqual(enriched.audits[0].anchor.block_id, "block-1")
        self.assertEqual(len(enriched.launch_page.decorations), 1)
        self.assertEqual(
            enriched.launch_page.decorations[0].rewritten_text,
            "Gemini 3.5 Flash leads several Google-reported launch benchmarks.",
        )

    def test_publication_info_matches_xai_proxy_input(self) -> None:
        document = Document(
            title="Grok 3 launch proxy",
            source="examples/xai_grok3_launch_input.md",
            text="Grok 3 proxy body.",
        )
        report = AuditReport(document=document, claims=[], audits=[])

        publication = publication_info_for_report(report)

        self.assertIsNotNone(publication)
        self.assertEqual(publication.slug, "xai-grok-3")
        self.assertEqual(publication.original_url, "https://x.ai/news/grok-3")

    def test_write_html_includes_modified_notice_and_archive_links(self) -> None:
        snapshot = build_snapshot_from_text(
            "# Gemini 3.5 Flash\n\nGemini 3.5 Flash is always best-in-class across every benchmark.\n",
            source_url="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
            title="Gemini 3.5 Flash",
        )
        document = Document(
            title="Gemini 3.5 Flash",
            source="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
            text="Gemini 3.5 Flash is always best-in-class across every benchmark.",
            snapshot=snapshot,
        )
        audit = _sample_audit()
        report = enrich_report_for_launch_page(
            AuditReport(
                document=document,
                claims=[audit.claim],
                audits=[audit],
                contrast_enabled=True,
                reference_urls=["https://deepmind.google/models/model-cards/gemini-3-5-flash"],
                run_profile=RunTimingProfile(),
            )
        )
        report.publication = publication_info_for_report(report)

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "report.html"
            write_html(report, path)
            markup = path.read_text(encoding="utf-8")

        self.assertIn("Audited modified version", markup)
        self.assertIn("Evidence Packet", markup)
        self.assertIn("Audit Ledger", markup)
        self.assertIn("Original Google launch post", markup)
        self.assertNotIn(">Methodology<", markup)
        self.assertNotIn(">Archive<", markup)

    def test_write_html_suppresses_opaque_grounding_redirects_in_ui(self) -> None:
        audit = _sample_audit()
        audit.supporting_evidence = [
            EvidenceItem(
                source_title="Claude API Docs",
                url="https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFake",
                snippet="Fast mode delivers up to 2.5x higher output tokens per second.",
                relevance="Qualifies the speed claim.",
            )
        ]
        report = AuditReport(
            document=Document(
                title="Claude Opus 4.8",
                source="https://www.anthropic.com/news/claude-opus-4-8",
                text="Fast mode is faster.",
            ),
            claims=[audit.claim],
            audits=[audit],
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "report.html"
            write_html(report, path)
            markup = path.read_text(encoding="utf-8")

        self.assertIn("isOpaqueGroundingUrl", markup)
        self.assertIn("Opaque Gemini grounding redirect hidden; source title retained above.", markup)

    def test_report_metrics_and_publication_gate(self) -> None:
        snapshot = build_snapshot_from_text(
            "# Gemini 3.5 Flash\n\nGemini 3.5 Flash is always best-in-class across every benchmark.\n",
            source_url="https://example.com/gemini",
            title="Gemini 3.5 Flash",
        )
        audit = _sample_audit()
        audit.tooltip_citations = build_tooltip_citations(
            audit,
            reference_urls=["https://deepmind.google/models/model-cards/gemini-3-5-flash"],
        )
        report = enrich_report_for_launch_page(
            AuditReport(
                document=Document(
                    title="Gemini 3.5 Flash",
                    source="https://example.com/gemini",
                    text="Gemini 3.5 Flash is always best-in-class across every benchmark.",
                    snapshot=snapshot,
                ),
                claims=[audit.claim],
                audits=[audit],
                reference_urls=["https://deepmind.google/models/model-cards/gemini-3-5-flash"],
            )
        )
        report.publication = PublicationInfo(
            slug="gemini-35-flash",
            original_url="https://example.com/gemini",
            evidence_packet_url="evidence_packets/gemini-35-flash.json",
            gate_status="pass",
        )

        metrics = report_metrics(report)
        gate = publication_gate(report)

        self.assertEqual(metrics["claimsAudited"], 1)
        self.assertEqual(metrics["rewrittenClaims"], 1)
        self.assertEqual(metrics["tooltipCitationCoveragePct"], 100)
        self.assertEqual(metrics["anchorCoveragePct"], 100)
        self.assertTrue(gate["overallPass"])

    def test_harden_report_curates_gemini_audits_and_references(self) -> None:
        source = "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
        document = Document(
            title="Gemini 3.5 Flash",
            source=source,
            text="Gemini 3.5 Flash launch.",
        )
        claims = [
            RiskyClaim(
                id="1",
                claim="old benchmark claim",
                claim_type=ClaimType.BENCHMARK,
                source_location="Performance",
                why_risky="old",
                audit_question="old",
            ),
            RiskyClaim(
                id="2",
                claim="old speed claim",
                claim_type=ClaimType.NUMERIC,
                source_location="Performance",
                why_risky="old",
                audit_question="old",
            ),
            RiskyClaim(
                id="3",
                claim="old time-cost claim",
                claim_type=ClaimType.GENERALIZATION,
                source_location="Performance",
                why_risky="old",
                audit_question="old",
            ),
            RiskyClaim(
                id="4",
                claim="old reliability claim",
                claim_type=ClaimType.DEPLOYMENT,
                source_location="Performance",
                why_risky="old",
                audit_question="old",
            ),
            RiskyClaim(
                id="6",
                claim="old partner claim",
                claim_type=ClaimType.DEPLOYMENT,
                source_location="Real-world impact",
                why_risky="old",
                audit_question="old",
            ),
            RiskyClaim(
                id="8",
                claim="old safety claim",
                claim_type=ClaimType.SAFETY,
                source_location="Safety",
                why_risky="old",
                audit_question="old",
            ),
        ]
        audits = [
            ClaimAudit(
                claim=claims[0],
                verdict=Verdict.MISSING_CONTEXT,
                confidence="high",
                stretch_score=40,
                why="old",
                weaker_supported_rewrite="old",
            ),
            ClaimAudit(
                claim=claims[1],
                verdict=Verdict.MISSING_CONTEXT,
                confidence="medium",
                stretch_score=35,
                why="old",
                weaker_supported_rewrite="old",
            ),
            ClaimAudit(
                claim=claims[2],
                verdict=Verdict.OVERSTATED,
                confidence="high",
                stretch_score=80,
                why="old",
                weaker_supported_rewrite="old",
            ),
            ClaimAudit(
                claim=claims[3],
                verdict=Verdict.OVERSTATED,
                confidence="high",
                stretch_score=80,
                why="old",
                weaker_supported_rewrite="old",
            ),
        ]
        report = AuditReport(document=document, claims=claims, audits=audits, reference_urls=[])

        hardened = harden_report(report)

        self.assertEqual(len(hardened.audits), 7)
        self.assertEqual(hardened.audits[0].claim.id, "1")
        self.assertEqual(hardened.audits[0].verdict, Verdict.SUPPORTED)
        self.assertEqual(hardened.audits[1].claim.id, "1b")
        self.assertEqual(hardened.audits[1].verdict, Verdict.MISSING_CONTEXT)
        self.assertEqual(hardened.audits[-2].claim.id, "6")
        self.assertEqual(hardened.audits[-2].verdict, Verdict.NOT_CHECKABLE)
        self.assertEqual(hardened.audits[-1].claim.id, "8")
        self.assertEqual(hardened.audits[-1].verdict, Verdict.MISSING_CONTEXT)
        self.assertGreaterEqual(len(hardened.reference_urls), 10)
        self.assertIn("https://ai.google.dev/gemini-api/docs/pricing", hardened.reference_urls)


def _sample_audit() -> ClaimAudit:
    claim = RiskyClaim(
        id="c1",
        claim="Gemini 3.5 Flash is always best-in-class across every benchmark.",
        claim_type=ClaimType.GENERALIZATION,
        source_location="headline",
        why_risky="Absolute leaderboard language outruns the official card.",
        audit_question="Does the official model card support an all-benchmarks claim?",
    )
    contrast = EvidenceContrast(
        claim_id="c1",
        claim_text=claim.claim,
        reference_sources=[
            ReferenceSource(
                title="Gemini 3.5 Flash model card",
                url="https://deepmind.google/models/model-cards/gemini-3-5-flash",
                source_type="official_doc",
                why_relevant="Official launch reference for the benchmark framing.",
                authority_score=95,
            )
        ],
        best_sources=[
            ContrastSource(
                title="Gemini 3.5 Flash model card",
                url="https://deepmind.google/models/model-cards/gemini-3-5-flash",
                stance="narrows",
                evidence_summary="Text-only and multimodal launch results lead several published benchmarks, not every benchmark.",
                key_qualification="Benchmarks are reported for the launch setup, not every setting.",
            )
        ],
        delta_type="broader_than_claim",
        delta_explanation="The launch materials support several benchmark wins, not an all-benchmarks universal claim.",
        suggested_rewrite="Gemini 3.5 Flash leads several Google-reported launch benchmarks.",
        recommended_verdict=Verdict.OVERSTATED,
        confidence="high",
    )
    return ClaimAudit(
        claim=claim,
        verdict=Verdict.OVERSTATED,
        confidence="high",
        stretch_score=84,
        why="The source supports strong launch benchmark positioning, but not an always-best universal claim.",
        weaker_supported_rewrite="Gemini 3.5 Flash leads several Google-reported launch benchmarks.",
        contrast=contrast,
    )


if __name__ == "__main__":
    unittest.main()
