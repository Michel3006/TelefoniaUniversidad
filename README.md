# Sistema de Gestión de Telefonía

Aplicación web para inventariar, administrar y controlar los costos de la telefonía de una organización (fija, móvil, SIMs y equipos). Adaptada al contexto cubano: operadora fija **ETECSA**, costos en **CUP** y directorio de personas/cargos/áreas/departamentos sincronizado desde el sistema institucional de RRHH (**ASSETS_RH**, SQL Server).

- **Backend**: Python 3.12 · FastAPI · SQLAlchemy 2.0 · Alembic · JWT
- **Frontend**: React 18 + TypeScript + Vite + TailwindCSS
- **Documentación**: `docs/` contiene el manual de usuario, la documentación técnica y la documentación de bases de datos (`.md`, `.docx` y `.pdf`)

## Estructura

```
backend/   # API REST (FastAPI) en /api/v1
frontend/  # SPA (React + Vite)
docs/      # Manual de usuario y documentación técnica
```

## Puesta en marcha local

### Backend
```
cd backend
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
# crear .env con: DATABASE_URL / SECRET_KEY / ACCESS_TOKEN_EXPIRE_MINUTES
alembic upgrade head
python app/seed.py          # crea usuario admin / admin123
uvicorn app.main:app --reload   # http://localhost:8000
```

### Sincronización con RRHH (ASSETS_RH)

El directorio de personas, cargos, áreas y unidades organizativas se copia desde el sistema institucional de RRHH (SQL Server `10.8.6.191` / `ASSETS_RH`). Opcional:

1. Habilitar la conexión en `backend/.env`:
   ```
   ASSETS_RRH_HABILITADO=true
   ASSETS_RRH_SERVER=10.8.6.191
   ASSETS_RRH_DATABASE=ASSETS_RH
   ASSETS_RRH_USERNAME=usuario
   ASSETS_RRH_PASSWORD=clave
   # ASSETS_RRH_DRIVER="ODBC Driver 17 for SQL Server"   # ajustar si es otro
   ```
2. Instalar el driver ODBC correspondiente (`pyodbc` ya está en `requirements.txt`).
3. Ejecutar la sincronización por consola o desde la interfaz:
   ```
   cd backend
   python scripts/sincronizar_rrhh.py --host 10.8.6.191 --port 1433 --username ... --password ...
   # o desde la app: Administración → Sincronización RRHH
   ```
Si no hay conexión directa, se puede importar el mismo contenido en JSON desde esa misma pantalla.

### Frontend
```
cd frontend
npm install
# crear .env con VITE_API_URL=http://localhost:8000/api/v1
npm run dev                 # http://localhost:5173
```

### Credenciales iniciales
`admin` / `admin123` (cambiar desde Administración → Usuarios)

## Deploy en Render

La infraestructura se define en `render.yaml` (blueprint de Render):

1. Creá un repositorio en GitHub con este proyecto y subilo.
2. En [Render](https://dashboard.render.com), andá a **New → Blueprint** y conectá el repositorio.
3. Render crea automáticamente:
   - **Web service** `sistema-telefonia-api` (FastAPI + PostgreSQL)
   - **Static site** `sistema-telefonia-frontend` (SPA)
   - **Base de datos** `sistema-telefonia-db` (PostgreSQL free)

El frontend obtiene `VITE_API_URL` del `RENDER_EXTERNAL_URL` del backend automáticamente.

