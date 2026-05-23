from __future__ import annotations

import html
import json
from pathlib import Path

from .schemas import AuditReport, ClaimAudit


def write_json(report: AuditReport, path: Path) -> None:
    path.write_text(report.model_dump_json(indent=2), encoding="utf-8")


def write_markdown(report: AuditReport, path: Path) -> None:
    lines = [
        f"# ClaimLens Report: {report.document.title}",
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
    data = json.dumps(report.model_dump(), indent=2)
    markup = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ClaimLens Report</title>
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
    .claim-row {{
      width: 100%;
      text-align: left;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 10px;
      cursor: pointer;
    }}
    .claim-row.active {{ border-color: var(--ink); box-shadow: 0 0 0 2px rgba(31,35,40,.08); }}
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
    .muted {{ color: var(--muted); }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 14px;
    }}
    .score {{
      height: 10px;
      background: #eaecf0;
      border-radius: 999px;
      overflow: hidden;
      margin-top: 8px;
    }}
    .score > div {{ height: 100%; background: var(--cap); }}
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
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>ClaimLens</h1>
      <div class="muted">{html.escape(report.document.title)}</div>
    </div>
    <div class="muted">{len(report.audits)} audited claims</div>
  </header>
  <main>
    <aside>
      <h2>Claim Ledger</h2>
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
    const cls = (vibe) => vibe.replaceAll(' ', '-');
    function render() {{
      const audits = report.audits;
      document.getElementById('claim-list').innerHTML = audits.map((audit, i) => `
        <button class="claim-row ${{i === selected ? 'active' : ''}}" onclick="selected=${{i}}; render();">
          <span class="badge ${{cls(audit.vibe)}}">${{audit.vibe}}</span>
          <span class="muted">${{audit.claim.claim_type}}</span>
          <div>${{audit.claim.claim}}</div>
        </button>
      `).join('');
      const audit = audits[selected];
      document.getElementById('claim-detail').innerHTML = `
        <div class="panel">
          <span class="badge ${{cls(audit.vibe)}}">${{audit.vibe}}</span>
          <strong>${{audit.verdict}}</strong>
          <div class="score"><div style="width: ${{audit.cap_score}}%"></div></div>
          <p class="muted">Cap Score: ${{audit.cap_score}} / 100 · Confidence: ${{audit.confidence}}</p>
        </div>
        <div class="panel"><h3>Original</h3><p>${{audit.claim.claim}}</p></div>
        <div class="panel"><h3>Defensible Rewrite</h3><p>${{audit.weaker_supported_rewrite}}</p></div>
        <div class="panel"><h3>Why</h3><p>${{audit.why}}</p></div>
        <div class="panel"><h3>Numeric Findings</h3><ul>${{audit.numeric_findings.map(x => `<li>${{x}}</li>`).join('')}}</ul></div>
      `;
      document.getElementById('evidence').innerHTML = `
        <div class="panel"><h3>Supporting</h3>${{items(audit.supporting_evidence)}}</div>
        <div class="panel"><h3>Counter</h3>${{items(audit.counter_evidence)}}</div>
        <div class="panel"><h3>Missing Context</h3><ul>${{audit.missing_context.map(x => `<li>${{x}}</li>`).join('')}}</ul></div>
      `;
      document.getElementById('raw').textContent = JSON.stringify(audit, null, 2);
    }}
    function items(values) {{
      if (!values.length) return '<p class="muted">None recorded.</p>';
      return values.map(item => `<p><strong>${{item.source_title}}</strong><br>${{item.snippet}}<br><span class="muted">${{item.url || ''}}</span></p>`).join('');
    }}
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

