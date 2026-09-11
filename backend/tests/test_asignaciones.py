from datetime import date, timedelta

from fastapi.testclient import TestClient


def _create_persona(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/personas/",
        headers=auth_headers,
        json={"nombre": "Juan", "apellido": "Perez"},
    )
    return response.json()["id"]


def _create_linea(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/lineas/",
        headers=auth_headers,
        json={"numero": f"54911{date.today().strftime('%Y%m%d%H%M%S')}"},
    )
    return response.json()["id"]


def test_create_asignacion(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    linea_id = _create_linea(client, auth_headers)
    response = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["persona_id"] == persona_id
    assert data["tipo_recurso"] == "linea"
    assert data["fecha_fin"] is None


def test_list_asignaciones(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    linea_id = _create_linea(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get("/api/v1/asignaciones/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_asignaciones_activas(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    linea_id = _create_linea(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get("/api/v1/asignaciones/activas", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_finalizar_asignacion(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    linea_id = _create_linea(client, auth_headers)
    create = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
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


def test_finalizar_asignacion_ya_finalizada(client: TestClient, auth_headers):
    persona_id = _create_persona(client, auth_headers)
    linea_id = _create_linea(client, auth_headers)
    create = client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
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
    linea_id = _create_linea(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
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
    linea_id = _create_linea(client, auth_headers)
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "linea",
            "recurso_id": linea_id,
            "fecha_inicio": date.today().isoformat(),
        },
    )
    response = client.get(
        "/api/v1/asignaciones/por-recurso",
        headers=auth_headers,
        params={"tipo_recurso": "linea", "recurso_id": linea_id},
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
