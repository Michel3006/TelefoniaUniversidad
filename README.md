# Sistema de Gestión de Telefonía

Aplicación web para inventariar, administrar y controlar los costos de la telefonía de una organización (fija, móvil, SIMs y equipos).

- **Backend**: Python 3.12 · FastAPI · SQLAlchemy 2.0 · Alembic · JWT
- **Frontend**: React 18 + TypeScript + Vite + TailwindCSS
- **Documentación**: `docs/` contiene el manual de usuario y la documentación técnica (`.md`, `.docx` y `.pdf`)

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

