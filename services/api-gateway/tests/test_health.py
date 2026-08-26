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
