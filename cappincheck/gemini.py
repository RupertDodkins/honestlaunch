from __future__ import annotations

import json
import os
from pathlib import Path
from typing import TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class GeminiClient:
    def __init__(self, model: str | None = None) -> None:
        _load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is required unless --mock is used.")
        self.client = genai.Client(api_key=api_key)
        self.model = model or os.getenv("CLAIMLENS_MODEL", "gemini-3.5-flash")

    def structured(self, prompt: str, schema: type[T], *, tools: bool = True) -> T:
        timeout_seconds = int(os.getenv("CAPPINCHECK_TIMEOUT_SECONDS", "90"))
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
            return response.parsed
        text = response.text or "{}"
        return schema.model_validate(json.loads(text))


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
