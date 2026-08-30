from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
from pydantic import BaseModel

from sbai_api_gateway.core.exception_handlers import (
    sbai_error_handler,
    validation_error_handler,
)
from sbai_api_gateway.core.exceptions import SBAIError
from sbai_api_gateway.main import app
from sbai_api_gateway.middleware.request_id import RequestIDMiddleware


client = TestClient(app)


def test_health():
    request_id = "550e8400-e29b-41d4-a716-446655440000"

    response = client.get(
        "/api/v1/health",
        headers={"X-Request-ID": request_id},
    )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == request_id

    assert response.json() == {
        "success": True,
        "data": {
            "status": "ok",
            "service": "api-gateway",
            "version": "0.1.0",
        },
        "meta": {
            "request_id": request_id,
        },
    }


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "service": "api-gateway",
        "version": "0.1.0",
        "status": "ok",
    }


def test_api_v1_info():
    response = client.get("/api/v1")

    assert response.status_code == 200
    assert response.json() == {
        "api_version": "v1",
        "service": "api-gateway",
        "status": "ok",
    }


def test_system_info():
    request_id = "550e8400-e29b-41d4-a716-446655440000"

    response = client.get(
        "/api/v1/system",
        headers={"X-Request-ID": request_id},
    )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == request_id

    assert response.json() == {
        "success": True,
        "data": {
            "service": "api-gateway",
            "version": "0.1.0",
            "status": "ok",
        },
        "meta": {
            "request_id": request_id,
        },
    }

def test_sbai_error_http_contract():
    test_app = FastAPI()
    test_app.add_middleware(RequestIDMiddleware)
    test_app.add_exception_handler(SBAIError, sbai_error_handler)

    @test_app.get("/test-error")
    async def test_error():
        raise SBAIError(
            error="SBAI_TEST_ERROR",
            message="This is a test error.",
            details={"field": "test"},
        )

    test_client = TestClient(test_app)

    request_id = "550e8400-e29b-41d4-a716-446655440000"

    response = test_client.get(
        "/test-error",
        headers={"X-Request-ID": request_id},
    )

    assert response.status_code == 400
    assert response.headers["X-Request-ID"] == request_id

    assert response.json() == {
        "success": False,
        "error": {
            "code": "SBAI_TEST_ERROR",
            "message": "This is a test error.",
            "details": {
                "field": "test",
            },
        },
        "meta": {
            "request_id": request_id,
        },
    }


def test_request_id_is_generated():
    from uuid import UUID

    response = client.get("/")

    assert response.status_code == 200

    request_id = response.headers.get("X-Request-ID")

    assert request_id is not None
    UUID(request_id)

def test_validation_error_http_contract():
    test_app = FastAPI()
    test_app.add_middleware(RequestIDMiddleware)
    test_app.add_exception_handler(
        RequestValidationError,
        validation_error_handler,
    )

    class TestRequest(BaseModel):
        name: str
        age: int

    @test_app.post("/test-validation")
    async def test_validation(payload: TestRequest):
        return payload

    test_client = TestClient(test_app)

    request_id = "6ba7b810-9dad-11d1-80b4-00c04fd430c8"

    response = test_client.post(
        "/test-validation",
        headers={"X-Request-ID": request_id},
        json={
            "name": "SBAI",
            "age": "not-an-integer",
        },
    )

    assert response.status_code == 422
    assert response.headers["X-Request-ID"] == request_id

    body = response.json()

    assert body["success"] is False
    assert body["error"]["code"] == "SBAI_VALIDATION_ERROR"
    assert body["error"]["message"] == "Request validation failed."
    assert body["error"]["details"]["errors"]
    assert body["meta"]["request_id"] == request_id

def test_api_response_contract():
    from sbai_api_gateway.core.errors import APIResponse

    response = APIResponse(
        data={
            "service": "api-gateway",
            "status": "ok",
        },
        meta={
            "request_id": "response-test-123",
        },
    )

    assert response.model_dump() == {
        "success": True,
        "data": {
            "service": "api-gateway",
            "status": "ok",
        },
        "meta": {
            "request_id": "response-test-123",
        },
    }

def test_invalid_request_id_is_replaced():
    response = client.get(
        "/",
        headers={"X-Request-ID": "not-a-uuid"},
    )

    assert response.status_code == 200

    request_id = response.headers["X-Request-ID"]

    from uuid import UUID

    UUID(request_id)


def test_valid_request_id_is_preserved():
    request_id = "550e8400-e29b-41d4-a716-446655440000"

    response = client.get(
        "/",
        headers={"X-Request-ID": request_id},
    )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == request_id

