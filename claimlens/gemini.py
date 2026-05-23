from __future__ import annotations

import json
import os
from typing import TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class GeminiClient:
    def __init__(self, model: str | None = None) -> None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is required unless --mock is used.")
        self.client = genai.Client(api_key=api_key)
        self.model = model or os.getenv("CLAIMLENS_MODEL", "gemini-3.5-flash")

    def structured(self, prompt: str, schema: type[T], *, tools: bool = True) -> T:
        config = types.GenerateContentConfig(
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
