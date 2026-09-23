from fastapi.testclient import TestClient


def test_create_contrato(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/contratos/",
        headers=auth_headers,
        json={"numero": "C-001", "fecha_inicio": "2026-01-01", "fecha_vencimiento": "2026-12-31"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["numero"] == "C-001"
    assert data["id"] > 0


def test_list_contratos(client: TestClient, auth_headers):
    client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "C-002"})
    response = client.get("/api/v1/contratos/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_contrato(client: TestClient, auth_headers):
    create = client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "C-003"})
    contrato_id = create.json()["id"]
    response = client.get(f"/api/v1/contratos/{contrato_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["numero"] == "C-003"


def test_update_contrato(client: TestClient, auth_headers):
    create = client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "C-004"})
    contrato_id = create.json()["id"]
    response = client.put(
        f"/api/v1/contratos/{contrato_id}",
        headers=auth_headers,
        json={"numero": "C-004", "observaciones": "Renovado"},
    )
    assert response.status_code == 200
    assert response.json()["observaciones"] == "Renovado"


def test_delete_contrato(client: TestClient, auth_headers):
    create = client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "C-005"})
    contrato_id = create.json()["id"]
    response = client.delete(f"/api/v1/contratos/{contrato_id}", headers=auth_headers)
    assert response.status_code == 204


def test_consulta_no_puede_crear_contrato(client: TestClient, consulta_headers):
    response = client.post(
        "/api/v1/contratos/",
        headers=consulta_headers,
        json={"numero": "C-100"},
    )
    assert response.status_code == 403


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/contratos/")
    assert response.status_code == 401