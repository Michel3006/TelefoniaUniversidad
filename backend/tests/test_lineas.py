from fastapi.testclient import TestClient


def test_create_linea(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": "5491112345678"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["numero"] == "5491112345678"


def test_list_lineas(client: TestClient, auth_headers):
    client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": "5491111111111"},
    )
    response = client.get("/api/v1/lineas/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_linea(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": "5491122222222"},
    )
    linea_id = create.json()["id"]
    response = client.get(f"/api/v1/lineas/{linea_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "5491122222222"


def test_update_linea(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": "5491133333333"},
    )
    linea_id = create.json()["id"]
    response = client.put(
        f"/api/v1/lineas/{linea_id}",
        headers=auth_headers,
        json={"numero": "5491144444444"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "5491144444444"


def test_delete_linea(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": "5491155555555"},
    )
    linea_id = create.json()["id"]
    response = client.delete(f"/api/v1/lineas/{linea_id}", headers=auth_headers)
    assert response.status_code == 204


def test_detalle_linea(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": "5491166666666"},
    )
    linea_id = create.json()["id"]
    response = client.get(f"/api/v1/lineas/{linea_id}/detalle", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "5491166666666"


def test_detalle_linea_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/lineas/99999/detalle", headers=auth_headers)
    assert response.status_code == 404


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/lineas/")
    assert response.status_code == 401
