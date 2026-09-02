from typing import Literal

from fastapi import APIRouter, Request
from pydantic import BaseModel

from sbai_api_gateway.core.config import settings
from sbai_api_gateway.core.responses import success_response


router = APIRouter()


class SystemInfo(BaseModel):
    service: str
    version: str
    status: Literal["ok"]


@router.get("/system")
async def system_info(request: Request):
    data = SystemInfo(
        service=settings.service_name,
        version=settings.service_version,
        status="ok",
    )

    request_id = getattr(request.state, "request_id", None)

    return success_response(
        data=data,
        request_id=request_id,
    )
