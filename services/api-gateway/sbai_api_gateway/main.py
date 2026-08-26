from contextlib import asynccontextmanager

from fastapi import FastAPI

from sbai_api_gateway.api.router import router as api_router
from sbai_api_gateway.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="SBAI API Gateway",
    version=settings.service_version,
    lifespan=lifespan,
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "service": settings.service_name,
        "version": settings.service_version,
        "status": "ok",
    }


app.include_router(api_router)
