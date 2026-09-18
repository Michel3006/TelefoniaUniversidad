from fastapi.testclient import TestClient


def _create_edificio(client: TestClient, auth_headers) -> int:
    response = client.post(
        "/api/v1/edificios/",
        headers=auth_headers,
        json={"nombre": "Sede Central", "direccion": "Calle 1"},
    )
    return response.json()["id"]


def test_create_edificio(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/edificios/",
        headers=auth_headers,
        json={"nombre": "Edificio A"},
    )
    assert response.status_code == 201
    assert response.json()["nombre"] == "Edificio A"


def test_list_edificios(client: TestClient, auth_headers):
    _create_edificio(client, auth_headers)
    response = client.get("/api/v1/edificios/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_edificio(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    response = client.get(f"/api/v1/edificios/{edificio_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == edificio_id


def test_update_edificio(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    response = client.put(
        f"/api/v1/edificios/{edificio_id}",
        headers=auth_headers,
        json={"nombre": "Sede Renovada"},
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Sede Renovada"


def test_delete_edificio(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    response = client.delete(f"/api/v1/edificios/{edificio_id}", headers=auth_headers)
    assert response.status_code == 204


def test_create_local(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    response = client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "3", "oficina": "301"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["edificio_id"] == edificio_id


def test_list_locales(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "2", "oficina": "201"},
    )
    response = client.get("/api/v1/locales/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_local(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    create = client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "1", "oficina": "101"},
    )
    local_id = create.json()["id"]
    response = client.get(f"/api/v1/locales/{local_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == local_id


def test_update_local(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    create = client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "1", "oficina": "102"},
    )
    local_id = create.json()["id"]
    response = client.put(
        f"/api/v1/locales/{local_id}",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "5", "oficina": "501", "descripcion": "Salon"},
    )
    assert response.status_code == 200
    assert response.json()["oficina"] == "501"


def test_delete_local(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    create = client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "4", "oficina": "401"},
    )
    local_id = create.json()["id"]
    response = client.delete(f"/api/v1/locales/{local_id}", headers=auth_headers)
    assert response.status_code == 204


def test_locales_por_edificio(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "2", "oficina": "202"},
    )
    response = client.get(f"/api/v1/locales/por-edificio/{edificio_id}", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_estado(client: TestClient, auth_headers):
    response = client.post(
        "/api/v1/estados/",
        headers=auth_headers,
        json={"nombre": "En uso", "descripcion": "Activo"},
    )
    assert response.status_code == 201
    assert response.json()["nombre"] == "En uso"


def test_list_estados(client: TestClient, auth_headers):
    client.post("/api/v1/estados/", headers=auth_headers, json={"nombre": "Disponible"})
    response = client.get("/api/v1/estados/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_estado(client: TestClient, auth_headers):
    create = client.post("/api/v1/estados/", headers=auth_headers, json={"nombre": "Reparacion"})
    estado_id = create.json()["id"]
    response = client.get(f"/api/v1/estados/{estado_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Reparacion"


def test_update_estado(client: TestClient, auth_headers):
    create = client.post("/api/v1/estados/", headers=auth_headers, json={"nombre": "Baja"})
    estado_id = create.json()["id"]
    response = client.put(
        f"/api/v1/estados/{estado_id}",
        headers=auth_headers,
        json={"nombre": "Baja", "descripcion": "Retirado"},
    )
    assert response.status_code == 200
    assert response.json()["descripcion"] == "Retirado"


def test_delete_estado(client: TestClient, auth_headers):
    create = client.post("/api/v1/estados/", headers=auth_headers, json={"nombre": "Vendido"})
    estado_id = create.json()["id"]
    response = client.delete(f"/api/v1/estados/{estado_id}", headers=auth_headers)
    assert response.status_code == 204


def test_gestor_no_puede_crear_estado(client: TestClient, gestor_headers):
    response = client.post(
        "/api/v1/estados/",
        headers=gestor_headers,
        json={"nombre": "Restringido"},
    )
    assert response.status_code == 403


def test_departamentos_raices(client: TestClient, auth_headers, db):
    from app.models.organizacion import Departamento

    depto = Departamento(nombre="Organo Superior")
    db.add(depto)
    db.commit()

    response = client.get("/api/v1/departamentos/raices", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_departamentos_listar_y_get(client: TestClient, auth_headers, db):
    from app.models.organizacion import Departamento

    depto = Departamento(nombre="Direccion")
    db.add(depto)
    db.commit()
    db.refresh(depto)

    listado = client.get("/api/v1/departamentos/", headers=auth_headers)
    assert listado.status_code == 200
    assert len(listado.json()) >= 1

    response = client.get(f"/api/v1/departamentos/{depto.id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Direccion"


def test_departamentos_subordinados(client: TestClient, auth_headers, db):
    from app.models.organizacion import Departamento

    padre = Departamento(nombre="Padre", id_direccion="P1")
    hijo = Departamento(nombre="Hijo", id_direccion="H1", departamento_padre_id=None)
    db.add_all([padre, hijo])
    db.flush()
    hijo.departamento_padre_id = padre.id
    db.commit()

    response = client.get(f"/api/v1/departamentos/{padre.id}/subordinados", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["nombre"] == "Hijo"


def test_telefono_puede_referenciar_local_estado(client: TestClient, auth_headers):
    edificio_id = _create_edificio(client, auth_headers)
    local = client.post(
        "/api/v1/locales/",
        headers=auth_headers,
        json={"edificio_id": edificio_id, "piso": "1", "oficina": "001"},
    )
    local_id = local.json()["id"]
    estado = client.post("/api/v1/estados/", headers=auth_headers, json={"nombre": "Operativo"})
    estado_id = estado.json()["id"]
    response = client.post(
        "/api/v1/telefonos/",
        headers=auth_headers,
        json={"numero": "9999999990", "local_id": local_id, "estado_id": estado_id},
    )
    assert response.status_code == 201

    detalle = client.get(f"/api/v1/telefonos/{response.json()['id']}/detalle", headers=auth_headers)
    assert detalle.status_code == 200
    assert detalle.json()["edificio"] == "Sede Central"
    assert detalle.json()["estado"] == "Operativo"


def test_no_auth_edificios(client: TestClient):
    response = client.get("/api/v1/edificios/")
    assert response.status_code == 401


def test_no_auth_estados(client: TestClient):
    response = client.get("/api/v1/estados/")
    assert response.status_code == 401