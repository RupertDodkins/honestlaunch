from __future__ import annotations

import html
import json
from pathlib import Path

from .archive_registry import publication_info_for_report
from .schemas import AuditReport, ClaimAudit, PublicationInfo


def write_json(report: AuditReport, path: Path) -> None:
    path.write_text(report.model_dump_json(indent=2, exclude_none=True), encoding="utf-8")


def write_markdown(report: AuditReport, path: Path) -> None:
    verdict_counts = _verdict_counts(report)
    average_stretch = _average_stretch(report.audits)
    lines = [
        f"# HonestLaunch Report: {report.document.title}",
        "",
        f"Source: `{report.document.source}`",
        "",
        "## Provenance",
        "",
        f"- Mode: `{report.mode}`",
        f"- Model: `{report.model or 'none'}`",
        f"- Evidence Contrast: `{'enabled' if report.contrast_enabled else 'disabled'}`",
        f"- Provided reference URLs: {', '.join(f'`{url}`' for url in report.reference_urls) if report.reference_urls else '`none`'}",
        "",
        "## Scorecard",
        "",
        f"- Claims audited: `{len(report.audits)}`",
        (
            "- Verdict counts: "
            f"`supported={verdict_counts['supported']}` · "
            f"`overstated={verdict_counts['overstated']}` · "
            f"`missing_context={verdict_counts['missing_context']}` · "
            f"`contradicted={verdict_counts['contradicted']}` · "
            f"`not_checkable={verdict_counts['not_checkable']}`"
        ),
        f"- Average stretch score: `{average_stretch}/100`",
        f"- Provided reference URL count: `{len(report.reference_urls)}`",
        "",
        "| Claim | Formal Verdict | Confidence | Stretch Score |",
        "| --- | --- | --- | ---: |",
    ]
    if report.run_profile:
        lines[8:8] = [
            f"- Pipeline wall: `{_format_duration_ms(report.run_profile.total_duration_ms)}`",
            (
                f"- Load / Extract / Audit / Contrast: "
                f"`{_format_duration_ms(report.run_profile.load_document_ms)}` / "
                f"`{_format_duration_ms(report.run_profile.extract_claims_ms)}` / "
                f"`{_format_duration_ms(report.run_profile.audit_claims_ms)}` / "
                f"`{_format_duration_ms(report.run_profile.contrast_duration_ms)}`"
            ),
            (
                f"- Claims extracted / audited: `{report.run_profile.claims_extracted}` / "
                f"`{report.run_profile.claims_audited}`"
            ),
            (
                f"- Specialist passes / unique sources: `{report.run_profile.agent_passes}` / "
                f"`{report.run_profile.unique_source_count}`"
            ),
            "",
        ]
    for audit in report.audits:
        lines.append(
            f"| {audit.claim.claim} | {audit.verdict.value} | {audit.confidence} | {audit.stretch_score} |"
        )

    for audit in report.audits:
        lines.extend(_audit_markdown(audit))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(report: AuditReport, path: Path) -> None:
    publication = publication_info_for_report(report)
    data = json.dumps(report.model_dump(exclude_none=True), indent=2).replace("</", "<\\/")
    launch_page = json.dumps(_build_launch_page_data(report), indent=2).replace("</", "<\\/")
    publication_data = json.dumps(
        publication.model_dump(exclude_none=True) if publication else {},
        indent=2,
    ).replace("</", "<\\/")
    header_summary = f"{len(report.audits)} audited claims"
    if report.run_profile:
        header_summary += f" · {_format_duration_ms(report.run_profile.total_duration_ms)} pipeline"
    header_summary += f" · {html.escape(report.mode)}"
    page_title = publication.launch_name if publication and publication.launch_name else report.document.title
    markup = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page_title)} · Honest Launches</title>
  <style>
    :root {{
      --ink: #1f2328;
      --muted: #667085;
      --line: #d0d7de;
      --bg: #f6f8fa;
      --panel: #ffffff;
      --overstated: #b42318;
      --missing: #b54708;
      --supported: #067647;
      --receipts: #344054;
    }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    header {{
      padding: 20px 24px;
      border-bottom: 1px solid var(--line);
      background: var(--panel);
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: baseline;
    }}
    .eyebrow {{
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 8px;
    }}
    h1 {{ margin: 0; font-size: 24px; letter-spacing: 0; }}
    main {{
      min-height: calc(100vh - 74px);
    }}
    [hidden] {{ display: none !important; }}
    .notice-strip {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 18px;
      padding: 16px 18px;
      border-bottom: 1px solid var(--line);
      background: linear-gradient(180deg, #fff7ed 0%, #ffffff 100%);
    }}
    .notice-copy {{
      max-width: 920px;
    }}
    .notice-copy p {{
      margin: 6px 0 0;
      color: var(--ink);
    }}
    .notice-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }}
    .notice-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: var(--panel);
      padding: 9px 12px;
      font-size: 13px;
      font-weight: 800;
      text-decoration: none;
      color: var(--ink);
    }}
    .notice-link.primary {{
      background: var(--ink);
      border-color: var(--ink);
      color: #ffffff;
    }}
    .view-switcher {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      padding: 14px 18px 0;
      background: var(--bg);
    }}
    .view-toggle {{
      appearance: none;
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--ink);
      border-radius: 999px;
      padding: 9px 14px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
    }}
    .view-toggle.active {{
      background: var(--ink);
      color: #ffffff;
      border-color: var(--ink);
    }}
    .launch-shell {{
      padding: 18px;
      background: var(--bg);
    }}
    .launch-article {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 22px;
      line-height: 1.7;
      box-shadow: 0 8px 24px rgba(31,35,40,.06);
    }}
    .launch-block {{
      margin: 0 0 18px;
      overflow-wrap: anywhere;
    }}
    .launch-block:last-child {{
      margin-bottom: 0;
    }}
    .launch-block.list-item {{
      padding-left: 18px;
      position: relative;
    }}
    .launch-block.list-item::before {{
      content: '•';
      position: absolute;
      left: 0;
      color: var(--muted);
    }}
    .launch-block.preformatted {{
      white-space: pre-wrap;
      background: #0d1117;
      color: #f0f6fc;
      border-radius: 8px;
      padding: 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }}
    .launch-kicker {{
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 10px;
    }}
    .launch-note {{
      margin: 0 0 14px;
      color: var(--muted);
    }}
    .launch-meta {{
      display: grid;
      gap: 8px;
      margin-top: 14px;
    }}
    .launch-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 14px;
    }}
    .launch-meta p {{
      margin: 0;
    }}
    .audit-mark {{
      appearance: none;
      border: 0;
      border-bottom: 2px dotted rgba(181, 71, 8, 0.9);
      background: transparent;
      color: inherit;
      padding: 0;
      margin: 0;
      font: inherit;
      line-height: inherit;
      cursor: pointer;
      text-align: left;
    }}
    .audit-mark:hover,
    .audit-mark:focus-visible {{
      background: rgba(181, 71, 8, 0.08);
      outline: none;
      border-bottom-style: solid;
    }}
    .audit-tooltip {{
      position: fixed;
      z-index: 1000;
      max-width: min(360px, calc(100vw - 32px));
      border: 1px solid var(--line);
      border-radius: 10px;
      background: var(--panel);
      color: var(--ink);
      padding: 12px 14px;
      box-shadow: 0 18px 42px rgba(31,35,40,.18);
    }}
    .audit-tooltip p {{
      margin: 0 0 10px;
      color: inherit;
    }}
    .audit-tooltip p:last-child {{
      margin-bottom: 0;
    }}
    .audit-tooltip .tooltip-label {{
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--muted);
      margin-bottom: 4px;
    }}
    .audit-tooltip .tooltip-citations {{
      display: grid;
      gap: 10px;
      margin-top: 12px;
    }}
    .audit-tooltip .tooltip-citation {{
      border-top: 1px solid var(--line);
      padding-top: 10px;
    }}
    .claim-strip {{
      padding: 16px 18px;
      border-bottom: 1px solid var(--line);
      background: var(--bg);
    }}
    .headline-strip {{
      padding: 18px;
      border-bottom: 1px solid var(--line);
      background:
        linear-gradient(180deg, rgba(255,255,255,0.94), rgba(246,248,250,0.96));
    }}
    .summary-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 10px;
      margin-bottom: 12px;
    }}
    .telemetry-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 10px;
    }}
    .stat-card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px;
    }}
    .stat-label {{
      font-size: 12px;
      font-weight: 700;
      color: var(--muted);
      margin-bottom: 4px;
    }}
    .stat-value {{
      font-size: 24px;
      font-weight: 800;
      line-height: 1.1;
      letter-spacing: -0.02em;
    }}
    .stat-note {{
      margin-top: 6px;
      font-size: 12px;
      color: var(--muted);
      overflow-wrap: anywhere;
    }}
    .report-grid {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 380px;
      min-height: calc(100vh - 250px);
    }}
    section {{ padding: 18px; border-right: 1px solid var(--line); }}
    section:last-child {{ border-right: 0; }}
    .filters {{
      display: grid;
      grid-template-columns: minmax(180px, 260px);
      gap: 10px;
      margin: 0 0 12px;
    }}
    label {{
      display: grid;
      gap: 5px;
      font-size: 12px;
      font-weight: 700;
      color: var(--muted);
    }}
    select {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px 10px;
      background: var(--panel);
      color: var(--ink);
    }}
    .claim-row {{
      width: 100%;
      text-align: left;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      cursor: pointer;
      overflow-wrap: anywhere;
    }}
    .claim-row.active {{ border-color: var(--ink); box-shadow: 0 0 0 2px rgba(31,35,40,.08); }}
    #claim-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 10px;
    }}
    .claim-meta {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 8px;
    }}
    .badge {{
      display: inline-block;
      font-size: 12px;
      font-weight: 700;
      padding: 3px 7px;
      border-radius: 999px;
      margin-right: 6px;
      color: white;
      background: var(--receipts);
    }}
    .hint {{
      display: inline-grid;
      place-items: center;
      width: 18px;
      height: 18px;
      border: 1px solid var(--line);
      border-radius: 999px;
      color: var(--muted);
      font-size: 12px;
      font-weight: 800;
      cursor: help;
      position: relative;
      background: var(--panel);
      vertical-align: middle;
    }}
    .hint:focus {{
      outline: 2px solid var(--ink);
      outline-offset: 2px;
    }}
    .hint::after {{
      content: attr(data-tip);
      display: none;
      position: absolute;
      z-index: 10;
      top: calc(100% + 8px);
      left: 50%;
      transform: translateX(-50%);
      width: min(280px, 72vw);
      padding: 9px 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--ink);
      color: #ffffff;
      font-size: 12px;
      font-weight: 600;
      line-height: 1.35;
      box-shadow: 0 8px 24px rgba(31,35,40,.18);
    }}
    .hint:hover::after,
    .hint:focus::after {{
      display: block;
    }}
    .muted {{ color: var(--muted); }}
    .wrap {{
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 14px;
      overflow-wrap: anywhere;
    }}
    .score {{
      height: 10px;
      background: #eaecf0;
      border-radius: 999px;
      overflow: hidden;
      margin-top: 8px;
    }}
    .score > div {{ height: 100%; background: var(--overstated); }}
    .strength-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin-top: 12px;
    }}
    .strength-card {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
      background: var(--bg);
    }}
    .strength-label {{
      display: flex;
      justify-content: space-between;
      gap: 8px;
      font-size: 12px;
      font-weight: 700;
      color: var(--muted);
    }}
    .meter {{
      height: 8px;
      background: var(--line);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 8px;
    }}
    .meter > div {{ height: 100%; background: var(--receipts); }}
    .meter.overstated > div, .meter.contradicted > div {{ background: var(--overstated); }}
    .meter.missing-context > div {{ background: var(--missing); }}
    .meter.supported > div {{ background: var(--supported); }}
    a {{
      color: var(--receipts);
      font-weight: 700;
      overflow-wrap: anywhere;
    }}
    .source-item {{
      padding-bottom: 12px;
      border-bottom: 1px solid var(--line);
    }}
    .source-item:last-child {{
      padding-bottom: 0;
      border-bottom: 0;
    }}
    h2, h3 {{ margin: 0 0 10px; letter-spacing: 0; }}
    .title-row {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}
    pre {{
      white-space: pre-wrap;
      background: #0d1117;
      color: #f0f6fc;
      padding: 12px;
      border-radius: 8px;
      max-height: 260px;
      overflow: auto;
    }}
    details {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--bg);
      padding: 10px 12px;
      margin-top: 10px;
    }}
    details:first-of-type {{
      margin-top: 0;
    }}
    summary {{
      cursor: pointer;
      font-weight: 800;
    }}
    @media (max-width: 980px) {{
      .report-grid {{ grid-template-columns: 1fr; }}
      section {{ border-right: 0; border-bottom: 1px solid var(--line); }}
      .strength-grid {{ grid-template-columns: 1fr; }}
      .notice-strip {{
        display: block;
      }}
      .notice-links {{
        margin-top: 12px;
      }}
    }}
  </style>
</head>
<body>
  <header id="artifact-header">
    <div>
      <div class="eyebrow">Honest Launches audit artifact</div>
      <h1>{html.escape(page_title)}</h1>
      <div class="muted">{html.escape(report.document.title)}</div>
    </div>
    <div class="muted">{header_summary}</div>
  </header>
  <main>
    <div class="view-switcher">
      <button class="view-toggle active" id="launch-toggle" onclick="setView('launch')">Audited Launch Page</button>
      <button class="view-toggle" id="ledger-toggle" onclick="setView('ledger')">Audit Ledger</button>
    </div>
    <div id="launch-view" class="launch-shell">
      <div id="launch-summary"></div>
      <article class="launch-article">
        <div id="launch-article"></div>
      </article>
    </div>
    <div id="ledger-view" hidden>
      <div class="notice-strip">
        <div class="notice-copy" id="publication-notice"></div>
        <div class="notice-links" id="publication-links"></div>
      </div>
      <div class="headline-strip">
        <div class="title-row">
          <h2>Run Summary</h2>
          <span class="hint" tabindex="0" data-tip="This strip summarizes the audit punchline: how many claims were audited, how severe they were, and what runtime/profile telemetry was recorded for the run.">?</span>
        </div>
        <div class="summary-grid" id="scorecard-grid"></div>
        <div class="telemetry-grid" id="telemetry-grid"></div>
      </div>
      <div class="claim-strip">
        <div class="title-row">
          <h2>Audit Ledger</h2>
          <span class="hint" tabindex="0" data-tip="Gemini extracts risky factual claims, then Honest Launches audits the selected claims. Click a card to inspect verdict, evidence, contrast, and agent steps.">?</span>
        </div>
        <div class="filters single">
          <label>Verdict
            <span class="hint" tabindex="0" data-tip="Formal verdict definitions: supported = evidence supports the claim as written; overstated = directionally supported but too broad/strong/certain; missing_context = may be true but key scope/baseline/method/source context is absent; contradicted = evidence conflicts with the claim; not_checkable = insufficient evidence to verify or falsify.">?</span>
            <select id="verdict-filter" onchange="filters.verdict=this.value; syncSelection(); render();"></select>
          </label>
        </div>
        <p class="muted" id="filter-summary"></p>
        <div id="claim-list"></div>
      </div>
      <div class="report-grid">
        <section>
          <div class="title-row">
            <h2>Selected Claim</h2>
            <span class="hint" tabindex="0" data-tip="This panel shows the selected claim, the Honest Launches verdict, and the strongest defensible rewrite.">?</span>
          </div>
          <div id="claim-detail"></div>
        </section>
        <section>
          <div class="title-row">
            <h2>Source Provenance</h2>
            <span class="hint" tabindex="0" data-tip="Separates explicit references you provided from claim-level contrast references and Gemini-discovered supporting or caveat/counter sources.">?</span>
          </div>
          <div id="evidence"></div>
        </section>
      </div>
    </div>
  </main>
  <div id="audit-tooltip" class="audit-tooltip" hidden></div>
  <script>
    const report = {data};
    const launchPage = {launch_page};
    const publication = {publication_data};
    let selected = 0;
    let activeView = window.location.hash === '#ledger' ? 'ledger' : 'launch';
    let launchTooltipGlobalsBound = false;
    const filters = {{ verdict: 'all' }};
    const cls = (value) => String(value).replaceAll('_', '-').replaceAll(' ', '-');
    const confidenceScore = {{ low: 34, medium: 67, high: 100 }};
    const verdictOrder = ['supported', 'overstated', 'missing_context', 'contradicted', 'not_checkable'];
    const verdictLabels = {{
      supported: 'Supported',
      overstated: 'Overstated',
      missing_context: 'Missing Context',
      contradicted: 'Contradicted',
      not_checkable: 'Not Checkable'
    }};
    const esc = (value) => String(value ?? '').replace(/[&<>"']/g, char => ({{
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    }}[char]));
    const safeHref = (value) => {{
      if (!value) return '';
      try {{
        const url = new URL(String(value), document.baseURI);
        if (['http:', 'https:', 'mailto:'].includes(url.protocol)) return url.href;
      }} catch (_) {{}}
      return '';
    }};
    const hint = (text) => `<span class="hint" tabindex="0" data-tip="${{esc(text)}}">?</span>`;
    const fmtMs = (value) => {{
      const durationMs = Number(value ?? 0);
      if (!Number.isFinite(durationMs) || durationMs <= 0) return '0ms';
      if (durationMs >= 1000) return `${{(durationMs / 1000).toFixed(2)}}s`;
      return `${{durationMs}}ms`;
    }};
    function verdictTip(verdict) {{
      return ({{
        supported: 'Available evidence supports the claim as written or with only minor caveats.',
        overstated: 'Evidence points in the same direction, but the wording is stronger, broader, or more certain than supported.',
        missing_context: 'The claim may be true, but key scope, baseline, methodology, source, or denominator context is missing.',
        contradicted: 'Available evidence conflicts with the claim as written.',
        not_checkable: 'The available sources do not provide enough evidence to verify or falsify the claim.'
      }})[verdict] || 'Formal Honest Launches verdict for this claim.';
    }}
    function verdictLabel(verdict) {{
      return verdictLabels[verdict] || String(verdict || '').replaceAll('_', ' ');
    }}
    function renderPublicationHeader() {{
      const defaultSource = safeHref(launchPage.source_url || report.document?.source || '');
      const originalHref = safeHref(publication.original_url || defaultSource);
      const originalLabel = publication.original_label || (defaultSource ? 'Original source' : 'Source');
      const note = publication.source_note || '';
      const disclaimer = publication.disclaimer || 'Audited modified version of the original source.';
      const status = publication.status || 'reviewed';
      const publishedAt = publication.published_at || 'unknown';
      const gateStatus = publication.gate_status || 'unknown';
      const evidenceHref = safeHref(publication.evidence_packet_url || '');
      document.getElementById('publication-notice').innerHTML = `
        <strong>Audited modified version</strong>
        <p class="wrap">${{esc(disclaimer)}}</p>
        <p class="wrap"><strong>Status:</strong> ${{esc(status)}} · <strong>Published:</strong> ${{esc(publishedAt)}} · <strong>Gate:</strong> ${{esc(gateStatus)}}${{note ? ` · ${{esc(note)}}` : ''}}</p>
      `;
      document.getElementById('publication-links').innerHTML = [
        evidenceHref ? `<a class="notice-link" href="${{esc(evidenceHref)}}" target="_blank" rel="noopener noreferrer">Evidence Packet</a>` : '',
      ].filter(Boolean).join('');
    }}
    function verdictCounts(audits) {{
      const counts = {{
        supported: 0,
        overstated: 0,
        missing_context: 0,
        contradicted: 0,
        not_checkable: 0,
      }};
      for (const audit of audits) {{
        if (counts[audit.verdict] != null) counts[audit.verdict] += 1;
      }}
      return counts;
    }}
    function averageStretch(audits) {{
      if (!audits.length) return 0;
      const total = audits.reduce((sum, audit) => sum + Number(audit.stretch_score || 0), 0);
      return Math.round(total / audits.length);
    }}
    function statCard(label, value, note = '') {{
      return `
        <div class="stat-card">
          <div class="stat-label">${{esc(label)}}</div>
          <div class="stat-value">${{esc(value)}}</div>
          ${{note ? `<div class="stat-note">${{esc(note)}}</div>` : ''}}
        </div>
      `;
    }}
    function renderHeadline() {{
      const counts = verdictCounts(report.audits || []);
      const avgStretch = averageStretch(report.audits || []);
      const run = report.run_profile || {{}};
      document.getElementById('scorecard-grid').innerHTML = [
        statCard('Claims Audited', String((report.audits || []).length), `${{run.claims_extracted ?? (report.claims || []).length}} extracted`),
        ...verdictOrder.map(key => statCard(verdictLabels[key], String(counts[key]), key === 'supported' ? 'best-case verdict' : '')),
        statCard('Avg Stretch', `${{avgStretch}}/100`, 'higher means riskier wording'),
      ].join('');
      document.getElementById('telemetry-grid').innerHTML = [
        statCard('Model', report.model || 'none', report.contrast_enabled ? 'contrast enabled' : 'contrast disabled'),
        statCard('Execution Mode', report.mode),
        statCard('Pipeline Wall', fmtMs(run.total_duration_ms || 0), `audit ${{fmtMs(run.audit_claims_ms || 0)}} · contrast ${{fmtMs(run.contrast_duration_ms || 0)}}`),
        statCard('Specialist Passes', String(run.agent_passes || 0), `${{run.claims_audited || (report.audits || []).length}} claims`),
        statCard('Unique Sources', String(run.unique_source_count || 0), 'support + caveat + contrast urls'),
        statCard('Provided References', String((report.reference_urls || []).length), 'explicit --reference inputs'),
      ].join('');
    }}
    function setView(view) {{
      activeView = view === 'ledger' ? 'ledger' : 'launch';
      document.getElementById('launch-view').hidden = activeView !== 'launch';
      document.getElementById('ledger-view').hidden = activeView !== 'ledger';
      document.getElementById('launch-toggle').classList.toggle('active', activeView === 'launch');
      document.getElementById('ledger-toggle').classList.toggle('active', activeView === 'ledger');
      const targetHash = activeView === 'ledger' ? '#ledger' : '#launch';
      if (window.location.hash !== targetHash) {{
        history.replaceState(null, '', targetHash);
      }}
      if (activeView === 'launch') renderLaunchPage();
    }}
    function renderLaunchPage() {{
      document.getElementById('launch-summary').innerHTML = '';
      const decorations = launchPage.decorations || [];
      const byBlock = new Map();
      for (const decoration of decorations) {{
        const blockId = decoration.anchor?.block_id;
        if (!blockId) continue;
        if (!byBlock.has(blockId)) byBlock.set(blockId, []);
        byBlock.get(blockId).push(decoration);
      }}
      for (const values of byBlock.values()) {{
        values.sort((left, right) => (left.anchor.start_char || 0) - (right.anchor.start_char || 0));
      }}
      document.getElementById('launch-article').innerHTML = (launchPage.blocks || [])
        .map(block => renderLaunchBlock(block, byBlock.get(block.block_id) || []))
        .join('');
      bindAuditMarks();
    }}
    function renderLaunchBlock(block, decorations) {{
      const text = String(block.text || '');
      const markup = decorateBlockText(text, decorations);
      const kind = String(block.kind || 'paragraph').toLowerCase();
      if (/^h[1-6]$/.test(kind)) {{
        return `<${{kind}} class="launch-block">${{markup}}</${{kind}}>`;
      }}
      if (kind === 'blockquote') {{
        return `<blockquote class="launch-block">${{markup}}</blockquote>`;
      }}
      if (kind === 'pre' || kind === 'table') {{
        return `<pre class="launch-block preformatted">${{markup}}</pre>`;
      }}
      if (kind === 'li') {{
        return `<p class="launch-block list-item">${{markup}}</p>`;
      }}
      return `<p class="launch-block">${{markup}}</p>`;
    }}
    function decorateBlockText(text, decorations) {{
      if (!decorations.length) return esc(text);
      let cursor = 0;
      let output = '';
      for (const decoration of decorations) {{
        const anchor = decoration.anchor || {{}};
        const start = Number(anchor.start_char || 0);
        const end = Number(anchor.end_char || 0);
        if (!Number.isFinite(start) || !Number.isFinite(end) || end <= start || start < cursor) continue;
        output += esc(text.slice(cursor, start));
        output += `<button type="button" class="audit-mark" data-claim-id="${{esc(decoration.claim_id)}}">${{esc(decoration.rewritten_text)}}</button>`;
        cursor = end;
      }}
      output += esc(text.slice(cursor));
      return output;
    }}
    function bindAuditMarks() {{
      const tooltip = document.getElementById('audit-tooltip');
      const decorations = new Map((launchPage.decorations || []).map(item => [item.claim_id, item]));
      document.querySelectorAll('.audit-mark').forEach(node => {{
        if (node.dataset.tooltipBound === '1') return;
        node.dataset.tooltipBound = '1';
        const claimId = node.getAttribute('data-claim-id');
        if (!claimId) return;
        const decoration = decorations.get(claimId);
        if (!decoration) return;
        const show = (event) => {{
          tooltip.innerHTML = tooltipMarkup(decoration);
          tooltip.hidden = false;
          positionTooltip(node, tooltip);
          event?.stopPropagation?.();
        }};
        const hide = () => {{
          tooltip.hidden = true;
        }};
        node.addEventListener('mouseenter', show);
        node.addEventListener('focus', show);
        node.addEventListener('mouseleave', hide);
        node.addEventListener('blur', hide);
        node.addEventListener('click', show);
      }});
      if (!launchTooltipGlobalsBound) {{
        launchTooltipGlobalsBound = true;
        document.addEventListener('click', (event) => {{
          if (!event.target.closest('.audit-mark') && !event.target.closest('#audit-tooltip')) {{
            tooltip.hidden = true;
          }}
        }});
        document.addEventListener('keydown', (event) => {{
          if (event.key === 'Escape') {{
            tooltip.hidden = true;
          }}
        }});
        window.addEventListener('scroll', () => {{
          tooltip.hidden = true;
        }}, {{ passive: true }});
      }}
    }}
    function tooltipMarkup(decoration) {{
      const citations = decoration.citations || [];
      return `
        <div class="tooltip-label">Original wording</div>
        <p class="wrap">${{esc(decoration.original_text)}}</p>
        <div class="tooltip-label">Why it changed</div>
        <p class="wrap"><strong>${{esc(verdictLabel(decoration.verdict))}}</strong> - ${{esc(decoration.reason)}}</p>
        <div class="tooltip-label">Citations</div>
        <div class="tooltip-citations">
          ${{citations.length ? citations.map(citation => tooltipCitationMarkup(citation)).join('') : '<p class="muted">No explicit reference citations were attached to this claim.</p>'}}
        </div>
      `;
    }}
    function tooltipCitationMarkup(citation) {{
      const href = safeHref(citation.url);
      const titleMarkup = href
        ? `<a href="${{esc(href)}}" target="_blank" rel="noopener noreferrer">${{esc(citation.title)}}</a>`
        : `<strong>${{esc(citation.title)}}</strong>`;
      return `
        <div class="tooltip-citation">
          <p class="wrap">${{titleMarkup}}</p>
          ${{citation.snippet ? `<p class="muted wrap">${{esc(citation.snippet)}}</p>` : ''}}
          ${{citation.why_relevant ? `<p class="muted wrap">${{esc(citation.why_relevant)}}</p>` : ''}}
        </div>
      `;
    }}
    function positionTooltip(target, tooltip) {{
      const rect = target.getBoundingClientRect();
      const margin = 12;
      const desiredTop = rect.bottom + margin;
      const maxLeft = window.innerWidth - tooltip.offsetWidth - margin;
      const left = Math.max(margin, Math.min(rect.left, maxLeft));
      let top = desiredTop;
      if (top + tooltip.offsetHeight > window.innerHeight - margin) {{
        top = Math.max(margin, rect.top - tooltip.offsetHeight - margin);
      }}
      tooltip.style.left = `${{left}}px`;
      tooltip.style.top = `${{top}}px`;
    }}
    const filteredAudits = () => report.audits
      .map((audit, index) => ({{ ...audit, __index: index }}))
      .filter(audit => filters.verdict === 'all' || audit.verdict === filters.verdict);
    function setupFilters() {{
      fillSelect('verdict-filter', 'All verdicts', [...new Set(report.audits.map(audit => audit.verdict))]);
    }}
    function fillSelect(id, allLabel, values) {{
      document.getElementById(id).innerHTML = [
        `<option value="all">${{allLabel}}</option>`,
        ...values.map(value => `<option value="${{esc(value)}}">${{esc(value)}}</option>`)
      ].join('');
    }}
    function syncSelection() {{
      const audits = filteredAudits();
      if (!audits.some(audit => audit.__index === selected)) selected = audits[0]?.__index ?? 0;
    }}
    function render() {{
      const audits = filteredAudits();
      document.getElementById('filter-summary').textContent = `${{audits.length}} of ${{report.audits.length}} claims shown`;
      document.getElementById('claim-list').innerHTML = audits.map((audit, i) => `
        <button class="claim-row ${{audit.__index === selected ? 'active' : ''}}" onclick="selected=${{audit.__index}}; render();">
          <div class="claim-meta">
            <span class="muted">${{esc(audit.verdict)}} · ${{esc(audit.claim.claim_type)}} · score ${{audit.stretch_score}}/100</span>
          </div>
          <div class="wrap">${{esc(audit.claim.claim)}}</div>
          <div class="meter ${{cls(audit.verdict)}}" title="Stretch score ${{audit.stretch_score}} / 100"><div style="width: ${{audit.stretch_score}}%"></div></div>
          <p class="muted wrap">${{esc(audit.claim.why_risky || '')}}</p>
        </button>
      `).join('');
      if (!audits.length) {{
        document.getElementById('claim-detail').innerHTML = '<div class="panel"><p class="muted">No claims match the selected filters.</p></div>';
        document.getElementById('evidence').innerHTML = '';
        return;
      }}
      const audit = audits.find(item => item.__index === selected) ?? audits[0];
      const evidenceCount = audit.supporting_evidence.length + audit.counter_evidence.length;
      const evidenceScore = Math.min(100, evidenceCount * 25);
      const confidence = confidenceScore[audit.confidence] ?? 0;
      const computedChecks = audit.numeric_findings?.length
        ? `<div class="panel"><h3>Computed Checks</h3>${{list(audit.numeric_findings)}}</div>`
        : '';
      const runProfile = report.run_profile
        ? `
            <p class="wrap"><strong>Pipeline wall:</strong> ${{fmtMs(report.run_profile.total_duration_ms)}} · <strong>Load:</strong> ${{fmtMs(report.run_profile.load_document_ms)}} · <strong>Extract:</strong> ${{fmtMs(report.run_profile.extract_claims_ms)}} · <strong>Audit:</strong> ${{fmtMs(report.run_profile.audit_claims_ms)}} · <strong>Contrast:</strong> ${{fmtMs(report.run_profile.contrast_duration_ms)}}</p>
            <p class="wrap"><strong>Claims extracted / audited:</strong> ${{report.run_profile.claims_extracted}} / ${{report.run_profile.claims_audited}} · <strong>Specialist passes:</strong> ${{report.run_profile.agent_passes}} · <strong>Unique sources:</strong> ${{report.run_profile.unique_source_count}}</p>
          `
        : '';
      document.getElementById('claim-detail').innerHTML = `
        <div class="panel">
          <h3>Report Provenance</h3>
          <p class="wrap"><strong>Mode:</strong> ${{esc(report.mode)}} · <strong>Model:</strong> ${{esc(report.model || 'none')}}</p>
          <p class="wrap"><strong>Evidence Contrast:</strong> ${{report.contrast_enabled ? 'enabled' : 'disabled'}}</p>
          <p class="wrap"><strong>Provided reference URLs:</strong> ${{(report.reference_urls || []).length ? (report.reference_urls || []).map(esc).join(', ') : 'none'}}</p>
          ${{runProfile}}
        </div>
        <div class="panel">
          <strong>Formal verdict: ${{esc(audit.verdict)}}</strong> ${{hint(verdictTip(audit.verdict))}}
          <div class="score"><div style="width: ${{audit.stretch_score}}%"></div></div>
          <p class="muted">
            Confidence: ${{esc(audit.confidence)}} ${{hint('Confidence reflects how strongly the available evidence supports this verdict, not whether the original claim is true.')}}
            · Stretch Score: ${{audit.stretch_score}} / 100 ${{hint('Higher means the original wording stretches further beyond what the evidence supports.')}}
            · Evidence items: ${{evidenceCount}} ${{hint('Evidence items are supporting or counter-evidence records attached to this claim.')}}
          </p>
          <div class="strength-grid">
            ${{strengthCard('Stretch pressure', audit.stretch_score, audit.verdict, `${{audit.stretch_score}}/100`, 'How much the wording outruns the evidence.')}}
            ${{strengthCard('Confidence', confidence, audit.verdict, esc(audit.confidence), 'How confident Honest Launches is in this verdict from available evidence.')}}
            ${{strengthCard('Evidence depth', evidenceScore, audit.verdict, `${{evidenceCount}} item${{evidenceCount === 1 ? '' : 's'}}`, 'How much direct evidence is attached to this claim audit.')}}
          </div>
        </div>
        <div class="panel"><h3>Original</h3><p class="wrap">${{esc(audit.claim.claim)}}</p></div>
        ${{contrastCard(audit.contrast)}}
        <div class="panel"><h3>Defensible Rewrite</h3><p class="wrap">${{esc(audit.weaker_supported_rewrite)}}</p></div>
        <div class="panel"><h3>Why</h3><p class="wrap">${{esc(audit.why)}}</p></div>
        ${{claimTimingPanel(audit.claim_timing)}}
        ${{computedChecks}}
        <div class="panel"><h3>Agent Steps</h3>${{agentSteps(audit.agent_outputs || [])}}</div>
      `;
      document.getElementById('evidence').innerHTML = `
        ${{providedReferencesPanel(report.reference_urls || [])}}
        ${{sourcesChecked(audit.contrast)}}
        <div class="panel"><h3>Gemini-Discovered Supporting Sources</h3><p class="muted">Sources found by the verifier while looking for the strongest support for this claim.</p>${{items(audit.supporting_evidence)}}</div>
        <div class="panel"><h3>Gemini-Discovered Caveat / Counter Sources</h3><p class="muted">Sources found by the contradiction-finder while looking for caveats, missing context, benchmark limits, or contrary evidence.</p>${{items(audit.counter_evidence)}}</div>
        <div class="panel"><h3>Missing Context</h3>${{list(audit.missing_context)}}</div>
      `;
    }}
    function strengthCard(label, value, verdict, display, tip) {{
      return `
        <div class="strength-card">
          <div class="strength-label"><span>${{label}} ${{hint(tip)}}</span><span>${{display}}</span></div>
          <div class="meter ${{cls(verdict)}}"><div style="width: ${{value}}%"></div></div>
        </div>
      `;
    }}
    function contrastCard(contrast) {{
      if (!contrast) return '';
      const best = contrast.best_sources?.[0];
      const sourceSummary = best ? best.evidence_summary : 'No usable reference source was available.';
      const qualification = best?.key_qualification ? `<p><strong>Key qualification:</strong> ${{esc(best.key_qualification)}}</p>` : '';
      return `
        <div class="panel">
          <h3>Evidence Contrast</h3>
          <p><strong>Claim says:</strong> <span class="wrap">${{esc(contrast.claim_text)}}</span></p>
          <p><strong>Best reference says:</strong> <span class="wrap">${{esc(sourceSummary)}}</span></p>
          ${{qualification}}
          <p><strong>Delta:</strong> ${{esc(contrast.delta_type)}} — ${{esc(contrast.delta_explanation)}}</p>
          <p><strong>Final verdict:</strong> ${{esc(contrast.recommended_verdict)}} · Confidence: ${{esc(contrast.confidence)}}</p>
          <p><strong>Defensible rewrite:</strong> <span class="wrap">${{esc(contrast.suggested_rewrite)}}</span></p>
        </div>
      `;
    }}
    function claimTimingPanel(timing) {{
      if (!timing) return '';
      return `
        <div class="panel">
          <h3>Claim Timing</h3>
          <p class="muted">Measured wall-clock time for this claim during the run.</p>
          <p><strong>Total:</strong> ${{fmtMs(timing.total_duration_ms)}} · <strong>Contrast:</strong> ${{fmtMs(timing.contrast_ms)}}</p>
          <ul>
            <li class="wrap"><strong>Verifier:</strong> ${{fmtMs(timing.verifier_ms)}}</li>
            <li class="wrap"><strong>Contradiction finder:</strong> ${{fmtMs(timing.contradiction_finder_ms)}}</li>
            <li class="wrap"><strong>Numeric calibrator:</strong> ${{fmtMs(timing.numeric_calibrator_ms)}}</li>
            <li class="wrap"><strong>Aggregator:</strong> ${{fmtMs(timing.aggregator_ms)}}</li>
          </ul>
        </div>
      `;
    }}
    function providedReferencesPanel(values) {{
      if (!values.length) {{
        return `
          <div class="panel">
            <h3>Provided Reference URLs</h3>
            <p class="muted">No explicit reference URLs were provided for this run.</p>
          </div>
        `;
      }}
      return `
        <div class="panel">
          <h3>Provided Reference URLs</h3>
          <p class="muted">Explicit sources supplied on the CLI with <code>--reference</code>. These anchor Evidence Contrast and define the source-of-truth packet for this run.</p>
          ${{plainUrlItems(values)}}
        </div>
      `;
    }}
    function sourcesChecked(contrast) {{
      if (!contrast) return '<div class="panel"><h3>Claim-Level Contrast References</h3><p class="muted">No contrast references checked for this claim. Contrast is applied only to the selected top-risk claims controlled by --contrast-top.</p></div>';
      const references = contrast.reference_sources || [];
      const best = contrast.best_sources || [];
      return `
        <div class="panel">
          <h3>Claim-Level Contrast References</h3>
          <p class="muted">References used by the Evidence Contrast pass for this selected claim. These are anchored by provided reference URLs, but Gemini may resolve nearby canonical pages or source titles while reading them.</p>
          ${{referenceItems(references)}}
        </div>
        <div class="panel">
          <h3>Reference Snippets / Mismatches</h3>
          <p class="muted">Claim-level snippets showing how the referenced source supports, narrows, or conflicts with the original wording.</p>
          ${{contrastSourceItems(best)}}
        </div>
      `;
    }}
    function plainUrlItems(values) {{
      return values.map(value => {{
        const href = safeHref(value);
        const source = href
          ? `<a href="${{esc(href)}}" target="_blank" rel="noopener noreferrer">${{esc(value)}}</a>`
          : `<span class="muted">${{esc(value)}}</span>`;
        return `<div class="source-item"><p class="wrap">${{source}}</p></div>`;
      }}).join('');
    }}
    function referenceItems(values) {{
      if (!values.length) return '<p class="muted">None recorded.</p>';
      return values.map(item => {{
        const href = safeHref(item.url);
        const source = href
          ? `<a href="${{esc(href)}}" target="_blank" rel="noopener noreferrer">${{esc(item.url)}}</a>`
          : `<span class="muted">${{esc(item.url || 'No URL recorded')}}</span>`;
        return `
          <div class="source-item">
            <p><strong>${{esc(item.title)}}</strong> <span class="muted">(${{esc(item.source_type)}} · authority ${{item.authority_score}}/100)</span></p>
            <p class="wrap">${{source}}</p>
            <p class="muted wrap">${{esc(item.why_relevant || '')}}</p>
          </div>
        `;
      }}).join('');
    }}
    function contrastSourceItems(values) {{
      if (!values.length) return '<p class="muted">None recorded.</p>';
      return values.map(item => {{
        const href = safeHref(item.url);
        const source = href
          ? `<a href="${{esc(href)}}" target="_blank" rel="noopener noreferrer">${{esc(item.url)}}</a>`
          : `<span class="muted">${{esc(item.url || 'No URL recorded')}}</span>`;
        return `
          <div class="source-item">
            <p><strong>${{esc(item.title)}}</strong> <span class="muted">(${{esc(item.stance)}})</span></p>
            <p class="wrap">${{esc(item.evidence_summary)}}</p>
            <p class="wrap">${{source}}</p>
            <p class="muted wrap">${{esc(item.key_qualification || '')}}</p>
          </div>
        `;
      }}).join('');
    }}
    function agentSteps(values) {{
      if (!values.length) return '<p class="muted">No agent step trace recorded.</p>';
      return values.map(step => `
        <details>
          <summary>${{esc(step.agent)}} — ${{esc(step.summary)}}</summary>
          <p class="muted">Claim ID: ${{esc(step.claim_id)}}</p>
          <p class="muted">Duration: ${{step.duration_ms == null ? 'not recorded' : fmtMs(step.duration_ms)}}</p>
          <h4>Supporting evidence</h4>
          ${{items(step.supporting_evidence || [])}}
          <h4>Contradictions / narrowing evidence</h4>
          ${{items(step.counter_evidence || [])}}
          <h4>Missing context</h4>
          ${{list(step.missing_context || [])}}
          <h4>Computed checks</h4>
          ${{list(step.numeric_findings || [])}}
        </details>
      `).join('');
    }}
    function list(values) {{
      if (!values.length) return '<p class="muted">None recorded.</p>';
      return `<ul>${{values.map(value => `<li class="wrap">${{esc(value)}}</li>`).join('')}}</ul>`;
    }}
    function items(values) {{
      if (!values.length) return '<p class="muted">None recorded.</p>';
      return values.map(item => {{
        const href = safeHref(item.url);
        const source = href
          ? `<a href="${{esc(href)}}" target="_blank" rel="noopener noreferrer">${{esc(item.url)}}</a>`
          : `<span class="muted">${{esc(item.url || 'No URL recorded')}}</span>`;
        return `
          <div class="source-item">
            <p><strong>${{esc(item.source_title)}}</strong></p>
            <p class="wrap">${{esc(item.snippet)}}</p>
            <p class="wrap">${{source}}</p>
            <p class="muted wrap">${{esc(item.relevance || '')}}</p>
          </div>
        `;
      }}).join('');
    }}
    setupFilters();
    renderPublicationHeader();
    renderHeadline();
    render();
    setView(activeView);
    window.addEventListener('hashchange', () => {{
      const nextView = window.location.hash === '#ledger' ? 'ledger' : 'launch';
      if (nextView !== activeView) {{
        setView(nextView);
      }}
    }});
  </script>
</body>
</html>
"""
    path.write_text(markup, encoding="utf-8")


def _audit_markdown(audit: ClaimAudit) -> list[str]:
    lines = [
        "",
        f"## {audit.claim.id}: {audit.verdict.value}",
        "",
        f"**Confidence:** {audit.confidence}",
        "",
        f"**Original:** {audit.claim.claim}",
        "",
        f"**Stretch Score:** {audit.stretch_score}/100",
        "",
        f"**Why:** {audit.why}",
        "",
        f"**Defensible rewrite:** {audit.weaker_supported_rewrite}",
        "",
    ]
    if audit.claim_timing:
        lines.extend(
            [
                "**Claim timing:**",
                (
                    f"- Total / Verifier / Contradiction / Numeric / Aggregator / Contrast: "
                    f"{_format_duration_ms(audit.claim_timing.total_duration_ms)} / "
                    f"{_format_duration_ms(audit.claim_timing.verifier_ms)} / "
                    f"{_format_duration_ms(audit.claim_timing.contradiction_finder_ms)} / "
                    f"{_format_duration_ms(audit.claim_timing.numeric_calibrator_ms)} / "
                    f"{_format_duration_ms(audit.claim_timing.aggregator_ms)} / "
                    f"{_format_duration_ms(audit.claim_timing.contrast_ms)}"
                ),
                "",
            ]
        )
    if audit.agent_outputs:
        lines.extend(_agent_outputs_markdown(audit))
    if audit.contrast:
        lines.extend(_contrast_markdown(audit))
    if audit.numeric_findings:
        lines.append("**Computed checks:**")
        lines.extend(f"- {finding}" for finding in audit.numeric_findings)
        lines.append("")
    if audit.supporting_evidence:
        lines.append("**Gemini-discovered supporting sources:**")
        lines.extend(_evidence_markdown_item(item) for item in audit.supporting_evidence)
        lines.append("")
    if audit.counter_evidence:
        lines.append("**Gemini-discovered caveat / counter sources:**")
        lines.extend(_evidence_markdown_item(item) for item in audit.counter_evidence)
        lines.append("")
    if audit.missing_context:
        lines.append("**Missing context:**")
        lines.extend(f"- {item}" for item in audit.missing_context)
        lines.append("")
    return lines


def _agent_outputs_markdown(audit: ClaimAudit) -> list[str]:
    lines = ["### Agent Steps", ""]
    for step in audit.agent_outputs:
        lines.extend(
            [
                f"<details><summary>{step.agent}: {step.summary}</summary>",
                "",
            ]
        )
        if step.duration_ms is not None:
            lines.extend([f"**Duration:** {_format_duration_ms(step.duration_ms)}", ""])
        if step.supporting_evidence:
            lines.append("**Supporting evidence:**")
            lines.extend(_evidence_markdown_item(item) for item in step.supporting_evidence)
            lines.append("")
        if step.counter_evidence:
            lines.append("**Contradictions / narrowing evidence:**")
            lines.extend(_evidence_markdown_item(item) for item in step.counter_evidence)
            lines.append("")
        if step.missing_context:
            lines.append("**Missing context:**")
            lines.extend(f"- {item}" for item in step.missing_context)
            lines.append("")
        if step.numeric_findings:
            lines.append("**Computed checks:**")
            lines.extend(f"- {finding}" for finding in step.numeric_findings)
            lines.append("")
        lines.extend(["</details>", ""])
    return lines


def _contrast_markdown(audit: ClaimAudit) -> list[str]:
    contrast = audit.contrast
    if not contrast:
        return []
    lines = [
        "### Evidence Contrast",
        "",
        f"**Claim says:** {contrast.claim_text}",
        "",
    ]
    if contrast.best_sources:
        best = contrast.best_sources[0]
        lines.extend(
            [
                f"**Best reference says:** {best.evidence_summary}",
                "",
            ]
        )
        if best.key_qualification:
            lines.extend([f"**Key qualification:** {best.key_qualification}", ""])
    else:
        lines.extend(["**Best reference says:** No usable reference source was available.", ""])
    lines.extend(
        [
            f"**Delta:** {contrast.delta_type} — {contrast.delta_explanation}",
            "",
            f"**Final verdict:** {contrast.recommended_verdict.value}",
            "",
            f"**Defensible rewrite:** {contrast.suggested_rewrite}",
            "",
            "### Claim-Level Contrast References",
            "",
        ]
    )
    if contrast.reference_sources:
        for source in contrast.reference_sources:
            source_url = source.url or "internal fixture source"
            lines.append(
                f"- {source.title} ({source.source_type}, authority {source.authority_score}/100): {source_url}. "
                f"{source.why_relevant}"
            )
        lines.append("")
    else:
        lines.extend(["- None recorded.", ""])
    if contrast.best_sources:
        lines.append("**Reference snippets / mismatches:**")
        for source in contrast.best_sources:
            source_url = source.url or "internal fixture source"
            lines.append(
                f"- {source.evidence_summary} ({source.title}, {source.stance}, {source_url}). "
                f"{source.key_qualification}"
            )
        lines.append("")
    return lines


def _evidence_markdown_item(item) -> str:
    source = item.source_title
    if item.url:
        source = f"[{item.source_title}]({item.url})"
    suffix = f" Relevance: {item.relevance}" if item.relevance else ""
    return f"- {item.snippet} ({source}).{suffix}"


def _build_launch_page_data(report: AuditReport) -> dict[str, object]:
    if report.launch_page is not None:
        return report.launch_page.model_dump(exclude_none=True)
    snapshot = report.document.snapshot
    return {
        "source_title": report.document.title,
        "source_url": report.document.source,
        "blocks": snapshot.model_dump(exclude_none=True).get("blocks", []) if snapshot else [],
        "decorations": [],
        "rewritten_claim_count": 0,
        "explicit_reference_count": len(report.reference_urls),
        "primary_view": "audited_launch_page",
    }


def _verdict_counts(report: AuditReport) -> dict[str, int]:
    counts = {
        "supported": 0,
        "overstated": 0,
        "missing_context": 0,
        "contradicted": 0,
        "not_checkable": 0,
    }
    for audit in report.audits:
        key = audit.verdict.value
        if key in counts:
            counts[key] += 1
    return counts


def _average_stretch(audits: list[ClaimAudit]) -> int:
    if not audits:
        return 0
    return round(sum(audit.stretch_score for audit in audits) / len(audits))


def _format_duration_ms(duration_ms: int) -> str:
    if duration_ms >= 1000:
        return f"{duration_ms / 1000:.2f}s"
    return f"{duration_ms}ms"
