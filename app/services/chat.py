"""Chat provider abstractions with offline and OpenAI-compatible implementations."""

from __future__ import annotations

from typing import Protocol

import httpx

from app.config import Settings


class ProviderConfigurationError(RuntimeError):
    """Raised when a provider is selected without the required configuration."""


class ChatProvider(Protocol):
    name: str
    model: str

    async def generate(self, message: str, context: list[str]) -> str: ...


class DemoStudyCoach:
    """Deterministic offline provider used for local demos and automated tests."""

    name = "demo"
    model = "study-coach-v1"

    async def generate(self, message: str, context: list[str]) -> str:
        normalized = message.lower()
        context_hint = f"\n已参考 {len(context)} 条补充背景。" if context else ""

        if "fastapi" in normalized:
            advice = "先实现健康检查和请求模型，再补充业务路由、异常处理与测试。"
        elif "rag" in normalized:
            advice = "先验证切分、检索和引用链路，再接入生成模型并评估召回质量。"
        elif "langgraph" in normalized or "agent" in normalized:
            advice = "先定义状态、节点和退出条件，再逐步增加工具调用与持久化记忆。"
        else:
            advice = "把目标拆成一个可运行的最小版本，为关键路径补测试，再迭代模型能力。"

        return f"学习建议：{advice}{context_hint}"


class OpenAICompatibleProvider:
    """Minimal client for APIs implementing the chat-completions contract."""

    name = "openai-compatible"

    def __init__(self, settings: Settings) -> None:
        if not settings.api_key:
            raise ProviderConfigurationError(
                "LLM_API_KEY is required when LLM_PROVIDER=openai-compatible"
            )
        self.model = settings.model
        self._api_key = settings.api_key
        self._base_url = settings.base_url
        self._timeout = settings.timeout_seconds

    async def generate(self, message: str, context: list[str]) -> str:
        system_prompt = (
            "You are a concise AI engineering study coach. "
            "Give practical, verifiable next steps."
        )
        if context:
            system_prompt += " Context: " + " | ".join(context)

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(
                f"{self._base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self._api_key}"},
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": message},
                    ],
                },
            )
            response.raise_for_status()
            payload = response.json()

        try:
            return str(payload["choices"][0]["message"]["content"])
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError("The provider returned an unexpected response shape") from exc


def build_provider(settings: Settings) -> ChatProvider:
    if settings.provider == "demo":
        return DemoStudyCoach()
    if settings.provider == "openai-compatible":
        return OpenAICompatibleProvider(settings)
    raise ProviderConfigurationError(
        f"Unsupported LLM_PROVIDER={settings.provider!r}; use 'demo' or 'openai-compatible'"
    )
