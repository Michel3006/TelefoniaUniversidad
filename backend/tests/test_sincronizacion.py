from fastapi.testclient import TestClient


PAYLOAD = {
    "cargos": [{"codigo": "01", "nombre": "Especialista"}],
    "areas": [{"codigo": "001", "nombre": "Informatica"}],
    "unidades": [
        {"id_direccion": "100", "desc_direccion": "Direccion de Informatica", "nivel": 1, "id_area": "001"}
    ],
    "empleados": [
        {
            "id_empleado": "E001",
            "id_expediente": "X001",
            "no_ci": "91010112345",
            "nombre": "Carlos",
            "apellido_1": "Perez",
            "apellido_2": "Diaz",
            "exttelef": "12345",
            "id_ccosto": "CC01",
            "id_cargo": "01",
            "id_direccion": "100",
            "cubiculo": "A-205",
            "direccion": "Calle 12, Vedado",
            "ciudad": "La Habana",
            "baja": False,
        }
    ],
}


def test_rh_json_sincroniza(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/sincronizacion/rh-json",
        headers=auth_headers,
        json=PAYLOAD,
    )
    assert response.status_code == 200
    data = response.json()
    assert data == {"cargos": 1, "areas": 1, "unidades": 1, "empleados": 1}

    cargos = client.get("/api/v1/cargos/", headers=auth_headers)
    assert len(cargos.json()) == 1
    assert cargos.json()[0]["codigo"] == "01"

    areas = client.get("/api/v1/areas/", headers=auth_headers)
    assert len(areas.json()) == 1
    assert areas.json()[0]["nombre"] == "Informatica"

    departamentos = client.get("/api/v1/departamentos/", headers=auth_headers)
    assert len(departamentos.json()) == 1
    assert departamentos.json()[0]["id_direccion"] == "100"

    personas = client.get("/api/v1/personas/", headers=auth_headers)
    assert len(personas.json()) == 1
    persona = personas.json()[0]
    assert persona["id_empleado"] == "E001"
    assert persona["nombre"] == "Carlos"
    assert persona["apellido"] == "Perez"
    assert persona["cargo_id"] is not None
    assert persona["area_id"] is not None
    assert persona["cubiculo"] == "A-205"
    assert persona["direccion"] == "Calle 12, Vedado"
    assert persona["ciudad"] == "La Habana"


def test_rh_json_idempotente(client: TestClient, auth_headers):
    first = client.post("/api/v1/sincronizacion/rh-json", headers=auth_headers, json=PAYLOAD)
    second = client.post("/api/v1/sincronizacion/rh-json", headers=auth_headers, json=PAYLOAD)
    assert first.status_code == 200
    assert second.status_code == 200
    personas = client.get("/api/v1/personas/", headers=auth_headers)
    assert len(personas.json()) == 1


def test_rh_json_vacio(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/sincronizacion/rh-json",
        headers=auth_headers,
        json={"cargos": [], "areas": [], "unidades": [], "empleados": []},
    )
    assert response.status_code == 200
    assert response.json() == {"cargos": 0, "areas": 0, "unidades": 0, "empleados": 0}


def test_rrhh_no_habilitado_devuelve_503(client: TestClient, auth_headers):
    response = client.post("/api/v1/sincronizacion/rrhh", headers=auth_headers)
    assert response.status_code == 503


def test_gestor_no_puede_sincronizar(client: TestClient, gestor_headers):
    response = client.post(
        "/api/v1/sincronizacion/rh-json",
        headers=gestor_headers,
        json=PAYLOAD,
    )
    assert response.status_code == 403


def test_no_auth(client: TestClient):
    response = client.post(
        "/api/v1/sincronizacion/rh-json",
        json=PAYLOAD,
    )
    assert response.status_code == 401


def test_rh_json_body_demasiado_grande(client: TestClient, auth_headers):
    """M3/A5: un payload mayor al tope declarado se rechaza antes de procesar."""
    import json as _json

    body = _json.dumps(
        {
            "cargos": [{"codigo": "0", "nombre": "x" * (5 * 1024 * 1024)}],
            "areas": [],
            "unidades": [],
            "empleados": [],
        }
    ).encode()
    response = client.post(
        "/api/v1/sincronizacion/rh-json",
        headers={"Authorization": auth_headers["Authorization"], "Content-Type": "application/json"},
        content=body,
    )
    assert response.status_code == 413