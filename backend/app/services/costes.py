from decimal import Decimal

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.costes import Coste


def total_por_periodo(db: Session, periodo: str) -> Decimal | None:
    return db.scalar(
        select(func.sum(Coste.monto)).where(Coste.periodo == periodo)
    )


def total_por_departamento(db: Session, departamento_id: int) -> Decimal | None:
    return db.scalar(
        select(func.sum(Coste.monto)).where(Coste.departamento_id == departamento_id)
    )


def total_por_linea(db: Session, linea_id: int) -> Decimal | None:
    return db.scalar(
        select(func.sum(Coste.monto)).where(Coste.linea_id == linea_id)
    )


def total_por_contrato(db: Session, contrato_id: int) -> Decimal | None:
    return db.scalar(
        select(func.sum(Coste.monto)).where(Coste.contrato_id == contrato_id)
    )


def resumen_por_departamento(db: Session) -> list[dict]:
    results = db.execute(
        select(
            Coste.departamento_id,
            func.sum(Coste.monto).label("total"),
            func.count(Coste.id).label("cantidad"),
        )
        .group_by(Coste.departamento_id)
    ).all()
    return [
        {"departamento_id": r[0], "total": r[1], "cantidad": r[2]}
        for r in results
    ]


def resumen_por_periodo(db: Session) -> list[dict]:
    results = db.execute(
        select(
            Coste.periodo,
            func.sum(Coste.monto).label("total"),
            func.count(Coste.id).label("cantidad"),
        )
        .group_by(Coste.periodo)
        .order_by(Coste.periodo.desc())
    ).all()
    return [
        {"periodo": r[0], "total": r[1], "cantidad": r[2]}
        for r in results
    ]
