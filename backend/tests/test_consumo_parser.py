from decimal import Decimal

import pytest

from app.services.consumo import FacturaMalFormadaError, parsear_factura

# Texto de ejemplo replicando el formato real de extraccion de un PDF de
# ETECSA: los campos de cabecera vienen con saltos de linea normales, pero
# las filas de la tabla "Resumen por Servicios" quedan pegadas entre si sin
# espacio (importe de una fila seguido inmediatamente por el numero de la
# siguiente), que es el caso mas dificil de parsear correctamente.
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


def test_parsea_cabecera():
    datos = parsear_factura(FACTURA_EJEMPLO)
    assert datos["no_factura"] == "41012682713947"
    assert datos["periodo"] == "2026-07"
    assert datos["numero_cliente"] == "7166091"
    assert datos["moneda"] == "CUP"
    assert datos["consumo_voz"] == Decimal("700.80")
    assert datos["consumo_sms"] == Decimal("310.51")
    assert datos["atraso"] == Decimal("182226.21")
    assert datos["total_a_pagar"] == Decimal("289140.52")


def test_parsea_filas_pegadas_sin_espacio():
    """Caso real: dos filas consecutivas quedan unidas sin separador.
    El parser debe poder separarlas igualmente (requisito de importacion
    robusta, no un parser fragil basado en posiciones exactas)."""
    datos = parsear_factura(FACTURA_EJEMPLO)
    numeros = [f["numero"] for f in datos["filas"]]
    assert numeros == ["59921173", "59921170", "52880232", "52885278"]

    fila = next(f for f in datos["filas"] if f["numero"] == "52880232")
    assert fila["consumo"] == Decimal("38.94")
    assert fila["importe"] == Decimal("493.94")


def test_factura_sin_no_factura_lanza_error():
    with pytest.raises(FacturaMalFormadaError):
        parsear_factura("Periodo de consumo: 01/07/26 – 31/07/26\nsin numero de factura")


def test_factura_sin_periodo_lanza_error():
    with pytest.raises(FacturaMalFormadaError):
        parsear_factura("No. factura: 123456\nsin periodo")
