from fastapi.testclient import TestClient


def test_create_dispositivo(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "Apple", "modelo": "iPhone 13", "imei": "000000000000001"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["marca"] == "Apple"
    assert data["modelo"] == "iPhone 13"


def test_dispositivo_observaciones(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={
            "marca": "Samsung",
            "modelo": "Galaxy A54",
            "imei": "000000000000009",
            "observaciones": "Equipo de reposicion",
        },
    )
    assert response.status_code == 201
    assert response.json()["observaciones"] == "Equipo de reposicion"

    dispositivo_id = response.json()["id"]
    updated = client.put(
        f"/api/v1/dispositivos/{dispositivo_id}",
        headers=auth_headers,
        json={
            "marca": "Samsung",
            "modelo": "Galaxy A54",
            "imei": "000000000000009",
            "observaciones": "Asignado a ventas",
        },
    )
    assert updated.status_code == 200
    assert updated.json()["observaciones"] == "Asignado a ventas"


def test_list_dispositivos(client: TestClient, auth_headers):
    client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "Samsung", "modelo": "Galaxy A54", "imei": "000000000000002"},
    )
    response = client.get("/api/v1/dispositivos/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_dispositivo(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "Xiaomi", "modelo": "Redmi Note", "imei": "000000000000003"},
    )
    dispositivo_id = create.json()["id"]
    response = client.get(f"/api/v1/dispositivos/{dispositivo_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["imei"] == "000000000000003"


def test_update_dispositivo(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "Motorola", "modelo": "G62", "imei": "000000000000004"},
    )
    dispositivo_id = create.json()["id"]
    response = client.put(
        f"/api/v1/dispositivos/{dispositivo_id}",
        headers=auth_headers,
        json={"marca": "Motorola", "modelo": "G84", "imei": "000000000000004"},
    )
    assert response.status_code == 200
    assert response.json()["modelo"] == "G84"


def test_delete_dispositivo(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "Huawei", "modelo": "P30", "imei": "000000000000005"},
    )
    dispositivo_id = create.json()["id"]
    response = client.delete(f"/api/v1/dispositivos/{dispositivo_id}", headers=auth_headers)
    assert response.status_code == 204


def test_buscar_dispositivo(client: TestClient, auth_headers):
    client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "LG", "modelo": "K51", "imei": "000000000000006"},
    )
    response = client.get(
        "/api/v1/dispositivos/buscar",
        headers=auth_headers,
        params={"q": "K51"},
    )
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_sim_detalle_incluye_dispositivo(client: TestClient, auth_headers):
    sim = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491191111111"},
    )
    sim_id = sim.json()["id"]
    client.post(
        "/api/v1/dispositivos/",
        headers=auth_headers,
        json={"marca": "Apple", "modelo": "iPhone 15", "imei": "000000000000007", "sim_id": sim_id},
    )
    response = client.get(f"/api/v1/sims/{sim_id}/detalle", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["dispositivo"] == "Apple iPhone 15"


def test_consulta_no_puede_crear_dispositivo(client: TestClient, consulta_headers):
    response = client.post(
        "/api/v1/dispositivos/",
        headers=consulta_headers,
        json={"marca": "Apple", "modelo": "iPhone", "imei": "000000000000008"},
    )
    assert response.status_code == 403


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/dispositivos/")
    assert response.status_code == 401