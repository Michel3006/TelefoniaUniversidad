from datetime import date, timedelta

from fastapi.testclient import TestClient


def _create_sim(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/sims/",
        headers=auth_headers,
        json={"numero": f"54922{date.today().strftime('%Y%m%d%H%M%S')}"},
    )
    return response.json()["id"]


def _create_persona(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/personas/",
        headers=auth_headers,
        json={"nombre": "Ana", "apellido": "Lopez"},
    )
    return response.json()["id"]


def test_crear_limite(client: TestClient, auth_headers):
    sim_id = _create_sim(client, auth_headers)
    response = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "valor_limite": "50.00",
            "vigente_desde": date.today().isoformat(),
        },
    )
    assert response.status_code == 201
    assert response.json()["sim_id"] == sim_id


def test_gestor_no_puede_crear_limite(client: TestClient, gestor_headers, auth_headers):
    """Los limites de consumo son sensibles: solo admin puede crearlos."""
    sim_id = _create_sim(client, auth_headers)
    response = client.post(
        "/api/v1/limites/",
        headers=gestor_headers,
        json={
            "sim_id": sim_id,
            "valor_limite": "50.00",
            "vigente_desde": date.today().isoformat(),
        },
    )
    assert response.status_code == 403


def test_crear_autorizacion_exceso(client: TestClient, auth_headers):
    sim_id = _create_sim(client, auth_headers)
    persona_id = _create_persona(client, auth_headers)
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
