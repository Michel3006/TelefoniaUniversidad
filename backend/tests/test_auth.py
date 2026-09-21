from fastapi.testclient import TestClient

import pytest


def test_politica_password():
    """C2: minima 10 chars y al menos una letra y un digito."""
    from app.core.security import validar_politica_password

    valida = ["clave123456", "abcdefghij1", "1abcdefghij"]
    invalidas = ["pass123", "clave1234", "sololetras", "1234567890", ""]

    for pw in valida:
        validar_politica_password(pw)
    for pw in invalidas:
        with pytest.raises(ValueError):
            validar_politica_password(pw)


def test_login_success(client: TestClient, admin_user):
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "admin", "password": "admin123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client: TestClient, admin_user):
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "admin", "password": "wrong"},
    )
    assert response.status_code == 401


def test_login_nonexistent_user(client: TestClient):
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "nonexistent", "password": "pass"},
    )
    assert response.status_code == 401


def test_me(client: TestClient, auth_headers):
    response = client.get("/api/v1/auth/me", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"


def test_me_no_auth(client: TestClient):
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401


def test_create_usuario(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/usuarios/",
        headers=auth_headers,
        json={
            "username": "newuser",
            "email": "new@test.com",
            "password": "pass123456",
            "rol_id": 1,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"


def test_create_usuario_password_debil(client: TestClient, auth_headers):
    """C2: la politica de contrasenas se aplica al crear un usuario."""
    response = client.post(
        "/api/v1/usuarios/",
        headers=auth_headers,
        json={
            "username": "newuser2",
            "email": "new2@test.com",
            "password": "pass123",
            "rol_id": 1,
        },
    )
    assert response.status_code == 422


def test_create_usuario_password_sin_digito(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/usuarios/",
        headers=auth_headers,
        json={
            "username": "newuser3",
            "email": "new3@test.com",
            "password": "passwordabcabc",
            "rol_id": 1,
        },
    )
    assert response.status_code == 422


def test_create_usuario_duplicate(client: TestClient, auth_headers, admin_user):
    response = client.post(
        "/api/v1/usuarios/",
        headers=auth_headers,
        json={
            "username": "admin",
            "email": "other@test.com",
            "password": "pass123456",
            "rol_id": 1,
        },
    )
    assert response.status_code == 409


def test_list_usuarios(client: TestClient, auth_headers, admin_user):
    response = client.get("/api/v1/usuarios/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_get_usuario(client: TestClient, auth_headers, admin_user):
    response = client.get(f"/api/v1/usuarios/{admin_user.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"


def test_update_usuario(client: TestClient, auth_headers, admin_user):
    response = client.put(
        f"/api/v1/usuarios/{admin_user.id}",
        headers=auth_headers,
        json={"email": "updated@test.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "updated@test.com"


def test_delete_usuario(client: TestClient, auth_headers, gestor_user):
    response = client.delete(f"/api/v1/usuarios/{gestor_user.id}", headers=auth_headers)
    assert response.status_code == 204


def test_delete_ultimo_admin_rechazado(client: TestClient, auth_headers, admin_user):
    """No se puede eliminar al ultimo administrador activo."""
    response = client.delete(f"/api/v1/usuarios/{admin_user.id}", headers=auth_headers)
    assert response.status_code == 409


def test_update_usuario_no_permite_auto_desactivacion(
    client: TestClient, auth_headers, admin_user
):
    response = client.put(
        f"/api/v1/usuarios/{admin_user.id}",
        headers=auth_headers,
        json={"activo": False},
    )
    assert response.status_code == 409


def test_cambiar_password(client: TestClient, admin_user, auth_headers):
    wrong = client.post(
        "/api/v1/auth/cambiar-password",
        headers=auth_headers,
        json={"password_actual": "incorrecta", "password_nueva": "nueva123456"},
    )
    assert wrong.status_code == 400

    ok = client.post(
        "/api/v1/auth/cambiar-password",
        headers=auth_headers,
        json={"password_actual": "admin123", "password_nueva": "nueva123456"},
    )
    assert ok.status_code == 204

    # La password anterior deja de funcionar y la nueva entra
    assert (
        client.post(
            "/api/v1/auth/login",
            data={"username": "admin", "password": "admin123"},
        ).status_code
        == 401
    )
    login = client.post(
        "/api/v1/auth/login",
        data={"username": "admin", "password": "nueva123456"},
    )
    assert login.status_code == 200


def test_cambiar_password_politica(client: TestClient, admin_user, auth_headers):
    res = client.post(
        "/api/v1/auth/cambiar-password",
        headers=auth_headers,
        json={"password_actual": "admin123", "password_nueva": "short"},
    )
    assert res.status_code == 422


def test_login_rate_limit(client: TestClient, admin_user, monkeypatch):
    """A2: tras N intentos fallidos desde la misma IP se devuelve 429."""
    from app.core.config import settings
    from app.core.login_limit import login_limiter

    login_limiter.reset()
    original = settings.login_rate_limit_habilitado
    settings.login_rate_limit_habilitado = True
    try:
        for _ in range(settings.login_max_intentos):
            res = client.post(
                "/api/v1/auth/login",
                data={"username": "admin", "password": "incorrecta"},
            )
            assert res.status_code == 401
        bloqueado = client.post(
            "/api/v1/auth/login",
            data={"username": "admin", "password": "admin123"},
        )
        assert bloqueado.status_code == 429
    finally:
        settings.login_rate_limit_habilitado = original
        login_limiter.reset()


def test_create_rol(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/roles/",
        headers=auth_headers,
        json={"nombre": "test_role", "descripcion": "Test"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "test_role"


def test_list_roles(client: TestClient, auth_headers):
    response = client.get("/api/v1/roles/", headers=auth_headers)
    assert response.status_code == 200


def test_gestor_cannot_manage_usuarios(client: TestClient, gestor_headers):
    response = client.post(
        "/api/v1/usuarios/",
        headers=gestor_headers,
        json={
            "username": "test",
            "email": "test@test.com",
            "password": "pass123456",
            "rol_id": 1,
        },
    )
    assert response.status_code == 403
