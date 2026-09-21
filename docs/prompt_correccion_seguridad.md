# PROMPT: Corrección de seguridad del Sistema de Gestión de Telefonía

## 1. Rol y contexto

Eres un ingeniero de seguridad y backend senior. Vas a corregir problemas de seguridad detectados en una auditoría estática de este repositorio (backend FastAPI + SQLAlchemy 2 + Alembic, frontend React + TypeScript + Vite + Tailwind, despliegue en Render). Es una aplicación para una universidad cubana: gestiona teléfonos, SIM, dispositivos, asignaciones a personas y consumo mensual importado desde PDF de ETECSA. El directorio de personas se sincroniza desde una base institucional de RRHH (ASSETS_RH, SQL Server).

Todavía **no hay datos reales** en el sistema, así que puedes crear migraciones sin preocuparte por transformar datos existentes.

## 2. Reglas de trabajo (obligatorias)

1. **El código es la única fuente de verdad.** La carpeta `docs/` y partes del README están desactualizadas o mal. No te guíes por ellas. No las actualices; solo elimina credenciales literales (ver C1).
2. Antes de tocar nada, ejecuta la suite actual (`cd backend && pytest`) y anota el resultado base. Al terminar, todo lo que pasaba debe seguir pasando. Si un test existente choca con una corrección porque usa datos inválidos (por ejemplo un IMEI de 14 dígitos), ajusta el test y explícalo en el informe. Nunca debilites un test para que pase.
3. Cada corrección lleva sus tests, incluyendo **tests negativos** (el caso de ataque debe fallar).
4. Todo cambio de esquema va en una migración Alembic nueva (`007_seguridad.py`, `down_revision = "006_mejoras_consumo_observaciones"`). Usa `op.batch_alter_table` para que funcione en SQLite y PostgreSQL. Incluye `downgrade()`.
5. Sin refactors ajenos a seguridad. No cambies el diseño visual del frontend. Mantén el estilo del código existente (español, `build_crud`, servicios en `app/services/`).
6. Los errores hacia el cliente no deben contener trazas, SQL ni detalles internos. Los detalles van a logs.
7. Si una decisión de la sección 6 requiere confirmación del usuario y puedes preguntar, pregunta. Si no puedes, implementa el **valor por defecto indicado** y márcalo en el informe final.
8. No borres archivos de `docs/` ni reescribas el historial de git. Solo repórtalo.
9. Cuando un hallazgo dice **"verificar primero"**, escribe un test que reproduzca el problema antes de arreglarlo. Si no se reproduce, documenta que era un falso positivo y no lo "arregles".

## 3. Orden de trabajo

1. Críticos: C1, C2.
2. Sesión y autenticación: A2.
3. Higiene del repositorio: A3 (antes de cualquier push a GitHub).
4. Importación de PDF y sincronización RRHH: A5, A4.
5. Datos personales: A1.
6. Auditoría y lógica de negocio: M1, M2.
7. Validación y errores: M3.
8. Configuración, despliegue y dependencias: M4, M5.

Haz commits separados por hallazgo (`security(C2): ...`).

---

## 4. Hallazgos a corregir

### C1 (CRÍTICO): Credenciales `admin` / `admin123` sembradas en cada despliegue

**Archivos:** `backend/app/seed.py`, `render.yaml` (`startCommand`), `backend/app/core/config.py`, README y documentos con la contraseña escrita.

**Problema:** `render.yaml` ejecuta `python -m app.seed` en cada arranque, y el seed crea `admin/admin123` si no existe. Es una cuenta administradora pública en producción.

**Cambios:**
- `seed.py` debe leer la contraseña inicial de una variable de entorno nueva `ADMIN_INITIAL_PASSWORD` (añádela a `Settings`). Si no hay ningún usuario admin y la variable falta o no cumple la política de contraseña (ver A2), el seed **aborta con error claro y código de salida distinto de cero**. Nunca crea credenciales por defecto ni imprime la contraseña.
- Si ya existe un admin, el seed no hace nada.
- `render.yaml`: declara `ADMIN_INITIAL_PASSWORD` con `sync: false` (el usuario la introduce en el panel de Render). Mantén el seed en el arranque, ahora seguro e idempotente.
- Añade la columna `usuarios.debe_cambiar_password` (Boolean, `server_default false`). El admin creado por seed nace con `true`. Exponla en `UsuarioRead` y en `frontend/src/lib/types.ts`.
- Añade `POST /auth/cambiar-password` (autenticado). Recibe `password_actual` y `password_nueva`, verifica la actual, aplica la política de A2 y pone `debe_cambiar_password=false`. Registra en `Historial` (sin valores de contraseña).
- Frontend (mínimo): si `user.debe_cambiar_password`, redirige a una pantalla `/cuenta` con el formulario de cambio de contraseña y no permite navegar hasta completarlo.
- Elimina el texto literal `admin123` y las instrucciones de credenciales por defecto de README y de cualquier `.md`. Sustitúyelo por "usa la contraseña definida en `ADMIN_INITIAL_PASSWORD`". No toques nada más de `docs/`.

**Tests:** el seed sin variable no crea usuario y falla; con variable válida crea un admin con `debe_cambiar_password=True`; `cambiar-password` rechaza una actual incorrecta y una nueva débil.

### C2 (CRÍTICO): Escalada de privilegios mediante `/roles/`

**Archivos:** `backend/app/api/v1/endpoints/auth.py`, `backend/app/api/v1/router.py`, `backend/app/core/security.py`.

**Problema:** `build_crud(roles_router, Rol, ...)` no lleva `write_dependency`, así que cualquier usuario autenticado puede crear, renombrar y borrar roles. `require_role` compara el **nombre** del rol. Cadena de ataque: un usuario `consulta` renombra el rol `admin` a `x` y luego su propio rol a `admin`, y queda como administrador (los admins reales pierden acceso).

**Cambios:**
- Todos los endpoints de `/roles/` (lectura incluida) exigen `require_role("admin")`.
- Sustituye el `build_crud` de roles por endpoints propios con estas reglas: los roles de sistema (`admin`, `gestor`, `consulta`) **no se pueden renombrar ni borrar**; ningún rol puede renombrarse a un nombre de sistema; no se puede borrar un rol que tenga usuarios (409). Define la constante `ROLES_SISTEMA` en un único lugar.
- `GET /usuarios/` y `GET /usuarios/{id}` pasan a exigir `require_role("admin")`. `/auth/me` sigue abierto a cualquier autenticado.
- Revisa el frontend: `/roles/` solo se usa en `UsuariosPage` (solo admin), no debe romperse.

**Tests (negativos):** con tokens `gestor` y `consulta`, los `GET/POST/PUT/DELETE` de `/roles/` devuelven 403 y `GET /usuarios/` devuelve 403; el admin no puede renombrar ni borrar `admin`, ni renombrar otro rol a `admin`; no puede borrar un rol con usuarios.

### A2 (ALTO): Sesión, contraseñas y protección del login

**Archivos:** `backend/app/core/security.py`, `backend/app/core/config.py`, `backend/app/schemas/auth.py`, `backend/app/api/v1/endpoints/auth.py`, `frontend/src/lib/validation.ts`.

**Cambios:**
1. `get_current_user` debe rechazar usuarios con `activo == False` (401). Hoy un usuario desactivado conserva acceso hasta que expira el token.
2. **Política de contraseña en el backend** (`UsuarioCreate`, `UsuarioUpdate`, cambio de contraseña, seed): mínimo 10 caracteres, al menos una letra y un dígito, máximo 72 **bytes** (bcrypt trunca silenciosamente). Centraliza el validador en un solo sitio. Alinea el frontend (`validation.ts`, tipo `password` → mínimo 10).
3. `email` como `EmailStr` (añade `email-validator` a `requirements.txt`).
4. **Rate limiting del login:** máximo 5 intentos por minuto por IP en `POST /auth/login` (por ejemplo con `slowapi`), y además un bloqueo temporal por usuario tras 5 fallos consecutivos (15 min). Hazlo configurable en `Settings` y desactivable en tests. Para que la IP real llegue tras el proxy de Render, arranca uvicorn con `--proxy-headers`.
5. **Timing:** si el usuario no existe, ejecuta igualmente un `verify_password` contra un hash ficticio para igualar tiempos.
6. **Logging de seguridad:** logger `security` con login correcto/fallido (usuario e IP, **nunca** contraseñas ni tokens), bloqueos, cambios de contraseña y de rol.
7. **Fail-closed de `SECRET_KEY`:** añade `environment: str = "development"` a `Settings`. Si `environment == "production"` y `secret_key` es el valor por defecto, el placeholder de `.env.example` o tiene menos de 32 caracteres, la app **no arranca**. En `render.yaml` define `ENVIRONMENT=production`.
8. (Recomendado) Invalida tokens al cambiar contraseña o rol: añade `password_changed_at` al usuario e `iat` al JWT, y rechaza tokens emitidos antes.
9. El token sigue en `localStorage` (decisión aceptada), pero por eso son obligatorios la CSP de M4 y no introducir `dangerouslySetInnerHTML`. Deja un comentario en `api.ts` que lo explique.

**Tests:** usuario desactivado con token válido → 401; contraseña corta o sin dígito → 422 en la API; el 6.º login fallido seguido → 429 o bloqueo; arranque con `ENVIRONMENT=production` y clave por defecto → error.

### A3 (ALTO): Secretos e infraestructura en el repositorio

**Archivos:** `.gitignore`, `backend/tests/test_consumo_pdf_real.py`, `backend/app/core/config.py`, `backend/.env.example`, `backend/alembic.ini`, README.

**Cambios:**
- El test espera `202607_73212_41012682713947.pdf` en la raíz del repo (factura real de ETECSA con número de cliente y 207 servicios). Cambia el test para localizarlo con la variable `ETECSA_PDF_PATH` o en `backend/tests/private/` y **si no existe, `skip`**. Añade a `.gitignore`: `/*.pdf` y `backend/tests/private/`. (No uses un `*.pdf` global: `docs/` contiene PDFs generados.) Si el PDF ya está en el árbol de trabajo, sácalo con `git rm --cached` y avisa al usuario.
- Quita las IPs internas. En `config.py`, `assets_rrhh_server` por defecto `""`; en `.env.example` y README usa un marcador (`servidor-rrhh.ejemplo.local`).
- Quita credenciales por defecto: `config.py` (`postgres:postgres`) y `alembic.ini` (`sqlalchemy.url`; `env.py` ya la sobrescribe desde `settings`, déjala con un marcador sin credenciales). El default de `database_url` en desarrollo será `sqlite:///./dev.db`. Si `environment == "production"`, `DATABASE_URL` es obligatoria.
- Escanea el repo con `gitleaks` o un `grep` de patrones (contraseñas, claves, IPs 10.x/172.x) y lista lo encontrado en el informe. **Informa** al usuario de que, si ya hubo un push, hay que limpiar el historial (no lo hagas tú) y de que `docs/DOCUMENTACION_BD.md` describe servidores y esquemas internos (Sigenu/ASSETS_RH): que decida si se publica o se elimina.

**Test:** el test de PDF real hace `skip` limpio sin el archivo.

### A4 (ALTO): Integración con ASSETS_RH (`backend/app/services/institucional.py`)

**Cambios:**
- La cadena ODBC debe usar `Encrypt=yes` y `TrustServerCertificate=no` **por defecto**. Añade a `Settings` `assets_rrhh_encrypt: bool = True` y `assets_rrhh_trust_server_certificate: bool = False`; documenta en `.env.example` que un servidor con certificado autofirmado exige activar lo segundo conscientemente.
- Escapa los valores de la cadena de conexión. Envuelve `UID` y `PWD` en llaves duplicando `}` internos, y rechaza `SERVER`/`DATABASE` que contengan `;`, `{` o `}`:

```python
def _odbc_val(v: str) -> str:
    return "{" + v.replace("}", "}}") + "}"
```

- `pyodbc.connect(cadena, timeout=15)` y cierra la conexión con `contextlib.closing` (el `with` de pyodbc no la cierra).
- **No devuelvas `str(exc)` de pyodbc al cliente.** `conectar_rrhh` registra el detalle en el logger y lanza `RuntimeError("No se pudo conectar a ASSETS_RH")`; el endpoint devuelve 503 genérico.
- `SincronizacionRrhh`: limita el tamaño de cada lista (por ejemplo `Field(max_length=50_000)`) y añade un tope de tamaño de cuerpo para `/sincronizacion/rh-json`.
- Entrega `backend/scripts/sql/assets_rh_readonly.sql`: un login/usuario **solo lectura** con `GRANT SELECT` limitado a las 4 tablas usadas (`RH_Cargos`, `RH_Area_Trabajo_Actual`, `RH_Unidades_Organizativas`, `Empleados_Gral`). En `Empleados_Gral`, hazlo por columnas: solo las del `SELECT` de `_SQL` (`Id_Empleado, Id_Expediente, No_CI, Nombre, Apellido_1, Apellido_2, Exttelef, Telefono_Particular, Id_CCosto, Id_Cargo, Id_Direccion, Baja`). Usa marcadores para nombre y contraseña. La base contiene nómina completa; el principio es mínimo privilegio.

**Tests:** prueba unitaria de la construcción de la cadena (escape de `}` y `;`, `Encrypt=yes` por defecto) sin conectar; el error de conexión no filtra el mensaje original.

### A5 (ALTO): Importación de PDF

**Archivos:** `backend/app/api/v1/endpoints/consumo.py`, `backend/app/services/consumo.py`, `backend/requirements.txt`.

**Cambios:**
1. El endpoint `importar_pdf` es `async def` pero llama a código bloqueante (pdfplumber + BD), y congela todo el servidor mientras procesa. Conviértelo a `def` normal (FastAPI lo ejecuta en threadpool).
2. Lee con tope: `contenido = archivo.file.read(MAX + 1)`. Si supera 15 MB → 413. Hoy se lee **todo** en memoria antes de comprobar el tamaño.
3. Valida por contenido, no por cabecera: los primeros bytes deben ser `%PDF-`. Maneja `archivo.filename is None`. Trunca el nombre guardado en `archivo_origen` a 255. El nombre nunca se usa como ruta de disco (mantenlo así).
4. Límites al parseo: máximo de páginas (por ejemplo 100) y de longitud del texto extraído (por ejemplo 5 MB) antes de aplicar regex; excedidos → 422.
5. **Regex (verificar primero):** `_FILA_RE` y las regex de `totales_match` y `cabecera_match` usan `[\d,]+` sin cota y `\s*` entre grupos numéricos, y son probablemente cuadráticas con largas secuencias de dígitos. Escribe un test con ~50.000 dígitos seguidos y exige que `parsear_factura` termine en menos de 1 s. Si falla, acota los cuantificadores (por ejemplo `[\d,]{1,12}\.\d{2}`). **No añadas `(?<!\d)` antes del número de servicio:** filas consecutivas llegan pegadas (`560.0059921170`) y `test_parsea_filas_pegadas_sin_espacio` debe seguir pasando.
6. **Coherencia de totales:** tras el parseo, la suma de `cuota`, `consumo`, `comision`, `impuesto` e `importe` de las filas debe coincidir con la fila `Total` (tolerancia 0,01). Si la fila `Total` existe y no coincide → 422 con mensaje claro y sin guardar nada. Si el PDF real (cuando esté disponible) no cumple la comprobación de forma legítima, **no la relajes a ciegas**: repórtalo.
7. Fija la versión de `pdfplumber` (y, si es posible, `pdfminer.six`) en `requirements.txt`.

**Tests:** archivo > límite → 413; contenido no PDF con `content_type` PDF → 400; regex rápida con entrada patológica; totales incoherentes → 422 y nada persistido; los tests existentes de consumo siguen verdes.

### A1 (ALTO): Datos personales visibles para cualquier usuario autenticado

**Archivos:** `backend/app/api/v1/endpoints/personas.py`, `backend/app/schemas/personas.py`, `backend/app/api/v1/endpoints/historial.py`, frontend (`PersonasPage.tsx`, `types.ts`, `nav.ts`, `router.tsx`).

**Cambios:**
- El rol `consulta` **no** recibe `documento` (CI), `email`, `telefono` ni `exttelef` de personas. Crea `PersonaReadBasico` (sin esos campos) y devuelve el schema según el rol del usuario (dependencia que resuelva el rol). `admin` y `gestor` reciben el completo. La búsqueda `/personas/buscar` no debe buscar por `documento` ni `email` para `consulta`.
- `GET /historial/` pasa a `require_role("admin")`; en el frontend marca `Historial` como `soloAdmin` en `nav.ts` y con `AdminRoute` en `router.tsx`.
- Todos los `/buscar` (personas, sims, telefonos, extensiones, dispositivos) reciben `limit` (por defecto 20, máximo 50) y `skip` (>= 0).
- **Escapa los comodines LIKE** (`%`, `_`, `\`). Crea el helper en `app/api/v1/utils.py` y úsalo en todos los `ilike`:

```python
def like_seguro(q: str) -> str:
    q = q.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    return f"%{q}%"
# .ilike(like_seguro(q), escape="\\")
```

- El frontend debe tolerar campos ausentes (`documento?: string | null`, etc.).

**Tests:** `consulta` no ve los campos sensibles y `gestor` sí; `q="%"` no devuelve toda la tabla; `historial` da 403 a no admin.

### M1 (MEDIO): Auditoría incompleta y trazabilidad reescribible

**Archivos:** `backend/app/api/v1/endpoints/asignaciones.py`, `backend/app/api/v1/crud.py`, `backend/app/api/v1/endpoints/consumo.py`, `backend/app/api/v1/endpoints/auth.py`, `backend/app/models/asignaciones.py`.

**Cambios:**
- **Asignaciones:** `create_item`, `update_item` y `delete_item` registran `usuario_id` (inyecta `Request` como ya hace `finalizar`). `update_item` solo puede modificar `observaciones`; cualquier intento de cambiar `persona_id`, `tipo_recurso`, `recurso_id` o `fecha_inicio` → 400 (el historial no se reescribe; se finaliza y se crea una nueva). Registra cada campo cambiado con valor anterior y nuevo. Valida que la persona exista (404) y que `fecha_fin >= fecha_inicio` cuando venga informada. `delete_item` solo para `admin`.
- **Carrera de doble asignación:** índice único parcial en la migración y en el modelo, y captura el `IntegrityError` → 409:

```python
sa.Index("uq_asignacion_activa", "tipo_recurso", "recurso_id", unique=True,
         postgresql_where=sa.text("fecha_fin IS NULL"),
         sqlite_where=sa.text("fecha_fin IS NULL"))
```

- **Borrados con evidencia:** en `build_crud.delete_item` y `asignaciones.delete_item`, guarda en `Historial.valor_anterior` una copia JSON del registro borrado. Opcional: hazlo también en la creación (`valor_nuevo`).
- `eliminar_factura` escribe `Historial` (`accion="eliminado"`, entidad `facturas_etecsa`, número de factura, período, nº de consumos y usuario).
- Usuarios: `update_usuario` registra campos cambiados (`rol_id`, `activo`, `username`, `email`) con anterior y nuevo, y para la contraseña solo `campo="password"` sin valores.
- (Recomendado) Migración solo PostgreSQL con trigger que impida `UPDATE` y `DELETE` sobre `historial`; se omite en SQLite.

**Tests:** el `PUT` de asignación con `persona_id` distinto → 400; las tres operaciones dejan `usuario_id`; dos asignaciones activas simultáneas → 409 incluso vía inserción directa; el borrado deja copia; eliminar factura genera historial.

### M2 (MEDIO): Lógica de límites y autorizaciones (`evaluacion_limite`)

**Archivos:** `backend/app/services/consumo.py`, `backend/app/api/v1/endpoints/limites.py`, `backend/app/api/v1/endpoints/autorizaciones.py`, `backend/app/schemas/consumo.py`.

**Problemas:** se evalúa contra el **día 1** del período (una autorización o límite que empieza el día 15 no se aplica en ese mes, y una que termina el día 20 cubre el mes entero); `db.scalar(select(...))` sin orden elige un registro arbitrario si hay varios vigentes; una autorización con importe menor que el límite normal **reduce** el límite.

**Cambios (semántica por defecto, ver sección 6):**
- Un límite o autorización aplica al período si su rango **se solapa** con él: `vigente_desde <= último_día_del_mes` y (`vigente_hasta IS NULL` o `vigente_hasta >= primer_día_del_mes`). La factura es mensual y no se puede partir.
- Selección determinista: límite normal = el de mayor `vigente_desde`; autorización = la de mayor `limite_autorizado`.
- `limite_efectivo = max(limite_normal, limite_autorizado)` cuando hay autorización. Si no hay límite normal, vale el autorizado.
- Impide solapamientos al escribir: endpoints de `POST/PUT` propios (o hook de validación en `build_crud`) que devuelvan 409 si ya existe otro límite (o autorización) de la misma SIM cuyo rango se solape. Valida `vigente_hasta >= vigente_desde` y `fecha_fin >= fecha_inicio`, `valor_limite >= 0` y `limite_autorizado > 0`. Mantén `write_dependency=require_role("admin")`.

**Tests:** autorización iniciada a mitad de mes se aplica; solapamiento → 409; autorización menor que el límite normal no lo reduce; los tests actuales de consumo (`test_exceso_con_autorizacion_marca_campo`, etc.) siguen verdes.

### M3 (MEDIO): Validación en backend y manejo de errores

**Archivos:** `backend/app/schemas/*.py`, `backend/app/main.py`, `backend/app/api/v1/crud.py`, `backend/app/api/v1/endpoints/auth.py`, endpoints con `list`.

**Cambios:**
- **Validación de esquema en Pydantic** (hoy solo existe en el frontend). Longitudes máximas iguales a las columnas y formatos: `Sim.numero` (dígitos, `+`, espacios y guiones; 6–30), `iccid` (15–20 dígitos, opcional), `imsi` (15 dígitos, opcional), `Dispositivo.imei` (15 dígitos), `Telefono.numero`, `Extension.numero` (1–6 dígitos), `Coste.periodo` (`^\d{4}-(0[1-9]|1[0-2])$`), `Coste.importe > 0`, `Contrato` (`fecha_vencimiento >= fecha_inicio`). Las cadenas vacías en opcionales se convierten a `None`.
- **Handler global** en `main.py` para `IntegrityError` → 409 y `DataError` → 422, con mensaje genérico en español (ej. "El registro ya existe o viola una restricción") y detalle solo en logs.
- **Usuarios:** no permitir eliminar ni desactivar la propia cuenta ni al **último admin activo** (409). `PUT` con `username` o `email` duplicado → 409; `rol_id` inexistente → 404. `DELETE` de un usuario con filas en `historial` → 409 con el mensaje de que debe desactivarlo (`historial.usuario_id` es una FK sin `ondelete`).
- **Paginación:** `skip: int = Query(0, ge=0)` y `limit: int = Query(100, ge=1, le=500)` en todos los `list` que hoy no lo tienen (`usuarios`, `asignaciones`, `cargos`, `areas`, `departamentos`) y un tope en los listados por relación (`asignaciones/activas`, `por-persona`, `por-recurso`, `costes/por-*`, `locales/por-edificio`, `extensiones/por-telefono`, `departamentos/raices` y `subordinados`). Cuidado: el frontend llama a algunos sin parámetros (`/asignaciones/activas`, `/asignaciones/por-persona/{id}`); usa 500 como valor por defecto ahí para no truncar la UI.

**Tests:** entradas inválidas → 422 (IMEI de 14 dígitos, período `2026-13`); duplicados → 409 sin texto SQL; no se puede borrar el último admin ni a uno mismo; `skip=-1` → 422.

### M4 (MEDIO): Configuración, despliegue y frontend

**Archivos:** `backend/app/main.py`, `backend/app/core/config.py`, `backend/.env.example`, `render.yaml`, `frontend/src/index.css`, `frontend/package.json`.

**Cambios:**
- **CORS:** `render.yaml` no define `CORS_ORIGINS`, y el backend solo permite `localhost`. Define `CORS_ORIGINS` con la URL exacta del frontend. Como usas cabecera Bearer y no cookies, pon `allow_credentials=False` y nunca `*`.
- **Verificar primero:** `.env.example` usa `CORS_ORIGINS=a,b` (separado por comas), pero un `list[str]` en pydantic-settings espera JSON y probablemente falla al arrancar. Reprodúcelo con un test. Arreglo robusto: leer la variable como `str` y exponer una propiedad `cors_origins_list` que separe por comas (aceptando también JSON).
- **Docs de la API:** si `environment == "production"`, crea `FastAPI(docs_url=None, redoc_url=None, openapi_url=None)`.
- **Cabeceras de seguridad** en el static site (bloque `headers:` de `render.yaml`): `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Permissions-Policy` restrictiva y una CSP: `default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' <URL_API>; frame-ancestors 'none'`. (`unsafe-inline` en estilos es necesario por los `style={{}}` de React; la URL de la API se rellena con el valor real, déjalo señalado con un comentario.)
- **Fuentes locales:** quita el `@import` de Google Fonts en `index.css` y autoaloja Archivo e IBM Plex Mono (paquetes `@fontsource/*`).
- **Drivers de BD:** hay inconsistencia entre `requirements.txt` (`psycopg2-binary`) y los defaults `postgresql+psycopg://` de `config.py`/`alembic.ini`. Unifica en psycopg2 (compatible con la URL `postgresql://` que entrega Render) y ajusta defaults.
- `uvicorn ... --proxy-headers` en el `startCommand`.

**Tests:** origen no permitido → sin cabecera `Access-Control-Allow-Origin`; con `ENVIRONMENT=production`, `/openapi.json` → 404; el `.env.example` se parsea sin error.

### M5 (MEDIO): Dependencias

- Sustituye `python-jose==3.3.0` (sin mantenimiento y con CVEs conocidos) por **PyJWT** en `core/security.py`: `jwt.encode`/`jwt.decode(..., algorithms=[settings.algorithm])`, captura `jwt.PyJWTError` y añade el claim `iat`. Mantén `create_access_token(subject)` con la misma firma para no romper tests ni fixtures.
- Ejecuta `pip-audit -r backend/requirements.txt` y `npm audit` en `frontend/`. Actualiza lo que se pueda sin romper y **lista lo demás** en el informe.
- Elimina dependencias no usadas del frontend (`zod`, `react-hook-form`, `@hookform/resolvers`) y regenera `package-lock.json`. `recharts` sí se usa en el Dashboard.

### Bajos (incluir si no bloquean lo anterior)

- La búsqueda en `PersonasPage` filtra en cliente sobre 500 registros: no es de seguridad, pero no la amplíes con datos sensibles.
- Observado, fuera de alcance: en `index.css`, `.dato` declara `font-family: '"IBM Plex Mono"'` con comillas anidadas, que probablemente impide que la fuente cargue. Corrígelo solo si tocas ese archivo por las fuentes locales.

---

## 5. Batería de tests exigida (resumen)

Añade a `backend/tests/` (por ejemplo `test_seguridad_*.py`) todo lo indicado en cada hallazgo. Comprobaciones mínimas transversales:

1. Roles y usuarios: matriz `admin / gestor / consulta / sin token` contra `/roles`, `/usuarios`, `/historial`, `/personas` (campos sensibles), `/limites`, `/autorizaciones`, `/sincronizacion`, `DELETE /facturas-etecsa`, `DELETE /asignaciones`.
2. Sesión: usuario desactivado, contraseña débil, rate limit, arranque en producción con clave insegura.
3. PDF: tamaño, magic bytes, regex con entrada patológica, totales incoherentes.
4. Integridad: doble asignación (índice parcial), errores 409/422 sin texto SQL.
5. Lógica de límites: solape, mitad de mes, autorización menor.
6. Auditoría: `usuario_id` presente, borrados con copia, factura eliminada registrada.

Al terminar, ejecuta: `cd backend && pytest`, `cd frontend && npm run typecheck && npm run build`, y `alembic upgrade head` sobre una base vacía (SQLite y, si es posible, PostgreSQL).

## 6. Decisiones pendientes (implementa el valor por defecto y márcalo en el informe)

| # | Decisión | Valor por defecto |
|---|---|---|
| 1 | Quién ve CI, email y teléfono particular de personas | `admin` y `gestor` sí; `consulta` no |
| 2 | Quién lee el historial | Solo `admin` |
| 3 | Política de contraseña | Mín. 10 caracteres, letra + dígito, máx. 72 bytes |
| 4 | Semántica de vigencia en períodos parciales | Se aplica si el rango se solapa con el mes |
| 5 | Dónde se despliega (Render vs. servidor propio) | Render, pero avisa: un servicio en Render **no alcanza** una IP interna `10.x` (ASSETS_RH), así que la sincronización directa solo funcionaría en servidor propio o con VPN; en Render quedaría la importación por JSON |
| 6 | Si `gestor` puede crear, editar y borrar personas (son un espejo de RRHH que la sincronización sobrescribe) | No se cambia en esta pasada; solo se informa |
| 7 | Qué hacer con `docs/DOCUMENTACION_BD.md` | No se toca; se informa |

## 7. Entrega

Al terminar, responde con este informe:

1. **Tabla de hallazgos:** ID, estado (corregido / parcial / no reproducido / pendiente de decisión), archivos tocados, tests añadidos.
2. **Resultado de la suite:** antes y después (nº de tests que pasan y fallan).
3. **Desviaciones:** tests existentes que hubo que ajustar y por qué.
4. **Decisiones tomadas** por defecto de la sección 6.
5. **Pendientes para el usuario:** limpieza de historial git si hubo push, creación del login solo lectura en SQL Server, definir `ADMIN_INITIAL_PASSWORD` y `CORS_ORIGINS` en Render, revisar `docs/DOCUMENTACION_BD.md`, resultado de `pip-audit`/`npm audit`.
6. **Riesgos residuales** que no se pudieron cerrar en código (por ejemplo, token en `localStorage`, hosting, backups).
