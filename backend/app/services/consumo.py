"""Importacion de facturas mensuales de ETECSA (PDF).

Punto 7 del PLAN_CAMBIOS: el PDF es la fuente de verdad de cuota,
consumo (excedente) e importe. No existen modulos de Costos/Planes/
Limites: la cuota reemplaza al plan/limite manual.

Reglas:
- Servicio = numero de SIM (se crea si es movil inexistente).
- Cuota = lo que le toca a la SIM (asociada a la SIM, solo lectura).
- Consumo = excedente; si es > 0 y no hay autorizacion vigente => ALARMA.
- Importe = total a pagar, tomado directamente del PDF (no calculado).
"""
import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.consumo import AutorizacionExceso, Consumo, FacturaEtecsa
from app.models.historial import Historial
from app.models.telefonia import Sim

_AMOUNT = r"[\d,]{1,12}\.\d{2}"
_FILA_RE = re.compile(
    rf"(?P<numero>\d{{6,10}})\s*"
    rf"(?P<cuota>{_AMOUNT})\s*"
    rf"(?P<consumo>{_AMOUNT})\s*"
    rf"(?P<comision>{_AMOUNT})\s*"
    rf"(?P<impuesto>{_AMOUNT})\s*"
    rf"(?P<importe>{_AMOUNT})"
)

_PREFIJOS_SIM = ("5", "6")


def _es_numero_sim(numero: str) -> bool:
    return len(numero) == 8 and numero.startswith(_PREFIJOS_SIM)


_MAX_PAGINAS = 100
_MAX_TEXTO_CARACTERES = 5_000_000
_TOLERANCIA_TOTALES = Decimal("0.01")


def _decimal(texto: str) -> Decimal:
    try:
        return Decimal(texto.replace(",", ""))
    except (InvalidOperation, AttributeError):
        return Decimal("0")


def _fecha_corta(texto: str | None) -> date | None:
    if not texto:
        return None
    try:
        return datetime.strptime(texto.strip(), "%d/%m/%y").date()
    except ValueError:
        return None


def _campo(patron: str, texto: str) -> str | None:
    m = re.search(patron, texto)
    return m.group(1).strip() if m else None


class FacturaMalFormadaError(Exception):
    pass


class FacturaDemasiadoGrandeError(Exception):
    pass


class TotalesIncoherentesError(Exception):
    pass


def parsear_factura(texto: str) -> dict:
    no_factura = _campo(r"[Nn]o\.?\s*[Ff]actura:?\s*(\S+)", texto)
    if not no_factura:
        raise FacturaMalFormadaError("No se pudo identificar el numero de factura en el PDF")

    periodo_match = re.search(
        r"Periodo de consumo:?\s*(\d{2}/\d{2}/\d{2})\s*[-–]\s*(\d{2}/\d{2}/\d{2})",
        texto,
    )
    if not periodo_match:
        raise FacturaMalFormadaError("No se pudo identificar el periodo de consumo en el PDF")
    fecha_inicio_periodo = _fecha_corta(periodo_match.group(1))
    periodo = fecha_inicio_periodo.strftime("%Y-%m") if fecha_inicio_periodo else None
    if periodo is None:
        raise FacturaMalFormadaError("Periodo de consumo con formato de fecha invalido")

    numero_cliente = _campo(r"[NnÚú]mero de [Cc]liente:?\s*(\S+)", texto)
    folio = _campo(r"Folio:?\s*(\S+)", texto)
    fecha_factura = _fecha_corta(_campo(r"Fecha Factura:?\s*(\S+)", texto))
    fecha_vencimiento = _fecha_corta(_campo(r"Fecha de Vencimiento:?\s*(\S+)", texto))
    moneda = _campo(r"Moneda:?\s*(CUP|USD)", texto) or "CUP"

    consumo_voz = _campo(rf"Consumo Voz\s*({_AMOUNT})", texto)
    consumo_sms = _campo(rf"Consumo SMS\s*({_AMOUNT})", texto)

    totales_match = re.search(
        rf"\bTotal\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})",
        texto,
    )
    cuota_total = consumo_total = comision_total = impuesto_total = facturado_total = None
    if totales_match:
        cuota_total, consumo_total, comision_total, impuesto_total, facturado_total = (
            _decimal(g) for g in totales_match.groups()
        )

    atraso = None
    total_a_pagar = None
    cabecera_match = re.search(
        rf"({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})\s+({_AMOUNT})",
        texto,
    )
    if cabecera_match:
        valores = [_decimal(g) for g in cabecera_match.groups()]
        atraso = valores[5]
        total_a_pagar = valores[6]

    seccion = texto
    inicio = texto.find("Resumen por Servicios")
    fin = texto.find("Pagar a:")
    if inicio != -1:
        seccion = texto[inicio: fin if fin != -1 else None]

    filas = []
    for m in _FILA_RE.finditer(seccion):
        filas.append(
            {
                "numero": m.group("numero"),
                "cuota": _decimal(m.group("cuota")),
                "consumo": _decimal(m.group("consumo")),
                "comision": _decimal(m.group("comision")),
                "impuesto": _decimal(m.group("impuesto")),
                "importe": _decimal(m.group("importe")),
            }
        )

    return {
        "no_factura": no_factura,
        "numero_cliente": numero_cliente,
        "folio": folio,
        "periodo": periodo,
        "fecha_factura": fecha_factura,
        "fecha_vencimiento": fecha_vencimiento,
        "moneda": moneda,
        "cuota_total": cuota_total,
        "consumo_total": consumo_total,
        "comision_total": comision_total,
        "impuesto_total": impuesto_total,
        "facturado_total": facturado_total,
        "atraso": atraso,
        "total_a_pagar": total_a_pagar,
        "consumo_voz": _decimal(consumo_voz) if consumo_voz else None,
        "consumo_sms": _decimal(consumo_sms) if consumo_sms else None,
        "filas": filas,
    }


def extraer_texto_pdf(contenido: bytes) -> str:
    import io

    import pdfplumber  # noqa: PLC0415

    texto_paginas = []
    with pdfplumber.open(io.BytesIO(contenido)) as pdf:
        if len(pdf.pages) > _MAX_PAGINAS:
            raise FacturaDemasiadoGrandeError(
                f"El PDF excede el numero maximo de paginas ({_MAX_PAGINAS})"
            )
        for pagina in pdf.pages:
            texto_paginas.append(pagina.extract_text() or "")
    texto = "\n".join(texto_paginas)
    if len(texto) > _MAX_TEXTO_CARACTERES:
        raise FacturaDemasiadoGrandeError("El PDF excede el tamano maximo de texto extraible")
    return texto


def _verificar_totales(datos: dict) -> None:
    if datos["cuota_total"] is None:
        return
    comprobaciones = (
        ("cuota_total", "cuota"),
        ("consumo_total", "consumo"),
        ("comision_total", "comision"),
        ("impuesto_total", "impuesto"),
        ("facturado_total", "importe"),
    )
    desviaciones = []
    for esperado, campo in comprobaciones:
        suma = sum((fila[campo] for fila in datos["filas"]), start=Decimal("0"))
        if abs(suma - datos[esperado]) > _TOLERANCIA_TOTALES:
            desviaciones.append(f"{campo}: {suma} != {datos[esperado]}")
    if desviaciones:
        raise TotalesIncoherentesError(
            "La fila Total no coincide con la suma de los servicios: " + "; ".join(desviaciones)
        )


def _rango_mes(periodo: str) -> tuple[date, date]:
    import calendar

    anio, mes = (int(p) for p in periodo.split("-"))
    ultimo = calendar.monthrange(anio, mes)[1]
    return date(anio, mes, 1), date(anio, mes, ultimo)


def tiene_autorizacion(db: Session, sim_id: int, periodo: str) -> bool:
    """True si hay autorizacion de exceso vigente para la SIM en el periodo."""
    inicio, fin = _rango_mes(periodo)
    existe = db.scalar(
        select(AutorizacionExceso.id)
        .where(
            AutorizacionExceso.sim_id == sim_id,
            AutorizacionExceso.fecha_inicio <= fin,
            (AutorizacionExceso.fecha_fin.is_(None)) | (AutorizacionExceso.fecha_fin >= inicio),
        )
        .limit(1)
    )
    return existe is not None


def importar_factura(
    db: Session, contenido: bytes, nombre_archivo: str, usuario_id: int | None = None
) -> dict:
    texto = extraer_texto_pdf(contenido)
    datos = parsear_factura(texto)
    _verificar_totales(datos)

    existente = db.scalar(select(FacturaEtecsa).where(FacturaEtecsa.no_factura == datos["no_factura"]))
    if existente is not None:
        raise ValueError(f"La factura {datos['no_factura']} ya fue importada anteriormente")

    factura = FacturaEtecsa(
        no_factura=datos["no_factura"],
        numero_cliente=datos["numero_cliente"],
        folio=datos["folio"],
        periodo=datos["periodo"],
        fecha_factura=datos["fecha_factura"],
        fecha_vencimiento=datos["fecha_vencimiento"],
        moneda=datos["moneda"],
        cuota_total=datos["cuota_total"],
        consumo_total=datos["consumo_total"],
        comision_total=datos["comision_total"],
        impuesto_total=datos["impuesto_total"],
        facturado_total=datos["facturado_total"],
        atraso=datos["atraso"],
        total_a_pagar=datos["total_a_pagar"],
        consumo_voz=datos["consumo_voz"],
        consumo_sms=datos["consumo_sms"],
        archivo_origen=nombre_archivo,
    )
    db.add(factura)
    db.flush()

    asociados = 0
    no_asociados: list[str] = []
    sims_creadas: list[str] = []
    excesos = 0
    alarmas = 0

    for fila in datos["filas"]:
        sim = db.scalar(select(Sim).where(Sim.numero == fila["numero"]))
        if sim is None and _es_numero_sim(fila["numero"]):
            sim = Sim(numero=fila["numero"])
            db.add(sim)
            db.flush()
            sims_creadas.append(fila["numero"])

        con_autorizacion = False
        if sim:
            con_autorizacion = tiene_autorizacion(db, sim.id, datos["periodo"])

        # Punto 7: excedente = consumo > 0 (la cuota del PDF es el limite).
        excedente = fila["consumo"] > 0
        # Alarma solo si hay excedente Y no esta autorizado.
        alarma = bool(sim and excedente and not con_autorizacion)
        en_exceso = bool(excedente and (sim is None or not con_autorizacion))

        # El limite "normal" es la cuota del PDF (solo informativo, no manual).
        limite_normal = fila["cuota"]
        limite_efectivo = fila["cuota"]

        db.add(
            Consumo(
                factura_id=factura.id,
                sim_id=sim.id if sim else None,
                numero_detectado=fila["numero"],
                cuota=fila["cuota"],
                consumo=fila["consumo"],
                comision=fila["comision"],
                impuesto=fila["impuesto"],
                importe=fila["importe"],
                en_exceso=en_exceso,
                con_autorizacion=con_autorizacion,
                limite_normal=limite_normal,
                limite_efectivo=limite_efectivo,
            )
        )

        if alarma:
            alarmas += 1
            db.add(
                Historial(
                    entidad="alarma_excedente",
                    entidad_id=sim.id if sim else None,
                    accion="alarma",
                    valor_nuevo=(
                        f"numero={fila['numero']} periodo={datos['periodo']} "
                        f"cuota={fila['cuota']} consumo={fila['consumo']} "
                        f"importe={fila['importe']} sin_autorizacion"
                    ),
                    usuario_id=usuario_id,
                )
            )

        if sim:
            asociados += 1
        else:
            no_asociados.append(fila["numero"])
        if en_exceso:
            excesos += 1

    db.commit()

    return {
        "factura_id": factura.id,
        "no_factura": datos["no_factura"],
        "periodo": datos["periodo"],
        "procesados": len(datos["filas"]),
        "asociados": asociados,
        "sims_creadas": len(sims_creadas),
        "no_asociados": len(no_asociados),
        "excesos": excesos,
        "alarmas": alarmas,
        "numeros_no_asociados": no_asociados,
        "numeros_sims_creadas": sims_creadas,
    }
