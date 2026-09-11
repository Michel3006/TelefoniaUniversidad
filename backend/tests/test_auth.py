from fastapi.testclient import TestClient


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
            "password": "pass123",
            "rol_id": 1,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"


def test_create_usuario_duplicate(client: TestClient, auth_headers, admin_user):
    response = client.post(
        "/api/v1/usuarios/",
        headers=auth_headers,
        json={
            "username": "admin",
            "email": "other@test.com",
            "password": "pass123",
            "rol_id": 1,
        },
    )
    assert response.status_code == 400


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
            "password": "pass",
            "rol_id": 1,
        },
    )
    assert response.status_code == 403
