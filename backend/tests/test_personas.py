from fastapi.testclient import TestClient


def test_list_personas(client: TestClient, auth_headers, crear_persona):
    crear_persona(nombre="Maria", apellido="Gomez")
    response = client.get("/api/v1/personas/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_persona(client: TestClient, auth_headers, crear_persona):
    persona_id = crear_persona()
    response = client.get(f"/api/v1/personas/{persona_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == persona_id


def test_get_persona_con_ubicacion(client: TestClient, auth_headers, crear_persona):
    persona_id = crear_persona(
        nombre="Ana",
        apellido="Lopez",
        id_empleado="E123",
        id_expediente="X456",
        exttelef="12345",
        id_ccosto="CC01",
        cubiculo="A-205",
        direccion="Calle 12, Vedado",
        ciudad="La Habana",
    )
    data = client.get(f"/api/v1/personas/{persona_id}", headers=auth_headers).json()
    assert data["cubiculo"] == "A-205"
    assert data["direccion"] == "Calle 12, Vedado"
    assert data["ciudad"] == "La Habana"


def test_get_persona_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/personas/99999", headers=auth_headers)
    assert response.status_code == 404


def test_buscar_personas(client: TestClient, auth_headers, crear_persona):
    crear_persona(nombre="Maria", apellido="Gomez")
    response = client.get(
        "/api/v1/personas/buscar",
        headers=auth_headers,
        params={"q": "Gomez"},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_consulta_no_ve_campos_sensibles(client: TestClient, auth_headers, consulta_headers, crear_persona):
    """A1: el rol consulta recibe la persona sin documento/email/telefono/exttelef."""
    persona_id = crear_persona(
        nombre="Sensible",
        apellido="Datos",
        documento="88010112345",
        email="sensible@test.com",
        telefono="5555555",
        exttelef="101",
    )

    admin_view = client.get(f"/api/v1/personas/{persona_id}", headers=auth_headers).json()
    assert admin_view["documento"] == "88010112345"
    assert admin_view["email"] == "sensible@test.com"

    consult_view = client.get(f"/api/v1/personas/{persona_id}", headers=consulta_headers).json()
    assert "documento" not in consult_view
    assert "email" not in consult_view
    assert "telefono" not in consult_view
    assert "exttelef" not in consult_view
    assert consult_view["nombre"] == "Sensible"

    busqueda = client.get(
        "/api/v1/personas/buscar",
        headers=consulta_headers,
        params={"q": "Datos"},
    ).json()
    assert len(busqueda) == 1
    assert "documento" not in busqueda[0]


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/personas/")
    assert response.status_code == 401