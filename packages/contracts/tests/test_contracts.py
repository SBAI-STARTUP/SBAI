from sbai_contracts.errors import ErrorDetail, ErrorResponse
from sbai_contracts.responses import APIResponse
from sbai_contracts.health import HealthResponse
from sbai_contracts.identifiers import is_valid_request_id
from sbai_contracts.metadata import ServiceMetadata


def test_api_response_contract():
    response = APIResponse(
        data={"service": "api-gateway", "status": "ok"},
        meta={"request_id": "response-test-123"},
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


def test_error_response_contract():
    response = ErrorResponse(
        error=ErrorDetail(
            code="SBAI_TEST_ERROR",
            message="This is a test error.",
            details={"field": "test"},
        ),
        meta={"request_id": "request-test"},
    )

    assert response.model_dump() == {
        "success": False,
        "error": {
            "code": "SBAI_TEST_ERROR",
            "message": "This is a test error.",
            "details": {"field": "test"},
        },
        "meta": {
            "request_id": "request-test",
        },
    }


def test_health_response_contract():
    response = HealthResponse(
        status="ok",
        service="api-gateway",
        version="0.1.0",
    )

    assert response.model_dump() == {
        "status": "ok",
        "service": "api-gateway",
        "version": "0.1.0",
    }


def test_request_id_validation():
    assert is_valid_request_id(
        "550e8400-e29b-41d4-a716-446655440000"
    )

    assert not is_valid_request_id("not-a-uuid")
    assert not is_valid_request_id(None)


def test_service_metadata_contract():
    metadata = ServiceMetadata(
        service="api-gateway",
        version="0.1.0",
    )

    assert metadata.model_dump() == {
        "service": "api-gateway",
        "version": "0.1.0",
    }
