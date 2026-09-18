from fastapi.testclient import TestClient


def test_create_coste(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/costes/",
        headers=auth_headers,
        json={"periodo": "2026-08", "importe": "125.50", "observaciones": "Agosto"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["periodo"] == "2026-08"
    assert data["importe"] == "125.50"


def test_list_costes(client: TestClient, auth_headers):
    client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-08", "importe": "10.00"})
    response = client.get("/api/v1/costes/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_coste(client: TestClient, auth_headers):
    create = client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-08", "importe": "20.00"})
    coste_id = create.json()["id"]
    response = client.get(f"/api/v1/costes/{coste_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["importe"] == "20.00"


def test_update_coste(client: TestClient, auth_headers):
    create = client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-08", "importe": "30.00"})
    coste_id = create.json()["id"]
    response = client.put(
        f"/api/v1/costes/{coste_id}",
        headers=auth_headers,
        json={"periodo": "2026-08", "importe": "35.00", "observaciones": "Corregido"},
    )
    assert response.status_code == 200
    assert str(response.json()["importe"]) == "35.00"


def test_delete_coste(client: TestClient, auth_headers):
    create = client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-08", "importe": "40.00"})
    coste_id = create.json()["id"]
    response = client.delete(f"/api/v1/costes/{coste_id}", headers=auth_headers)
    assert response.status_code == 204


def test_por_periodo(client: TestClient, auth_headers):
    client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-08", "importe": "50.00"})
    client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-09", "importe": "60.00"})
    response = client.get(
        "/api/v1/costes/por-periodo",
        headers=auth_headers,
        params={"periodo": "2026-08"},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["periodo"] == "2026-08"


def test_por_departamento(client: TestClient, auth_headers, db):
    from app.models.organizacion import Departamento

    depto = Departamento(nombre="Direccion General")
    db.add(depto)
    db.commit()
    db.refresh(depto)

    client.post(
        "/api/v1/costes/",
        headers=auth_headers,
        json={"periodo": "2026-08", "importe": "70.00", "departamento_id": depto.id},
    )
    response = client.get(f"/api/v1/costes/por-departamento/{depto.id}", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_por_sim(client: TestClient, auth_headers):
    sim = client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "5491192222222"})
    sim_id = sim.json()["id"]
    client.post(
        "/api/v1/costes/",
        headers=auth_headers,
        json={"periodo": "2026-08", "importe": "80.00", "sim_id": sim_id},
    )
    response = client.get(f"/api/v1/costes/por-sim/{sim_id}", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_reportes_costes_reflejan_datos(client: TestClient, auth_headers):
    client.post("/api/v1/costes/", headers=auth_headers, json={"periodo": "2026-08", "importe": "100.00"})
    response = client.get("/api/v1/reportes/costes-totales", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["importe_total"] == 100.00


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/costes/")
    assert response.status_code == 401