from fastapi.testclient import TestClient


def test_auditoria_vacia(client: TestClient, auth_headers):
    response = client.get("/api/v1/auditoria/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_no_auth(client: TestClient):
    assert client.get("/api/v1/auditoria/").status_code == 401


def test_solo_admin_puede_ver(client: TestClient, gestor_headers, consulta_headers):
    assert client.get("/api/v1/auditoria/", headers=gestor_headers).status_code == 403
    assert client.get("/api/v1/auditoria/", headers=consulta_headers).status_code == 403


def test_audita_creacion_con_detalle(client: TestClient, auth_headers):
    telefono = client.post("/api/v1/telefonos/", headers=auth_headers, json={"numero": "6666666999"})
    assert telefono.status_code == 201

    data = client.get("/api/v1/auditoria/", headers=auth_headers).json()
    registros = [r for r in data if r["ruta"] == "/api/v1/telefonos/" and r["usuario_nombre"] == "admin"]
    assert registros, data
    registro = registros[0]
    assert registro["metodo"] == "POST"
    assert registro["cargo"] == "admin"
    assert registro["estatus"] == 201
    assert '"numero": "6666666999"' in (registro["detalle"] or "")


def test_audita_lectura(client: TestClient, auth_headers):
    client.get("/api/v1/personas/", headers=auth_headers)
    data = client.get("/api/v1/auditoria/", headers=auth_headers).json()
    get = [r for r in data if r["metodo"] == "GET" and "personas" in r["ruta"]]
    assert get
    assert get[0]["usuario_nombre"] == "admin"


def test_login_registrado_sin_password_plano(client: TestClient, admin_user, auth_headers):
    client.post("/api/v1/auth/login", data={"username": "admin", "password": "admin123"})
    data = client.get("/api/v1/auditoria/?metodo=POST", headers=auth_headers).json()
    registros = [r for r in data if "auth/login" in r["ruta"]]
    assert registros
    registro = registros[0]
    assert registro["metodo"] == "POST"
    assert registro["estatus"] == 200
    detalle = registro["detalle"] or ""
    assert "<<enmascarado>>" in detalle
    assert "admin123" not in detalle
    # el login aún no emite token, por eso queda como anónimo
    assert registro["usuario_nombre"] == "<<anonimo>>"


def test_filtro_por_metodo(client: TestClient, auth_headers):
    client.get("/api/v1/personas/", headers=auth_headers)
    solo_post = client.get("/api/v1/auditoria/?metodo=POST", headers=auth_headers).json()
    assert all(r["metodo"] == "POST" for r in solo_post)


def test_leer_panel_no_se_autoregistra(client: TestClient, auth_headers):
    """Leer el panel de auditoría no debe auto-registrarse (evita recursión)."""
    antes = len(client.get("/api/v1/auditoria/", headers=auth_headers).json())
    client.get("/api/v1/auditoria/", headers=auth_headers)
    despues = len(client.get("/api/v1/auditoria/", headers=auth_headers).json())
    assert antes == despues


def test_resumen(client: TestClient, auth_headers):
    client.get("/api/v1/personas/", headers=auth_headers)
    r = client.get("/api/v1/auditoria/resumen", headers=auth_headers)
    assert r.status_code == 200
    assert r.json()["total"] >= 1