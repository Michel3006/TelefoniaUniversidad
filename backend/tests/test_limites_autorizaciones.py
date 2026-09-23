from datetime import date, timedelta

from fastapi.testclient import TestClient


def _create_sim(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": f"54922{date.today().strftime('%Y%m%d%H%M%S')}"},
    )
    return response.json()["id"]


def test_crear_autorizacion_exceso(client: TestClient, auth_headers, crear_persona):
    sim_id = _create_sim(client, auth_headers)
    persona_id = crear_persona()
    response = client.post(
        "/api/v1/autorizaciones/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "persona_id": persona_id,
            "limite_autorizado": "200.00",
            "fecha_inicio": date.today().isoformat(),
            "fecha_fin": (date.today() + timedelta(days=30)).isoformat(),
            "motivo": "Viaje institucional",
            "responsable": "Jefe de Departamento",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["sim_id"] == sim_id
    assert data["persona_id"] == persona_id


def test_listar_autorizaciones(client: TestClient, auth_headers):
    response = client.get("/api/v1/autorizaciones/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_autorizacion_solapada_rechazada(client: TestClient, auth_headers, crear_persona):
    sim_id = _create_sim(client, auth_headers)
    persona_id = crear_persona()
    base = {
        "sim_id": sim_id,
        "persona_id": persona_id,
        "limite_autorizado": "200.00",
        "fecha_inicio": "2026-01-01",
        "fecha_fin": "2026-01-31",
    }
    ok = client.post("/api/v1/autorizaciones/", headers=auth_headers, json=base)
    assert ok.status_code == 201

    solape = client.post(
        "/api/v1/autorizaciones/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "persona_id": persona_id,
            "limite_autorizado": "300.00",
            "fecha_inicio": "2026-01-10",
            "fecha_fin": "2026-02-10",
        },
    )
    assert solape.status_code == 409


def test_autorizacion_fechas_invalidas(client: TestClient, auth_headers, crear_persona):
    sim_id = _create_sim(client, auth_headers)
    persona_id = crear_persona()
    response = client.post(
        "/api/v1/autorizaciones/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "persona_id": persona_id,
            "limite_autorizado": "200.00",
            "fecha_inicio": "2026-02-01",
            "fecha_fin": "2026-01-01",
        },
    )
    assert response.status_code == 422
