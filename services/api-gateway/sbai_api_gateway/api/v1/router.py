from fastapi import APIRouter

from sbai_api_gateway.api.health import router as health_router
from sbai_api_gateway.api.v1.system import router as system_router
from sbai_api_gateway.core.config import settings


router = APIRouter()


@router.get("")
async def api_v1_info() -> dict[str, str]:
    return {
        "api_version": "v1",
        "service": settings.service_name,
        "status": "ok",
    }


router.include_router(health_router)
router.include_router(system_router)
