"""FastAPI entrypoint for the runnable AI study-coach demo."""

from __future__ import annotations

import httpx
from fastapi import FastAPI, HTTPException

from app.config import Settings
from app.schemas import ChatRequest, ChatResponse, HealthResponse
from app.services.chat import ProviderConfigurationError, build_provider

app = FastAPI(
    title="AI Study Coach API",
    description="A small, testable LLM full-stack demo with an offline provider.",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "AI Study Coach API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    settings = Settings.from_env()
    return HealthResponse(status="ok", provider=settings.provider)


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    settings = Settings.from_env()
    try:
        provider = build_provider(settings)
        reply = await provider.generate(request.message, request.context)
    except ProviderConfigurationError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail="The configured LLM provider failed") from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return ChatResponse(reply=reply, provider=provider.name, model=provider.model)
