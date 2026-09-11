from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import (
    create_access_token,
    get_current_user,
    hash_password,
    require_role,
    verify_password,
)
from app.db.session import get_db
from app.models.auth import Rol, Usuario
from app.models.historial import Historial
from app.schemas.auth import RolCreate, RolRead, RolUpdate, Token, UsuarioCreate, UsuarioRead, UsuarioUpdate

auth_router = APIRouter(prefix="/auth", tags=["auth"])
usuarios_router = APIRouter(prefix="/usuarios", tags=["usuarios"])
roles_router = APIRouter(prefix="/roles", tags=["roles"])

build_crud(roles_router, Rol, RolCreate, RolUpdate, RolRead, entidad="roles")


@auth_router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.scalar(select(Usuario).where(Usuario.username == form.username))
    if user is None or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contrasena incorrectos")
    if not user.activo:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario inactivo")
    return Token(access_token=create_access_token(user.username))


@auth_router.get("/me", response_model=UsuarioRead)
def me(user: Usuario = Depends(get_current_user)):
    return user


@usuarios_router.get("/", response_model=list[UsuarioRead])
def list_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return db.scalars(select(Usuario).offset(skip).limit(limit)).all()


@usuarios_router.get("/{usuario_id}", response_model=UsuarioRead)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    user = db.get(Usuario, usuario_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No existe el usuario")
    return user


@usuarios_router.post("/", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
def create_usuario(
    payload: UsuarioCreate,
    request: Request,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    exists = db.scalar(
        select(Usuario).where(or_(Usuario.username == payload.username, Usuario.email == payload.email))
    )
    if exists is not None:
        raise HTTPException(status_code=400, detail="Username o email ya existe")
    user = Usuario(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
        rol_id=payload.rol_id,
    )
    db.add(user)
    db.flush()
    db.add(Historial(
        entidad="usuarios",
        entidad_id=user.id,
        accion="creado",
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()
    db.refresh(user)
    return user


@usuarios_router.put("/{usuario_id}", response_model=UsuarioRead)
def update_usuario(
    usuario_id: int,
    payload: UsuarioUpdate,
    request: Request,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    user = db.get(Usuario, usuario_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No existe el usuario")
    data = payload.model_dump(exclude_unset=True)
    if "password" in data and data["password"]:
        user.password_hash = hash_password(data.pop("password"))
    for campo, valor in data.items():
        setattr(user, campo, valor)
    db.add(Historial(
        entidad="usuarios",
        entidad_id=usuario_id,
        accion="actualizado",
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()
    db.refresh(user)
    return user


@usuarios_router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usuario(
    usuario_id: int,
    request: Request,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    user = db.get(Usuario, usuario_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No existe el usuario")
    db.delete(user)
    db.add(Historial(
        entidad="usuarios",
        entidad_id=usuario_id,
        accion="eliminado",
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()


def _usuario_id_from_request(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None