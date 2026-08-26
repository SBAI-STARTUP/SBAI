from fastapi.testclient import TestClient

from sbai_api_gateway.main import app


client = TestClient(app)


def test_health():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "api-gateway",
        "version": "0.1.0",
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
    response = client.get("/api/v1/system")

    assert response.status_code == 200
    assert response.json() == {
        "service": "api-gateway",
        "version": "0.1.0",
        "status": "ok",
    }
