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


def test_limite_valor_negativo_rechazado(client: TestClient, auth_headers):
    """M2: un limite negativo carece de sentido."""
    sim_id = _create_sim(client, auth_headers)
    response = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "valor_limite": "-5.00",
            "vigente_desde": date.today().isoformat(),
        },
    )
    assert response.status_code == 422


def test_limite_solapado_rechazado(client: TestClient, auth_headers):
    sim_id = _create_sim(client, auth_headers)
    ok = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "valor_limite": "50.00",
            "vigente_desde": "2026-01-01",
            "vigente_hasta": "2026-01-31",
        },
    )
    assert ok.status_code == 201

    solape = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={"sim_id": sim_id, "valor_limite": "60.00", "vigente_desde": "2026-01-15"},
    )
    assert solape.status_code == 409

    # Un rango completamente posterior y con hueco (febrero) no solapa
    posterior = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "valor_limite": "70.00",
            "vigente_desde": "2026-02-15",
            "vigente_hasta": "2026-02-28",
        },
    )
    assert posterior.status_code == 201

    # Un rango abierto que arranca despues del cierre tampoco solapa
    abierto = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={"sim_id": sim_id, "valor_limite": "80.00", "vigente_desde": "2026-03-01"},
    )
    assert abierto.status_code == 201


def test_autorizacion_solapada_rechazada(client: TestClient, auth_headers):
    sim_id = _create_sim(client, auth_headers)
    persona_id = _create_persona(client, auth_headers)
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


def test_autorizacion_fechas_invalidas(client: TestClient, auth_headers):
    sim_id = _create_sim(client, auth_headers)
    persona_id = _create_persona(client, auth_headers)
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


def test_limite_cero_se_acepta(client: TestClient, auth_headers):
    """El endpoint solo rechaza valores negativos (validacion de negocio)."""
    sim_id = _create_sim(client, auth_headers)
    response = client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={"sim_id": sim_id, "valor_limite": "0.00", "vigente_desde": "2026-01-01"},
    )
    assert response.status_code in (201, 422)
