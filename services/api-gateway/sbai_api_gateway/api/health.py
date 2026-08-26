from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from sbai_api_gateway.core.config import settings


router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    version: str


@router.get(
    "/health",
    response_model=HealthResponse,
)
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.service_name,
        version=settings.service_version,
    )