from fastapi import APIRouter

from sbai_api_gateway.api.health import router as health_router


router = APIRouter()

router.include_router(health_router)
