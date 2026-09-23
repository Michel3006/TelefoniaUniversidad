from fastapi.testclient import TestClient


def test_historial_vacio(client: TestClient, auth_headers):
    response = client.get("/api/v1/historial/", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == []


def test_historial_registra_creacion(client: TestClient, auth_headers):
    telefono = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "6666666001"},
    )
    telefono_id = telefono.json()["id"]

    response = client.get("/api/v1/historial/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["entidad"] == "telefonos"
    assert data[0]["entidad_id"] == telefono_id
    assert data[0]["accion"] == "creado"


def test_historial_filtro_por_entidad(client: TestClient, auth_headers):
    client.post("/api/v1/telefonos/", headers=auth_headers, json={"numero": "6666666002"})
    client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "5491199999001"})

    telefonos = client.get(
        "/api/v1/historial/",
        headers=auth_headers,
        params={"entidad": "telefonos"},
    )
    assert len(telefonos.json()) == 1

    sims = client.get(
        "/api/v1/historial/",
        headers=auth_headers,
        params={"entidad": "sims"},
    )
    assert len(sims.json()) == 1


def test_historial_filtro_por_entidad_id(client: TestClient, auth_headers):
    contrato = client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "H-001"})
    contrato_id = contrato.json()["id"]
    response = client.get(
        "/api/v1/historial/",
        headers=auth_headers,
        params={"entidad": "contratos", "entidad_id": contrato_id},
    )
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_historial_registra_actualizacion(client: TestClient, auth_headers):
    contrato = client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "H-002"})
    contrato_id = contrato.json()["id"]
    client.put(
        f"/api/v1/contratos/{contrato_id}",
        headers=auth_headers,
        json={"numero": "H-002", "observaciones": "Nueva descripcion"},
    )
    response = client.get(
        "/api/v1/historial/",
        headers=auth_headers,
        params={"entidad": "contratos", "entidad_id": contrato_id},
    )
    data = response.json()
    acciones = {d["accion"] for d in data}
    assert "creado" in acciones
    assert "actualizado" in acciones


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/historial/")
    assert response.status_code == 401


def test_gestor_no_puede_ver_historial(client: TestClient, gestor_headers):
    """A1: el historial es exclusivo de admin."""
    response = client.get("/api/v1/historial/", headers=gestor_headers)
    assert response.status_code == 403


def test_consulta_no_puede_ver_historial(client: TestClient, consulta_headers):
    response = client.get("/api/v1/historial/", headers=consulta_headers)
    assert response.status_code == 403


def test_historial_eliminacion_con_valor_anterior(client: TestClient, auth_headers):
    """M1: al eliminar un registro queda el JSON del valor anterior."""
    contrato = client.post("/api/v1/contratos/", headers=auth_headers, json={"numero": "H-003"})
    contrato_id = contrato.json()["id"]
    assert client.delete(f"/api/v1/contratos/{contrato_id}", headers=auth_headers).status_code == 204

    data = client.get(
        "/api/v1/historial/",
        headers=auth_headers,
        params={"entidad": "contratos", "entidad_id": contrato_id},
    ).json()
    assert any(h["accion"] == "eliminado" for h in data)
    eliminado = next(h for h in data if h["accion"] == "eliminado")
    assert eliminado["valor_anterior"] is not None