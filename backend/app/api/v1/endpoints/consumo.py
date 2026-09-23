from fastapi import APIRouter, Depends, HTTPException, Query, Request, UploadFile, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.security import require_role
from app.db.session import get_db
from app.models.consumo import Consumo, FacturaEtecsa
from app.models.historial import Historial
from app.schemas.consumo import ConsumoRead, FacturaEtecsaRead, ImportacionResumen
from app.services.consumo import (
    FacturaDemasiadoGrandeError,
    FacturaMalFormadaError,
    TotalesIncoherentesError,
    importar_factura,
)

router = APIRouter(prefix="/consumo", tags=["consumo"])
facturas_router = APIRouter(prefix="/facturas-etecsa", tags=["facturas-etecsa"])

_TAMANO_MAXIMO_MB = 15
_NOMBRE_ARCHIVO_MAX = 255


@router.post(
    "/importar-pdf",
    response_model=ImportacionResumen,
    dependencies=[Depends(require_role("admin", "gestor"))],
)
def importar_pdf(
    archivo: UploadFile,
    request: Request,
    db: Session = Depends(get_db),
):
    if archivo.content_type != "application/pdf" and not archivo.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")

    limite_bytes = _TAMANO_MAXIMO_MB * 1024 * 1024
    contenido = archivo.file.read(limite_bytes + 1)
    if len(contenido) > limite_bytes:
        raise HTTPException(status_code=400, detail=f"El archivo supera el tamano maximo ({_TAMANO_MAXIMO_MB} MB)")

    if not contenido.startswith(b"%PDF-"):
        raise HTTPException(status_code=400, detail="El archivo no es un PDF valido")

    nombre = (archivo.filename or "factura.pdf")[:_NOMBRE_ARCHIVO_MAX]

    try:
        resumen = importar_factura(db, contenido, nombre)
    except FacturaMalFormadaError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except (FacturaDemasiadoGrandeError, TotalesIncoherentesError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    usuario = getattr(request.state, "user", None)
    db.add(
        Historial(
            entidad="facturas_etecsa",
            entidad_id=resumen["factura_id"],
            accion="importado",
            valor_nuevo=(
                f"factura={resumen['no_factura']} periodo={resumen['periodo']} "
                f"procesados={resumen['procesados']} asociados={resumen['asociados']} "
                f"sims_creadas={resumen['sims_creadas']} no_asociados={resumen['no_asociados']} "
                f"excesos={resumen['excesos']} alarmas={resumen['alarmas']}"
            ),
            usuario_id=usuario.id if usuario else None,
        )
    )
    db.commit()

    return resumen


@router.get("/", response_model=list[ConsumoRead])
def listar(
    sim_id: int | None = Query(None),
    periodo: str | None = Query(None, description="Formato: YYYY-MM"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    query = select(Consumo)
    if sim_id is not None:
        query = query.where(Consumo.sim_id == sim_id)
    if periodo is not None:
        query = query.join(FacturaEtecsa).where(FacturaEtecsa.periodo == periodo)
    return db.scalars(query.offset(skip).limit(limit)).all()


@router.get("/no-asociados", response_model=list[ConsumoRead])
def no_asociados(
    periodo: str | None = Query(None, description="Formato: YYYY-MM"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    query = select(Consumo).where(Consumo.sim_id.is_(None))
    if periodo is not None:
        query = query.join(FacturaEtecsa).where(FacturaEtecsa.periodo == periodo)
    return db.scalars(query.offset(skip).limit(limit)).all()


@router.get("/excesos", response_model=list[ConsumoRead])
def excesos(
    periodo: str | None = Query(None, description="Formato: YYYY-MM"),
    autorizado: bool | None = Query(None, description="Filtrar excesos cubiertos por autorizacion"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    query = select(Consumo).where(Consumo.en_exceso.is_(True))
    if periodo is not None:
        query = query.join(FacturaEtecsa).where(FacturaEtecsa.periodo == periodo)
    if autorizado is not None:
        query = query.where(Consumo.con_autorizacion.is_(autorizado))
    return db.scalars(query.offset(skip).limit(limit)).all()


@facturas_router.get("/", response_model=list[FacturaEtecsaRead])
def listar_facturas(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(FacturaEtecsa).order_by(FacturaEtecsa.periodo.desc()).offset(skip).limit(limit)
    ).all()


@facturas_router.get("/{factura_id}", response_model=FacturaEtecsaRead)
def obtener_factura(factura_id: int, db: Session = Depends(get_db)):
    factura = db.get(FacturaEtecsa, factura_id)
    if factura is None:
        raise HTTPException(status_code=404, detail="No existe la factura")
    return factura


@facturas_router.delete(
    "/{factura_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_role("admin"))],
)
def eliminar_factura(
    factura_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    """Permite reimportar una factura: borra la cabecera y sus consumos
    asociados (cascade) para poder volver a subir el PDF corregido."""
    factura = db.get(FacturaEtecsa, factura_id)
    if factura is None:
        raise HTTPException(status_code=404, detail="No existe la factura")
    n_consumos = db.scalar(
        select(func.count()).select_from(Consumo).where(Consumo.factura_id == factura_id)
    ) or 0
    usuario = getattr(request.state, "user", None)
    db.add(
        Historial(
            entidad="facturas_etecsa",
            entidad_id=factura_id,
            accion="eliminado",
            valor_nuevo=(
                f"no_factura={factura.no_factura} periodo={factura.periodo} "
                f"consumos={n_consumos}"
            ),
            usuario_id=usuario.id if usuario else None,
        )
    )
    db.delete(factura)
    db.commit()
