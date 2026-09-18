from fastapi.testclient import TestClient


def test_listar_cargos(client: TestClient, auth_headers, db):
    from app.models.institucional import Cargo

    db.add(Cargo(codigo="02", nombre="Analista"))
    db.commit()

    response = client.get("/api/v1/cargos/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_cargo(client: TestClient, auth_headers, db):
    from app.models.institucional import Cargo

    cargo = Cargo(codigo="03", nombre="Tecnico")
    db.add(cargo)
    db.commit()
    db.refresh(cargo)

    response = client.get(f"/api/v1/cargos/{cargo.id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Tecnico"


def test_get_cargo_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/cargos/99999", headers=auth_headers)
    assert response.status_code == 404


def test_listar_areas(client: TestClient, auth_headers, db):
    from app.models.institucional import Area

    db.add(Area(codigo="002", nombre="Recursos Humanos"))
    db.commit()

    response = client.get("/api/v1/areas/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_area(client: TestClient, auth_headers, db):
    from app.models.institucional import Area

    area = Area(codigo="003", nombre="Finanzas")
    db.add(area)
    db.commit()
    db.refresh(area)

    response = client.get(f"/api/v1/areas/{area.id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["codigo"] == "003"


def test_get_area_not_found(client: TestClient, auth_headers):
    response = client.get("/api/v1/areas/99999", headers=auth_headers)
    assert response.status_code == 404


def test_no_auth(client: TestClient):
    response = client.get("/api/v1/cargos/")
    assert response.status_code == 401