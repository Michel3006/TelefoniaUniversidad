from sqlalchemy import select
from app.core.security import hash_password
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
        if user is None:
            user = Usuario(
                username="admin",
                email="admin@telefonia.local",
                password_hash=hash_password("admin123"),
                rol_id=rol.id,
            )
            db.add(user)
            print("Usuario 'admin' creado.")
        else:
            print("Usuario 'admin' ya existe.")

        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    main()