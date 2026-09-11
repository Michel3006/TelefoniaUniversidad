from fastapi.testclient import TestClient


def test_create_telefono(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "1234567890"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["numero"] == "1234567890"
    assert "id" in data


def test_list_telefonos(client: TestClient, auth_headers):
    client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "1111111111"},
    )
    response = client.get("/api/v1/telefonos/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_telefono(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "2222222222"},
    )
    telefono_id = create.json()["id"]
    response = client.get(f"/api/v1/telefonos/{telefono_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "2222222222"


def test_update_telefono(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "3333333333"},
    )
    telefono_id = create.json()["id"]
    response = client.put(
        f"/api/v1/telefonos/{telefono_id}",
        headers=auth_headers,
        json={"numero": "4444444444", "observaciones": "test"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "4444444444"
    assert data["observaciones"] == "test"


def test_delete_telefono(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "5555555555"},
    )
    telefono_id = create.json()["id"]
    response = client.delete(f"/api/v1/telefonos/{telefono_id}", headers=auth_headers)
    assert response.status_code == 204


def test_detalle_telefono(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "6666666666"},
    )
    telefono_id = create.json()["id"]
    response = client.get(
        f"/api/v1/telefonos/{telefono_id}/detalle", headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "6666666666"
    assert "extensiones" in data


def test_detalle_telefono_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/telefonos/99999/detalle", headers=auth_headers)
    assert response.status_code == 404


def test_get_telefono_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/telefonos/99999", headers=auth_headers)
    assert response.status_code == 404


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/telefonos/")
    assert response.status_code == 401
