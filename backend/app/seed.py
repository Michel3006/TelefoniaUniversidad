import sys

from sqlalchemy import select

from app.core.config import settings
from app.core.security import hash_password, validar_politica_password
from app.db.session import SessionLocal
from app.models.auth import Rol, Usuario


def main():
    db = SessionLocal()
    try:
        rol = db.scalar(select(Rol).where(Rol.nombre == "admin"))
        if rol is None:
            rol = Rol(nombre="admin", descripcion="Administrador del sistema")
            db.add(rol)
            db.flush()
            print("Rol 'admin' creado.")
        else:
            print("Rol 'admin' ya existe.")

        user = db.scalar(select(Usuario).where(Usuario.username == "admin"))
        if user is not None:
            print("Usuario 'admin' ya existe.")
            db.commit()
            return

        password = settings.admin_initial_password
        if not password:
            print("ADMIN_INITIAL_PASSWORD no definido: no se crea el usuario 'admin'.", file=sys.stderr)
            print("Defina ADMIN_INITIAL_PASSWORD en las variables de entorno o en .env", file=sys.stderr)
            db.commit()
            return

        try:
            validar_politica_password(password)
        except ValueError as exc:
            print(
                f"ADMIN_INITIAL_PASSWORD no cumple la politica de seguridad: {exc}",
                file=sys.stderr,
            )
            print("El usuario 'admin' NO se creo. Corrija la password antes de ejecutar el seed.", file=sys.stderr)
            db.commit()
            return

        user = Usuario(
            username="admin",
            email="admin@telefonia.local",
            password_hash=hash_password(password),
            rol_id=rol.id,
            debe_cambiar_password=True,
        )
        db.add(user)
        db.commit()
        print(
            "Usuario 'admin' creado con ADMIN_INITIAL_PASSWORD. "
            "Debera cambiar la contrasena en el primer ingreso."
        )
    finally:
        db.close()


if __name__ == "__main__":
    main()