"""Environment-backed application settings."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True, slots=True)
class Settings:
    """Configuration for the demo and OpenAI-compatible providers."""

    provider: str = "demo"
    api_key: str | None = None
    base_url: str = "https://api.openai.com/v1"
    model: str = "gpt-4o-mini"
    timeout_seconds: float = 30.0

    @classmethod
    def from_env(cls) -> Settings:
        load_dotenv()
        return cls(
            provider=os.getenv("LLM_PROVIDER", "demo").strip().lower(),
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/"),
            model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            timeout_seconds=float(os.getenv("LLM_TIMEOUT_SECONDS", "30")),
        )
