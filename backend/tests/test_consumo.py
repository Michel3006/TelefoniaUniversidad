from fastapi.testclient import TestClient

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
Desglose (Consumo)
Consumo Voz 700.80
Consumo SMS 310.51
Resumen por Servicios
Servicio Cuota Consumo Comisión Impuesto Importe
59921173 560.00 0.00 0.00 0.00 560.0059921170 770.00 0.00 0.00 0.00 770.00
52880232 455.00 38.94 0.00 0.00 493.9452885278 455.00 3.15 0.00 0.00 458.15
Total 2,240.00 42.09 0.00 0.00 2,282.09
Pagar a:
"""

TEXTO_MALFORMADO = "esto no es una factura valida"


def _subir_factura(client: TestClient, auth_headers, monkeypatch, texto=FACTURA_EJEMPLO):
    monkeypatch.setattr(
        "app.services.consumo.extraer_texto_pdf",
        lambda contenido: texto,
    )
    return client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": ("factura.pdf", b"%PDF-contenido-simulado", "application/pdf")},
    )


def test_importar_factura(client: TestClient, auth_headers, monkeypatch):
    response = _subir_factura(client, auth_headers, monkeypatch)
    assert response.status_code == 200
    data = response.json()
    assert data["no_factura"] == "41012682713947"
    assert data["periodo"] == "2026-07"
    assert data["procesados"] == 4
    assert data["asociados"] == 0
    assert data["no_asociados"] == 4
    assert data["excesos"] == 0
    assert "59921173" in data["numeros_no_asociados"]


def test_importar_factura_asocia_sims_y_detecta_excesos(client: TestClient, auth_headers, monkeypatch):
    sim = client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "59921173"})
    sim_asociada = client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "52880232"})
    client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={
            "sim_id": sim_asociada.json()["id"],
            "valor_limite": "10.00",
            "vigente_desde": "2026-01-01",
        },
    )

    response = _subir_factura(client, auth_headers, monkeypatch)
    assert response.status_code == 200
    data = response.json()
    assert data["asociados"] == 2
    assert data["no_asociados"] == 2
    assert data["excesos"] == 1
    assert "59921173" not in data["numeros_no_asociados"]


def test_importar_factura_duplicada_conflicto(client: TestClient, auth_headers, monkeypatch):
    _subir_factura(client, auth_headers, monkeypatch)
    response = _subir_factura(client, auth_headers, monkeypatch)
    assert response.status_code == 409


def test_importar_factura_malformada(client: TestClient, auth_headers, monkeypatch):
    response = _subir_factura(client, auth_headers, monkeypatch, texto=TEXTO_MALFORMADO)
    assert response.status_code == 422


def test_importar_no_pdf(client: TestClient, auth_headers, monkeypatch):
    response = client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": ("factura.txt", b"texto", "text/plain")},
    )
    assert response.status_code == 400


FACTURA_TOTALES_INCOHERENTES = """
Número de Cliente:7166091
Folio: 00062639
No. factura: 41012682713948
Fecha de Vencimiento: 31/08/26
Periodo de consumo: 01/08/26 – 31/08/26
Moneda: CUP
Fecha Factura: 05/09/26
Cuota Mensual Consumo Comisión Impuesto Facturado Atraso Total a Pagar
105,903.00 1,011.31 0.00 0.00 106,914.31 182,226.21 289,140.52
Desglose (Consumo)
Consumo Voz 700.80
Consumo SMS 310.51
Resumen por Servicios
Servicio Cuota Consumo Comisión Impuesto Importe
59921173 560.00 0.00 0.00 0.00 560.0059921170 770.00 0.00 0.00 0.00 770.00
Total 1,330.00 0.00 0.00 0.00 999,999.00
Pagar a:
"""


def test_importar_factura_totales_incoherentes(client: TestClient, auth_headers, monkeypatch):
    """A5: si el footer no coincide con las filas, la importacion se rechaza."""
    monkeypatch.setattr(
        "app.services.consumo.extraer_texto_pdf",
        lambda contenido: FACTURA_TOTALES_INCOHERENTES,
    )
    response = client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": ("factura.pdf", b"%PDF-contenido-simulado", "application/pdf")},
    )
    assert response.status_code == 422


def test_importar_archivo_demasiado_grande(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": ("factura.pdf", b"%PDF-simulado" + b"x" * (15 * 1024 * 1024), "application/pdf")},
    )
    assert response.status_code == 400


def test_consulta_no_puede_importar(client: TestClient, consulta_headers, monkeypatch):
    response = _subir_factura(client, consulta_headers, monkeypatch)
    assert response.status_code == 403


def test_listar_consumos(client: TestClient, auth_headers, monkeypatch, db):
    _subir_factura(client, auth_headers, monkeypatch)
    response = client.get("/api/v1/consumo/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_listar_consumos_por_periodo(client: TestClient, auth_headers, monkeypatch):
    _subir_factura(client, auth_headers, monkeypatch)
    response = client.get(
        "/api/v1/consumo/",
        headers=auth_headers,
        params={"periodo": "2026-07"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 4

    response = client.get(
        "/api/v1/consumo/",
        headers=auth_headers,
        params={"periodo": "2025-01"},
    )
    assert response.status_code == 200
    assert response.json() == []


def test_consumo_no_asociados(client: TestClient, auth_headers, monkeypatch):
    _subir_factura(client, auth_headers, monkeypatch)
    response = client.get("/api/v1/consumo/no-asociados", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_consumo_excesos(client: TestClient, auth_headers, monkeypatch):
    sim = client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "52880232"})
    client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={"sim_id": sim.json()["id"], "valor_limite": "10.00", "vigente_desde": "2026-01-01"},
    )
    _subir_factura(client, auth_headers, monkeypatch)
    response = client.get("/api/v1/consumo/excesos", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["en_exceso"] is True


def test_factura_detalle_incluye_consumos(client: TestClient, auth_headers, monkeypatch):
    _subir_factura(client, auth_headers, monkeypatch)
    facturas = client.get("/api/v1/facturas-etecsa/", headers=auth_headers)
    assert facturas.status_code == 200
    facturas_json = facturas.json()
    assert len(facturas_json) == 1
    assert facturas_json[0]["no_factura"] == "41012682713947"
    assert facturas_json[0]["periodo"] == "2026-07"

    factura_id = facturas_json[0]["id"]
    detalle = client.get(f"/api/v1/facturas-etecsa/{factura_id}", headers=auth_headers)
    assert detalle.status_code == 200
    assert detalle.json()["total_a_pagar"] == "289140.52"


def test_factura_get_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/facturas-etecsa/99999", headers=auth_headers)
    assert response.status_code == 404


def test_eliminar_factura_cascade(client: TestClient, auth_headers, monkeypatch):
    _subir_factura(client, auth_headers, monkeypatch)
    factura_id = client.get("/api/v1/facturas-etecsa/", headers=auth_headers).json()[0]["id"]

    response = client.delete(f"/api/v1/facturas-etecsa/{factura_id}", headers=auth_headers)
    assert response.status_code == 204

    assert client.get("/api/v1/facturas-etecsa/", headers=auth_headers).json() == []
    assert client.get("/api/v1/consumo/", headers=auth_headers).json() == []


def test_gestor_no_puede_eliminar_factura(client: TestClient, gestor_headers, auth_headers, monkeypatch):
    _subir_factura(client, auth_headers, monkeypatch)
    factura_id = client.get("/api/v1/facturas-etecsa/", headers=auth_headers).json()[0]["id"]
    response = client.delete(f"/api/v1/facturas-etecsa/{factura_id}", headers=gestor_headers)
    assert response.status_code == 403


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/consumo/")
    assert response.status_code == 401


def test_importar_factura_registra_historial(client: TestClient, auth_headers, monkeypatch, db):
    _subir_factura(client, auth_headers, monkeypatch)
    response = client.get("/api/v1/historial/", headers=auth_headers)
    assert response.status_code == 200
    acciones = [h["accion"] for h in response.json() if h["entidad"] == "facturas_etecsa"]
    assert "importado" in acciones


def test_exceso_con_autorizacion_marca_campo(client: TestClient, auth_headers, monkeypatch):
    """Consumo que supera el limite normal pero esta cubierto por una
    autorizacion vigente: queda con_autorizacion=True y limite_efectivo=limite
    autorizado."""
    sim = client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "52880232"})
    sim_id = sim.json()["id"]
    persona = client.post(
        "/api/v1/personas/", headers=auth_headers, json={"nombre": "Ana", "apellido": "Lopez"}
    )
    client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={"sim_id": sim_id, "valor_limite": "10.00", "vigente_desde": "2026-01-01"},
    )

    response = _subir_factura(client, auth_headers, monkeypatch)
    assert response.json()["excesos"] == 1
    consumo = client.get("/api/v1/consumo/", headers=auth_headers).json()
    fila_52880232 = [c for c in consumo if c["numero_detectado"] == "52880232"][0]
    assert fila_52880232["en_exceso"] is True
    assert fila_52880232["con_autorizacion"] is False
    assert fila_52880232["limite_efectivo"] == "10.00"

    client.post(
        "/api/v1/autorizaciones/",
        headers=auth_headers,
        json={
            "sim_id": sim_id,
            "persona_id": persona.json()["id"],
            "limite_autorizado": "50.00",
            "fecha_inicio": "2026-07-01",
            "fecha_fin": "2026-07-31",
        },
    )
    factura_id = client.get("/api/v1/facturas-etecsa/", headers=auth_headers).json()[0]["id"]
    client.delete(f"/api/v1/facturas-etecsa/{factura_id}", headers=auth_headers)
    _subir_factura(client, auth_headers, monkeypatch)

    fila = client.get("/api/v1/consumo/", headers=auth_headers).json()
    autorizada = [c for c in fila if c["numero_detectado"] == "52880232"][0]
    assert autorizada["en_exceso"] is False
    assert autorizada["con_autorizacion"] is True
    assert autorizada["limite_normal"] == "10.00"
    assert autorizada["limite_efectivo"] == "50.00"

    excesos = client.get(
        "/api/v1/consumo/excesos", headers=auth_headers, params={"autorizado": "true"}
    ).json()
    assert excesos == []


def test_excesos_paginado_y_filtro_autorizado(client: TestClient, auth_headers, monkeypatch):
    sim = client.post("/api/v1/sims/", headers=auth_headers, json={"numero": "52880232"})
    client.post(
        "/api/v1/limites/",
        headers=auth_headers,
        json={"sim_id": sim.json()["id"], "valor_limite": "10.00", "vigente_desde": "2026-01-01"},
    )
    _subir_factura(client, auth_headers, monkeypatch)

    response = client.get(
        "/api/v1/consumo/no-asociados", headers=auth_headers, params={"skip": 0, "limit": 2}
    )
    assert response.status_code == 200
    assert len(response.json()) == 2