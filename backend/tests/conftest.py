import os
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

os.environ["DATABASE_URL"] = "sqlite://"
os.environ["LOGIN_RATE_LIMIT_HABILITADO"] = "false"

from app.core.security import create_access_token, hash_password
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.auth import Rol, Usuario

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db() -> Generator[Session, None, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_db():
    print(f"SETUP_DB: Creating tables, metadata tables: {list(Base.metadata.tables.keys())}")
    Base.metadata.create_all(bind=engine)
    print(f"SETUP_DB: Tables created")
    yield
    print(f"TEARDOWN_DB: Dropping tables")
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db() -> Generator[Session, None, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def crear_persona(db: Session):
    """Crea una persona directamente en la BD (el API de personas es solo lectura)."""
    from app.models.personas import Persona

    def _crear(nombre: str = "Juan", apellido: str = "Perez", **extra) -> int:
        persona = Persona(nombre=nombre, apellido=apellido, **extra)
        db.add(persona)
        db.commit()
        db.refresh(persona)
        return persona.id

    return _crear


@pytest.fixture()
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def admin_role(db: Session) -> Rol:
    role = db.query(Rol).filter(Rol.nombre == "admin").first()
    if role is None:
        role = Rol(nombre="admin", descripcion="Administrador")
        db.add(role)
        db.commit()
        db.refresh(role)
    return role


@pytest.fixture()
def gestor_role(db: Session) -> Rol:
    role = db.query(Rol).filter(Rol.nombre == "gestor").first()
    if role is None:
        role = Rol(nombre="gestor", descripcion="Gestor")
        db.add(role)
        db.commit()
        db.refresh(role)
    return role


@pytest.fixture()
def consulta_role(db: Session) -> Rol:
    role = db.query(Rol).filter(Rol.nombre == "consulta").first()
    if role is None:
        role = Rol(nombre="consulta", descripcion="Consulta")
        db.add(role)
        db.commit()
        db.refresh(role)
    return role


@pytest.fixture()
def admin_user(db: Session, admin_role: Rol) -> Usuario:
    user = db.query(Usuario).filter(Usuario.username == "admin").first()
    if user is None:
        user = Usuario(
            username="admin",
            email="admin@test.com",
            password_hash=hash_password("admin123"),
            rol_id=admin_role.id,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


@pytest.fixture()
def gestor_user(db: Session, gestor_role: Rol) -> Usuario:
    user = db.query(Usuario).filter(Usuario.username == "gestor").first()
    if user is None:
        user = Usuario(
            username="gestor",
            email="gestor@test.com",
            password_hash=hash_password("gestor123"),
            rol_id=gestor_role.id,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


@pytest.fixture()
def consulta_user(db: Session, consulta_role: Rol) -> Usuario:
    user = db.query(Usuario).filter(Usuario.username == "consulta").first()
    if user is None:
        user = Usuario(
            username="consulta",
            email="consulta@test.com",
            password_hash=hash_password("consulta123"),
            rol_id=consulta_role.id,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


@pytest.fixture()
def admin_token(admin_user: Usuario) -> str:
    return create_access_token(admin_user.username)


@pytest.fixture()
def gestor_token(gestor_user: Usuario) -> str:
    return create_access_token(gestor_user.username)


@pytest.fixture()
def consulta_token(consulta_user: Usuario) -> str:
    return create_access_token(consulta_user.username)


@pytest.fixture()
def auth_headers(admin_token: str) -> dict:
    return {"Authorization": f"Bearer {admin_token}"}


@pytest.fixture()
def gestor_headers(gestor_token: str) -> dict:
    return {"Authorization": f"Bearer {gestor_token}"}


@pytest.fixture()
def consulta_headers(consulta_token: str) -> dict:
    return {"Authorization": f"Bearer {consulta_token}"}
