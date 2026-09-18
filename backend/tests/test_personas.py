from fastapi.testclient import TestClient


def _create_persona(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/personas/",
        headers=auth_headers,
        json={"nombre": "Maria", "apellido": "Gomez"},
    )
    return response.json()["id"]


def test_create_persona(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/personas/",
        headers=auth_headers,
        json={"nombre": "Juan", "apellido": "Perez"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Juan"
    assert data["apellido"] == "Perez"
    assert data["baja"] is False


def test_create_persona_con_campos_institucionales(client: TestClient, auth_headers, db):
    from app.models.institucional import Area, Cargo

    area = Area(codigo="001", nombre="Informatica")
    cargo = Cargo(codigo="01", nombre="Especialista")
    db.add_all([area, cargo])
    db.commit()
    db.refresh(area)
    db.refresh(cargo)

    response = client.post(
        "/api/v1/personas/",
        headers=auth_headers,
        json={
            "nombre": "Ana",
            "apellido": "Lopez",
            "apellido_2": "Perez",
            "documento": "88010112345",
            "email": "ana@test.com",
            "id_empleado": "E123",
            "id_expediente": "X456",
            "exttelef": "12345",
            "id_ccosto": "CC01",
            "area_id": area.id,
            "cargo_id": cargo.id,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id_empleado"] == "E123"
    assert data["area_id"] == area.id
    assert data["cargo_id"] == cargo.id


def test_list_personas(client: TestClient, auth_headers):
    _create_persona(client, auth_headers)
    response = client.get("/api/v1/personas/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_persona(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    response = client.get(f"/api/v1/personas/{persona_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == persona_id


def test_update_persona(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    response = client.put(
        f"/api/v1/personas/{persona_id}",
        headers=auth_headers,
        json={"nombre": "Maria", "apellido": "Gomez", "email": "maria@test.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "maria@test.com"


def test_delete_persona(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    response = client.delete(f"/api/v1/personas/{persona_id}", headers=auth_headers)
    assert response.status_code == 204
    assert client.get(f"/api/v1/personas/{persona_id}", headers=auth_headers).status_code == 404


def test_buscar_personas(client: TestClient, auth_headers):
    _create_persona(client, auth_headers)
    response = client.get(
        "/api/v1/personas/buscar",
        headers=auth_headers,
        params={"q": "Gomez"},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_persona_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/personas/99999", headers=auth_headers)
    assert response.status_code == 404


def test_consulta_no_puede_crear_persona(client: TestClient, consulta_headers):
    response = client.post(
        "/api/v1/personas/",
        headers=consulta_headers,
        json={"nombre": "Pepe", "apellido": "Perez"},
    )
    assert response.status_code == 403


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/personas/")
    assert response.status_code == 401