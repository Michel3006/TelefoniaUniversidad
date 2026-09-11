from fastapi.testclient import TestClient


def test_inventario(client: TestClient, auth_headers):
    response = client.get("/api/v1/reportes/inventario", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "telefonos_fijos" in data
    assert "lineas_moviles" in data
    assert "dispositivos" in data
    assert "edificios" in data
    assert "locales" in data
    assert "personas" in data


def test_costes_totales(client: TestClient, auth_headers):
    response = client.get("/api/v1/reportes/costes-totales", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "monto_total" in data
    assert "periodos" in data


def test_costes_por_departamento(client: TestClient, auth_headers):
    response = client.get(
        "/api/v1/reportes/costes-por-departamento", headers=auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_costes_por_operador(client: TestClient, auth_headers):
    response = client.get(
        "/api/v1/reportes/costes-por-operador", headers=auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_costes_por_periodo(client: TestClient, auth_headers):
    response = client.get(
        "/api/v1/reportes/costes-por-periodo", headers=auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/reportes/inventario")
    assert response.status_code == 401
