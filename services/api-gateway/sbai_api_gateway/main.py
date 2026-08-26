from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from sbai_api_gateway.api.router import router as api_router
from sbai_api_gateway.core.config import settings
from sbai_api_gateway.core.exception_handlers import (
    sbai_error_handler,
    validation_error_handler,
)
from sbai_api_gateway.core.exceptions import SBAIError
from sbai_api_gateway.middleware.request_id import RequestIDMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="SBAI API Gateway",
    version=settings.service_version,
    lifespan=lifespan,
)

app.add_middleware(RequestIDMiddleware)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "service": settings.service_name,
        "version": settings.service_version,
        "status": "ok",
    }


app.add_exception_handler(SBAIError, sbai_error_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)

app.include_router(api_router)
