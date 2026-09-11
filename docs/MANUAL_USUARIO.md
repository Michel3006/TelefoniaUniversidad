# Manual de Usuario — Sistema de Gestión de Telefonía

Versión del documento: 1.0
Fecha: 11 de septiembre de 2026

---

## 1. ¿Qué es esta aplicación?

El **Sistema de Gestión de Telefonía** te ayuda a llevar el control de los teléfonos de tu organización en un solo lugar:

- Quién tiene cada teléfono, línea móvil, chip (SIM) o equipo asignado.
- Dónde está cada teléfono fijo (edificio, piso, oficina) y con qué extensiones cuenta.
- Los contratos y planes con sus fechas de vencimiento.
- Cuánto se gasta por mes y por departamento en telefonía.

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

Si las credenciales son incorrectas aparece un mensaje de error. Si la sesión vence (se vence a los 30 minutos de inactividad), la aplicación te pide iniciar sesión de nuevo automáticamente.

### 2.3 Cerrar sesión

Tocá el botón **Salir** en la barra superior. La próxima vez que entres tendrás que iniciar sesión otra vez.

### 2.4 Los tres tipos de usuario

| Rol | Qué puede hacer |
| --- | --- |
| **Administrador** | Todo, incluido administrar los usuarios del sistema (crearlos, cambiarlos, desactivarlos). |
| **Gestor** | Administra los recursos (personas, teléfonos, líneas, costos, etc.). |
| **Consulta** | Puede ver la información. |

Algunas opciones del menú (por ejemplo **Usuarios**) solo aparecen para el administrador.

---

## 3. La pantalla principal (Panel)

Al entrar verás una barra lateral con el **menú** y una barra superior con tu nombre y el botón **Salir**.

El **Panel** (primera pantalla) te da una foto rápida de la organización:

- **Contadores**: líneas móviles, teléfonos fijos, dispositivos, personas, edificios y locales.
- **Vencimientos próximos**: contratos que se vencen en los próximos 60 días (en rojo si faltan 15 días o menos).
- **Costes por departamento**: un gráfico de barras con lo gastado por cada departamento.

Estos datos se actualizan solos cada vez que entrás al Panel.

Barra lateral: la podés **colapsar** tocando las dobles flechas para ganar espacio.

El menú está organizado en grupos:

- **Directorio**: Personas, Departamentos, Locales.
- **Recursos**: Líneas, Teléfonos, Extensiones, Dispositivos, SIMs.
- **Contratos**: Contratos, Planes.
- **Catálogos**: Estados, Operadores.
- **Costes, Asignaciones, Historial**.
- **Administración**: Usuarios (solo admin).

---

## 4. Cómo funcionan las pantallas de listado

Todas las pantallas (salvo el Panel) funcionan igual:

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

### 4.5 Errores de formulario

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

Sirven para agrupar a las personas y después poder ver los costos por departamento.

- **Nombre**: por ejemplo "Recursos Humanos" (obligatorio).
- **Departamento padre** (opcional): si un departamento depende de otro, elegí el superior (por ejemplo "Contabilidad" dentro de "Finanzas"). Si es la raíz, dejalo vacío.

**Consejo**: cargá primero los departamentos madre y después los hijos.

### 5.3 Personas (pantalla **Personas**)

Cada persona que usa teléfonos de la organización:

- **Nombre** y **Apellido** (obligatorios).
- **Documento**: el DNI o carné, solo números (opcional).
- **Email** (opcional): debe tener formato válido (ej. `juan@gmail.com`).
- **Teléfono** (opcional): solo números, espacios y guiones.
- **Departamento** (opcional): elegí de la lista a qué departamento pertenece.

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
- **Operador**: de la lista (en Cuba, ETECSA).
- **Plan**: de la lista de planes cargados.
- **SIM**: el chip físico que usa esa línea.
- **Estado** (de la lista).

Al tocar **Ver**: vas a ver la línea con su operador, plan, chip (ICCID/IMSI), el dispositivo que la usa y la persona responsable.

**Orden recomendado**: cargá el operador y los planes antes de las líneas; y el chip (SIM) si querés asociarlo.

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
- **Operador**: de la lista.
- **Estado**.

---

## 7. Contratos y planes

### 7.1 Contratos

El contrato firmado con la empresa de telecomunicaciones.

- **Número** (obligatorio): identificador del contrato.
- **Fecha de inicio** y **Fecha de vencimiento** (opcionales). La aplicación no te deja poner un vencimiento **anterior** al inicio.
- **Descripción** (opcional).

En el Panel vas a ver los contratos que están por vencer (y en la pantalla Contratos la fecha de vencimiento con un aviso `(Xd)` cuando faltan 30 días o menos).

### 7.2 Planes

- **Nombre** (obligatorio): por ejemplo "Pospago 20GB".
- **Operador**: de la lista.
- **Contrato**: el contrato al que pertenece.
- **Coste mensual** (opcional): el costo por mes, con decimales (ej. `1200.50`).
- **Descripción** (opcional).

Los planes pueden asociarse a las líneas móviles.

---

## 8. Catálogos

### 8.1 Estados

Lista de estados para marcar los recursos (por ejemplo: "Activo", "De baja", "Pendiente"). Servís de etiqueta para saber el estado de cada teléfono, línea, chip o dispositivo.

- **Nombre** (obligatorio y único).
- **Descripción** (opcional).

**Consejo**: creá primero los estados que necesites (Activo, Baja, Pendiente) y después usalos en todos los recursos.

### 8.2 Operadores

La empresa de telecomunicaciones (en Cuba: ETECSA).

- **Nombre** (obligatorio y único).
- **Descripción** (opcional).

---

## 9. Costes: el control de gastos

Acá cargás los gastos de telefonía para llevar el control por mes.

- **Período** (obligatorio): el mes, con formato `AAAA-MM`. Ejemplo: `2026-09` es septiembre de 2026. Se valida que el mes sea válido.
- **Concepto** (obligatorio): qué gasto es (ej. "Factura móviles", "Recarga de tarjeta").
- **Monto** (obligatorio): el importe, con decimales (ej. `12500.75`).
- **Moneda** (opcional): ej. "ARS".
- **Departamento** / **Línea** / **Contrato** (opcionales): a qué imputás el gasto. Si pertenece a un departamento, tocá el botón para la vista por departamento y vas a ver el total.

La pantalla de Costes permite **filtrar por período** para ver solo un mes, y muestra el **total del filtro**.

En el **Panel** vas a ver el gráfico de costos por departamento; y hay reportes que suman por período y por operador.

---

## 10. Asignaciones: quién usa cada recurso

Este es el corazón del sistema: registrar **a qué persona** se le entrega cada línea, dispositivo o extensión.

1. Tocá **Crear**.
2. **Persona** (obligatorio): a quién se entrega.
3. **Tipo de recurso** (obligatorio): Línea, Dispositivo o Extensión. Al elegir el tipo, la lista de **Recurso** se actualiza mostrando solo recursos de ese tipo.
4. **Recurso** (obligatorio): el número/equipo específico.
5. **Fecha de inicio** (obligatorio): desde cuándo lo tiene.
6. **Fecha de fin** (opcional): si ya lo devolvió, ponelo acá.

Para registrar que una persona **devolvió** el recurso, en la fila de la asignación podés **Finalizar** (la aplicación pone la fecha de hoy automáticamente). También la podés eliminar si se cargó por error.

Los detalles de línea y teléfono muestran automáticamente el **responsable** (la persona con asignación activa más reciente).

---

## 11. Historial

Registro de auditoría de todo lo que se crea, modifica o elimina en el sistema: entidad, registro, acción, campo cambiado, valor anterior → valor nuevo, y cuándo.

- Usá el selector **Entidad** para filtrar por tipo de registro.
- Es de solo lectura: no se puede borrar desde la interfaz.

---

## 12. Administración de usuarios (solo admin)

En **Usuarios** podés crear y administrar las cuentas para que otras personas entren:

1. **Crear** un usuario: **usuario** (nombre de login), **email**, **contraseña** (mínimo 6 caracteres) y **rol** (admin/gestor/consulta).
2. Con **Editar** podés cambiar contraseña, rol y **activar/desactivar** la cuenta (un usuario inactivo no puede ingresar).
3. Con **Eliminar** borrás la cuenta.

**Recomendación**: creá cuentas individuales para cada persona en vez de compartir la de `admin`.

---

## 13. Preguntas frecuentes

**¿Puedo borrar una persona que tiene asignaciones?**
El sistema lo permite, pero queda el historial. Es preferible primero **Finalizar** sus asignaciones y después borrarla si ya no existe.

**¿Por qué no me deja escribir letras en el campo IMEI/ICCID?**
Son campos numéricos; el sistema solo acepta dígitos para evitar errores de tipeo.

**El campo "Período" me da error, ¿qué formato usa?**
`AAAA-MM`. Escribí el año con 4 dígitos, un guion y el mes con 2 dígitos (ej. `2026-09`).

**¿Qué es "CUIT" y por qué pide tantos dígitos?**
Es el número tributario de 11 dígitos con un dígito de verificación. Si lo ingresás mal, el sistema te avisa. Si la persona no tiene, podés dejarlo vacío (es opcional).

**¿Cómo sé quién tiene asignada una línea?**
Entrá a **Líneas**, tocá **Ver** en la línea; ahí figura el responsable. También podés consultar en **Asignaciones**.

**Se vence mi sesión seguido.**
El token dura 30 minutos. Si estás mucho tiempo sin usar la app, tenés que volver a ingresar.

**¿Dónde veo cuánto gasta mi entidad por mes?**
Cargá los gastos en **Costes** con su **período**; el Panel muestra el gráfico por departamento y los reportes resumen por período y operador.

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
| **CUIT/CUIL** | Número tributario de 11 dígitos. |
| **Plan** | Paquete de servicio asociado a una operadora y a un costo mensual. |
| **Asignación** | Registro de "qué persona → qué recurso, desde cuándo". |
| **Período** | Mes en formato `AAAA-MM` para los costos. |
| **Estado** | Etiqueta que define la situación de un recurso (Activo, Baja, etc.). |

---

## 15. Ayuda y soporte

Si algo no funciona o querés que la aplicación haga algo nuevo (otra pantalla, otro campo, otro reporte), avisale al administrador del sistema. Los cambios se hacen en el código del proyecto con la documentación técnica que acompaña esta aplicación.