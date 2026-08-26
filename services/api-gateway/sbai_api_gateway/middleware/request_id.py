from uuid import UUID, uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


REQUEST_ID_HEADER = "X-Request-ID"
MAX_REQUEST_ID_LENGTH = 128


def _is_valid_request_id(value: str | None) -> bool:
    if not value:
        return False

    if len(value) > MAX_REQUEST_ID_LENGTH:
        return False

    try:
        UUID(value)
    except ValueError:
        return False

    return True


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = request.headers.get(REQUEST_ID_HEADER)

        if not _is_valid_request_id(request_id):
            request_id = str(uuid4())

        request.state.request_id = request_id

        response = await call_next(request)
        response.headers[REQUEST_ID_HEADER] = request_id

        return response
