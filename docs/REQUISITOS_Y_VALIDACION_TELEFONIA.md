# ESPECIFICACIÓN FUNCIONAL Y MATRIZ DE VALIDACIÓN
## Aplicación de Gestión Integral de Telefonía Universitaria

Este documento es la especificación funcional y checklist que debe utilizar una IA/agente de desarrollo para evaluar el proyecto completo existente. Debe probar la aplicación de extremo a extremo, comprobar qué requisitos están implementados, cuáles están incompletos, cuáles faltan y qué errores existen.

---

# 1. OBJETIVO

La aplicación debe gestionar integralmente la telefonía de una universidad cubana:

- telefonía fija;
- extensiones;
- SIM institucionales;
- dispositivos móviles;
- personas y organización;
- ubicaciones físicas;
- asignaciones;
- límites de consumo;
- consumo mensual;
- importación de PDF de ETECSA;
- autorizaciones especiales;
- historial y auditoría;
- usuarios, autenticación y permisos;
- búsquedas, filtros, estadísticas y reportes.

Debe comportarse como un sistema empresarial real, manteniendo integridad, trazabilidad, seguridad y capacidad de crecimiento.

---

# 2. REGLAS DE DOMINIO

## 2.1 Operador

El operador móvil es **ETECSA**.

No es necesario un módulo de múltiples proveedores. La interfaz no debe ofrecer CRUD innecesario de operadores/proveedores. La arquitectura puede permitir una futura ampliación.

## 2.2 Terminología: SIM

El recurso móvil debe llamarse **SIM**.

No utilizar "línea" como entidad del dominio.

La SIM representa conjuntamente el número telefónico y el recurso SIM.

Si el proyecto existente tiene `Linea` y `Sim` separadas, debe comprobarse que el modelo final no mantenga una separación innecesaria. Deben actualizarse modelos, schemas, endpoints, servicios, relaciones, migraciones, tests y documentación cuando corresponda.

## 2.3 ICCID e IMSI

ICCID e IMSI son opcionales. Una SIM debe poder registrarse sin ellos.

---

# 3. FUENTES DE INFORMACIÓN

Existen tres fuentes principales.

## 3.1 Base institucional

Puede proporcionar:

- ID de empleado;
- nombre;
- apellidos;
- CI;
- teléfono particular;
- `Exttelef`;
- unidad/departamento;
- área;
- cargo;
- centro de costo;
- estructura organizativa;
- unidad padre/nivel;
- estado de unidad;
- provincia y municipio;
- información de cargos y áreas.

La aplicación no debe pedir manualmente datos que ya pueda obtener de esta fuente.

Debe existir una estrategia clara de consulta/sincronización/integración.

## 3.2 Base propia

La aplicación debe ser responsable de la información específica de telefonía:

- teléfonos;
- extensiones;
- SIM;
- dispositivos;
- ubicaciones;
- asignaciones;
- consumo;
- límites;
- autorizaciones;
- estados;
- historial;
- auditoría;
- configuración propia.

## 3.3 PDF de ETECSA

El PDF mensual de ETECSA es la fuente del consumo y facturación del período. El usuario no debe introducir manualmente el consumo de cada número.

---

# 4. PERSONAS

Los trabajadores deben identificarse mediante la información institucional.

No duplicar innecesariamente:

- nombre;
- apellido;
- CI;
- cargo;
- departamento;
- área.

`Telefono_Particular` es el teléfono personal del trabajador y **no** una SIM institucional.

---

# 5. ORGANIZACIÓN

Debe poder relacionarse cada recurso con:

- unidad/departamento;
- área;
- cargo;
- centro de costo;
- jerarquía;
- unidad padre;
- nivel;
- estado;
- provincia;
- municipio.

Los datos provenientes de la institución no deben convertirse en información manual duplicada sin justificación.

---

# 6. TELEFONÍA FIJA

Debe permitir registrar y administrar:

- número;
- estado;
- ubicación;
- persona asignada cuando corresponda;
- información organizativa;
- observaciones;
- historial.

---

# 7. EXTENSIONES

Debe gestionar:

- número de extensión;
- estado;
- teléfono fijo asociado cuando corresponda;
- persona asignada cuando corresponda;
- observaciones;
- historial.

Debe distinguir correctamente entre teléfono físico y extensión. No asumir que toda extensión es un teléfono físico independiente.

---

# 8. UBICACIONES

Debe representar ubicaciones institucionales, como:

```text
Edificio
 └── Piso
      └── Oficina / Local
```

Debe poder manejar edificio, dirección del edificio cuando corresponda, piso, oficina/local y descripción.

La dirección personal de RRHH no es la ubicación física del recurso.

---

# 9. SIM

Cada SIM debe poder manejar:

- número telefónico;
- ICCID opcional;
- IMSI opcional;
- operador ETECSA;
- estado;
- plan cuando corresponda;
- asignación;
- dispositivo asociado cuando corresponda;
- límite de consumo cuando corresponda;
- historial;
- consumo histórico.

El número debe tener las restricciones de unicidad apropiadas.

---

# 10. DISPOSITIVOS

Debe poder gestionar:

- marca;
- modelo;
- IMEI;
- estado;
- ubicación;
- SIM asociada;
- asignación;
- observaciones;
- historial.

SIM y dispositivo son conceptos distintos.

---

# 11. ESTADOS

Los recursos deben tener estados coherentes.

Ejemplos posibles:

- activo;
- inactivo;
- disponible;
- asignado;
- dado de baja;
- bloqueado.

Los nombres definitivos pueden adaptarse al dominio, pero no deben permitirse combinaciones incoherentes.

---

# 12. ASIGNACIONES

Debe existir trazabilidad de asignaciones de:

- SIM;
- dispositivo;
- teléfono fijo;
- extensión.

Debe conocerse:

- persona;
- recurso;
- fecha de inicio;
- fecha de fin;
- historial.

Ejemplo:

```text
SIM 59921173

Empleado A
01/01/2026 → 15/05/2026

Empleado B
16/05/2026 → actual
```

No sobrescribir asignaciones históricas de forma que se pierda trazabilidad.

---

# 13. IMPORTACIÓN DEL PDF DE ETECSA

Debe existir un flujo:

```text
Usuario
 ↓
Subir PDF
 ↓
Validar
 ↓
Extraer
 ↓
Identificar período
 ↓
Extraer servicios
 ↓
Asociar con SIM
 ↓
Guardar consumo
 ↓
Evaluar límites
 ↓
Mostrar resultado
```

Debe:

1. recibir el archivo;
2. validarlo;
3. procesarlo;
4. identificar números;
5. extraer consumos;
6. identificar período;
7. asociar números con SIM;
8. guardar información;
9. conservar histórico;
10. detectar excesos;
11. registrar problemas de asociación.

---

# 14. DATOS DEL PDF

El PDF de referencia contiene información como:

- período de consumo;
- fecha de vencimiento;
- moneda;
- cuota mensual;
- consumo;
- comisión;
- impuesto;
- importe facturado;
- números/servicios;
- cuota por servicio;
- consumo por servicio;
- importe;
- consumo de voz;
- consumo SMS;
- totales.

La aplicación debe almacenar los datos que tengan utilidad para control, auditoría, cálculo, consultas y reportes.

---

# 15. ROBUSTEZ DEL PARSER

Debe soportar razonablemente:

- varias páginas;
- encabezados repetidos;
- saltos/espacios variables;
- múltiples servicios;
- consumo cero;
- registros con consumo;
- números no registrados;
- datos incompletos;
- cambios menores de formato.

No debe depender innecesariamente de posiciones exactas.

Los registros que no puedan asociarse no deben desaparecer silenciosamente. Deben quedar identificados para revisión.

---

# 16. RESULTADO DE IMPORTACIÓN

Después de importar debe poder conocerse:

- período;
- registros encontrados;
- registros asociados;
- registros no asociados;
- errores;
- resultado general.

---

# 17. DUPLICADOS

Si se procesa nuevamente el mismo PDF/período, no deben crearse consumos duplicados.

Debe existir una estrategia basada en datos como período, número/SIM y, cuando corresponda, factura/documento.

---

# 18. HISTÓRICO DE CONSUMO

Cada período debe conservarse.

Ejemplo:

```text
SIM 59921173

Julio 2026       → consumo
Agosto 2026      → consumo
Septiembre 2026  → consumo
```

Nunca sobrescribir el período anterior.

Debe poder consultarse por:

- SIM;
- persona;
- unidad;
- período.

---

# 19. LÍMITES

Debe poder configurarse un límite de consumo.

Ejemplo:

```text
SIM: 59921173
Límite: 500 CUP
Consumo: 650 CUP
Exceso: 150 CUP
```

La lógica debe existir en backend.

---

# 20. AUTORIZACIONES ESPECIALES

Debe poder registrarse una excepción para una persona/recurso autorizado a superar el límite.

Puede incluir:

- recurso;
- persona;
- límite autorizado;
- fecha inicial;
- fecha final;
- motivo;
- responsable;
- observaciones.

Una autorización vigente debe ser considerada. Una autorización vencida no debe aplicarse.

---

# 21. EVALUACIÓN DEL CONSUMO

Conceptualmente:

```text
Obtener consumo
 ↓
Obtener límite
 ↓
Comprobar autorización vigente
 ↓
Comparar
 ↓
Determinar resultado
```

Debe distinguir al menos:

- dentro del límite;
- excedido;
- excedido pero autorizado;
- sin límite;
- no asociado;
- datos insuficientes.

---

# 22. AUDITORÍA

Las operaciones importantes deben registrarse:

- creación;
- modificación;
- eliminación;
- asignación;
- desasignación;
- cambio de estado;
- importación PDF;
- cambios de límites;
- autorizaciones.

Debe conocerse:

- entidad;
- ID;
- acción;
- campo;
- valor anterior;
- valor nuevo;
- usuario;
- fecha.

---

# 23. USUARIOS Y SEGURIDAD

Debe existir autenticación y autorización mediante roles/permisos cuando corresponda.

Debe protegerse especialmente:

- administración;
- modificación;
- eliminación;
- importaciones;
- límites;
- autorizaciones;
- datos de trabajadores.

El backend debe validar permisos, no solamente el frontend.

---

# 24. VALIDACIONES

Validar como mínimo:

- números telefónicos;
- IMEI;
- ICCID;
- IMSI;
- fechas;
- estados;
- relaciones;
- archivos;
- límites;
- asignaciones;
- duplicados.

Los campos opcionales deben ser realmente opcionales.

No exponer trazas internas al usuario.

---

# 25. INTEGRIDAD

Debe evitar:

- SIM duplicadas;
- números duplicados;
- IMEI duplicados;
- asignaciones incompatibles;
- referencias inexistentes;
- períodos duplicados;
- relaciones inválidas.

Utilizar constraints, claves foráneas, índices y transacciones cuando corresponda.

---

# 26. API

La API debe tener una separación razonable:

```text
Router
 ↓
Schema
 ↓
Service / lógica de negocio
 ↓
Acceso a datos
 ↓
Base de datos
```

No concentrar toda la lógica en los endpoints.

Las respuestas y errores deben ser consistentes.

---

# 27. RENDIMIENTO

Las consultas que puedan devolver muchos registros deben tener:

- paginación;
- filtros;
- búsqueda;
- ordenamiento;
- índices apropiados.

Evitar:

- N+1 queries;
- cargar tablas completas;
- consultas repetitivas;
- procesamiento excesivo en memoria.

---

# 28. ESCALABILIDAD

Debe soportar razonablemente el crecimiento hacia:

- miles de trabajadores;
- miles de SIM;
- miles de dispositivos;
- miles de teléfonos;
- años de consumo;
- gran cantidad de historial.

No debe requerir una reescritura completa para crecer.

No introducir microservicios, Kafka, Kubernetes, CQRS, etc. sin necesidad técnica real.

Un monolito modular bien estructurado es válido.

---

# 29. PROCESAMIENTO PESADO

La importación de archivos debe poder evolucionar hacia procesamiento asíncrono si el volumen aumenta.

No es obligatorio introducir workers si actualmente no son necesarios.

---

# 30. FRONTEND

El frontend debe permitir operar realmente las funcionalidades:

- dashboard;
- personas;
- teléfonos fijos;
- extensiones;
- SIM;
- dispositivos;
- asignaciones;
- consumo;
- importaciones;
- límites;
- autorizaciones;
- historial/auditoría;
- usuarios/permisos.

La interfaz debe ser clara, responsive y utilizar Bootstrap como base si esa es la tecnología definida.

---

# 31. BÚSQUEDA Y FILTROS

Debe poder buscarse por:

- número;
- SIM;
- ICCID;
- IMSI;
- IMEI;
- persona;
- CI;
- departamento;
- área;
- estado;
- ubicación;
- período.

Los filtros deben funcionar realmente contra el backend cuando existan más registros de los cargados en pantalla.

---

# 32. DASHBOARD

Debe proporcionar indicadores útiles, por ejemplo:

- teléfonos fijos;
- extensiones;
- SIM;
- dispositivos;
- activos;
- inactivos;
- asignados;
- disponibles;
- consumo del período;
- excesos;
- excesos autorizados;
- importaciones recientes.

Las estadísticas deben calcularse eficientemente.

---

# 33. REPORTES

Debe poder obtener información sobre:

- inventario;
- recursos por persona;
- recursos por unidad;
- consumo por período;
- excesos;
- excesos autorizados;
- recursos sin asignar;
- histórico.

Si existen exportaciones, también deben probarse.

---

# 34. MANEJO DE ERRORES

No mostrar errores técnicos internos.

Incorrecto:

```text
sqlalchemy.exc.IntegrityError...
```

Correcto:

```text
No se puede registrar la SIM porque el número ya existe.
```

Los detalles técnicos deben quedar en logs.

---

# 35. CONFIGURACIÓN

Comprobar:

- secretos fuera del código;
- credenciales fuera de Git;
- `.env.example`;
- configuración por entorno;
- desarrollo y producción correctamente diferenciados.

---

# 36. MIGRACIONES

Toda modificación estructural debe tener migración.

Comprobar:

- migraciones aplicables;
- orden correcto;
- compatibilidad con datos existentes;
- modelos y BD sincronizados;
- ausencia de migraciones rotas.

Antes de eliminar `Linea` u otra entidad obsoleta, buscar todas sus referencias.

---

# 37. TESTING OBLIGATORIO

La IA debe ejecutar los tests existentes y crear/ajustar los necesarios.

## Unitarias

Probar:

- validaciones;
- límites;
- autorizaciones;
- parser;
- reglas de consumo;
- asignaciones.

## Integración

Probar:

- API;
- base de datos;
- importación;
- relaciones;
- integración institucional cuando sea posible.

## End-to-end

Probar el flujo:

```text
Persona
 ↓
Recurso
 ↓
Asignación
 ↓
PDF ETECSA
 ↓
Consumo
 ↓
Límite
 ↓
Autorización
 ↓
Resultado
 ↓
Historial
```

---

# 38. PRUEBA CON EL PDF REAL

Debe utilizarse el PDF de ETECSA proporcionado como caso de prueba real.

Debe comprobarse:

1. carga;
2. período;
3. servicios;
4. cuotas;
5. consumos;
6. importes;
7. múltiples páginas;
8. asociación con SIM;
9. números no registrados;
10. histórico;
11. comportamiento al importar nuevamente.

El PDF de referencia corresponde al período de consumo **01/07/26–31/07/26** y contiene múltiples servicios y totales de facturación.

---

# 39. CASOS LÍMITE

## SIM

- válida;
- número duplicado;
- ICCID vacío;
- IMSI vacío;
- sin dispositivo;
- sin persona;
- inactiva.

## Dispositivo

- IMEI duplicado;
- sin SIM;
- sin persona;
- inactivo.

## Asignación

- válida;
- doble asignación incompatible;
- desasignación;
- reasignación;
- histórico.

## Consumo

- cero;
- menor al límite;
- igual al límite;
- mayor al límite;
- sin límite;
- autorización vigente;
- autorización vencida.

## PDF

- válido;
- duplicado;
- incompleto;
- número no registrado;
- formato inesperado;
- varias páginas.

---

# 40. CRITERIO DE ACEPTACIÓN

Una funcionalidad no está cumplida simplemente porque exista:

- un modelo;
- un endpoint;
- una pantalla;
- código que compile.

Debe comprobarse:

```text
Modelo
 +
API
 +
Lógica de negocio
 +
Base de datos
 +
Frontend
 +
Validaciones
 +
Permisos
 +
Tests
 =
Funcionalidad realmente operativa
```

---

# 41. MATRIZ DE VALIDACIÓN

La IA debe generar una matriz:

| ID | Requisito | Implementado | Probado | Resultado | Problemas | Evidencia |
|---|---|---|---|---|---|---|
| REQ-001 | Teléfonos fijos | | | | | |
| REQ-002 | Extensiones | | | | | |
| REQ-003 | SIM | | | | | |
| REQ-004 | ICCID/IMSI opcionales | | | | | |
| REQ-005 | Dispositivos | | | | | |
| REQ-006 | Integración institucional | | | | | |
| REQ-007 | Ubicaciones | | | | | |
| REQ-008 | Asignaciones e histórico | | | | | |
| REQ-009 | PDF ETECSA | | | | | |
| REQ-010 | Histórico de consumo | | | | | |
| REQ-011 | Límites | | | | | |
| REQ-012 | Autorizaciones | | | | | |
| REQ-013 | Detección de excesos | | | | | |
| REQ-014 | Auditoría | | | | | |
| REQ-015 | Usuarios/permisos | | | | | |
| REQ-016 | Búsqueda/filtros | | | | | |
| REQ-017 | Dashboard | | | | | |
| REQ-018 | Reportes | | | | | |
| REQ-019 | Validaciones | | | | | |
| REQ-020 | Seguridad | | | | | |
| REQ-021 | Rendimiento | | | | | |
| REQ-022 | Migraciones | | | | | |
| REQ-023 | Tests | | | | | |

No marcar un requisito como cumplido solamente por inspección superficial.

Debe existir evidencia de funcionamiento.

---

# 42. REVISIÓN DE CALIDAD

Además de probar funcionalidades, revisar:

- SOLID;
- DRY;
- separación de responsabilidades;
- cohesión;
- acoplamiento;
- modelo de datos;
- N+1;
- índices;
- transacciones;
- concurrencia;
- seguridad;
- validaciones;
- logging;
- mantenibilidad;
- duplicación;
- código muerto;
- deuda técnica.

Evaluar el proyecto como si estuviera pasando un Code Review profesional.

---

# 43. REGLA CONTRA FALSOS POSITIVOS

Si algo parece implementado pero no funciona:

**NO marcarlo como cumplido.**

Si existe un endpoint pero falla:

**NO está correctamente implementado.**

Si existe una pantalla pero no persiste:

**NO está correctamente implementado.**

Si funciona con datos artificiales pero falla con el PDF real:

**NO está correctamente implementado.**

---

# 44. EVIDENCIA

Para cada requisito importante indicar, cuando sea posible:

- archivo/código involucrado;
- endpoint;
- modelo/tabla;
- prueba ejecutada;
- resultado;
- problema encontrado.

---

# 45. RESULTADO FINAL DE LA AUDITORÍA

La IA debe entregar:

## A. Resumen

- requisitos cumplidos;
- requisitos parciales;
- requisitos ausentes;
- errores críticos.

## B. Matriz de requisitos

La tabla anterior completamente rellenada.

## C. Problemas

Clasificados:

- crítico;
- alto;
- medio;
- bajo.

## D. Pruebas

Para cada prueba:

- entrada;
- resultado esperado;
- resultado obtenido;
- estado.

## E. Arquitectura

Problemas que afecten:

- escalabilidad;
- seguridad;
- mantenimiento;
- integridad.

## F. Correcciones

Plan de corrección priorizado.

---

# 46. PROCEDIMIENTO OBLIGATORIO DE LA IA

Si recibe el proyecto completo:

### Primero

1. Leer todo el proyecto.
2. Analizar backend.
3. Analizar frontend.
4. Analizar modelos.
5. Analizar migraciones.
6. Analizar endpoints.
7. Analizar configuración.
8. Analizar tests.
9. Ejecutar la aplicación.
10. Ejecutar tests.
11. Probar flujos reales.
12. Utilizar el PDF de ETECSA.
13. Comparar comportamiento con este documento.
14. Generar matriz de cumplimiento.

### Después

Si se solicita corregir:

1. corregir críticos;
2. corregir errores funcionales;
3. corregir problemas de arquitectura;
4. actualizar tests;
5. ejecutar nuevamente;
6. volver a evaluar la matriz.

---

# 47. PRINCIPIO FINAL

La pregunta no es:

> "¿Existe código para esta funcionalidad?"

La pregunta correcta es:

> **"¿La aplicación completa cumple realmente este requisito y puedo demostrarlo mediante una prueba?"**

Ese es el criterio de aceptación de este documento.
