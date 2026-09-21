# Informe de corrección de seguridad y auditoría

Fecha: 2026-09-20
Base de trabajo: `docs/prompt_correccion_seguridad.md`

Estado de la suite tras los cambios:

```
202 passed, 2 skipped, 1 warning in 513.78s
```

La suite incluye 20 tests nuevos (negativos de roles, rate-limit, política de
contraseñas, solape de períodos, totales incoherentes, archivos demasiado
grandes, campos sensibles por rol, historial por rol, payload de sincronización
excesivo, etc.). Antes de los cambios: `182 passed, 2 skipped`.

Migración de base de datos aplicada:

- `backend/alembic/versions/007_seguridad.py` (`down_revision=006_mejoras_consumo_observaciones`):
  - `usuarios.debe_cambiar_password` (bool, `NOT NULL DEFAULT false`)
  - `usuarios.password_changed_at` (datetime nullable)
  - índice único parcial `uq_asignacion_activa` en `asignaciones (tipo_recurso, recurso_id) WHERE fecha_fin IS NULL`
- Verificado `upgrade head -> downgrade base -> upgrade head` sobre SQLite limpia.
- Aplicado sobre `backend/telefonia.db` (versión = `007_seguridad`, índice presente).

---

## Por hallazgo

### C1 — Credenciales por defecto / password inicial
- `backend/app/seed.py`: el admin solo se crea si existe `ADMIN_INITIAL_PASSWORD`.
  Sin valor o si no cumple la política, NO se crea (mensajes a stderr, exit 0).
  El admin creado queda con `debe_cambiar_password=True`.
- Eliminada toda mención de `admin123` en README, docs y `.env(.example)`.
- `render.yaml`: `ADMIN_INITIAL_PASSWORD` con `sync: false` (la define el operador
  en el panel de Render; vacío por defecto → el seed no crea admin).
- Backend recuperado: `settings.admin_initial_password` mapeado desde el entorno.

### C2 — Política de contraseñas
- `validar_politica_password` (raises `ValueError`): mín. 10 caracteres, al menos
  una letra y un dígito; máx. 128 caracteres / 72 bytes.
- Aplicada en crear usuario, actualizar usuario y cambiar contraseña (schemas).
- Frontend: `frontend/src/lib/validation.ts` valida los mismos criterios al escribir.
- Tests: `test_politica_password`, `test_create_usuario_password_debil`,
  `test_create_usuario_password_sin_digito`, `test_cambiar_password_politica`.

### A1 — Exposición de datos sensibles por rol
- `GET/POST/PUT/DELETE /personas/*`: el rol `consulta` no recibe
  `documento`, `email`, `telefono`, `exttelef`; la búsqueda por esos campos se
  excluye para `consulta`.
- Búsqueda sanitizada (`like_seguro` escapa `\ % _`) y paginada (20/50 máx).
- `/historial` solo para `admin` (403 para gestor/consulta).
- Tests: `test_consulta_no_ve_campos_sensibles`,
  `test_gestor_no_puede_ver_historial`, `test_consulta_no_puede_ver_historial`.

### A2 — Autenticación y sesión
- Login con comparación de hash en tiempo constante vía hash ficticio
  (`_dummy_hash()`), una sola llamada a `verify_password` (evita revelar la
  existencia del usuario).
- Rate-limit por IP y por usuario (`app/core/login_limit.py`, sin deps):
  5 intentos/ventana → `429`; desactivable en tests (`LOGIN_RATE_LIMIT_HABILITADO=false`).
- Logs de seguridad de login fallido/exitoso/bloqueado, cambio de password,
  creación/eliminación/cambio de rol de usuarios.
- `cambiar-password` (204) guarda `password_changed_at` y `debe_cambiar_password=False`.
- Protección: no auto-desactivación (409), no eliminar al último admin (409),
  borrado de usuarios con historial bloqueado (409).
- JWT con `pyjwt` (se reemplazó `python-jose`); error `jwt` mapeado a 401.
- Tests: `test_login_rate_limit`, `test_cambiar_password`, `test_delete_ultimo_admin_rechazado`,
  `test_update_usuario_no_permite_auto_desactivacion`.

### A3 — Higiene del repositorio
- `.gitignore`: `/*.pdf`, `backend/tests/private/`.
- `alembic.ini`: marcador `# alembic`.
- `test_consumo_pdf_real.py`: rutas de búsqueda del PDF real por env o `backend/tests/private/`.
- Sin credenciales en git: `.env` no versionado; en `docs/` queda solo la decisión
  de IPs internas (ver "Decisions pendientes del usuario").
- Verificado: PDFs en repo solo en `docs/`.

### A4 — Integración ASSETS_RH (ODBC/SQL Server)
- Cadena de conexión: valores con `{}` escapados; `SERVER`/`DATABASE` rechazan `;{}`.
- `Encrypt` y `TrustServerCertificate` configurables desde el entorno.
- Error de conexión genérico (`RuntimeError("No se pudo conectar a ASSETS_RH")`)
  sin fuga del mensaje real; el detalle queda en el log del servidor.
- `backend/scripts/sql/assets_rh_readonly.sql`: usuario/rol de solo lectura (`db_datareader`
  o `GRANT SELECT` por tabla: `RH_Cargos`, `RH_Area_Trabajo_Actual`, `RH_Unidades_Organizativas`, `Empleados_Gral`).
- `POST /sincronizacion/rrhh` → `503` genérico cuando está deshabilitado.

### A5 — Consumo ETECSA
- Límites: 15 MB por PDF (400), `%PDF-` verificado (400), nombre ≤ 255 chars.
- `extraer_texto_pdf`: máx. 100 páginas y 5.000.000 caracteres.
- Expresión de montos con cuantificador acotado (anti-ReDoS).
- Verificación de totales contra filas (tolerancia 0.01): mismatch → `422`.
- `evaluacion_limite`: mes-ventana del período; autorización vigente si
  solapa el período (elige el límite autorizado mayor); límite normal el de
  mayor `vigente_desde` en la ventana.
- `eliminar_factura` registra en historial (no_factura, período, nº de consumos).
- Tests: `test_importar_factura_totales_incoherentes`, `test_importar_archivo_demasiado_grande`.
  Ajustados `test_consumo.py`, `test_consumo_parser.py`, `test_reportes.py` (totales coherentes y magic bytes `%PDF-`).

### M1 — Auditoría (historial)
- CRUD genérico y endpoints custom guardan `valor_anterior`/`valor_nuevo` como JSON
  (create/update/delete) y `usuario_id` del actuante.
- `asignaciones`: update solo de `observaciones`; delete solo admin; 409 en doble
  asignación activa.
- Tests: `test_historial_eliminacion_con_valor_anterior`.

### M2 — Límites y autorizaciones como endpoints propios
- Solape de períodos → `409` (POST y PUT).
- Validaciones: `fecha_fin >= fecha_inicio`, `vigente_hasta >= vigente_desde`,
  `valor_limite >= 0`, `limite_autorizado > 0` (422); escritura solo admin; historial; paginación.
- Tests: `test_limite_solapado_rechazado`, `test_autorizacion_solapada_rechazada`,
  `test_limite_valor_negativo_rechazado`, `test_autorizacion_fechas_invalidas`.

### M3 — Validación de schemas
- `telefonia.py`: patrones de teléfono/extension/SIM/ICCID/IMSI/IMEI; `_no_vacio`.
- `costes.py`: período `AAAA-MM` válido y montos positivos.
- `planes.py`: `fecha_vencimiento >= fecha_inicio`, `coste_mensual >= 0`.
- `institucional.py`: listas de sincronización acotadas (50k) y payload de
  `/rh-json` ≤ 5 MB → `413`.
- Handlers globales en `main.py`: `IntegrityError→409`, `DataError→422`,
  `RequestValidationError→422`, `Exception→500` (mensaje genérico en producción);
  CORS desde `settings.cors_origins_list` (coma o JSON).

### M4 — Configuración e higiene de deps
- `render.yaml`: headers de seguridad (CSP, X-Frame-Options, HSTS, nosniff),
  `--proxy-headers`, `ADMIN_INITIAL_PASSWORD sync:false`.
- Fuentes autoalojadas (`@fontsource/archivo`, `@fontsource/ibm-plex-mono`) en lugar
  de Google Fonts remoto.
- Se eliminaron dependencias sin uso: `zod`, `react-hook-form`, `@hookform/resolvers`.
- Frontend: cuenta y cambio obligatorio de password (`/cuenta`) redirigido por
  `ProtectedRoute` cuando `debe_cambiar_password`; Historial en navegación y ruta
  soloAdmin; `Persona` con campos sensibles opcionales; comentario A2.9 sobre
  `localStorage`.
- `npm run typecheck` y `npm run build` OK (2m01s).

---

## Correcciones que requieren tests de integración pendientes (puntos que verificar manualmente)
- El PDF real de ETECSA no está en el repo; los 2 tests de `test_consumo_pdf_real.py`
  quedan skipped. Con la nueva validación de totales, un PDF legítimo cuyas filas
  no sumen al pie será rechazado (422) — evaluar contra el PDF real antes de producción.

---

## Decisiones pendientes del usuario
1. `ADMIN_INITIAL_PASSWORD`: generar una password fuerte y definirla como variable
   de entorno (Render/producción) antes de ejecutar el seed.
2. IPs internas que siguen en la documentación (`10.8.6.191` y `172.27.240.8` en
   `docs/DOCUMENTACION_TECNICA.md` y `docs/DOCUMENTACION_BD.md`): son referencias
   históricas; se respetó la regla de no tocar `docs/` salvo credenciales literales.
3. Commit por hallazgo: no se ejecutaron `git commit` en esta sesión. Se puede
   agrupar por C1/C2/A1-A5/M1-M5; se deja pendiente por indicación explícita.
4. Validar contra el PDF real la regla de coherencia de totales (punto anterior).