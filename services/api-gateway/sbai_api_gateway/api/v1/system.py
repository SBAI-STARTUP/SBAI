from fastapi import APIRouter

from sbai_api_gateway.core.config import settings


router = APIRouter()


@router.get("/system")
async def system_info() -> dict[str, str]:
    return {
        "service": settings.service_name,
        "version": settings.service_version,
        "status": "ok",
    }
