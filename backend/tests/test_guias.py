from datetime import date

from fastapi.testclient import TestClient


def test_guia_telefonica_vacia(client: TestClient, auth_headers):
    response = client.get("/api/v1/guias/telefonica", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == []


def test_guia_telefonica_incluye_persona_y_recursos(
    client: TestClient, auth_headers, crear_persona
):
    persona_id = crear_persona(nombre="Maria", apellido="Gomez", exttelef="102")
    sim = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5341111111"},
    ).json()
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim["id"],
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get("/api/v1/guias/telefonica", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    persona = next(p for p in data if p["persona_id"] == persona_id)
    assert persona["nombre"] == "Maria"
    assert persona["apellido"] == "Gomez"
    assert persona["exttelef"] == "102"
    assert any(
        r["tipo"] == "sim" and r["etiqueta"] == "5341111111"
        for r in persona["recursos"]
    )
    assert persona["departamento"] is None
    assert persona["cargo"] is None


def test_guia_consulta_no_ve_campos_sensibles(
    client: TestClient, auth_headers, consulta_headers, crear_persona
):
    crear_persona(
        nombre="Sensible",
        apellido="Datos",
        documento="88010112345",
        email="sensible@test.com",
        telefono="5555555",
        exttelef="101",
    )

    admin_view = client.get("/api/v1/guias/telefonica", headers=auth_headers).json()
    persona_admin = next(p for p in admin_view if p["nombre"] == "Sensible")
    assert persona_admin["documento"] == "88010112345"
    assert persona_admin["email"] == "sensible@test.com"

    consult_view = client.get("/api/v1/guias/telefonica", headers=consulta_headers).json()
    persona_consulta = next(p for p in consult_view if p["nombre"] == "Sensible")
    assert persona_consulta["documento"] is None
    assert persona_consulta["email"] is None
    assert persona_consulta["telefono"] is None
    assert persona_consulta["exttelef"] is None


def test_guia_no_incluye_asignacion_finalizada(
    client: TestClient, auth_headers, crear_persona
):
    persona_id = crear_persona(nombre="Hist", apellido="Orica")
    sim = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": "5342222222"},
    ).json()
    asignacion = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim["id"],
            "fecha_inicio": date.today().isoformat(),
        },
    ).json()
    client.put(
        f"/api/v1/asignaciones/{asignacion['id']}/finalizar",
        headers=auth_headers,
    )
    response = client.get("/api/v1/guias/telefonica", headers=auth_headers)
    persona = next(p for p in response.json() if p["persona_id"] == persona_id)
    assert persona["recursos"] == []


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/guias/telefonica")
    assert response.status_code == 401