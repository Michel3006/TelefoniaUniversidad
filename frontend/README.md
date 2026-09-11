# Troncal — Frontend del Sistema de Telefonía

Frontend en React + TypeScript para el backend FastAPI de gestión de
telefonía. Implementa la especificación de diseño acordada (ver
`ESPECIFICACION-FRONTEND.md` del proyecto general): tablero tipo "libro de
registro", monoespaciada solo para datos reales, sin tarjetas ni sombras,
paneles laterales en vez de modales.

## Requisitos

- Node 18+
- El backend corriendo (ver `backend/README` o `uvicorn app.main:app`)

## Puesta en marcha

```bash
npm install
cp .env.example .env      # ajustá VITE_API_URL si el backend no está en localhost:8000
npm run dev
```

## Importante: rol del usuario

Este frontend asume que `GET /api/v1/auth/me` devuelve el usuario con su rol
anidado (`{ ..., "rol": { "id": 1, "nombre": "admin" } }`). Si tu backend
todavía no lo expone así, la sección "Usuarios" nunca va a aparecer aunque
el usuario sea admin — actualizá `UsuarioRead` en
`backend/app/schemas/auth.py` para incluir `rol: RolRead` antes de probar
esta parte (ver `lib/auth-context.tsx`).

## Decisiones de arquitectura

- **`CrudPage` genérico** (`components/crud/CrudPage.tsx`): los catálogos
  simples (Estados, Proveedores, Operadores, Planes, SIMs, Dispositivos,
  Extensiones) reusan un único componente configurado por entidad en vez de
  repetir la misma tabla+formulario 7 veces. Las páginas con comportamiento
  propio (detalle, árbol, agrupación, finalizar) están escritas a mano:
  Personas, Departamentos, Locales, Líneas, Teléfonos, Contratos, Costes,
  Asignaciones, Usuarios, Historial.
- **Sin librería de componentes** (nada de shadcn/MUI/Ant/Chakra) — todo el
  sistema visual son primitivos propios sobre Tailwind, según la
  especificación de diseño.
- **TanStack Query** para todo el fetching; **TanStack Table** (headless)
  para las tablas.
- Cada endpoint usado fue verificado contra el código real del backend
  (`api/v1/endpoints/*.py`), no asumido de memoria.

## Qué falta / próximos pasos razonables

- Búsqueda server-side real (`/personas/buscar`, `/dispositivos/buscar`,
  etc.) — hoy la búsqueda de Personas filtra client-side sobre la lista ya
  cargada; para volúmenes grandes conviene pasar a los endpoints `/buscar`.
- Paginación real en las tablas grandes (hoy se trae `limit=500` de una).
- Tests (Vitest + Testing Library) — no incluidos en este entregable.
