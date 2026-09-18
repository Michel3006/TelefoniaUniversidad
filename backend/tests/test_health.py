from fastapi.testclient import TestClient


def test_health(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_sin_auth_requerida(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200


def test_no_auth_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 404