"""Prueba end-to-end con el PDF real de ETECSA aportado por el usuario
(periodo 07/2026). Se ejecuta solo si el archivo esta presente en
`backend/tests/private/`, en la ruta indicada por la variable `ETECSA_PDF_PATH`,
o en la raiz del repositorio; en caso contrario se omite (skip) para no
romper el CI en entornos que no lo tengan."""
import os

import pytest
from fastapi.testclient import TestClient


def _ruta_pdf() -> str | None:
    candidatas = []
    anon = os.environ.get("ETECSA_PDF_PATH")
    if anon:
        candidatas.append(anon)
    candidatas.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "private", "202607_73212_41012682713947.pdf"))
    )
    candidatas.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "202607_73212_41012682713947.pdf"))
    )
    for ruta in candidatas:
        if ruta and os.path.exists(ruta):
            return ruta
    return None


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
    assert data["asociados"] == data["sims_creadas"]
    assert data["asociados"] + data["no_asociados"] == 207
    # Punto 7: consumo > 0 sin autorizacion => excedente/alarma.
    assert data["excesos"] > 0
    assert data["alarmas"] == data["excesos"]

    consumos = client.get(
        "/api/v1/consumo/", headers=auth_headers, params={"limit": 500}
    ).json()
    assert len(consumos) == 207
    excesos = [c for c in consumos if c["en_exceso"] is True]
    assert len(excesos) == data["excesos"]
    assert all(c["con_autorizacion"] is False for c in excesos)

    sims = client.get("/api/v1/sims/", headers=auth_headers, params={"limit": 500}).json()
    assert len(sims) == data["sims_creadas"]
    for numero in data["numeros_sims_creadas"]:
        assert any(s["numero"] == numero for s in sims)
    for numero in data["numeros_no_asociados"]:
        assert all(s["numero"] != numero for s in sims)

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