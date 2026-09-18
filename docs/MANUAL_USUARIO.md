# Manual de Usuario — Sistema de Gestión de Telefonía

Versión del documento: 2.0
Fecha: 17 de septiembre de 2026

---

## 1. ¿Qué es esta aplicación?

El **Sistema de Gestión de Telefonía** te ayuda a llevar el control de los teléfonos de tu organización en un solo lugar:

- Quién tiene cada teléfono, línea móvil, chip (SIM) o equipo asignado.
- Dónde está cada teléfono fijo (edificio, piso, oficina) y con qué extensiones cuenta.
- Los contratos y planes con sus fechas de vencimiento.
- Cuánto se gasta por mes y por departamento en telefonía (en pesos cubanos, CUP).
- El **directorio de personas, cargos, áreas y departamentos se sincroniza** automáticamente desde el sistema institucional de RRHH (ASSETS_RH), para no cargar los datos dos veces.

Todo se administra desde una página web sencilla, con formularios que te **avisan si algo está mal** antes de guardar.

---

## 2. Primeros pasos

### 2.1 Cómo entrar

1. Abrí tu navegador (Chrome, Edge, Firefox).
2. Entrá a la dirección donde está instalada la aplicación (en desarrollo: `http://localhost:5173`).
3. Se abre la pantalla de **Iniciar sesión**.

### 2.2 Iniciar sesión

- En **Usuario** escribí tu nombre de usuario (ej. `admin`).
- En **Contraseña** escribí la tuya (ej. `admin123` para el usuario inicial).
- Tocá el botón **Ingresar**.

Si las credenciales son incorrectas aparece un mensaje de error. Si la sesión vence (a los 30 minutos de inactividad), la aplicación te pide iniciar sesión de nuevo automáticamente.

### 2.3 Cerrar sesión

Tocá el botón **Salir** en la barra superior. La próxima vez que entres tendrás que iniciar sesión otra vez.

### 2.4 Los tres tipos de usuario

| Rol | Qué puede hacer |
| --- | --- |
| **Administrador** | Todo, incluido administrar los usuarios del sistema (crearlos, cambiarlos, desactivarlos) y ejecutar la sincronización de RRHH. |
| **Gestor** | Administra los recursos (teléfonos, líneas, costos, etc.). |
| **Consulta** | Puede ver la información. |

Algunas opciones del menú (por ejemplo **Usuarios** y **Sincronización RRHH**) solo aparecen para el administrador.

---

## 3. La pantalla principal (Panel)

Al entrar verás una barra lateral con el **menú** y una barra superior con tu nombre y el botón **Salir**.

El **Panel** (primera pantalla) te da una foto rápida de la organización:

- **Contadores**: líneas móviles, teléfonos fijos, dispositivos, personas, edificios y locales.
- **Vencimientos próximos**: contratos que se vencen en los próximos 60 días (en rojo si faltan 15 días o menos).
- **Costos por departamento**: un gráfico de barras con lo gastado por cada departamento.

Estos datos se actualizan solos cada vez que entrás al Panel.

La barra lateral se puede **colapsar** tocando las dobles flechas para ganar espacio.

El menú está organizado en grupos:

- **Directorio**: Personas, Departamentos, Locales.
- **Recursos**: Líneas, Teléfonos, Extensiones, Dispositivos, SIMs.
- **Contratos**: Contratos, Planes.
- **Catálogos**: Estados, Cargos, Áreas.
- **Costos, Asignaciones, Historial**.
- **Administración**: Usuarios (solo admin) y **Sincronización RRHH** (solo admin).

---

## 4. Cómo funcionan las pantallas de listado

Casi todas las pantallas (salvo el Panel) funcionan igual:

1. **Listado**: una tabla con los registros cargados.
2. Botón **Crear** (arriba a la derecha) para agregar uno nuevo.
3. En cada fila, botones **Ver**, **Editar** y **Eliminar**.
4. **Buscador** y **paginación** en la tabla para encontrar rápido.

### 4.1 Crear un registro

1. Tocá el botón **Crear**.
2. Se abre un panel lateral con el formulario.
3. Completá los campos y tocá **Guardar cambios**.
4. Los campos marcados con **\*** son obligatorios.

### 4.2 Editar un registro

1. Tocá **Editar** en la fila.
2. Modificá lo que necesites.
3. Tocá **Guardar cambios**.

### 4.3 Ver un registro

Tocá **Ver** para abrir una ficha con todos los datos (por ejemplo, un teléfono con sus extensiones, o una línea con el chip y el responsable).

### 4.4 Eliminar un registro

1. Tocá **Eliminar**.
2. La aplicación te pregunta para confirmar. **Esta acción no se puede deshacer**.
3. Tocá **Eliminar** de nuevo para confirmar.

### 4.5 Recursos de solo lectura

Algunas pantallas (Personas, Departamentos, Cargos y Áreas) son **de solo lectura**: no tienen botón Crear ni Editar, porque sus datos se cargan desde el sistema institucional de RRHH mediante la sincronización. Si falta alguien o hay un dato desactualizado, ejecutá la sincronización (ver sección 12.2).

### 4.6 Errores de formulario

Si un campo tiene un problema, se marca **en rojo con un mensaje** debajo. No vas a poder guardar hasta corregirlo. La aplicación además **filtra caracteres inválidos al escribir** (por ejemplo, no te deja poner letras en un campo de número).

---

## 5. Directorio: la estructura de tu organización

### 5.1 Edificios y Locales (pantalla **Locales**)

Primero definís los **edificios** (la sede física) y después los **locales** (oficinas o celdas dentro del edificio).

**Edificio**:

- *Nombre*: por ejemplo "Edificio Central" (obligatorio).
- *Dirección*: la calle y número (opcional).

**Local**:

- *Edificio*: de la lista, elegí a qué edificio pertenece (obligatorio).
- *Piso*: por ejemplo "1", "Planta baja" (opcional).
- *Oficina*: por ejemplo "301" (opcional).
- *Descripción*: cualquier aclaración (opcional).

En la pantalla hay dos pestañas/formularios: uno para **locales** y otro para **edificios**.

### 5.2 Departamentos (pantalla **Departamentos**)

Pantalla de **solo lectura**: muestra la estructura organizativa que llega de la sincronización de RRHH, en forma de árbol.

Junto al nombre de cada departamento se muestra su **código de dirección** (`Dir. …`), el **área** a la que pertenece y si está **dado de baja**. Si la información no está completa, ejecutá la sincronización.

### 5.3 Personas (pantalla **Personas**)

Pantalla de **solo lectura**: lista los trabajadores sincronizados desde el sistema de RRHH. Al tocar **Ver** se abre una ficha con:

- **Datos institucionales**: empleado, expediente, cargo, área, departamento, documento, centro de costo, extensión y estado (activo o baja).
- **Recursos asignados**: las líneas, teléfonos, dispositivos y extensiones que tiene la persona (activos o finalizados).

Buscá por nombre, apellido, documento o empleado. Recordá: **no se crean personas desde aquí**; el directorio se carga y actualiza con la sincronización de RRHH.

**Consejo**: alcanza con que RRHH dé de alta a un trabajador en el sistema institucional; acá suele tenerse que ver reflejado de forma automática al sincronizar.

---

## 6. Recursos: la telefonía en sí

### 6.1 Teléfonos (fijos)

Armás el número del **equipo fijo** (el de la mesa o la sala).

- **Número**: el número del teléfono fijo, solo dígitos (obligatorio).
- **Local**: dónde está (edificio/piso/oficina), de la lista.
- **Estado**: de la lista (por ejemplo "Activo").
- **Observaciones** (opcional).

Al tocar **Ver** en la fila podés ver el teléfono con sus **extensiones** y quién es el responsable de cada extensión.

### 6.2 Extensiones

Son los números internos de marcación (ej. 410, 411) que cuelgan de un teléfono fijo.

- **Número**: el interno, solo dígitos (obligatorio).
- **Teléfono**: al teléfono fijo al que pertenece.
- **Estado** y **Observaciones** (opcional/consejo).

**Consejo**: cada extensión es un recurso asignable; por eso después en **Asignaciones** vas a poder decir qué persona "tiene" cada extensión.

### 6.3 Líneas (móviles)

Son los **números de celular** de la organización.

- **Número**: el número móvil, solo dígitos (obligatorio).
- **Operador**: fijo, **ETECSA** (la única operadora del país; no se elige).
- **Plan**: de la lista de planes cargados.
- **SIM**: el chip físico que usa esa línea.
- **Estado** (de la lista).

Al tocar **Ver**: vas a ver la línea con su operador, plan, chip (ICCID/IMSI), el dispositivo que la usa y la persona responsable.

**Orden recomendado**: cargá los planes y el chip (SIM) antes de las líneas.

### 6.4 Dispositivos (celulares/equipos)

El equipo en sí (marca y modelo):

- **Marca** (obligatorio): ejemplo "Samsung".
- **Modelo** (obligatorio): ejemplo "Galaxy A24".
- **IMEI**: número de identificación de 15 dígitos del equipo. Lo encontrás marcando `*#06#` en el teléfono o a veces debajo de la batería. Solo dígitos (obligatorio).
- **Línea**: a qué número móvil está asociado.
- **Local**: dónde está guardado si corresponde.
- **Estado**.

### 6.5 SIMs (chips)

- **ICCID** (obligatorio): número de identificación de la tarjeta SIM, normalmente impreso en la misma tarjeta (19–20 dígitos). Solo números.
- **IMSI** (opcional): los 15 dígitos que identifican a la SIM en la red.
- **Operador**: fijo, **ETECSA**.
- **Estado**.

---

## 7. Contratos y planes

### 7.1 Contratos

El contrato firmado con la empresa de telecomunicaciones.

- **Número** (obligatorio): identificador del contrato.
- **Fecha de inicio** y **Fecha de vencimiento** (opcionales). La aplicación no te deja poner un vencimiento **anterior** al inicio.
- **Observaciones** (opcional).

En el Panel vas a ver los contratos que están por vencer (y en la pantalla Contratos la fecha de vencimiento con un aviso `(Xd)` cuando faltan 30 días o menos).

### 7.2 Planes

- **Nombre** (obligatorio): por ejemplo "Pospago 20GB".
- **Operador**: fijo, **ETECSA**.
- **Contrato**: el contrato al que pertenece.
- **Costo mensual** (opcional): el costo por mes, con decimales (ej. `1200.50`).
- **Observaciones** (opcional).

Los planes pueden asociarse a las líneas móviles.

---

## 8. Catálogos

### 8.1 Estados

Lista de estados para marcar los recursos (por ejemplo: "Activo", "De baja", "Pendiente"). Sirven de etiqueta para saber el estado de cada teléfono, línea, chip o dispositivo.

- **Nombre** (obligatorio y único).
- **Descripción** (opcional).

**Consejo**: creá primero los estados que necesites (Activo, Baja, Pendiente) y después usalos en todos los recursos.

### 8.2 Cargos y Áreas (solo lectura)

- **Cargos**: el catálogo de cargos (ej. "Especialista", "Técnico en Informática") sincronizado desde el sistema de RRHH.
- **Áreas**: las áreas de trabajo sincronizadas desde el sistema de RRHH (ej. "Recursos Humanos", "Dirección").

Ambos se usan para complementar la ficha de cada **persona**. Se cargan solos con la sincronización.

---

## 9. Costos: el control de gastos

Acá cargás los gastos de telefonía para llevar el control por mes. Todo se registra en **pesos cubanos (CUP)**.

- **Período** (obligatorio): el mes, con formato `AAAA-MM`. Ejemplo: `2026-09` es septiembre de 2026. Se valida que el mes sea válido.
- **Importe** (obligatorio): el monto, con decimales (ej. `12500.75`).
- **Observaciones** (opcional): qué gasto es (ej. "Factura móviles", "Recarga de tarjeta").
- **Departamento** / **Línea** (opcionales): a qué imputás el gasto.

La pantalla de Costos permite **filtrar por período** y por **departamento**, y muestra el **importe total registrado (CUP)** con la cantidad de períodos distintos.

En el **Panel** vas a ver el gráfico de costos por departamento; en Reportes se resumen por período y por departamento.

---

## 10. Asignaciones: quién usa cada recurso

Este es el corazón del sistema: registrar **a qué persona** se le entrega cada línea, teléfono, dispositivo o extensión.

1. Tocá **Crear**.
2. **Persona** (obligatorio): a quién se entrega.
3. **Tipo de recurso** (obligatorio): Línea, **Teléfono**, Dispositivo o Extensión. Al elegir el tipo, la lista de **Recurso** se actualiza mostrando solo recursos de ese tipo.
4. **Recurso** (obligatorio): el número/equipo específico.
5. **Fecha de inicio** (obligatorio): desde cuándo lo tiene.
6. **Observaciones** (opcional): cualquier aclaración de la entrega.

Para registrar que una persona **devolvió** el recurso, en la fila de la asignación podés **Finalizar** (la aplicación pone la fecha de hoy automáticamente). También la podés eliminar si se cargó por error.

Los detalles de línea y teléfono muestran automáticamente el **responsable** (la persona con asignación activa más reciente).

---

## 11. Historial

Registro de auditoría de todo lo que se crea, modifica o elimina en el sistema: entidad, registro, acción, campo cambiado, valor anterior → valor nuevo, y cuándo.

- Usá el selector **Entidad** para filtrar por tipo de registro.
- Es de solo lectura: no se puede borrar desde la interfaz.

---

## 12. Administración (solo admin)

### 12.1 Usuarios

En **Usuarios** podés crear y administrar las cuentas para que otras personas entren:

1. **Crear** un usuario: **usuario** (nombre de login), **email**, **contraseña** (mínimo 6 caracteres) y **rol** (admin/gestor/consulta).
2. Con **Editar** podés cambiar contraseña, rol y **activar/desactivar** la cuenta (un usuario inactivo no puede ingresar).
3. Con **Eliminar** borrás la cuenta.

**Recomendación**: creá cuentas individuales para cada persona en vez de compartir la de `admin`.

### 12.2 Sincronización RRHH

Pantalla exclusiva del administrador para actualizar el directorio desde el sistema institucional de RRHH (ASSETS_RH). Hay dos formas:

- **Sincronización directa (SQL Server)**: el botón "Sincronizar desde ASSETS_RH" conecta al servidor institucional y copia trabajadores, unidades organizativas, cargos y áreas. Requiere que el servidor haya habilitado la conexión y configurado las credenciales; si no, la aplicación lo avisa.
- **Importación desde JSON**: si no hay conexión directa, se pega un archivo JSON con el mismo contenido (cargos, áreas, unidades y empleados) y se importa.

Al finalizar, la pantalla muestra un **resumen** de cuántos cargos, áreas, unidades organizativas y empleados se procesaron. La sincronización **actualiza** los registros existentes y **agrega** los nuevos; las personas y departamentos quedan listos para usarse en el resto de la aplicación.

---

## 13. Preguntas frecuentes

**¿Puedo borrar una persona que tiene asignaciones?**
Las personas son parte del directorio sincronizado y no se borran desde la interfaz. Si falta alguien o cambió su estado (por ejemplo pasó a baja), actualizá el directorio con la sincronización.

**¿Por qué no me deja escribir letras en el campo IMEI/ICCID?**
Son campos numéricos; el sistema solo acepta dígitos para evitar errores de tipeo.

**El campo "Período" me da error, ¿qué formato usa?**
`AAAA-MM`. Escribí el año con 4 dígitos, un guion y el mes con 2 dígitos (ej. `2026-09`).

**¿Qué es el "documento" de una persona?**
El número de identidad (carné de identidad / No. de CI) tal como lo registra RRHH. Es de solo lectura y llega con la sincronización.

**¿Cómo sé quién tiene asignada una línea?**
Entrá a **Líneas**, tocá **Ver** en la línea; ahí figura el responsable. También podés consultar en **Asignaciones**.

**Se vence mi sesión seguido.**
El token dura 30 minutos. Si estás mucho tiempo sin usar la app, tenés que volver a ingresar.

**¿Dónde veo cuánto gasta mi entidad por mes?**
Cargá los gastos en **Costos** con su **período** e **importe (CUP)**; el Panel muestra el gráfico por departamento y la pantalla Costos el total registrado.

**¿Cada cuánto se actualiza el directorio de personas?**
Cada vez que un administrador ejecuta la **Sincronización RRHH**. Conviene hacerlo cuando haya altas, bajas o cambios de departamento en el sistema institucional.

---

## 14. Glosario técnico

| Término | Qué significa |
| --- | --- |
| **SIM** | La tarjeta del chip que va dentro del teléfono y da la línea. |
| **ICCID** | Número único impreso en la SIM (19–20 dígitos). |
| **IMSI** | Identificador de 15 dígitos de la SIM en la red. |
| **IMEI** | Código único de 15 dígitos de cada equipo móvil (se ve con `*#06#`). |
| **Línea** | El número móvil (celular) que usa la organización. |
| **Extensión** | Número interno corto colgado de un teléfono fijo. |
| **Plan** | Paquete de servicio asociado a la operadora y a un costo mensual. |
| **CUP** | Peso cubano, la moneda en que se registran los costos. |
| **ETECSA** | La Empresa de Telecomunicaciones de Cuba (operadora única). |
| **Cargo** | El puesto que ocupa una persona (ej. "Especialista"). |
| **Área** | Área de trabajo a la que pertenece una persona o departamento. |
| **Sincronización** | Copia del directorio de RRHH (personas, cargos, áreas, unidades) hacia esta aplicación. |
| **Asignación** | Registro de "qué persona → qué recurso, desde cuándo". |
| **Período** | Mes en formato `AAAA-MM` para los costos. |
| **Estado** | Etiqueta que define la situación de un recurso (Activo, Baja, etc.). |

---

## 15. Ayuda y soporte

Si algo no funciona o querés que la aplicación haga algo nuevo (otra pantalla, otro campo, otro reporte), avisale al administrador del sistema. Los cambios se hacen en el código del proyecto con la documentación técnica que acompaña esta aplicación.