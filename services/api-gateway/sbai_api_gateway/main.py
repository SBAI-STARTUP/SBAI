from contextlib import asynccontextmanager

from fastapi import FastAPI

from sbai_api_gateway.api.health import router as health_router
from sbai_api_gateway.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="SBAI API Gateway",
    version=settings.service_version,
    lifespan=lifespan,
)

app.include_router(health_router)