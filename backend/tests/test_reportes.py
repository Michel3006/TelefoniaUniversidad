from fastapi.testclient import TestClient


def test_inventario(client: TestClient, auth_headers):
    response = client.get("/api/v1/reportes/inventario", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "telefonos_fijos" in data
    assert "sims" in data
    assert "dispositivos" in data
    assert "personas" in data


def test_recursos_por_departamento(client: TestClient, auth_headers):
    response = client.get(
        "/api/v1/reportes/recursos-por-departamento", headers=auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/reportes/inventario")
    assert response.status_code == 401


FACTURA_EJEMPLO = """
Número de Cliente:7166091
Folio: 00062639
No. factura: 41012682713947
Fecha de Vencimiento: 31/08/26
Periodo de consumo: 01/07/26 – 31/07/26
Moneda: CUP
Fecha Factura: 05/08/26
Cuota Mensual Consumo Comisión Impuesto Facturado Atraso Total a Pagar
105,903.00 1,011.31 0.00 0.00 106,914.31 182,226.21 289,140.52
Resumen por Servicios
Servicio Cuota Consumo Comisión Impuesto Importe
52880232 455.00 38.94 0.00 0.00 493.94
Total 455.00 38.94 0.00 0.00 493.94
Pagar a:
"""


def _subir_factura(client: TestClient, auth_headers, monkeypatch):
    monkeypatch.setattr(
        "app.services.consumo.extraer_texto_pdf",
        lambda contenido: FACTURA_EJEMPLO,
    )
    return client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": ("factura.pdf", b"%PDF-contenido-simulado", "application/pdf")},
    )


def test_consumo_por_periodo(client: TestClient, auth_headers, monkeypatch):
    client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "52880232"})
    _subir_factura(client, auth_headers, monkeypatch)

    response = client.get("/api/v1/reportes/consumo-por-periodo", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert any(r["periodo"] == "2026-07" for r in data)
    fila = next(r for r in data if r["periodo"] == "2026-07")
    assert fila["registros"] == 1
    assert fila["excesos"] == 1
    assert fila["excesos_autorizados"] == 0


def test_reporte_excesos(client: TestClient, auth_headers, monkeypatch):
    client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "52880232"})
    _subir_factura(client, auth_headers, monkeypatch)

    response = client.get("/api/v1/reportes/excesos", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["numero"] == "52880232"
    assert data[0]["periodo"] == "2026-07"
    assert data[0]["con_autorizacion"] is False

    response = client.get(
        "/api/v1/reportes/excesos", headers=auth_headers, params={"autorizado": "true"}
    )
    assert response.status_code == 200
    assert response.json() == []


def test_recursos_sin_asignar(client: TestClient, auth_headers):
    sim_resp = client.post(
        "/api/v1/sims/", headers=auth_headers, json={"numero": "5491000000001"}
    )
    client.post(
        "/api/v1/sims/", headers=auth_headers, json={"numero": "5491000000002"}
    )
    client.post(
        "/api/v1/telefonos/", headers=auth_headers, json={"numero": "33220001"}
    )

    asignados = client.get("/api/v1/asignaciones/activas", headers=auth_headers).json()
    for a in asignados:
        client.put(f"/api/v1/asignaciones/{a['id']}/finalizar", headers=auth_headers)

    response = client.get("/api/v1/reportes/recursos-sin-asignar", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    numeros_sim = {s["descripcion"] for s in data["sims"]}
    assert "5491000000001" in numeros_sim
    assert "5491000000002" in numeros_sim
    assert any(t["descripcion"] == "33220001" for t in data["telefonos"])


def test_recursos_por_persona(client: TestClient, auth_headers, crear_persona):
    persona_id = crear_persona(nombre="Ana", apellido="Lopez")
    sim = client.post(
        "/api/v1/sims/", headers=auth_headers, json={"numero": "5491999999999"}
    )
    client.post(
        "/api/v1/asignaciones/",
        headers=auth_headers,
        json={
            "persona_id": persona_id,
            "tipo_recurso": "sim",
            "recurso_id": sim.json()["id"],
            "fecha_inicio": "2026-01-01",
        },
    )

    response = client.get("/api/v1/reportes/recursos-por-persona", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert any(
        p["persona_id"] == persona_id
        and any(r["tipo_recurso"] == "sim" for r in p["recursos"])
        for p in data
    )
