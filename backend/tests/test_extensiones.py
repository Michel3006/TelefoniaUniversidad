from fastapi.testclient import TestClient


def test_create_extension(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/extensiones/",
        headers=auth_headers,
        json={"numero": "101"},
    )
    assert response.status_code == 201
    assert response.json()["numero"] == "101"


def test_list_extensiones(client: TestClient, auth_headers):
    client.post("/api/v1/extensiones/", headers=auth_headers, json={"numero": "102"})
    response = client.get("/api/v1/extensiones/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_extension(client: TestClient, auth_headers):
    create = client.post("/api/v1/extensiones/", headers=auth_headers, json={"numero": "103"})
    extension_id = create.json()["id"]
    response = client.get(f"/api/v1/extensiones/{extension_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["numero"] == "103"


def test_update_extension(client: TestClient, auth_headers):
    create = client.post("/api/v1/extensiones/", headers=auth_headers, json={"numero": "104"})
    extension_id = create.json()["id"]
    response = client.put(
        f"/api/v1/extensiones/{extension_id}",
        headers=auth_headers,
        json={"numero": "104", "observaciones": "Nueva"},
    )
    assert response.status_code == 200
    assert response.json()["observaciones"] == "Nueva"


def test_delete_extension(client: TestClient, auth_headers):
    create = client.post("/api/v1/extensiones/", headers=auth_headers, json={"numero": "105"})
    extension_id = create.json()["id"]
    response = client.delete(f"/api/v1/extensiones/{extension_id}", headers=auth_headers)
    assert response.status_code == 204


def test_buscar_extension(client: TestClient, auth_headers):
    client.post("/api/v1/extensiones/", headers=auth_headers, json={"numero": "106"})
    response = client.get(
        "/api/v1/extensiones/buscar",
        headers=auth_headers,
        params={"q": "106"},
    )
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_por_telefono(client: TestClient, auth_headers):
    telefono = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "7777777777"},
    )
    telefono_id = telefono.json()["id"]
    client.post(
        "/api/v1/extensiones/",
        headers=auth_headers,
        json={"numero": "107", "telefono_id": telefono_id},
    )
    response = client.get(f"/api/v1/extensiones/por-telefono/{telefono_id}", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_telefono_detalle_incluye_extension(client: TestClient, auth_headers):
    telefono = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "8888888888"},
    )
    telefono_id = telefono.json()["id"]
    client.post(
        "/api/v1/extensiones/",
        headers=auth_headers,
        json={"numero": "108", "telefono_id": telefono_id},
    )
    response = client.get(f"/api/v1/telefonos/{telefono_id}/detalle", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()["extensiones"]) == 1
    assert response.json()["extensiones"][0]["numero"] == "108"


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/extensiones/")
    assert response.status_code == 401