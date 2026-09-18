"""Sincronizacion de RRHH desde ASSETS_RH hacia el sistema de telefonia.

Uso (desde la carpeta backend):
    python -m scripts.sincronizar_rrhh
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.db.session import SessionLocal
from app.services import institucional


def main() -> None:
    with SessionLocal() as db:
        resumen = institucional.sincronizar_desde_rrhh(db)
    for clave, valor in resumen.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()