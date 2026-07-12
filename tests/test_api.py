"""API contract tests for the runnable demo."""

import asyncio

import httpx

from app.main import app


def api_request(method: str, path: str, **kwargs) -> httpx.Response:
    async def send() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            return await client.request(method, path, **kwargs)

    return asyncio.run(send())


def test_health_uses_offline_demo_by_default(monkeypatch) -> None:
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    response = api_request("GET", "/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "provider": "demo"}


def test_chat_returns_actionable_fastapi_advice(monkeypatch) -> None:
    monkeypatch.setenv("LLM_PROVIDER", "demo")
    response = api_request(
        "POST",
        "/api/chat",
        json={"message": "如何开始一个 FastAPI 项目？", "context": ["需要自动化测试"]},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["provider"] == "demo"
    assert payload["model"] == "study-coach-v1"
    assert "健康检查" in payload["reply"]
    assert "1 条补充背景" in payload["reply"]


def test_chat_rejects_empty_messages() -> None:
    response = api_request("POST", "/api/chat", json={"message": ""})

    assert response.status_code == 422


def test_openai_compatible_provider_requires_api_key(monkeypatch) -> None:
    monkeypatch.setenv("LLM_PROVIDER", "openai-compatible")
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    response = api_request("POST", "/api/chat", json={"message": "hello"})

    assert response.status_code == 503
    assert "LLM_API_KEY" in response.json()["detail"]
