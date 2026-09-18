from fastapi.testclient import TestClient


def test_create_sim(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491112345678"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["numero"] == "5491112345678"
    assert data["iccid"] is None
    assert data["imsi"] is None


def test_create_sim_sin_iccid_ni_imsi_es_valido(client: TestClient, auth_headers):
    """ICCID/IMSI son opcionales: crear una SIM sin ellos debe funcionar."""
    response = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491100000001"},
    )
    assert response.status_code == 201


def test_list_sims(client: TestClient, auth_headers):
    client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491111111111"},
    )
    response = client.get("/api/v1/sims/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_sim(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491122222222"},
    )
    sim_id = create.json()["id"]
    response = client.get(f"/api/v1/sims/{sim_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "5491122222222"


def test_update_sim(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491133333333"},
    )
    sim_id = create.json()["id"]
    response = client.put(
        f"/api/v1/sims/{sim_id}",
        headers=auth_headers,
        json={"numero": "5491144444444"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "5491144444444"


def test_delete_sim(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491155555555"},
    )
    sim_id = create.json()["id"]
    response = client.delete(f"/api/v1/sims/{sim_id}", headers=auth_headers)
    assert response.status_code == 204


def test_detalle_sim(client: TestClient, auth_headers):
    create = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491166666666"},
    )
    sim_id = create.json()["id"]
    response = client.get(f"/api/v1/sims/{sim_id}/detalle", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["numero"] == "5491166666666"


def test_detalle_sim_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/sims/99999/detalle", headers=auth_headers)
    assert response.status_code == 404


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/sims/")
    assert response.status_code == 401


def test_consulta_no_puede_crear_sim(client: TestClient, consulta_headers):
    """Un usuario con rol 'consulta' puede leer pero no escribir."""
    response = client.post(
        "/api/v1/sims/",
        headers=consulta_headers,
        json={"numero": "5491177777777"},
    )
    assert response.status_code == 403


def test_consulta_puede_listar_sims(client: TestClient, consulta_headers):
    response = client.get("/api/v1/sims/", headers=consulta_headers)
    assert response.status_code == 200


def test_gestor_puede_crear_sim(client: TestClient, gestor_headers):
    response = client.post(
        "/api/v1/sims/",
        headers=gestor_headers,
        json={"numero": "5491188888888"},
    )
    assert response.status_code == 201
