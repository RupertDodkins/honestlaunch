# CappinCheck Runtime Boundary

CappinCheck currently runs locally. The CLI loads the role definitions in `skills/*/SKILL.md`, dispatches local async Gemini calls for each specialist pass, then aggregates results into Markdown, JSON, and static HTML reports.

The supported default runtime is local. An experimental `--runtime managed` path uses the Google GenAI Interactions API to run the same specialist skill prompts through managed interactions. Google marks this API as experimental, so the local runtime remains the demo-safe default.

## Current Runtime

- `cappincheck audit ... --mock` uses deterministic fixture output for demos and tests.
- `cappincheck audit ... --runtime local` uses the local async Gemini client.
- `cappincheck audit ... --runtime managed` uses the experimental Interactions API and normalizes model-output JSON back into the same report schemas.
- `skills/*/SKILL.md` define the verifier, contradiction finder, numeric calibrator, and aggregator roles.
- Report generation is local and static; there is no hosted backend, account system, or database.

## Managed Runtime Boundary

The managed adapter plugs in at the specialist-dispatch boundary: load the same skill text, send each selected claim to a managed interaction, and return the same structured claim-audit payload consumed by the aggregator/report renderer.

The adapter should preserve:

- The deterministic `--mock` path.
- The existing public report schema.
- Explicit runtime selection via `--runtime local` and `--runtime managed`.
- Fail-fast behavior when Managed Agents are unavailable, rather than silently falling back to mock results.

## Current Caveat

The Interactions API is beta and may change. The managed runtime currently prompts for JSON and validates it locally instead of relying on server-side structured `response_format`, because the tested SDK/API combination rejected structured response-format requests while accepting ordinary interaction calls.
