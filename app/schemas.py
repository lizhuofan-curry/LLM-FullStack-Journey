"""API request and response models."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2_000)
    context: list[str] = Field(default_factory=list, max_length=10)


class ChatResponse(BaseModel):
    reply: str
    provider: str
    model: str


class HealthResponse(BaseModel):
    status: str
    provider: str
