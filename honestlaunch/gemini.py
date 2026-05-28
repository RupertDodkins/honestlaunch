from __future__ import annotations

import json
import os
from pathlib import Path
from typing import TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel, ValidationError


T = TypeVar("T", bound=BaseModel)


class StructuredResponseError(RuntimeError):
    def __init__(self, *, model: str, schema_name: str, raw_output: str, cause: Exception) -> None:
        preview = raw_output[:1000] if raw_output else "<empty response>"
        super().__init__(
            f"Gemini returned invalid JSON for schema {schema_name} using model {model}.\n"
            f"Cause: {cause}\n"
            f"Raw output preview:\n{preview}\n\n"
            "Try the deterministic fallback:\n"
            "  honestlaunch audit examples/demo_document.md --mock --out examples/demo_report.md "
            "--json examples/demo_report.json --html examples/demo_report.html"
        )


class GeminiClient:
    def __init__(self, model: str | None = None) -> None:
        _load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is required unless --mock is used.")
        self.client = genai.Client(api_key=api_key)
        self.model = model or os.getenv("CLAIMLENS_MODEL", "gemini-3.5-flash")

    def structured(self, prompt: str, schema: type[T], *, tools: bool = True) -> T:
        timeout_seconds = int(os.getenv("HONESTLAUNCH_TIMEOUT_SECONDS", "90"))
        config = types.GenerateContentConfig(
            http_options=types.HttpOptions(timeout=timeout_seconds * 1000),
            response_mime_type="application/json",
            response_schema=schema,
            tools=[
                types.Tool(google_search=types.GoogleSearch()),
                types.Tool(url_context=types.UrlContext()),
                types.Tool(code_execution=types.ToolCodeExecution()),
            ]
            if tools
            else None,
        )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=config,
        )
        if hasattr(response, "parsed") and response.parsed is not None:
            return _attach_grounding(response.parsed, response)
        text = response.text or "{}"
        try:
            parsed = schema.model_validate(json.loads(text))
        except (json.JSONDecodeError, ValidationError) as exc:
            parsed = self._repair_structured(text, schema, exc)
        return _attach_grounding(parsed, response)

    def structured_interaction(
        self,
        *,
        input_text: str,
        system_instruction: str,
        schema: type[T],
        tools: bool = True,
    ) -> T:
        try:
            response = self._create_interaction(
                input_text=input_text,
                system_instruction=system_instruction,
                tools=tools,
            )
        except Exception as exc:
            if not tools or "too many tool calls" not in str(exc).lower():
                raise
            response = self._create_interaction(
                input_text=(
                    "The previous managed interaction used too many tool calls. "
                    "Retry with at most one web/search/url tool call, then return JSON from available evidence.\n\n"
                    f"{input_text}"
                ),
                system_instruction=system_instruction,
                tools=False,
            )
        text = _interaction_text(response)
        try:
            return schema.model_validate(json.loads(text))
        except (json.JSONDecodeError, ValidationError) as exc:
            return self._repair_structured(text, schema, exc)

    def _create_interaction(self, *, input_text: str, system_instruction: str, tools: bool) -> object:
        return self.client.interactions.create(
            input=input_text,
            model=self.model,
            system_instruction=system_instruction,
            tools=_interaction_tools() if tools else None,
            timeout=int(os.getenv("HONESTLAUNCH_TIMEOUT_SECONDS", "90")),
        )

    def _repair_structured(self, raw_output: str, schema: type[T], cause: Exception) -> T:
        repair_prompt = f"""
Repair the following model output so it is valid JSON matching the {schema.__name__} schema.
Return only the repaired JSON. Do not add markdown.

RAW OUTPUT:
{raw_output[:8000]}
"""
        try:
            repaired = self.client.models.generate_content(
                model=self.model,
                contents=repair_prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    http_options=types.HttpOptions(
                        timeout=int(os.getenv("HONESTLAUNCH_TIMEOUT_SECONDS", "90")) * 1000
                    ),
                ),
            )
            if hasattr(repaired, "parsed") and repaired.parsed is not None:
                return repaired.parsed
            return schema.model_validate(json.loads(repaired.text or "{}"))
        except Exception as repair_exc:
            raise StructuredResponseError(
                model=self.model,
                schema_name=schema.__name__,
                raw_output=raw_output,
                cause=repair_exc or cause,
            ) from repair_exc


def _load_dotenv() -> None:
    env_path = Path.cwd() / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def _attach_grounding(parsed: T, response: object) -> T:
    """Best-effort metadata capture; skill prompts still own claim-specific citations."""
    try:
        from .schemas import AgentAudit, EvidenceItem
    except Exception:
        return parsed

    if not isinstance(parsed, AgentAudit):
        return parsed

    for item in _grounding_items(response):
        if item.url and not any(existing.url == item.url for existing in parsed.supporting_evidence):
            parsed.supporting_evidence.append(item)
    return parsed


def _grounding_items(response: object) -> list[object]:
    from .schemas import EvidenceItem

    items: list[EvidenceItem] = []
    for candidate in getattr(response, "candidates", []) or []:
        metadata = getattr(candidate, "grounding_metadata", None) or getattr(candidate, "groundingMetadata", None)
        chunks = getattr(metadata, "grounding_chunks", None) or getattr(metadata, "groundingChunks", None) or []
        for chunk in chunks:
            web = getattr(chunk, "web", None)
            if not web:
                continue
            uri = getattr(web, "uri", None)
            title = getattr(web, "title", None) or "Grounded source"
            if uri:
                items.append(
                    EvidenceItem(
                        source_title=title,
                        url=uri,
                        snippet="Source returned by Gemini grounding metadata.",
                        relevance="Grounding source used during specialist audit.",
                    )
                )
    return items


def _interaction_tools() -> list[dict[str, object]]:
    return [
        {"type": "google_search", "search_types": ["web_search"]},
        {"type": "url_context"},
        {"type": "code_execution"},
    ]


def _interaction_text(response: object) -> str:
    chunks: list[str] = []
    for step in getattr(response, "steps", []) or []:
        if getattr(step, "type", None) != "model_output":
            continue
        for content in getattr(step, "content", []) or []:
            text = getattr(content, "text", None)
            if text:
                chunks.append(text)
    return "\n".join(chunks).strip()
