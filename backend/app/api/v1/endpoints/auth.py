from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.login_limit import login_limiter
from app.core.security import (
    ROLES_SISTEMA,
    _dummy_hash,
    create_access_token,
    get_current_user,
    hash_password,
    require_role,
    security_logger,
    validar_politica_password,
    verify_password,
)
from app.db.session import get_db
from app.models.auth import Rol, Usuario
from app.models.historial import Historial
from app.schemas.auth import (
    CambiarPasswordRequest,
    RolCreate,
    RolRead,
    RolUpdate,
    Token,
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
)

auth_router = APIRouter(prefix="/auth", tags=["auth"])
usuarios_router = APIRouter(prefix="/usuarios", tags=["usuarios"])
roles_router = APIRouter(prefix="/roles", tags=["roles"])


def _usuario_id_from_request(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None


def _ip_from_request(request: Request) -> str:
    return request.client.host if request.client else "desconocida"


@auth_router.post("/login", response_model=Token)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    request: Request = None,
    db: Session = Depends(get_db),
):
    ip = _ip_from_request(request)
    login_limiter.verificar(ip, form.username)

    user = db.scalar(select(Usuario).where(Usuario.username == form.username))
    hash_a_verificar = user.password_hash if user is not None else _dummy_hash()
    password_ok = verify_password(form.password, hash_a_verificar)

    if user is None or not password_ok:
        login_limiter.registrar(ip, form.username, exitoso=False)
        user_label = user.username if user is not None else form.username
        security_logger.warning(
            "login_fallido usuario=%s ip=%s motivo=%s",
            user_label,
            ip,
            "inexistente" if user is None else "contrasena",
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contrasena incorrectos"
        )

    if not user.activo:
        security_logger.warning("login_bloqueado usuario=%s ip=%s motivo=inactivo", user.username, ip)
        login_limiter.registrar(ip, user.username, exitoso=False)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario inactivo")

    login_limiter.registrar(ip, user.username, exitoso=True)
    security_logger.info("login_exitoso usuario=%s ip=%s", user.username, ip)
    return Token(access_token=create_access_token(user.username))


@auth_router.get("/me", response_model=UsuarioRead)
def me(user: Usuario = Depends(get_current_user)):
    return user


@auth_router.post("/cambiar-password", status_code=status.HTTP_204_NO_CONTENT)
def cambiar_password(
    payload: CambiarPasswordRequest,
    request: Request,
    db: Session = Depends(get_db),
    user: Usuario = Depends(get_current_user),
):
    if not verify_password(payload.password_actual, user.password_hash):
        raise HTTPException(status_code=400, detail="La contrasena actual es incorrecta")
    validar_politica_password(payload.password_nueva)
    user.password_hash = hash_password(payload.password_nueva)
    user.debe_cambiar_password = False
    user.password_changed_at = datetime.now(timezone.utc)
    db.add(
        Historial(
            entidad="usuarios",
            entidad_id=user.id,
            accion="cambio_password",
            usuario_id=user.id,
        )
    )
    db.commit()
    security_logger.info("cambio_password usuario=%s ip=%s", user.username, _ip_from_request(request))


# ---------------------------------------------------------------------------
# Usuarios (solo admin)
# ---------------------------------------------------------------------------


@usuarios_router.get("/", response_model=list[UsuarioRead])
def list_usuarios(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    return db.scalars(select(Usuario).offset(skip).limit(limit)).all()


@usuarios_router.get("/{usuario_id}", response_model=UsuarioRead)
def get_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
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
        raise HTTPException(status_code=409, detail="Username o email ya existe")
    if db.get(Rol, payload.rol_id) is None:
        raise HTTPException(status_code=404, detail="No existe el rol indicado")
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
    security_logger.info("usuario_creado target=%s por=%s", user.username, _admin.username)
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

    nuevo_username = data.get("username")
    if nuevo_username and nuevo_username != user.username:
        otro = db.scalar(select(Usuario).where(Usuario.username == nuevo_username))
        if otro is not None and otro.id != user.id:
            raise HTTPException(status_code=409, detail="El username ya existe")

    nuevo_email = data.get("email")
    if nuevo_email and nuevo_email != user.email:
        otro = db.scalar(select(Usuario).where(Usuario.email == nuevo_email))
        if otro is not None and otro.id != user.id:
            raise HTTPException(status_code=409, detail="El email ya existe")

    nuevo_rol = data.get("rol_id")
    if nuevo_rol is not None and nuevo_rol != user.rol_id and db.get(Rol, nuevo_rol) is None:
        raise HTTPException(status_code=404, detail="No existe el rol indicado")

    if data.get("activo") is False and user.activo:
        if user.id == _admin.id:
            raise HTTPException(status_code=409, detail="No se puede desactivar la propia cuenta")
        _proteger_ultimo_admin(db, user)

    if "password" in data and data["password"]:
        user.password_hash = hash_password(data.pop("password"))
        user.password_changed_at = datetime.now(timezone.utc)
        db.add(Historial(
            entidad="usuarios",
            entidad_id=usuario_id,
            accion="actualizado",
            campo="password",
            usuario_id=_usuario_id_from_request(request),
        ))

    for campo, valor in data.items():
        anterior = getattr(user, campo)
        if anterior == valor:
            continue
        setattr(user, campo, valor)
        db.add(Historial(
            entidad="usuarios",
            entidad_id=usuario_id,
            accion="actualizado",
            campo=campo,
            valor_anterior=str(anterior) if anterior is not None else None,
            valor_nuevo=str(valor) if valor is not None else None,
            usuario_id=_usuario_id_from_request(request),
        ))

    if "rol_id" in data:
        nuevo_nombre = user.rol.nombre if user.rol else ""
        security_logger.info(
            "usuario_cambio_rol target=%s rol=%s por=%s",
            user.username,
            nuevo_nombre,
            _admin.username,
        )
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
    if user.id == _admin.id:
        raise HTTPException(status_code=409, detail="No se puede eliminar la propia cuenta")
    _proteger_ultimo_admin(db, user)

    con_historial = db.scalar(
        select(func.count()).select_from(Historial).where(Historial.usuario_id == usuario_id)
    )
    if con_historial:
        raise HTTPException(
            status_code=409,
            detail="El usuario tiene historial asociado: desactivalo en lugar de eliminarlo",
        )
    db.delete(user)
    db.add(Historial(
        entidad="usuarios",
        entidad_id=usuario_id,
        accion="eliminado",
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()
    security_logger.info("usuario_eliminado target=%s por=%s", user.username, _admin.username)


def _proteger_ultimo_admin(db: Session, user: Usuario) -> None:
    """Impide desactivar/eliminar al ultimo admin activo."""
    if user.rol.nombre != "admin" or not user.activo:
        return
    admins_activos = db.scalar(
        select(func.count())
        .select_from(Usuario)
        .join(Rol)
        .where(Rol.nombre == "admin", Usuario.activo.is_(True))
    )
    if admins_activos is not None and admins_activos <= 1:
        raise HTTPException(
            status_code=409,
            detail="No se puede realizar la operacion: quedaria el sistema sin administradores activos",
        )


# ---------------------------------------------------------------------------
# Roles (solo admin, con proteccion de roles de sistema)
# ---------------------------------------------------------------------------


@roles_router.get("/", response_model=list[RolRead])
def list_roles(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    return db.scalars(select(Rol).offset(skip).limit(limit)).all()


@roles_router.get("/{rol_id}", response_model=RolRead)
def get_rol(
    rol_id: int,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    rol = db.get(Rol, rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="No existe el rol")
    return rol


@roles_router.post("/", response_model=RolRead, status_code=status.HTTP_201_CREATED)
def create_rol(
    payload: RolCreate,
    request: Request,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    if payload.nombre in ROLES_SISTEMA:
        raise HTTPException(status_code=400, detail="No se puede crear un rol de sistema")
    existe = db.scalar(select(Rol).where(Rol.nombre == payload.nombre))
    if existe is not None:
        raise HTTPException(status_code=409, detail="Ya existe un rol con ese nombre")
    rol = Rol(nombre=payload.nombre, descripcion=payload.descripcion)
    db.add(rol)
    db.flush()
    db.add(Historial(
        entidad="roles",
        entidad_id=rol.id,
        accion="creado",
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()
    db.refresh(rol)
    return rol


@roles_router.put("/{rol_id}", response_model=RolRead)
def update_rol(
    rol_id: int,
    payload: RolUpdate,
    request: Request,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    rol = db.get(Rol, rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="No existe el rol")
    nuevo_nombre = payload.nombre
    if rol.nombre in ROLES_SISTEMA and nuevo_nombre != rol.nombre:
        raise HTTPException(status_code=400, detail="No se puede renombrar un rol de sistema")
    if nuevo_nombre in ROLES_SISTEMA and nuevo_nombre != rol.nombre:
        raise HTTPException(status_code=400, detail="No se puede usar un nombre de rol de sistema")
    if nuevo_nombre != rol.nombre:
        otro = db.scalar(select(Rol).where(Rol.nombre == nuevo_nombre))
        if otro is not None and otro.id != rol.id:
            raise HTTPException(status_code=409, detail="Ya existe un rol con ese nombre")
    anterior = rol.nombre
    rol.nombre = nuevo_nombre
    rol.descripcion = payload.descripcion
    db.add(Historial(
        entidad="roles",
        entidad_id=rol_id,
        accion="actualizado",
        campo="nombre",
        valor_anterior=anterior,
        valor_nuevo=nuevo_nombre,
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()
    db.refresh(rol)
    return rol


@roles_router.delete("/{rol_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rol(
    rol_id: int,
    request: Request,
    db: Session = Depends(get_db),
    _admin: Usuario = Depends(require_role("admin")),
):
    rol = db.get(Rol, rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="No existe el rol")
    if rol.nombre in ROLES_SISTEMA:
        raise HTTPException(status_code=400, detail="No se puede borrar un rol de sistema")
    con_usuarios = db.scalar(
        select(func.count()).select_from(Usuario).where(Usuario.rol_id == rol_id)
    )
    if con_usuarios:
        raise HTTPException(status_code=409, detail="No se puede borrar un rol que tiene usuarios")
    db.delete(rol)
    db.add(Historial(
        entidad="roles",
        entidad_id=rol_id,
        accion="eliminado",
        usuario_id=_usuario_id_from_request(request),
    ))
    db.commit()