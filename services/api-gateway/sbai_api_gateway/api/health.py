from typing import Literal

from fastapi import APIRouter, Request
from pydantic import BaseModel

from sbai_api_gateway.core.config import settings
from sbai_api_gateway.core.errors import APIResponse
from sbai_api_gateway.core.responses import success_response


router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    version: str


@router.get(
    "/health",
    response_model=APIResponse[HealthResponse],
)
async def health(request: Request) -> APIResponse[HealthResponse]:
    data = HealthResponse(
        status="ok",
        service=settings.service_name,
        version=settings.service_version,
    )

    request_id = getattr(request.state, "request_id", None)

    return success_response(
        data=data,
        request_id=request_id,
    )
