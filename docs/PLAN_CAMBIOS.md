# Plan de Cambios y Actualizaciones — Sistema de Telefonía

Versión del documento: 0.2 — 23 de septiembre de 2026
Base del trabajo: rama `feat/correccion-seguridad` (commit `6d895cc`), que es la versión desplegada en el contenedor (10.8.1.66).

> **Metodología:** los puntos se implementan **uno a uno**, en orden, y solo se pasa al siguiente cuando el usuario autoriza. Al resolver cada punto se actualiza el proyecto local de la PC para que quede a la par del original (rama `feat/correccion-seguridad` en GitHub / contenedor).

---

## 1. Personas 100 % desde la base de datos (ASSETS_RH)

- Cargar **todos** los datos de las personas desde `ASSETS_RH` (tabla `Empleados_Gral`) mediante la sincronización, **incluida su ubicación**:
  - **Ubicación física en el centro de trabajo**: la BD trae `Cubiculo` (cubículo/oficina de la persona) en `Empleados_Gral`.
  - **Ubicación administrativa**: `Id_Direccion` (departamento) e `Id_Area` (área de trabajo), que ya se sincronizan.
  - Dirección particular: `Direccion`, `Ciudad`, `Region`, `Pais`, `Id_Municipio`, etc.
- La BD **no tiene** catálogo de edificios/locales/oficinas: esa información física del puesto se obtiene del campo `Cubiculo` de cada persona, no de una tabla de locales.
- **Los departamentos y las áreas NO se eliminan**: se mantienen en la app, pero **se cargan también desde la base de datos** (`RH_Unidades_Organizativas` y `RH_Area_Trabajo_Actual`), como ya hace la sincronización. Nunca se escriben a mano.
- **Eliminar "locales" (y con ello "edificios")** de la aplicación: ese dato **no existe** en la base de datos. Implica quitar el módulo de la UI, la tabla `locales`/`edificios` (vía migración) y los campos `local_id` de `telefonos` y `dispositivos`.
- Objetivo global: **ningún dato de la persona se escribe a mano** (ni su ubicación); todo lo trae la sincronización.

## 2. Crear SIMs automáticamente al importar el PDF de ETECSA

- El PDF de ETECSA trae un listado de números telefónicos. Hay PDFs de **facturas de SIMs** y otros de **facturas de teléfonos fijos**.
- Al **cargar el PDF** en el apartado de consumo, se deben **agregar a la tabla de SIMs** los números de **móvil (SIM)** que **no estén en la base de datos** pero sí aparezcan en el PDF.
- Criterio para distinguir un número de SIM (móvil) de un fijo: **8 dígitos que comiencen con `5` o `6`**.
- Los números **fijos** (que no cumplen el criterio) **no se cargan** en la base de datos: se guardan como consumo sin SIM asociada, como hasta ahora.
- Las SIMs que ya existen se asocian/ligan a su consumo como hasta ahora.

## 3. Módulo de Auditoría completo

- Nuevo módulo de auditoría que registre **todas las operaciones** que se hacen en el sistema:
  - **Fecha y hora** de la operación.
  - **Qué usuario** la hizo y **qué cargo tiene**.
  - **Tipo de operación**: GET, POST, PUT, DELETE, PATCH, etc.
  - **Qué fue exactamente lo que hizo** (detalle de la operación / datos afectados).
- Nota: ya existe un módulo `historial` básico (registra entidad, acción y usuario). Este punto lo **extiende/completa** para cubrir método HTTP, fecha/hora completa, cargo del usuario y detalle exacto.

## 4. Responsable / asignación con buscador en Teléfonos fijos y Extensiones

- Permitir asignar un **responsable (una persona)** a los **teléfonos fijos** y a las **extensiones**.
- Al momento de asignar la persona debe aparecer un **buscador** (hay muchas personas, no se puede depender del scroll).

## 5. Buscador en todos los campos de asignación del proyecto

- En **todos** los campos que sean de asignación en el proyecto entero (personas, SIMs, dispositivos, teléfonos, extensiones, etc.), debe haber un **buscador** para no tener que hacer scroll hasta el elemento que se quiere asignar.

## 6. Guía telefónica (datos de persona + sus recursos)

- Nuevo apartado que cargue **todas las personas**.
- Al **seleccionar una persona** debe mostrar:
  - Sus **datos** (nombre, cargo, departamento/área, teléfono, etc.).
  - Si tiene alguna **extensión, teléfono, dispositivo o línea (SIM)** asociado.
- Funciona como una especie de **guía telefónica**.

## 7. Eliminar Costos, Planes y Límites: todo se deriva del PDF de ETECSA

- **Contexto:** el PDF de ETECSA (ej. `202607_73212_41012682713947.pdf` en la raíz del proyecto) trae, por cada línea, los campos: **Servicio** (número de SIM), **Cuota**, **Consumo** e **Importe**. Todo lo que hoy se carga/define manualmente en Costos, Planes y Límites **ya viene en el PDF**, por lo que esos módulos se eliminan.
- **Campo `Servicio`** → es el **número de la SIM**. Se usa para ligar la fila del PDF a su SIM (creándola si no existe, según el punto 2).
- **Campo `Cuota`** → es lo que le toca a esa SIM: equivale al concepto de "plan", pero **no se define a mano**. Se extrae del PDF y se guarda como **cuota**, siempre **asociada a una SIM**.
  - **Eliminar el módulo de "Planes"** de la UI. En su lugar (o como parte de Consumo/SIMs) se mostrarán las **cuotas existentes**, todas provenientes del PDF, cada una ligada a su SIM.
- **Campo `Consumo`** → equivale al **excedente**. Si el PDF trae un valor **distinto de 0**, la línea se excedió de su cuota.
  - **Alarma de excedente:** siempre que alguien **no autorizado** tenga `consumo > 0`, debe saltar una alerta/alarma en el sistema (solo si no tiene autorización vigente; si la tiene, se comporta como consumo autorizado).
  - **Eliminar el módulo de "Límites"** de la UI: el límite **es la cuota** que trae el PDF, no se define manualmente.
- **Campo `Importe`** → es el **total a pagar** de esa línea. **También se toma directamente del PDF** (no se calcula); se guarda/muestra como solo lectura. (A título informativo, suele corresponder a `Cuota + Consumo`.)
- **Eliminar por completo el módulo de "Costos"** de la UI, la ruta/endpoints y la tabla `costes` (vía migración), ya que su contenido ahora se obtiene del PDF (cuota + consumo + importe por SIM).
- **Resumen de impacto:**
  - UI: quitar menú/rutas de **Costos**, **Planes** y **Límites**; los datos pasan a visualizarse desde el resultado de la importación del PDF (cuotas por SIM, consumo/excedente, importe).
  - BD: eliminar tabla `costes`; eliminar `planes` y `limites_consumo` (o reconvertirlas según convenga) **solo cuando** el usuario autorice la migración; mientras tanto el nuevo flujo de importación del PDF es la fuente de verdad.
  - Backend: al importar el PDF, además de SIMs y consumo, persistir **cuota**, **excedente** y **importe** por SIM; disparar **alarma** si `consumo > 0` y la persona/SIM no tiene autorización vigente.
- **Orden de ejecución:** este punto se implementa **después** del punto 3 (auditoría), para quedar registrado todo el nuevo flujo de importación.

---

## Pendiente

- [x] 1. Personas 100 % desde ASSETS_RH (departamentos y áreas también desde la BD; eliminar Locales/Edificios)
- [x] 2. Crear SIMs automáticamente al importar el PDF de ETECSA
- [x] 3. Módulo de Auditoría completo
- [x] 4. Responsable con buscador en teléfonos fijos y extensiones
- [x] 5. Buscador en todos los campos de asignación
- [x] 6. Apartado Guía telefónica
- [x] 7. Eliminar Costos, Planes y Límites: todo se deriva del PDF de ETECSA (cuota, consumo/excedente, importe; alarma si excede sin autorización)

## Historial

- **23/09/2026**: creación del documento con los 6 puntos de trabajo planteados por el usuario.
- **23/09/2026**: aclarado el punto 1 — departamentos y áreas se cargan de la BD (no se eliminan); se eliminan Locales/Edificios (no existen en la BD). La ubicación de la persona en el centro de trabajo se toma del campo `Cubiculo` de `Empleados_Gral` (la BD no tiene catálogo de edificios/oficinas).
- **23/09/2026**: implementado el punto 1 (personas, departamentos y áreas son solo lectura desde ASSETS_RH; se agregó `cubiculo`/`direccion`/`ciudad` a Persona; se eliminaron Locales y Edificios con migración `008`).
- **23/09/2026**: el punto 2 original (eliminar costos) **se descartó** por decisión del usuario; en su lugar se agregó el nuevo punto 2: crear SIMs automáticamente desde el PDF de ETECSA.
- **23/09/2026**: aclarado el punto 2 — solo se crean los números de **SIM/móvil**; los fijos no se cargan del PDF. Criterio de móvil: **8 dígitos que comiencen con `5` o `6`** (decisión del usuario).
- **23/09/2026**: implementado el punto 2 — al importar un PDF de ETECSA, los números de SIM (8 dígitos que empiezan con 5 o 6) que no existen se crean automáticamente en `sims`; los fijos quedan como consumo sin asociar. El resumen de importación ahora reporta `sims_creadas`/`numeros_sims_creadas`.
- **23/09/2026**: implementados los puntos 4 y 5 — nuevo componente `SelectBuscador` (combobox) en todos los campos de asignación del frontend: persona, SIM, teléfono, dispositivo, extensión, departamento, plan y contrato. Para las personas la búsqueda es server-side (`/personas/buscar`), el resto filtra sobre el catálogo cargado. El detalle de teléfono ahora incluye su `responsable` (asignación activa tipo `telefono`), junto al responsable de cada extensión. Aplicado en `CrudPage` (Autorizaciones, Límites, Planes, Extensiones, Dispositivos y SIMs), `AsignacionesPage`, `CostesPage` y `TelefonosPage`.
- **23/09/2026**: implementado el punto 6 — nuevo apartado "Guía telefónica" (`/guia-telefonica`) con endpoint `GET /guias/telefonica` que devuelve todas las personas (con cargo, área, departamento, extensión, teléfono, cubículo, etc.) y las asignaciones activas resueltas (número de SIM/teléfono/extensión o marca+modelo de dispositivo). El rol `consulta` no recibe los campos sensibles (documento/email/teléfono/exttelef), igual que en Personas. La página listar personas con buscador y muestra el detalle en un panel lateral.
- **23/09/2026**: añadido el punto 7 (solicitado por el usuario) — eliminar por completo **Costos**, **Planes** y **Límites**: todo se deriva del PDF de ETECSA. El PDF trae por línea: `Servicio` (= número de SIM), `Cuota` (= lo que le toca a la SIM, antes "plan", ahora solo lectura desde el PDF y asociada a la SIM), `Consumo` (= excedente; si es > 0 y no hay autorización vigente debe saltar una **alarma**) e `Importe` (**también tomado directamente del PDF**, no calculado; solo lectura; informativamente equivale a Cuota + Consumo). Se eliminan los módulos UI de Costos/Planes/Límites y, en su momento, las tablas `costes`/`planes`/`limites_consumo` vía migración (previa autorización). La importación del PDF pasa a ser la fuente de verdad de cuota, consumo e importe. **Orden:** se implementa después del punto 3 (auditoría). PDF de referencia en la raíz: `202607_73212_41012682713947.pdf`.
- **23/09/2026**: aclarado el punto 7 — el campo `Importe` **también se toma directamente del PDF** (no se calcula como Cuota + Consumo); solo lectura.
- **23/09/2026**: implementado el punto 7 — se eliminaron los módulos de Costos, Planes y Límites (UI, endpoints, modelos y schemas); migración `009_eliminar_costes_planes_limites` elimina las tablas `costes`, `planes`, `limites_consumo` y la columna `sims.plan_id`. La importación del PDF ahora es la fuente de verdad: `cuota`/`limite_normal`/`limite_efectivo` = Cuota del PDF, `importe` se persiste tal cual, y `consumo > 0` sin autorización vigente marca `en_exceso` + escribe un registro de **alarma** en Historial (`entidad=alarma_excedente`, `accion=alarma`) y suma `alarmas` en el resumen de importación. El Dashboard ya no muestra "Costes por departamento"; el menú y las rutas de Costos/Planes/Límites fueron retirados. 157 pruebas backend en verde; typecheck del frontend limpio.
- **23/09/2026**: implementado el punto 3 — **Módulo de Auditoría completo**. Nueva tabla `auditoria` (migración `010_auditoria`) que registra **todas** las operaciones HTTP del sistema mediante middleware global: **fecha y hora completas**, **qué usuario** (id + nombre) y **qué cargo/rol** tenía al momento de operar (snapshot: el trail no se pierde si el rol cambia o el usuario se elimina, con `usuario_id` a `NULL` via `ON DELETE SET NULL`), **método HTTP** (GET/POST/PUT/PATCH/DELETE), **ruta exacta**, **estatus** de la respuesta e **IP** de origen. El **detalle exacto** guarda el payload de la petición y la cadena de consulta con **enmascarado de campos sensibles** (password, token, secret, etc. → `<<enmascarado>>`); el login queda registrado mostrando el `username` pero nunca la contraseña. El panel es **exclusivo del rol `admin`** (endpoint con `require_role("admin")` + ruta `/auditoria` envuelta en `AdminRoute` en el frontend, ícono en Administración); el propio panel no se auto-registra para evitar recursión/ruido. Filtros por método/cargo/usuario/estatus/rango de fechas y endpoint de resumen (`GET /auditoria/resumen`). El middleware escribe con su propia sesión (best-effort: nunca rompe la petición) y en pruebas apunta a la BD de tests (`usar_sesion_auditoria` en `conftest.py`). La página `AuditoriaPage` muestra tabla con resumen de totales y detalle de la operación seleccionada. Todo el árbol backend en verde (164 pruebas, antes 157) y typecheck del frontend limpio.