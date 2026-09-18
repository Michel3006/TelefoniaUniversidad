from datetime import date, timedelta

from fastapi.testclient import TestClient


def _create_persona(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/personas/",
        headers=auth_headers,
        json={"nombre": "Juan", "apellido": "Perez"},
    )
    return response.json()["id"]


def _create_sim(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": f"54911{date.today().strftime('%Y%m%d%H%M%S')}"},
    )
    return response.json()["id"]


def test_create_asignacion(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    response = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["persona_id"] == persona_id
    assert data["tipo_recurso"] == "sim"
    assert data["fecha_fin"] is None


def test_list_asignaciones(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get("/api/v1/asignaciones/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_asignaciones_activas(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get("/api/v1/asignaciones/activas", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_finalizar_asignacion(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    create = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    asignacion_id = create.json()["id"]
    response = client.put(
        f"/api/v1/asignaciones/{asignacion_id}/finalizar",
        headers=auth_headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["fecha_fin"] is not None

    historial = client.get("/api/v1/historial/", headers=auth_headers).json()
    acciones = [h["accion"] for h in historial if h["entidad"] == "asignaciones"]
    assert "desasignado" in acciones


def test_finalizar_asignacion_ya_finalizada(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    create = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    asignacion_id = create.json()["id"]
    client.put(
        f"/api/v1/asignaciones/{asignacion_id}/finalizar",
        headers=auth_headers,
    )
    response = client.put(
        f"/api/v1/asignaciones/{asignacion_id}/finalizar",
        headers=auth_headers,
    )
    assert response.status_code == 400


def test_por_persona(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get(
        f"/api/v1/asignaciones/por-persona/{persona_id}", headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_por_recurso(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get(
        "/api/v1/asignaciones/por-recurso",
        headers=auth_headers,
        params={"tipo_recurso": "sim", "recurso_id": sim_id},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_finalizar_not_found(client: TestClient, auth_headers):
    response = client.put(
        "/api/v1/asignaciones/99999/finalizar",
        headers=auth_headers,
    )
    assert response.status_code == 404


def test_no_permite_doble_asignacion_activa(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    otra_persona_id = _create_persona(client, auth_headers)
    sim_id = _create_sim(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": otra_persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    assert response.status_code == 409


def test_tipo_recurso_invalido(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    response = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": 1,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    assert response.status_code == 400


def test_recurso_inexistente(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    response = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": 999999,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    assert response.status_code == 404
