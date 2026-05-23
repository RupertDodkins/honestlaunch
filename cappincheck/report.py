from __future__ import annotations

import html
import json
from pathlib import Path

from .schemas import AuditReport, ClaimAudit


def write_json(report: AuditReport, path: Path) -> None:
    path.write_text(report.model_dump_json(indent=2, exclude_none=True), encoding="utf-8")


def write_markdown(report: AuditReport, path: Path) -> None:
    lines = [
        f"# CappinCheck Report: {report.document.title}",
        "",
        f"Source: `{report.document.source}`",
        "",
        "## Provenance",
        "",
        f"- Mode: `{report.mode}`",
        f"- Runtime: `{report.runtime}`",
        f"- Model: `{report.model or 'none'}`",
        f"- Evidence Contrast: `{'enabled' if report.contrast_enabled else 'disabled'}`",
        f"- Reference URLs: {', '.join(f'`{url}`' for url in report.reference_urls) if report.reference_urls else '`none`'}",
        "",
        "| Claim | Formal Verdict | Confidence | Stretch Score |",
        "| --- | --- | --- | ---: |",
    ]
    for audit in report.audits:
        lines.append(
            f"| {audit.claim.claim} | {audit.verdict.value} | {audit.confidence} | {audit.stretch_score} |"
        )

    for audit in report.audits:
        lines.extend(_audit_markdown(audit))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(report: AuditReport, path: Path) -> None:
    data = json.dumps(report.model_dump(exclude_none=True), indent=2).replace("</", "<\\/")
    markup = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CappinCheck Report</title>
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
    h1 {{ margin: 0; font-size: 24px; letter-spacing: 0; }}
    main {{
      min-height: calc(100vh - 74px);
    }}
    .claim-strip {{
      padding: 16px 18px;
      border-bottom: 1px solid var(--line);
      background: var(--bg);
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
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>CappinCheck</h1>
      <div class="muted">{html.escape(report.document.title)}</div>
    </div>
    <div class="muted">{len(report.audits)} audited claims · {html.escape(report.mode)} · {html.escape(report.runtime)}</div>
  </header>
  <main>
    <div class="claim-strip">
      <div class="title-row">
        <h2>Claim Ledger</h2>
        <span class="hint" tabindex="0" data-tip="Gemini extracts risky factual claims, then CappinCheck audits the selected claims. Click a card to inspect verdict, evidence, contrast, and agent steps.">?</span>
      </div>
      <div class="filters single">
        <label>Verdict
          <span class="hint" tabindex="0" data-tip="Formal verdict used in JSON/Markdown: supported, overstated, missing context, contradicted, or not checkable.">?</span>
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
          <span class="hint" tabindex="0" data-tip="This panel shows the selected claim, CappinCheck verdict, and strongest defensible rewrite.">?</span>
        </div>
        <div id="claim-detail"></div>
      </section>
      <section>
        <div class="title-row">
          <h2>Sources Checked</h2>
          <span class="hint" tabindex="0" data-tip="Sources checked includes contrast references, supporting evidence, narrowing evidence, and missing context.">?</span>
        </div>
        <div id="evidence"></div>
      </section>
    </div>
  </main>
  <script>
    const report = {data};
    let selected = 0;
    const filters = {{ verdict: 'all' }};
    const cls = (value) => String(value).replaceAll('_', '-').replaceAll(' ', '-');
    const confidenceScore = {{ low: 34, medium: 67, high: 100 }};
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
      document.getElementById('claim-detail').innerHTML = `
        <div class="panel">
          <h3>Report Provenance</h3>
          <p class="wrap"><strong>Mode:</strong> ${{esc(report.mode)}} · <strong>Runtime:</strong> ${{esc(report.runtime)}} · <strong>Model:</strong> ${{esc(report.model || 'none')}}</p>
          <p class="wrap"><strong>Evidence Contrast:</strong> ${{report.contrast_enabled ? 'enabled' : 'disabled'}}</p>
          <p class="wrap"><strong>Reference URLs:</strong> ${{(report.reference_urls || []).length ? (report.reference_urls || []).map(esc).join(', ') : 'none'}}</p>
        </div>
        <div class="panel">
          <strong>Formal verdict: ${{esc(audit.verdict)}}</strong>
          <div class="score"><div style="width: ${{audit.stretch_score}}%"></div></div>
          <p class="muted">
            Confidence: ${{esc(audit.confidence)}} ${{hint('Confidence reflects how strongly the available evidence supports this verdict, not whether the original claim is true.')}}
            · Stretch Score: ${{audit.stretch_score}} / 100 ${{hint('Higher means the original wording stretches further beyond what the evidence supports.')}}
            · Evidence items: ${{evidenceCount}} ${{hint('Evidence items are supporting or counter-evidence records attached to this claim.')}}
          </p>
          <div class="strength-grid">
            ${{strengthCard('Stretch pressure', audit.stretch_score, audit.verdict, `${{audit.stretch_score}}/100`, 'How much the wording outruns the evidence.')}}
            ${{strengthCard('Confidence', confidence, audit.verdict, esc(audit.confidence), 'How confident CappinCheck is in this verdict from available evidence.')}}
            ${{strengthCard('Evidence depth', evidenceScore, audit.verdict, `${{evidenceCount}} item${{evidenceCount === 1 ? '' : 's'}}`, 'How much direct evidence is attached to this claim audit.')}}
          </div>
        </div>
        <div class="panel"><h3>Original</h3><p class="wrap">${{esc(audit.claim.claim)}}</p></div>
        ${{contrastCard(audit.contrast)}}
        <div class="panel"><h3>Defensible Rewrite</h3><p class="wrap">${{esc(audit.weaker_supported_rewrite)}}</p></div>
        <div class="panel"><h3>Why</h3><p class="wrap">${{esc(audit.why)}}</p></div>
        <div class="panel"><h3>Numeric Findings</h3>${{list(audit.numeric_findings)}}</div>
        <div class="panel"><h3>Agent Steps</h3>${{agentSteps(audit.agent_outputs || [])}}</div>
      `;
      document.getElementById('evidence').innerHTML = `
        ${{sourcesChecked(audit.contrast)}}
        <div class="panel"><h3>Supporting Evidence Found</h3>${{items(audit.supporting_evidence)}}</div>
        <div class="panel"><h3>Contradictions / Narrowing Evidence</h3>${{items(audit.counter_evidence)}}</div>
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
    function sourcesChecked(contrast) {{
      if (!contrast) return '<div class="panel"><h3>Evidence Contrast References</h3><p class="muted">No contrast references checked for this claim. Contrast is applied only to the selected top-risk claims controlled by --contrast-top.</p></div>';
      const references = contrast.reference_sources || [];
      const best = contrast.best_sources || [];
      return `
        <div class="panel">
          <h3>Evidence Contrast References</h3>
          ${{referenceItems(references)}}
        </div>
        <div class="panel">
          <h3>Reference Snippets / Mismatches</h3>
          ${{contrastSourceItems(best)}}
        </div>
      `;
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
          <h4>Supporting evidence</h4>
          ${{items(step.supporting_evidence || [])}}
          <h4>Contradictions / narrowing evidence</h4>
          ${{items(step.counter_evidence || [])}}
          <h4>Missing context</h4>
          ${{list(step.missing_context || [])}}
          <h4>Numeric findings</h4>
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
    render();
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
    if audit.agent_outputs:
        lines.extend(_agent_outputs_markdown(audit))
    if audit.contrast:
        lines.extend(_contrast_markdown(audit))
    if audit.numeric_findings:
        lines.append("**Numeric findings:**")
        lines.extend(f"- {finding}" for finding in audit.numeric_findings)
        lines.append("")
    if audit.supporting_evidence:
        lines.append("**Supporting evidence found:**")
        lines.extend(_evidence_markdown_item(item) for item in audit.supporting_evidence)
        lines.append("")
    if audit.counter_evidence:
        lines.append("**Contradictions / narrowing evidence:**")
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
            lines.append("**Numeric findings:**")
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
            "### Sources Checked",
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
