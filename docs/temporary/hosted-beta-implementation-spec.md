# Hosted Beta Implementation Spec

Status: deferred implementation spec for a later hosted live-generation beta.

This is no longer the current product priority.

Current sequencing decision:

- `V1`: pre-generated, reviewed, static audited launch-page archive
- `V2`: disclosure benchmark built on top of that archive
- `V3` or later: revisit hosted live generation if it is still strategically useful

## Goal

Enable a live demo flow where a user can:

1. Paste a public launch-post URL.
2. Submit without creating an account.
3. Wait on a progress page.
4. Receive a shareable audited launch page plus audit ledger.

The first release should optimize for:

- low friction
- low operational complexity
- low platform cost
- bounded abuse risk
- reuse of the current Python audit engine

This document should be read as a later-path option, not the active implementation plan for the repo right now.

## Non-Goals For V1

- no ads
- no user accounts
- no multi-tenant billing
- no arbitrary unlimited usage on the platform key
- no promise of pixel-perfect cloning for every website
- no "bring your own Gemini key" flow in the first release

## Why Not BYO Key First

`BYO key` looks simpler on paper, but it complicates the actual product:

- many users will not already have a working Gemini key
- invalid keys, missing billing, and quota failures become the first user experience
- asynchronous jobs become harder because the worker must access the user secret later
- honest deletion guarantees require either:
  - synchronous in-request execution, or
  - encrypted temporary storage plus TTL cleanup

Recommendation:

- V1 uses the platform key with hard caps.
- V2 adds `BYO key` only if public demand exceeds the platform budget.

## Constraints And Principles Applied

- Keep the existing Python pipeline as the single source of truth.
- Add a thin web product around the current engine instead of rebuilding the audit logic in JavaScript.
- Use asynchronous jobs even though current runs fit within normal request timeouts.
- Keep the first beta limited to domains and page types the current fetcher can realistically handle.
- Treat "public launch URL" and "arbitrary modern website" as different support levels.

## Current Capability Verification

Backend audit pipeline: `Yes`

- CLI entry: `honestlaunch/cli.py`
- document fetch and normalization: `honestlaunch/ingest.py`
- source snapshot extraction: `honestlaunch/source_snapshot.py`
- claim extraction and audit: `honestlaunch/claims.py`, `honestlaunch/audit.py`
- audited launch-page enrichment: `honestlaunch/anchor_map.py`, `honestlaunch/citations.py`
- static HTML output: `honestlaunch/report.py`

Hosted job orchestration: `No`

- no API service
- no queue
- no persistent job store
- no artifact hosting surface

Frontend product surface: `No`

- no URL form
- no progress page
- no hosted report route

Anonymous abuse protection: `No`

- no rate limiting
- no captcha / bot challenge
- no per-IP quotas

Key handling for `BYO key`: `No`

- no transient secret handling
- no encryption-at-rest flow
- no TTL cleanup for secrets

Visual fidelity to original pages: `Partial`

- content structure preservation exists
- exact DOM and style preservation does not

## Recommended Product Shape

### V1 Product Contract

Public beta, no login, platform key only, hard platform limits.

User flow:

1. User pastes a launch URL.
2. User optionally edits auto-filled reference URLs.
3. User passes Turnstile.
4. System creates an async audit job.
5. User waits on a live status page.
6. On success, system redirects to the shareable report URL.

Scope limits:

- article-style HTML pages and public PDFs only
- best results on supported launch domains
- no arbitrary JS-heavy app surfaces yet
- default `limit=3` audited claims
- default `contrast_top=1`
- one reference preset for known domains

### Supported Domain Classes

Supported now:

- public article-like HTML pages that the current `httpx` fetcher can read
- public PDFs
- known launch domains with stable article structure

Partial:

- pages with interactive sections or repeated UI blocks
- pages that need domain-specific reference presets

Not supported in V1:

- login-required pages
- JS-only pages where server fetch returns shell HTML
- Cloudflare-blocked pages without proxy input
- pages whose main value is visual layout rather than textual claims

## Cheapest Sensible Hosting Stack

Recommendation:

- one Python web app deployed to Cloud Run
- Firestore for job metadata
- Cloud Tasks for async job dispatch
- Cloud Storage for HTML and JSON artifacts
- Cloudflare Turnstile for anonymous-submit abuse reduction

Why this stack:

- it keeps the existing Python engine intact
- Cloud Run already fits long-ish Python request workloads
- Cloud Tasks is designed for asynchronous HTTP work dispatch
- Firestore gives simple status documents plus TTL support
- Cloud Storage is a natural place for generated reports

## External Service Notes

- Cloud Run services default to a `5 minute` request timeout and can be extended to `60 minutes`; Google recommends retry-safe design for longer requests, which supports using async jobs rather than long browser-held requests. Inference: even though current Gemini runs are around `2-3 minutes`, the browser UX should still poll a job rather than hold the original submit request open. Source: [Cloud Run request timeout docs](https://cloud.google.com/run/docs/configuring/request-timeout?authuser=002).
- Cloud Tasks is explicitly for asynchronous work outside a user request and can target arbitrary HTTP endpoints. Source: [Cloud Tasks docs](https://cloud.google.com/tasks/docs?hl=en_US).
- Firestore TTL can automatically remove stale job metadata, though deletion is usually within `24 hours` after expiration rather than exactly at expiration. Source: [Firestore TTL docs](https://docs.cloud.google.com/firestore/docs/ttl).
- Turnstile tokens must be server-side validated, expire after `5 minutes`, and can only be redeemed once. Source: [Turnstile token validation docs](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/).

## System Architecture

### Services

`web` service on Cloud Run

- serves the landing page
- accepts job submissions
- serves progress polling
- serves completed report pages

`worker` endpoint on the same Cloud Run service

- invoked only by Cloud Tasks
- runs the actual audit pipeline
- writes artifacts
- updates job status

One deployable service is enough for the first release.

### Storage

Firestore collections:

- `jobs`
- `rate_limits` if Firestore-backed quotas are used

Cloud Storage objects:

- `reports/{job_id}/report.html`
- `reports/{job_id}/report.json`
- optional `reports/{job_id}/report.md`

### Internal Module Refactor

Add one shared pipeline module so CLI and web use the same logic:

- new `honestlaunch/pipeline.py`

Suggested interface:

```python
def run_audit_pipeline(
    source: str,
    *,
    runtime: str,
    limit: int,
    contrast: bool,
    reference_urls: list[str],
    contrast_top: int,
    mock: bool = False,
) -> AuditReport:
    ...
```

`cli.py` should call this module.

The hosted worker should also call this module.

Do not shell out to `python -m honestlaunch.cli` from the web app.

## Backend API

### `POST /api/jobs`

Creates an audit job.

Request body:

```json
{
  "url": "https://example.com/launch-post",
  "referenceUrls": ["https://example.com/model-card"],
  "turnstileToken": "token"
}
```

Validation:

- require `http` or `https`
- reject unsupported schemes
- reject oversized URL strings
- validate Turnstile token
- normalize domain
- optionally auto-fill references if none were provided and the domain has a preset

Response:

```json
{
  "jobId": "job_123",
  "status": "queued",
  "statusUrl": "/api/jobs/job_123",
  "reportUrl": "/r/job_123"
}
```

### `GET /api/jobs/:job_id`

Returns status and progress.

Response shape:

```json
{
  "jobId": "job_123",
  "status": "queued | fetching | auditing | rendering | succeeded | failed | expired",
  "message": "Extracting risky claims",
  "progressStep": 2,
  "progressTotal": 4,
  "reportUrl": "/r/job_123",
  "error": null
}
```

### `GET /r/:job_id`

Serves the final HTML report if complete.

Behavior:

- if `succeeded`, stream the saved HTML artifact
- if not complete, redirect to the job progress page
- if expired or missing, return a clear not-found page

### `GET /api/jobs/:job_id/artifacts`

Optional debug endpoint for internal use.

Returns JSON artifact metadata only.

Do not expose raw internal traces by default.

## Job Lifecycle

### Firestore Job Document

Suggested fields:

- `job_id`
- `status`
- `input_url`
- `normalized_domain`
- `reference_urls`
- `mode`: `platform`
- `created_at`
- `updated_at`
- `expires_at`
- `request_ip_hash`
- `user_agent_hash`
- `error_code`
- `error_message`
- `artifact_html_path`
- `artifact_json_path`
- `audit_limit`
- `contrast_top`
- `runtime_profile_summary`

### State Machine

`queued`

- job created
- task enqueued

`fetching`

- load document
- build source snapshot

`auditing`

- extract claims
- run audits
- enrich report

`rendering`

- write JSON
- write HTML
- upload artifacts

`succeeded`

- report available

`failed`

- user-visible failure reason recorded

`expired`

- artifact no longer available

## Worker Behavior

Cloud Task target:

- `POST /internal/run-job`

Request body:

```json
{
  "jobId": "job_123"
}
```

Worker steps:

1. Load job document.
2. Transition to `fetching`.
3. Run the shared pipeline module.
4. Transition to `rendering`.
5. Save artifacts to Cloud Storage.
6. Update Firestore with artifact paths and summary.
7. Transition to `succeeded`.

Failure behavior:

- catch pipeline exceptions
- store compact public-safe error message
- set `failed`
- never expose raw secrets or request headers

## Frontend Pages And States

### Landing Page

Components:

- URL input
- optional reference URL editor
- Turnstile widget
- submit button
- short note:
  - best on supported launch posts
  - reports expire after a limited time

### Progress Page

States:

- `queued`
- `fetching`
- `auditing`
- `rendering`
- `succeeded`
- `failed`

UI elements:

- source URL
- current step
- spinner / progress bar
- job retry link on failure

### Report Page

Use the existing audited HTML report.

Keep:

- audited launch page default tab
- audit ledger secondary tab

Add a small hosted header above the report only if needed:

- `Original page`
- `JSON`
- `Run another audit`

## Rate Limiting And Abuse Rules

### Initial Rules

- Turnstile required for every anonymous submission
- `1` active job per IP
- `3` successful or failed submissions per IP per hour
- `10` submissions per IP per day
- `1` worker task running per instance
- `max_instances=1` or `2` at launch to cap spend

### Request Caps

- max supported page size by response bytes
- max `3` audited claims
- max `2` reference URLs
- reject unsupported domains if they repeatedly fail fetch

### Enforcement Storage

Option A, simplest:

- Firestore counters by IP hash and time bucket

Option B, cleaner if Firestore counters become awkward:

- Upstash Redis rate limits via HTTP, which is designed for serverless environments. Source: [Upstash rate limit overview](https://upstash.com/docs/oss/sdks/ts/ratelimit/overview).

Recommendation:

- start with Firestore-backed counters
- only add Upstash if abuse or concurrency makes Firestore rate checks painful

## Key Handling

### V1

Only platform key.

- store Gemini key only as a server environment variable
- never send it to the browser
- never include it in report artifacts
- redact related error messages

### V2, If `BYO key` Is Added

Only add after the platform-key beta works.

Two acceptable designs:

Option A, simpler:

- synchronous `BYO key` runs only
- no queue
- key used in-process
- key dropped when request completes

Option B, more scalable:

- async queued `BYO key` jobs
- key encrypted before persistence
- decrypted only inside worker
- TTL cleanup plus log redaction

Recommendation:

- do not add `BYO key` until V1 proves useful

## Reference URL Presets

Known-domain presets should improve citation quality.

Suggested first presets:

- Google blog post -> DeepMind model card or evaluation report
- Anthropic news post -> system card
- OpenAI launch/system card pages -> official system card or research page
- xAI proxy input -> official xAI announcement plus leaderboard reference

Mechanism:

- new `honestlaunch/reference_presets.py`

Suggested interface:

```python
def preset_references_for_url(url: str) -> list[str]:
    ...
```

This is optional at input time but highly recommended for demo quality.

## Visual Fidelity Strategy

V1 does not attempt pixel-perfect arbitrary-site cloning.

V1 should do:

- preserve cleaned article block structure
- preserve headings, lists, paragraphs, tables
- use subtle audit underlines and tooltips

V2 should do:

- capture inline links and emphasis
- preserve simple DOM subtree structure
- preserve a subset of computed styles

V3, if needed:

- headless-browser DOM capture for richer fidelity
- limited domain adapters for especially important sites

Do not use screenshots as the primary render path.

Reason:

- screenshots are not editable
- rewritten text overlays become brittle
- interaction and accessibility are poor

## Artifact Retention

### Job Metadata

Use Firestore TTL on `expires_at`.

Initial retention:

- `7 days`

### HTML And JSON Artifacts

Initial retention:

- `7 days`

Cleanup options:

- Cloud Storage lifecycle rule, or
- scheduled cleanup worker

Recommendation:

- keep retention simple and short in beta

## Cost Controls

- small claim cap
- small contrast cap
- supported domains only at launch
- no background retries on model failures beyond a narrow internal retry
- low Cloud Run max instances
- short artifact retention
- no long-lived user data

No ads in the beta.

Monetization path later, if needed:

- invite-only or waitlist
- paid credits
- `BYO key`
- consulting / enterprise demo deployments

## Build Order

### Phase 1: Shared Pipeline Refactor

- add `honestlaunch/pipeline.py`
- move non-CLI orchestration out of `cli.py`
- verify CLI still works

### Phase 2: Minimal Web Service

- add FastAPI app
- landing page
- `POST /api/jobs`
- `GET /api/jobs/:id`
- `GET /r/:id`

### Phase 3: Async Jobs

- Firestore job store
- Cloud Tasks dispatch
- worker endpoint
- Cloud Storage artifact persistence

### Phase 4: Anonymous Guardrails

- Turnstile
- per-IP quotas
- single active job enforcement

### Phase 5: Demo Quality

- known-domain reference presets
- better hosted report chrome
- better failure messaging

### Phase 6: Optional `BYO key`

- only after the platform-key beta is stable

## Verification Criteria

The hosted beta is ready when:

- a user can submit a supported launch-post URL without logging in
- the backend creates an async job and completes it on the platform key
- the user receives a shareable report URL
- the report opens to the audited launch page by default
- rate limits stop obvious abuse
- the total system can fail safely without leaking secrets

## Recommended First Shipping Slice

If the goal is "show this to someone this week", ship this exact slice:

- one Cloud Run service
- one landing page
- Turnstile
- one `POST /api/jobs`
- one `GET /api/jobs/:id`
- one `GET /r/:id`
- Firestore jobs
- Cloud Tasks worker
- Cloud Storage artifacts
- platform key only
- supported domains only
- `limit=3`

That is the smallest real hosted product that matches the current repo and avoids premature auth, billing, and secret-management complexity.
