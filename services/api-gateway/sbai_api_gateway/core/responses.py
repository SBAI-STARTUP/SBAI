from typing import Any, TypeVar

from sbai_api_gateway.core.errors import APIResponse

T = TypeVar("T")


def success_response(
    data: T,
    request_id: str | None = None,
) -> APIResponse[T]:
    meta: dict[str, Any] | None = None

    if request_id:
        meta = {
            "request_id": request_id,
        }

    return APIResponse(
        data=data,
        meta=meta,
    )
