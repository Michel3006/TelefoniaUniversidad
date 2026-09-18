from fastapi.testclient import TestClient


def test_create_plan(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/planes/",
        headers=auth_headers,
        json={"nombre": "Plan Basico", "operador": "ETECSA", "coste_mensual": "250.00"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Plan Basico"
    assert data["coste_mensual"] == "250.00"


def test_list_planes(client: TestClient, auth_headers):
    client.post("/api/v1/planes/", headers=auth_headers, json={"nombre": "Plan A"})
    response = client.get("/api/v1/planes/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_plan(client: TestClient, auth_headers):
    create = client.post("/api/v1/planes/", headers=auth_headers, json={"nombre": "Plan B"})
    plan_id = create.json()["id"]
    response = client.get(f"/api/v1/planes/{plan_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Plan B"


def test_update_plan(client: TestClient, auth_headers):
    create = client.post("/api/v1/planes/", headers=auth_headers, json={"nombre": "Plan C"})
    plan_id = create.json()["id"]
    response = client.put(
        f"/api/v1/planes/{plan_id}",
        headers=auth_headers,
        json={"nombre": "Plan C", "descripcion": "Actualizado"},
    )
    assert response.status_code == 200
    assert response.json()["descripcion"] == "Actualizado"


def test_delete_plan(client: TestClient, auth_headers):
    create = client.post("/api/v1/planes/", headers=auth_headers, json={"nombre": "Plan D"})
    plan_id = create.json()["id"]
    response = client.delete(f"/api/v1/planes/{plan_id}", headers=auth_headers)
    assert response.status_code == 204


def test_sim_puede_referenciar_plan(client: TestClient, auth_headers):
    create = client.post("/api/v1/planes/", headers=auth_headers, json={"nombre": "Plan M"})
    plan_id = create.json()["id"]
    response = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5491190000000", "plan_id": plan_id},
    )
    assert response.status_code == 201
    assert response.json()["plan_id"] == plan_id


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/planes/")
    assert response.status_code == 401