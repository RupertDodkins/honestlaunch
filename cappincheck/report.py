from __future__ import annotations

import html
import json
from pathlib import Path

from .schemas import AuditReport, ClaimAudit


def write_json(report: AuditReport, path: Path) -> None:
    path.write_text(report.model_dump_json(indent=2), encoding="utf-8")


def write_markdown(report: AuditReport, path: Path) -> None:
    lines = [
        f"# CappinCheck Report: {report.document.title}",
        "",
        f"Source: `{report.document.source}`",
        "",
        "| Claim | Vibe | Formal Verdict | Cap Score | Confidence |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for audit in report.audits:
        lines.append(
            f"| {audit.claim.claim} | {audit.vibe} | {audit.verdict.value} | {audit.cap_score} | {audit.confidence} |"
        )

    for audit in report.audits:
        lines.extend(_audit_markdown(audit))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(report: AuditReport, path: Path) -> None:
    data = json.dumps(report.model_dump(), indent=2).replace("</", "<\\/")
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
      --cap: #b42318;
      --sus: #b54708;
      --nocap: #067647;
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
      display: grid;
      grid-template-columns: 360px minmax(0, 1fr) 380px;
      min-height: calc(100vh - 74px);
    }}
    aside, section {{ padding: 18px; border-right: 1px solid var(--line); }}
    section:last-child {{ border-right: 0; }}
    .filters {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin: 14px 0;
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
      margin-bottom: 10px;
      cursor: pointer;
      overflow-wrap: anywhere;
    }}
    .claim-row.active {{ border-color: var(--ink); box-shadow: 0 0 0 2px rgba(31,35,40,.08); }}
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
    .badge.cap {{ background: var(--cap); }}
    .badge.sus {{ background: var(--sus); }}
    .badge.no-cap, .badge.mostly-no-cap {{ background: var(--nocap); }}
    .badge.needs-receipts {{ background: var(--receipts); }}
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
    .score > div {{ height: 100%; background: var(--cap); }}
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
    .meter.cap > div {{ background: var(--cap); }}
    .meter.sus > div {{ background: var(--sus); }}
    .meter.no-cap > div, .meter.mostly-no-cap > div {{ background: var(--nocap); }}
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
    pre {{
      white-space: pre-wrap;
      background: #0d1117;
      color: #f0f6fc;
      padding: 12px;
      border-radius: 8px;
      max-height: 260px;
      overflow: auto;
    }}
    @media (max-width: 980px) {{
      main {{ grid-template-columns: 1fr; }}
      aside, section {{ border-right: 0; border-bottom: 1px solid var(--line); }}
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
    <div class="muted">{len(report.audits)} audited claims</div>
  </header>
  <main>
    <aside>
      <h2>Claim Ledger</h2>
      <div class="filters">
        <label>Vibe
          <select id="vibe-filter" onchange="filters.vibe=this.value; syncSelection(); render();"></select>
        </label>
        <label>Verdict
          <select id="verdict-filter" onchange="filters.verdict=this.value; syncSelection(); render();"></select>
        </label>
      </div>
      <p class="muted" id="filter-summary"></p>
      <div id="claim-list"></div>
    </aside>
    <section>
      <h2>Selected Claim</h2>
      <div id="claim-detail"></div>
    </section>
    <section>
      <h2>Evidence Stack</h2>
      <div id="evidence"></div>
      <h3>Raw JSON</h3>
      <pre id="raw"></pre>
    </section>
  </main>
  <script>
    const report = {data};
    let selected = 0;
    const filters = {{ vibe: 'all', verdict: 'all' }};
    const cls = (vibe) => String(vibe).replaceAll(' ', '-');
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
    const filteredAudits = () => report.audits
      .map((audit, index) => ({{ ...audit, __index: index }}))
      .filter(audit => filters.vibe === 'all' || audit.vibe === filters.vibe)
      .filter(audit => filters.verdict === 'all' || audit.verdict === filters.verdict);
    function setupFilters() {{
      fillSelect('vibe-filter', 'All vibes', [...new Set(report.audits.map(audit => audit.vibe))]);
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
            <span class="badge ${{cls(audit.vibe)}}">${{esc(audit.vibe)}}</span>
            <span class="muted">${{esc(audit.verdict)}} · ${{esc(audit.claim.claim_type)}}</span>
          </div>
          <div class="wrap">${{esc(audit.claim.claim)}}</div>
          <div class="meter ${{cls(audit.vibe)}}" title="Cap score ${{audit.cap_score}} / 100"><div style="width: ${{audit.cap_score}}%"></div></div>
        </button>
      `).join('');
      if (!audits.length) {{
        document.getElementById('claim-detail').innerHTML = '<div class="panel"><p class="muted">No claims match the selected filters.</p></div>';
        document.getElementById('evidence').innerHTML = '';
        document.getElementById('raw').textContent = '';
        return;
      }}
      const audit = audits.find(item => item.__index === selected) ?? audits[0];
      const evidenceCount = audit.supporting_evidence.length + audit.counter_evidence.length;
      const evidenceScore = Math.min(100, evidenceCount * 25);
      const confidence = confidenceScore[audit.confidence] ?? 0;
      document.getElementById('claim-detail').innerHTML = `
        <div class="panel">
          <span class="badge ${{cls(audit.vibe)}}">${{esc(audit.vibe)}}</span>
          <strong>${{esc(audit.verdict)}}</strong>
          <div class="score"><div style="width: ${{audit.cap_score}}%"></div></div>
          <p class="muted">Cap Score: ${{audit.cap_score}} / 100 · Confidence: ${{esc(audit.confidence)}} · Evidence items: ${{evidenceCount}}</p>
          <div class="strength-grid">
            ${{strengthCard('Cap pressure', audit.cap_score, audit.vibe, `${{audit.cap_score}}/100`)}}
            ${{strengthCard('Confidence', confidence, audit.vibe, esc(audit.confidence))}}
            ${{strengthCard('Evidence depth', evidenceScore, audit.vibe, `${{evidenceCount}} item${{evidenceCount === 1 ? '' : 's'}}`)}}
          </div>
        </div>
        <div class="panel"><h3>Original</h3><p class="wrap">${{esc(audit.claim.claim)}}</p></div>
        <div class="panel"><h3>Defensible Rewrite</h3><p class="wrap">${{esc(audit.weaker_supported_rewrite)}}</p></div>
        <div class="panel"><h3>Why</h3><p class="wrap">${{esc(audit.why)}}</p></div>
        <div class="panel"><h3>Numeric Findings</h3>${{list(audit.numeric_findings)}}</div>
      `;
      document.getElementById('evidence').innerHTML = `
        <div class="panel"><h3>Supporting</h3>${{items(audit.supporting_evidence)}}</div>
        <div class="panel"><h3>Counter</h3>${{items(audit.counter_evidence)}}</div>
        <div class="panel"><h3>Missing Context</h3>${{list(audit.missing_context)}}</div>
      `;
      document.getElementById('raw').textContent = JSON.stringify(audit, null, 2);
    }}
    function strengthCard(label, value, vibe, display) {{
      return `
        <div class="strength-card">
          <div class="strength-label"><span>${{label}}</span><span>${{display}}</span></div>
          <div class="meter ${{cls(vibe)}}"><div style="width: ${{value}}%"></div></div>
        </div>
      `;
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
        f"## {audit.claim.id}: {audit.vibe} / {audit.verdict.value}",
        "",
        f"**Original:** {audit.claim.claim}",
        "",
        f"**Cap Score:** {audit.cap_score}/100",
        "",
        f"**Why:** {audit.why}",
        "",
        f"**Defensible rewrite:** {audit.weaker_supported_rewrite}",
        "",
    ]
    if audit.numeric_findings:
        lines.append("**Numeric findings:**")
        lines.extend(f"- {finding}" for finding in audit.numeric_findings)
        lines.append("")
    if audit.supporting_evidence:
        lines.append("**Supporting evidence:**")
        lines.extend(f"- {item.snippet} ({item.source_title})" for item in audit.supporting_evidence)
        lines.append("")
    if audit.counter_evidence:
        lines.append("**Counter-evidence:**")
        lines.extend(f"- {item.snippet} ({item.source_title})" for item in audit.counter_evidence)
        lines.append("")
    if audit.missing_context:
        lines.append("**Missing context:**")
        lines.extend(f"- {item}" for item in audit.missing_context)
        lines.append("")
    return lines
