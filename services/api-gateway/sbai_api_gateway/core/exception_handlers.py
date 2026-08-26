from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from sbai_api_gateway.core.errors import ErrorDetail, ErrorResponse
from sbai_api_gateway.core.exceptions import SBAIError


async def sbai_error_handler(
    request: Request,
    exc: SBAIError,
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None)

    response = ErrorResponse(
        error=ErrorDetail(
            code=exc.error,
            message=exc.message,
            details=exc.details,
        ),
        meta={"request_id": request_id} if request_id else None,
    )

    return JSONResponse(
        status_code=400,
        content=response.model_dump(exclude_none=True),
    )


async def validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None)

    response = ErrorResponse(
        error=ErrorDetail(
            code="SBAI_VALIDATION_ERROR",
            message="Request validation failed.",
            details={"errors": exc.errors()},
        ),
        meta={"request_id": request_id} if request_id else None,
    )

    return JSONResponse(
        status_code=422,
        content=response.model_dump(exclude_none=True),
    )
