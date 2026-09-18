"""Prueba end-to-end con el PDF real de ETECSA aportado por el usuario
(periodo 07/2026). Se ejecuta solo si el archivo esta presente en la raiz
del repositorio; en caso contrario se omite (skip) para no romper el CI en
entornos que no lo tengan."""
import os

import pytest
from fastapi.testclient import TestClient

PDF_RELATIVO = os.path.join("..", "..", "202607_73212_41012682713947.pdf")


def _ruta_pdf() -> str | None:
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), PDF_RELATIVO))
    return ruta if os.path.exists(ruta) else None


_pdf_presente = _ruta_pdf() is not None


@pytest.mark.skipif(not _pdf_presente, reason="PDF real de ETECSA no presente en la raiz del repositorio")
def test_importar_pdf_real_etecsa(client: TestClient, auth_headers):
    ruta = _ruta_pdf()
    with open(ruta, "rb") as f:
        contenido = f.read()
    assert len(contenido) > 100

    response = client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": (os.path.basename(ruta), contenido, "application/pdf")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["no_factura"] == "41012682713947"
    assert data["periodo"] == "2026-07"
    assert data["procesados"] == 207
    assert data["asociados"] == 0
    assert data["no_asociados"] == 207
    assert data["excesos"] == 0

    consumos = client.get(
        "/api/v1/consumo/", headers=auth_headers, params={"limit": 500}
    ).json()
    assert len(consumos) == 207
    assert all(c["en_exceso"] is False for c in consumos)

    facturas = client.get("/api/v1/facturas-etecsa/", headers=auth_headers).json()
    assert len(facturas) == 1
    assert facturas[0]["no_factura"] == "41012682713947"
    assert facturas[0]["periodo"] == "2026-07"
    assert facturas[0]["total_a_pagar"] == "289140.52"


@pytest.mark.skipif(not _pdf_presente, reason="PDF real de ETECSA no presente en la raiz del repositorio")
def test_importar_pdf_real_duplicado(client: TestClient, auth_headers):
    ruta = _ruta_pdf()
    with open(ruta, "rb") as f:
        contenido = f.read()

    primera = client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": (os.path.basename(ruta), contenido, "application/pdf")},
    )
    assert primera.status_code == 200

    segunda = client.post(
        "/api/v1/consumo/importar-pdf",
        headers=auth_headers,
        files={"archivo": (os.path.basename(ruta), contenido, "application/pdf")},
    )
    assert segunda.status_code == 409

    historial = client.get(
        "/api/v1/historial/", headers=auth_headers, params={"entidad": "facturas_etecsa"}
    ).json()
    assert len(historial) == 1
    assert historial[0]["accion"] == "importado"