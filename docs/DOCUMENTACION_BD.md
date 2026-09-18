# Documentación de Bases de Datos — Proyecto sigenu2ldap

> Documentación autogenerada de las entidades (tablas, columnas, claves, restricciones, índices, vistas y triggers) de las dos bases de datos que usa el proyecto.

## Contenido

- [1. Assets](#1-assets-asseartxassespersonuploadimages_rh)
- [2. Sigenu](#2-sigenu-ces)

---

## 1. Assets (`ASSETS_RH`)

**Servidor:** SQL Server `10.8.6.191` · **Base de datos:** `ASSETS_RH` · **Origen:** trabajadores (RRHH).

### Tablas

#### `Empleados_Gral`

| Columna                    | Tipo             | Null | Default | PK  | Identity |
| -------------------------- | ---------------- | ---- | ------- | --- | -------- |
| Id_Empleado                | char(15)         | No   | -       | ✅   |          |
| Id_Expediente              | char(15)         | No   | -       |     |          |
| No_CI                      | char(15)         | No   | -       |     |          |
| Nombre                     | varchar(50)      | No   | -       |     |          |
| Apellido_1                 | varchar(50)      | No   | -       |     |          |
| Direccion                  | varchar(255)     | No   | -       |     |          |
| Ciudad                     | varchar(50)      | No   | -       |     |          |
| Region                     | varchar(50)      | No   | -       |     |          |
| Codigo_Postal              | varchar(20)      | No   | -       |     |          |
| Pais                       | varchar(50)      | No   | -       |     |          |
| Exttelef                   | char(15)         | No   | -       |     |          |
| Telefono_Particular        | varchar(30)      | No   | -       |     |          |
| Id_CCosto                  | char(10)         | No   | -       |     |          |
| Fecha_Nacimiento           | smalldatetime(4) | No   | -       |     |          |
| Nota                       | varchar(255)     | No   | -       |     |          |
| Tipo_Pago                  | tinyint(1)       | No   | -       |     |          |
| Id_Tipo_Contrato           | char(3)          | No   | -       |     |          |
| Regimen_Salarial           | tinyint(1)       | No   | -       |     |          |
| Tarifa_Horaria_con_Reporte | bit(1)           | No   | -       |     |          |
| Calendario                 | char(3)          | No   | -       |     |          |
| DescontarSabado            | bit(1)           | No   | -       |     |          |
| Baja                       | bit(1)           | No   | -       |     |          |
| Alta                       | bit(1)           | No   | -       |     |          |
| Id_Cargo                   | char(5)          | No   | -       |     |          |
| Id_Categoria               | char(5)          | No   | -       |     |          |
| NGrupo                     | tinyint(1)       | No   | -       |     |          |
| Fecha_Cargo                | smalldatetime(4) | No   | -       |     |          |
| Asignacion_por_Cargo       | bit(1)           | No   | -       |     |          |
| Nivel                      | tinyint(1)       | No   | -       |     |          |
| Id_Direccion               | char(15)         | No   | -       |     |          |
| Plaza                      | bigint(8)        | No   | -       |     |          |
| Id_CausaAlta               | char(5)          | No   | -       |     |          |
| Id_FundamentacionAlta      | char(5)          | No   | -       |     |          |
| Id_CausaBaja               | char(5)          | No   | -       |     |          |
| Fecha_Baja                 | smalldatetime(4) | No   | -       |     |          |
| Dias_Descontar_Alta        | tinyint(1)       | No   | -       |     |          |
| Dias_Descontar_Mov         | tinyint(1)       | No   | -       |     |          |
| Dias_Descontar_Baja        | tinyint(1)       | No   | -       |     |          |
| Saya                       | char(5)          | No   | -       |     |          |
| Pantalon                   | char(5)          | No   | -       |     |          |
| Camisa                     | char(5)          | No   | -       |     |          |
| Zapato                     | char(5)          | No   | -       |     |          |
| Sexo                       | char(1)          | No   | -       |     |          |
| Color_Piel                 | tinyint(1)       | No   | -       |     |          |
| Color_Pelo                 | tinyint(1)       | No   | -       |     |          |
| Estatura                   | numeric(5)       | No   | -       |     |          |
| Nombre_Madre               | varchar(50)      | No   | -       |     |          |
| Nombre_Padre               | varchar(50)      | No   | -       |     |          |
| Id_Provincia               | char(5)          | No   | -       |     |          |
| Id_Municipio               | char(5)          | No   | -       |     |          |
| Id_Nivel_Escolaridad       | char(3)          | No   | -       |     |          |
| Id_Profesion               | char(5)          | No   | -       |     |          |
| Fecha_Contratacion         | smalldatetime(4) | No   | -       |     |          |
| Fecha_Terminacion_Contrato | smalldatetime(4) | No   | -       |     |          |
| Docente                    | bit(1)           | No   | -       |     |          |
| Investigador               | bit(1)           | No   | -       |     |          |
| Id_Categoria_DI            | char(5)          | No   | -       |     |          |
| AnoInicioDocencia          | int(4)           | No   | -       |     |          |
| AnoInterruptoDocencia      | int(4)           | No   | -       |     |          |
| Numero_Radicacion_Plaza    | char(50)         | No   | -       |     |          |
| Id_Ubicacion_Defensa       | char(5)          | No   | -       |     |          |
| Especificacion_Defensa     | varchar(50)      | No   | -       |     |          |
| Imprescindible             | bit(1)           | No   | -       |     |          |
| FechaMilitar               | smalldatetime(4) | No   | -       |     |          |
| OC                         | bit(1)           | No   | -       |     |          |
| Militancia                 | tinyint(1)       | No   | -       |     |          |
| RequisitoIdiomatico        | bit(1)           | No   | -       |     |          |
| RequisitoTecnico           | bit(1)           | No   | -       |     |          |
| Id_Obra                    | char(10)         | No   | -       |     |          |
| Tipo_Vacuna                | tinyint(1)       | No   | -       |     |          |
| Fecha_Vacuna               | smalldatetime(4) | No   | -       |     |          |
| Nota_Vacuna                | varchar(100)     | No   | -       |     |          |
| Nivel_CP                   | tinyint(1)       | No   | -       |     |          |
| Id_Direccion_CP            | char(15)         | No   | -       |     |          |
| Id_Cargo_CP                | char(5)          | No   | -       |     |          |
| Id_Categoria_CP            | char(5)          | No   | -       |     |          |
| NGrupo_CP                  | tinyint(1)       | No   | -       |     |          |
| Fecha_Cargo_CP             | smalldatetime(4) | No   | -       |     |          |
| Asignacion_por_Cargo_CP    | bit(1)           | No   | -       |     |          |
| Id_GrpEvaluativo           | char(7)          | No   | -       |     |          |
| Id_GrpSendRec              | char(7)          | No   | -       |     |          |
| CuadroReserva              | tinyint(1)       | No   | -       |     |          |
| ClasifCuadros              | tinyint(1)       | No   | -       |     |          |
| SituacionReserva           | tinyint(1)       | No   | -       |     |          |
| Nivel_Reserva              | tinyint(1)       | No   | -       |     |          |
| Id_Direccion_Reserva       | char(15)         | No   | -       |     |          |
| Id_Cargo_Reserva           | char(5)          | No   | -       |     |          |
| AnosServicio               | tinyint(1)       | No   | -       |     |          |
| AntiguedadDispensa         | tinyint(1)       | No   | -       |     |          |
| Situacion                  | tinyint(1)       | No   | -       |     |          |
| Id_Actividad               | char(3)          | No   | -       |     |          |
| Albergado                  | bit(1)           | No   | -       |     |          |
| Cubiculo                   | char(5)          | No   | -       |     |          |
| ModuloUniforme             | char(50)         | No   | -       |     |          |
| FechaSector                | smalldatetime(4) | No   | -       |     |          |
| FechaDireccion             | smalldatetime(4) | No   | -       |     |          |
| Mision_Civil               | bit(1)           | No   | -       |     |          |
| Mision_Militar             | bit(1)           | No   | -       |     |          |
| Ayuda_Tecnica              | bit(1)           | No   | -       |     |          |
| Microbrigada               | bit(1)           | No   | -       |     |          |
| Doble_Expediente           | bit(1)           | No   | -       |     |          |
| DisposicionCargo           | bit(1)           | No   | -       |     |          |
| Prestacion_Servicio        | bit(1)           | No   | -       |     |          |
| Fecha_Prestacion_Servicio  | smalldatetime(4) | No   | -       |     |          |
| Mision                     | tinyint(1)       | No   | -       |     |          |
| Foto                       | image(16)        | Sí   | -       |     |          |
| Id_User                    | char(15)         | No   | -       |     |          |
| Fecha_Op                   | smalldatetime(4) | No   | -       |     |          |
| Id_Subcategoria            | char(5)          | No   | -       |     |          |
| Id_Categoria_IT            | char(5)          | No   | -       |     |          |
| Id_Jornada                 | char(5)          | No   | -       |     |          |
| Id_Tarjeta_Reloj           | char(15)         | No   | -       |     |          |
| Tarjeta_Reloj_On           | bit(1)           | No   | -       |     |          |
| Designacion                | bit(1)           | No   | -       |     |          |
| Dias_Dec_Ley_91            | numeric(9)       | No   | -       |     |          |
| Dias_Dec_Ley_91_Saldo      | numeric(9)       | No   | -       |     |          |
| Horario_Regular            | bit(1)           | No   | -       |     |          |
| Apellido_2                 | varchar(50)      | No   | -       |     |          |
| Id_Grado_Cientifico        | char(5)          | No   | -       |     |          |
| Fecha_Categoria_Docente    | smalldatetime(4) | No   | -       |     |          |
| Pluriempleo                | bit(1)           | No   | -       |     |          |
| Horas_Descontar_Alta       | numeric(5)       | No   | -       |     |          |
| Horas_Descontar_Mov        | numeric(5)       | No   | -       |     |          |
| Horas_Descontar_Baja       | numeric(5)       | No   | -       |     |          |
| Id_Alta                    | int(4)           | No   | -       |     |          |
| Agrupacion_Alta            | char(5)          | No   | -       |     |          |
| Ano_Alta                   | int(4)           | No   | -       |     |          |
| Id_Baja                    | int(4)           | No   | -       |     |          |
| Agrupacion_Baja            | char(5)          | No   | -       |     |          |
| Ano_Baja                   | int(4)           | No   | -       |     |          |

**Clave primaria:** Id_Empleado

**Restricciones CHECK:**
- CK_Empleados_Gral_ClasifCuadros: None
- CK_Empleados_Gral_Color_Pelo: None
- CK_Empleados_Gral_Color_Piel: None
- CK_Empleados_Gral_CuadroReserva: None
- CK_Empleados_Gral_Militancia: None
- CK_Empleados_Gral_Regimen_Salarial: None
- CK_Empleados_Gral_Sexo: None
- CK_Empleados_Gral_Situacion: None
- CK_Empleados_Gral_SituacionReserva: None
- CK_Empleados_Gral_Tipo_Pago: None

**Índices:**
- `PK_Empleados_Gral` (CLUSTERED) [unique,PRIMARY]
- `IX_Empleados_Gral` (NONCLUSTERED) [unique]

---

#### `Errores_Recibo`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Refer | varchar(50) | No | - |  |  |
| Error | varchar(255) | No | - |  |  |

---

#### `Factura_Def`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador1 | int(4) | No | - |  | ✅ |
| Id_Factura | int(4) | No | - |  |  |
| Referencia | varchar(15) | No | - |  |  |
| AplicaArancel | bit(1) | No | - |  |  |
| PrecioMB | numeric(13) | No | - |  |  |
| PrecioMC | numeric(13) | No | - |  |  |
| RecMB | money(8) | No | - |  |  |
| RecMC | money(8) | No | - |  |  |
| DescMB | money(8) | No | - |  |  |
| DescMC | money(8) | No | - |  |  |
| ImporteMB | money(8) | No | - |  |  |
| ImporteMC | money(8) | No | - |  |  |
| Devuelto | money(8) | No | - |  |  |
| AplicaPlazoCobro | bit(1) | No | - |  |  |
| Tributable | bit(1) | No | - |  |  |
| ImporDevueltoMB | numeric(13) | No | - |  |  |
| ImporDevueltoMC | numeric(13) | No | - |  |  |

---

#### `FzImport_Cmd`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador9 | int(4) | No | - | ✅ | ✅ |
| mTable | varchar(80) | No | - |  |  |
| hasTrigger | bit(1) | No | - |  |  |
| mCmd | varchar(4000) | No | - |  |  |
| mRows | int(4) | No | - |  |  |
| mMsg | nvarchar(900) | No | - |  |  |

**Clave primaria:** Contador9

**Índices:**
- `PK_FzImport_Cmd` (CLUSTERED) [unique,PRIMARY]
- `IX_FzImport_Cmd` (NONCLUSTERED)

---

#### `FzImport_Data`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador9 | int(4) | No | - |  | ✅ |
| mTable | varchar(80) | No | - |  |  |
| Importar | bit(1) | No | - |  |  |
| Limpiar | bit(1) | No | - |  |  |

**Índices:**
- `IX_FzImport_Data` (NONCLUSTERED)

---

#### `FzImport_SDBTables`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | int(4) | No | - |  | ✅ |
| STable | varchar(80) | No | - |  |  |

---

#### `FzImport_Source`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id | int(4) | No | - |  | ✅ |
| nTable | varchar(80) | No | - |  |  |
| hasTrigger | bit(1) | No | - |  |  |
| ordeni | int(4) | Sí | - |  |  |
| ordend | int(4) | Sí | - |  |  |
| usedel | bit(1) | Sí | - |  |  |

---

#### `FzImport_Source_Tables`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador9 | int(4) | No | - |  | ✅ |
| STable | varchar(80) | No | - |  |  |

**Índices:**
- `IX_FzImport_Source_Tables` (NONCLUSTERED)

---

#### `FzImport_Target`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id | int(4) | No | - |  | ✅ |
| nTable | varchar(80) | No | - |  |  |
| hasTrigger | bit(1) | No | - |  |  |

---

#### `InfoCorporativa_RRHH_Xml`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id | uniqueidentifier(16) | No | - | ✅ |  |
| CodAgrupa | char(5) | No | - |  |  |
| DesAgrupa | varchar(50) | No | - |  |  |
| Ano | int(4) | No | - |  |  |
| Mes | int(4) | No | - |  |  |
| TipoInfo | int(4) | No | - |  |  |
| Id_Clasificacion | char(10) | No | - |  |  |
| Desc_Clasificacion | varchar(120) | No | - |  |  |
| Indicador1 | int(4) | No | - |  |  |
| Indicador2 | int(4) | No | - |  |  |
| Indicador3 | int(4) | No | - |  |  |
| Indicador4 | int(4) | No | - |  |  |
| Indicador5 | int(4) | No | - |  |  |
| Indicador6 | int(4) | No | - |  |  |
| Indicador7 | money(8) | No | - |  |  |
| Indicador8 | money(8) | No | - |  |  |

**Clave primaria:** Id

**Índices:**
- `PK_InfoCorporativa_RRHH_Xml` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Actividades`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Actividad | char(3) | No | - | ✅ |  |
| Desc_Actividad | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Actividad

**Índices:**
- `PK_RH_Actividades` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Actividades_Normadas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Actividad | char(15) | No | - | ✅ |  |
| Desc_Actividad | varchar(100) | No | - |  |  |
| UM | char(10) | No | - |  |  |
| Tasa | numeric(9) | No | - |  |  |
| Tipo_Norma | char(1) | No | - |  |  |
| Norma_Tiempo | numeric(9) | No | - |  |  |

**Clave primaria:** Id_Actividad

**Restricciones CHECK:**
- RH_Actividades_Normadas_Tipo_Norma_Values: None

**Índices:**
- `PK_RH_Actividades_Normadas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_AjustesCSS`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Saldo | money(8) | No | - |  |  |
| Ajuste | money(8) | No | - |  |  |
| Observaciones | varchar(100) | No | - |  |  |
| ProcesarAjuste | bit(1) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_AjustesCSS` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_AjustesIIP`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Saldo | money(8) | No | - |  |  |
| Ajuste | money(8) | No | - |  |  |
| Observaciones | varchar(100) | No | - |  |  |
| ProcesarAjuste | bit(1) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_AjustesIIP` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_AjustesSubmayorRetenciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Deduccion | char(5) | No | - |  |  |
| Desc_Deduccion | varchar(50) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |
| Saldo | money(8) | No | - |  |  |
| Ajuste | money(8) | No | - |  |  |
| Observaciones | varchar(100) | No | - |  |  |
| ProcesarAjuste | bit(1) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |
| Valor_Deduccion1 | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_AjustesSubmayorRetenciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_AjustesSubmayorSubsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| SaldoFin | money(8) | No | - |  |  |
| Ajuste | money(8) | No | - |  |  |
| Observaciones | varchar(100) | No | - |  |  |
| ProcesarAjuste | bit(1) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_AjustesSubmayorSubsidios` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_AjustesSubmayorVacaciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| SaldoDias | numeric(5) | No | - |  |  |
| SaldoImporte | money(8) | No | - |  |  |
| AjusteDias | numeric(5) | No | - |  |  |
| AjusteImporte | money(8) | No | - |  |  |
| Observaciones | varchar(100) | No | - |  |  |
| ProcesarAjuste | bit(1) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |
| SaldoPuntos | money(8) | No | - |  |  |
| AjustePuntos | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_AjustesSubmayorVacaciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_AjustesTarjetaSNC_225`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| AnoAjustar | smallint(2) | No | - |  |  |
| MesAjustar | tinyint(1) | No | - |  |  |
| Dias | numeric(5) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Claves | char(6) | No | - |  |  |
| AjusteDias | numeric(5) | No | - |  |  |
| AjusteImporte | money(8) | No | - |  |  |
| AjusteClaves | char(6) | No | - |  |  |
| Observaciones | varchar(100) | No | - |  |  |
| ProcesarAjuste | bit(1) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_AjustesTarjetaSNC_225` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Area_Trabajo_Actual`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Area | char(3) | No | - | ✅ |  |
| Desc_Area | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Area

**Índices:**
- `PK_RH_Area_Trabajo_Actual` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Bank_Dbf_Merge`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| File_Path | varchar(255) | No | - |  |  |
| File_Name | char(25) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |

---

#### `RH_Bank_Dbf_Merge_Tmp`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| item | int(4) | No | - |  | ✅ |
| num_ideper | nchar(30) | No | - |  |  |
| cta | nchar(32) | No | - |  |  |
| importe | money(8) | No | - |  |  |

---

#### `RH_CSS_IIP_Saldos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| CSS_Saldo | money(8) | No | - |  |  |
| IIP_Saldo | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_CSS_IIP_Saldos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Calendarios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Calendario | char(3) | No | - | ✅ |  |
| Contador | int(4) | No | - |  | ✅ |
| FeriadosMes | tinyint(1) | No | - |  |  |
| Feriados1raQ | tinyint(1) | No | - |  |  |
| Feriados2daQ | tinyint(1) | No | - |  |  |
| DiasFondoJornaleros1Q | tinyint(1) | No | - |  |  |
| DiasFondoJornaleros2Q | tinyint(1) | No | - |  |  |
| Domingos | tinyint(1) | No | - |  |  |
| D1 | bit(1) | No | - |  |  |
| D2 | bit(1) | No | - |  |  |
| D3 | bit(1) | No | - |  |  |
| D4 | bit(1) | No | - |  |  |
| D5 | bit(1) | No | - |  |  |
| D6 | bit(1) | No | - |  |  |
| D7 | bit(1) | No | - |  |  |
| D8 | bit(1) | No | - |  |  |
| D9 | bit(1) | No | - |  |  |
| D10 | bit(1) | No | - |  |  |
| D11 | bit(1) | No | - |  |  |
| D12 | bit(1) | No | - |  |  |
| D13 | bit(1) | No | - |  |  |
| D14 | bit(1) | No | - |  |  |
| D15 | bit(1) | No | - |  |  |
| D16 | bit(1) | No | - |  |  |
| D17 | bit(1) | No | - |  |  |
| D18 | bit(1) | No | - |  |  |
| D19 | bit(1) | No | - |  |  |
| D20 | bit(1) | No | - |  |  |
| D21 | bit(1) | No | - |  |  |
| D22 | bit(1) | No | - |  |  |
| D23 | bit(1) | No | - |  |  |
| D24 | bit(1) | No | - |  |  |
| D25 | bit(1) | No | - |  |  |
| D26 | bit(1) | No | - |  |  |
| D27 | bit(1) | No | - |  |  |
| D28 | bit(1) | No | - |  |  |
| D29 | bit(1) | No | - |  |  |
| D30 | bit(1) | No | - |  |  |
| D31 | bit(1) | No | - |  |  |
| DiasComedor | tinyint(1) | No | - |  |  |
| FondoTiempoMes | numeric(5) | No | - |  |  |
| FondoTiempo1Q | numeric(5) | No | - |  |  |
| FondoTiempo2Q | numeric(5) | No | - |  |  |
| Hrs1 | numeric(5) | No | - |  |  |
| Hrs2 | numeric(5) | No | - |  |  |
| Hrs3 | numeric(5) | No | - |  |  |
| Hrs4 | numeric(5) | No | - |  |  |
| Hrs5 | numeric(5) | No | - |  |  |
| Hrs6 | numeric(5) | No | - |  |  |
| Hrs7 | numeric(5) | No | - |  |  |
| Hrs8 | numeric(5) | No | - |  |  |
| Hrs9 | numeric(5) | No | - |  |  |
| Hrs10 | numeric(5) | No | - |  |  |
| Hrs11 | numeric(5) | No | - |  |  |
| Hrs12 | numeric(5) | No | - |  |  |
| Hrs13 | numeric(5) | No | - |  |  |
| Hrs14 | numeric(5) | No | - |  |  |
| Hrs15 | numeric(5) | No | - |  |  |
| Hrs16 | numeric(5) | No | - |  |  |
| Hrs17 | numeric(5) | No | - |  |  |
| Hrs18 | numeric(5) | No | - |  |  |
| Hrs19 | numeric(5) | No | - |  |  |
| Hrs20 | numeric(5) | No | - |  |  |
| Hrs21 | numeric(5) | No | - |  |  |
| Hrs22 | numeric(5) | No | - |  |  |
| Hrs23 | numeric(5) | No | - |  |  |
| Hrs24 | numeric(5) | No | - |  |  |
| Hrs25 | numeric(5) | No | - |  |  |
| Hrs26 | numeric(5) | No | - |  |  |
| Hrs27 | numeric(5) | No | - |  |  |
| Hrs28 | numeric(5) | No | - |  |  |
| Hrs29 | numeric(5) | No | - |  |  |
| Hrs30 | numeric(5) | No | - |  |  |
| Hrs31 | numeric(5) | No | - |  |  |

**Clave primaria:** Ano, Mes, Calendario

**Restricciones CHECK:**
- CK_RH_Calendarios_Mes: None

**Índices:**
- `PK_RH_Calendarios` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Calendarios_Feriados`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Dia | tinyint(1) | No | - |  |  |
| Laborable | bit(1) | No | - |  |  |

---

#### `RH_Calendarios_Inicio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Calendario | char(3) | No | - | ✅ |  |
| Dias_Laborables | tinyint(1) | No | - |  |  |
| DiasFondoJornaleros1Q | tinyint(1) | No | - |  |  |
| DiasFondoJornaleros2Q | tinyint(1) | No | - |  |  |
| FondoTiempoMes | numeric(5) | No | - |  |  |
| FondoTiempo1Q | numeric(5) | No | - |  |  |
| FondoTiempo2Q | numeric(5) | No | - |  |  |

**Clave primaria:** Calendario

**Índices:**
- `PK_RH_Calendarios_Inicio` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Calendarios_Irregulares_Det`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Id_Jornada | char(5) | No | - | ✅ |  |
| IniDia | tinyint(1) | No | - | ✅ |  |
| IniHora | smalldatetime(4) | No | - |  |  |
| FinDia | tinyint(1) | No | - |  |  |
| FinHora | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Id_Jornada, IniDia

**Índices:**
- `PK_RH_Calendarios_Irregulares_Det` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Calendarios_Irregulares_Gen`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Id_Jornada | char(5) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Id_Jornada

**Índices:**
- `PK_RH_Calendarios_Irregulares_Gen` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Calendarios_Tipos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Calendario | char(3) | No | - | ✅ |  |
| Desc_Calendario | varchar(25) | No | - |  |  |
| Dias_Laborables | tinyint(1) | No | - |  |  |
| FondoTiempoMes | numeric(5) | No | - |  |  |
| FondoTiempoDia | numeric(5) | No | - |  |  |

**Clave primaria:** Calendario

**Índices:**
- `PK_RH_Calendarios_Tipos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Capacitacion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Curso | char(10) | No | - | ✅ |  |
| Desc_Curso | varchar(80) | No | - |  |  |

**Clave primaria:** Id_Curso

**Índices:**
- `PK_RH_Capacitacion` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Cargos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Cargo | char(5) | No | - | ✅ |  |
| Desc_Cargo | varchar(120) | No | - |  |  |
| RGrupo | char(9) | No | - |  |  |
| NGrupo | char(3) | No | - |  |  |
| Id_Categoria | char(5) | No | - |  |  |
| Desc_Categoria | varchar(25) | No | - |  |  |
| Id_Subcategoria | char(5) | No | - |  |  |
| Desc_Subcategoria | varchar(50) | No | - |  |  |
| Resolucion | char(20) | No | - |  |  |
| Clasificacion | char(1) | No | - |  |  |
| Porciento_Simultaneidad | numeric(9) | No | - |  |  |
| Funcionario | bit(1) | No | - |  |  |
| Ejecutivo | bit(1) | No | - |  |  |
| Apoyo | bit(1) | No | - |  |  |
| ReportFlag | bit(1) | No | - |  |  |
| Coeficiente_Multioficio | numeric(9) | No | - |  |  |
| Coeficente_Empresa_Empleadora | numeric(5) | No | - |  |  |
| MSCodGrupo | char(3) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Salario_Cargo | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| IETerritorial | numeric(5) | No | - |  |  |
| ETSector | numeric(5) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| Id_Clasif_P2 | char(3) | No | - |  |  |

**Clave primaria:** Id_Cargo

**Restricciones CHECK:**
- RH_Cargos_Clasificacion_Values: None

**Índices:**
- `PK_RH_Cargos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Cargos_RMPH`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Cargo | char(5) | No | - | ✅ |  |
| Desc_Cargo | varchar(120) | No | - |  |  |
| Requisitos | varchar(MAX) | No | - |  |  |
| Medidas_Proteccion_Higiene | varchar(MAX) | No | - |  |  |

**Clave primaria:** Id_Cargo

**Índices:**
- `PK_RH_Cargos_RMPH` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Categorias_Docente_Invest`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Categoria_DI | char(5) | No | - | ✅ |  |
| Desc_Categoria_DI | varchar(50) | No | - |  |  |
| Identificacion_DI | char(2) | No | - |  |  |
| Clasificacion_DI | char(1) | No | - |  |  |
| Anos_DI | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_Categoria_DI

**Restricciones CHECK:**
- RH_Categorias_Docente_Invest_Clasificacion_Values: None

**Índices:**
- `PK_RH_Categorias_Docente_Invest` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Categorias_Ocupacionales`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Categoria | char(5) | No | - | ✅ |  |
| Desc_Categoria | varchar(25) | No | - |  |  |
| Identificacion | char(2) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| CUCPromIndex | money(8) | No | - |  |  |
| Lim_Salario_Estimular | bit(1) | No | - |  |  |

**Clave primaria:** Id_Categoria

**Restricciones CHECK:**
- RH_Categorias_Ocupacionales_Clasificacion_Values: None

**Índices:**
- `PK_RH_Categorias_Ocupacionales` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Causas_Altas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_CausaAlta | char(5) | No | - | ✅ |  |
| Desc_CausaAlta | varchar(50) | No | - |  |  |
| Desc_Rpt | char(10) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_CausaAlta

**Índices:**
- `PK_RH_Causas_Altas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Causas_Bajas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_CausaBaja | char(5) | No | - | ✅ |  |
| Desc_CausaBaja | varchar(50) | No | - |  |  |
| Desc_Rpt | char(10) | No | - |  |  |
| Fluctuacion | bit(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_CausaBaja

**Índices:**
- `PK_RH_Causas_Bajas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Causas_Movimientos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_CausaMov | char(5) | No | - | ✅ |  |
| Desc_CausaMov | varchar(50) | No | - |  |  |

**Clave primaria:** Id_CausaMov

**Índices:**
- `PK_RH_Causas_Movimientos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Cedulas_Movimientos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Mov | int(4) | No | - | ✅ |  |
| Agrupacion | char(5) | No | - | ✅ |  |
| Ano_Mov | int(4) | No | - | ✅ |  |
| No_CIOld | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| No_CINew | char(15) | No | - |  |  |
| Nota | varchar(100) | No | - |  |  |
| Fecha_Mov | smalldatetime(4) | No | - |  |  |
| Fecha_Efectivo | smalldatetime(4) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Id_User | nchar(30) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Id_Mov, Agrupacion, Ano_Mov

**Índices:**
- `PK_RH_Cedulas_Movimientos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Clasificacion_Nominillas_MS`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Clasif_Nominilla | tinyint(1) | No | - | ✅ |  |
| Desc_Clasif_Nominilla | char(30) | No | - |  |  |
| MS | bit(1) | No | - |  |  |
| Aplicar | bit(1) | No | - |  |  |
| Vac | bit(1) | No | - |  |  |
| Acum_Vac_Dia | bit(1) | No | - |  |  |
| Acum_Vac_Imp | bit(1) | No | - |  |  |
| Perfeccionamiento | bit(1) | No | - |  |  |
| SNC_225 | bit(1) | No | - |  |  |
| IIP | bit(1) | No | - |  |  |

**Clave primaria:** Id_Clasif_Nominilla

**Índices:**
- `PK_RH_Clasificacion_Nominillas_MS` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Clasificacion_P2`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Clasif_P2 | char(3) | No | - | ✅ |  |
| Desc_Clasif_P2 | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Clasif_P2

**Índices:**
- `PK_RH_Clasificacion_P2` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Claves_Ausencias`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Clave | char(5) | No | - | ✅ |  |
| Desc_Clave | varchar(50) | No | - |  |  |
| Deducible | bit(1) | No | - |  |  |
| Porciento | numeric(5) | No | - |  |  |
| A_pagar_por | tinyint(1) | No | - |  |  |
| Afecta_Subsidio | bit(1) | No | - |  |  |
| Afecta_Vacaciones | bit(1) | No | - |  |  |
| Afecta_Vacaciones_Imp | bit(1) | No | - |  |  |
| Afecta_SNC_225 | bit(1) | No | - |  |  |
| Afecta_SNC_225_Imp | bit(1) | No | - |  |  |
| Afecta_Evaluacion_Tecnicos | bit(1) | No | - |  |  |
| Afecta_Estimulo | bit(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Suma_Reporte_Ausencia | bit(1) | No | - |  |  |
| Id_Clave_Externa | char(5) | No | - |  |  |
| Desc_Clave_Externa | varchar(100) | No | - |  |  |
| AfectaPromTrabajTot | bit(1) | No | - |  |  |
| CodFondodeTiempo | tinyint(1) | No | - |  |  |
| Prenomina_Hrs | bit(1) | No | - |  |  |

**Clave primaria:** Id_Clave

**Restricciones CHECK:**
- RH_Claves_Ausencias_Clasificacion_Values: None
- RH_Claves_Ausencias_A_pagar_por_Values: None
- RH_Claves_Ausencias_CodFondodeTiempo_Values: None

**Índices:**
- `PK_RH_Claves_Ausencias` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Claves_Impuntualidades`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Clave | char(5) | No | - | ✅ |  |
| Desc_Clave | varchar(50) | No | - |  |  |
| Justificada | bit(1) | No | - |  |  |

**Clave primaria:** Id_Clave

**Índices:**
- `PK_RH_Claves_Impuntualidades` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Claves_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Clave | char(5) | No | - | ✅ |  |
| Desc_Clave | varchar(50) | No | - |  |  |
| Porciento | numeric(5) | No | - |  |  |
| Carencia | bit(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Id_Clave_Ausencia | char(5) | No | - |  |  |
| SNC_225 | bit(1) | No | - |  |  |

**Clave primaria:** Id_Clave

**Restricciones CHECK:**
- RH_Claves_Subsidios_Clasificacion_Values: None

**Índices:**
- `PK_RH_Claves_Subsidios` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Claves_Tarjeta`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Vacaciones | char(1) | No | - |  |  |
| VacacionesAdelantadas | char(1) | No | - |  |  |
| Condiciones_Laborales_Anormales | char(1) | No | - |  |  |
| Cambio_de_Salario | char(1) | No | - |  |  |
| Trabajadores_de_Estipendio | char(1) | No | - |  |  |
| Interrupcion_Laboral | char(1) | No | - |  |  |
| Rehabilitacion_o_Pension | char(1) | No | - |  |  |
| Suspension_Laboral | char(1) | No | - |  |  |
| Maternidad | char(1) | No | - |  |  |
| Prestacion_Social | char(1) | No | - |  |  |
| Trabajador_Movilizado | char(1) | No | - |  |  |
| Primas | char(1) | No | - |  |  |
| Pago_por_Rendimiento | char(1) | No | - |  |  |
| Subsidio | char(1) | No | - |  |  |
| Horas_Extra | char(1) | No | - |  |  |
| Doble_Turno | char(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Estimulacion | char(1) | No | - |  |  |
| Medidas_Salariales | char(1) | No | - |  |  |
| Albergamiento | char(1) | No | - |  |  |
| Idoneidad | char(1) | No | - |  |  |
| IET | char(1) | No | - |  |  |
| ETS | char(1) | No | - |  |  |
| Retribucion_Complementaria | char(1) | No | - |  |  |

---

#### `RH_Colectivos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Colectivo | char(5) | No | - | ✅ |  |
| Desc_Colectivo | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Colectivo

**Índices:**
- `PK_RH_Colectivos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Comprobante`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador1 | int(4) | No | - |  | ✅ |
| Id_compro | int(4) | No | - |  |  |
| Ano_Compro | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Comp | char(15) | No | - |  |  |
| Hecho_Por | varchar(60) | No | - |  |  |
| Revisado_Por | varchar(60) | No | - |  |  |
| Observaciones | varchar(370) | No | - |  |  |
| Visto_Bueno | bit(1) | No | - |  |  |
| Mayorizado | bit(1) | No | - |  |  |
| Fecha | smalldatetime(4) | No | - |  |  |
| Modificado | char(1) | No | - |  |  |
| Cuadrado | char(2) | No | - |  |  |
| Incompleto | bit(1) | No | - |  |  |
| Id_ComproRef | int(4) | No | - |  |  |
| AnoRef | smallint(2) | No | - |  |  |
| MesRef | tinyint(1) | No | - |  |  |
| Id_AgrupacionRef | char(5) | No | - |  |  |
| Id_Agrupacion | char(5) | No | - |  |  |
| Xtrans | bit(1) | No | - |  |  |
| Anulado | bit(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Clave_Tipo_Comprobante | tinyint(1) | No | - |  |  |
| Notas | varchar(370) | No | - |  |  |

---

#### `RH_Comprobante_Export`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador1 | int(4) | No | - | ✅ |  |
| Id_compro | int(4) | No | - |  |  |
| Ano_Compro | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Hecho_Por | varchar(60) | No | - |  |  |
| Revisado_Por | varchar(60) | No | - |  |  |
| Observaciones | varchar(370) | No | - |  |  |
| Fecha | smalldatetime(4) | No | - |  |  |
| Clave_Tipo_Comprobante | tinyint(1) | No | - |  |  |
| Exportar | bit(1) | No | - |  |  |

**Clave primaria:** Contador1

**Índices:**
- `PK_RH_Comprobante_Export` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Contratos_Tipos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Tipo_Contrato | char(3) | No | - | ✅ |  |
| Desc_Tipo_Contrato | varchar(25) | No | - |  |  |
| Plantilla | bit(1) | No | - |  |  |
| LiquidarVacaciones | bit(1) | No | - |  |  |
| MSPagoMS | bit(1) | No | - |  |  |
| MSEstim | bit(1) | No | - |  |  |
| MSEstimEcon | bit(1) | No | - |  |  |
| Identificacion | char(2) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Grupo_Contable_Tipo_Contrato | tinyint(1) | No | - |  |  |
| NoPagoFinContrato | bit(1) | No | - |  |  |

**Clave primaria:** Id_Tipo_Contrato

**Índices:**
- `PK_RH_Contratos_Tipos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Control`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Agrupacion | varchar(5) | No | - | ✅ |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Movimiento | int(4) | No | - |  |  |
| Cedula | int(4) | No | - |  |  |
| Alta | int(4) | No | - |  |  |
| Baja | int(4) | No | - |  |  |

**Clave primaria:** Agrupacion, Ano

**Índices:**
- `PK_RH_Control` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Conversion_Plazas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NoConversion | bigint(8) | No | - |  | ✅ |
| Fecha_Aprobada | smalldatetime(4) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Desc_Direccion | varchar(100) | No | - |  |  |
| Id_CargoOld | char(5) | No | - |  |  |
| Desc_CargoOld | varchar(120) | No | - |  |  |
| Plaza | bigint(8) | No | - |  |  |
| Vacante | bit(1) | No | - |  |  |
| Id_CargoNew | char(5) | No | - |  |  |
| Desc_CargoNew | varchar(120) | No | - |  |  |
| Desc_Categoria | varchar(25) | No | - |  |  |
| Desc_Subcategoria | varchar(50) | No | - |  |  |
| RGrupo | char(5) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

---

#### `RH_Cuadre_SubM`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador1 | int(4) | No | - | ✅ | ✅ |
| Cta | varchar(20) | No | - |  |  |
| De_MB | bit(1) | No | - |  |  |
| SubCta | varchar(20) | No | - |  |  |
| Analisis | varchar(20) | No | - |  |  |
| SubAnalisis | varchar(20) | No | - |  |  |
| Epigrafe | varchar(20) | No | - |  |  |
| Partida | varchar(20) | No | - |  |  |
| Calcular | bit(1) | No | - |  |  |
| Id_Clasificacion | char(10) | No | - |  |  |

**Clave primaria:** Contador1

**Índices:**
- `PK_RH_Cuadre_SubM` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Deducciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Deduccion | char(5) | No | - | ✅ |  |
| Desc_Deduccion | varchar(50) | No | - |  |  |
| Grupo | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_Deduccion

**Restricciones CHECK:**
- RH_Deducciones_Grupo_Values: None

**Índices:**
- `PK_RH_Deducciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_DescuentosMasivos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NoDescuento | bigint(8) | No | - | ✅ | ✅ |
| Fecha_Aprobada | smalldatetime(4) | No | - |  |  |
| Criterio | tinyint(1) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Incluir_Niv_Hijos | bit(1) | No | - |  |  |
| Id_UOoCC | char(15) | No | - |  |  |
| Desc_UOoCC | varchar(120) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** NoDescuento

**Restricciones CHECK:**
- CK_RH_DescuentosMasivos_Descuento: None
- CK_RH_DescuentosMasivos_Criterio: None
- CK_RH_DescuentosMasivos_Nivel: None

**Índices:**
- `PK_RH_DescuentosMasivos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_DesglosePagoEfectivoBanco`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - |  |  |
| ACobrar | money(8) | No | - |  |  |
| Disponible | money(8) | No | - |  |  |
| CantBilletes1000 | int(4) | No | - |  |  |
| CantBilletes500 | int(4) | No | - |  |  |
| CantBilletes200 | int(4) | No | - |  |  |
| CantBilletes100 | int(4) | No | - |  |  |
| CantBilletes50 | int(4) | No | - |  |  |
| CantBilletes20 | int(4) | No | - |  |  |
| CantBilletes10 | int(4) | No | - |  |  |
| CantBilletes5 | int(4) | No | - |  |  |
| CantBilletes3 | int(4) | No | - |  |  |
| CantBilletes1 | int(4) | No | - |  |  |
| CantMonedas5Pesos | int(4) | No | - |  |  |
| CantMonedas3Pesos | int(4) | No | - |  |  |
| CantMonedas1Peso | int(4) | No | - |  |  |
| CantMonedas20Centavos | int(4) | No | - |  |  |
| CantMonedas5Centavos | int(4) | No | - |  |  |
| CantMonedas2Centavos | int(4) | No | - |  |  |
| CantMonedas1Centavo | int(4) | No | - |  |  |

---

#### `RH_DesglosePagoEfectivoBancoPorcientos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| TipoNomina | tinyint(1) | No | - |  |  |
| BaseCalculoDist | tinyint(1) | No | - |  |  |
| BaseCalculoDistLastCalc | tinyint(1) | No | - |  |  |
| BaseCalculoReDist | tinyint(1) | No | - |  |  |
| BaseCalculoReDistLastCalc | tinyint(1) | No | - |  |  |
| TipoInforme | tinyint(1) | No | - |  |  |
| TotalACobrar | money(8) | No | - |  |  |
| PorcBilletes1000 | int(4) | No | - |  |  |
| PorcBilletes500 | int(4) | No | - |  |  |
| PorcBilletes200 | int(4) | No | - |  |  |
| PorcBilletes100 | int(4) | No | - |  |  |
| PorcBilletes50 | int(4) | No | - |  |  |
| PorcBilletes20 | int(4) | No | - |  |  |
| PorcBilletes10 | int(4) | No | - |  |  |
| PorcBilletes5 | int(4) | No | - |  |  |
| PorcBilletes3 | int(4) | No | - |  |  |
| PorcBilletes1 | int(4) | No | - |  |  |
| PorcMonedas5Pesos | int(4) | No | - |  |  |
| PorcMonedas3Pesos | int(4) | No | - |  |  |
| PorcMonedas1Peso | int(4) | No | - |  |  |
| Billetes1000 | bit(1) | No | - |  |  |
| Billetes500 | bit(1) | No | - |  |  |
| Billetes200 | bit(1) | No | - |  |  |
| Billetes100 | bit(1) | No | - |  |  |
| Billetes50 | bit(1) | No | - |  |  |
| Billetes20 | bit(1) | No | - |  |  |
| Billetes10 | bit(1) | No | - |  |  |
| Billetes5 | bit(1) | No | - |  |  |
| Billetes3 | bit(1) | No | - |  |  |
| Billetes1 | bit(1) | No | - |  |  |
| Monedas5Pesos | bit(1) | No | - |  |  |
| Monedas3Pesos | bit(1) | No | - |  |  |
| Monedas1Peso | bit(1) | No | - |  |  |
| CB1000 | int(4) | No | - |  |  |
| CB500 | int(4) | No | - |  |  |
| CB200 | int(4) | No | - |  |  |
| CB100 | int(4) | No | - |  |  |
| CB50 | int(4) | No | - |  |  |
| CB20 | int(4) | No | - |  |  |
| CB10 | int(4) | No | - |  |  |
| CB5 | int(4) | No | - |  |  |
| CB3 | int(4) | No | - |  |  |
| CB1 | int(4) | No | - |  |  |
| CM5P | int(4) | No | - |  |  |
| CM3P | int(4) | No | - |  |  |
| CM1P | int(4) | No | - |  |  |
| CM20C | int(4) | No | - |  |  |
| CM5C | int(4) | No | - |  |  |
| CM2C | int(4) | No | - |  |  |
| CM1C | int(4) | No | - |  |  |
| BB1000 | int(4) | No | - |  |  |
| BB500 | int(4) | No | - |  |  |
| BB200 | int(4) | No | - |  |  |
| BB100 | int(4) | No | - |  |  |
| BB50 | int(4) | No | - |  |  |
| BB20 | int(4) | No | - |  |  |
| BB10 | int(4) | No | - |  |  |
| BB5 | int(4) | No | - |  |  |
| BB3 | int(4) | No | - |  |  |
| BB1 | int(4) | No | - |  |  |
| BM5P | int(4) | No | - |  |  |
| BM3P | int(4) | No | - |  |  |
| BM1P | int(4) | No | - |  |  |
| BM20C | int(4) | No | - |  |  |
| BM5C | int(4) | No | - |  |  |
| BM2C | int(4) | No | - |  |  |
| BM1C | int(4) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

---

#### `RH_DesglosePagoEfectivoBancoRD`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| ACobrar | money(8) | No | - |  |  |
| ACobrarDesglosado | money(8) | No | - |  |  |
| CantBilletes1000 | int(4) | No | - |  |  |
| CantBilletes500 | int(4) | No | - |  |  |
| CantBilletes200 | int(4) | No | - |  |  |
| CantBilletes100 | int(4) | No | - |  |  |
| CantBilletes50 | int(4) | No | - |  |  |
| CantBilletes20 | int(4) | No | - |  |  |
| CantBilletes10 | int(4) | No | - |  |  |
| CantBilletes5 | int(4) | No | - |  |  |
| CantBilletes3 | int(4) | No | - |  |  |
| CantBilletes1 | int(4) | No | - |  |  |
| CantMonedas5Pesos | int(4) | No | - |  |  |
| CantMonedas3Pesos | int(4) | No | - |  |  |
| CantMonedas1Peso | int(4) | No | - |  |  |
| CantMonedas20Centavos | int(4) | No | - |  |  |
| CantMonedas5Centavos | int(4) | No | - |  |  |
| CantMonedas2Centavos | int(4) | No | - |  |  |
| CantMonedas1Centavo | int(4) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_DesglosePagoEfectivoBancoRD` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalle_Comprobante`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador1 | int(4) | No | - |  |  |
| Id_Compro | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Compro | char(15) | No | - |  |  |
| Id_Doc | varchar(20) | No | - |  |  |
| Tipo_Doc | char(10) | No | - |  |  |
| Cta | varchar(20) | No | - |  |  |
| SubCta | varchar(20) | No | - |  |  |
| Analisis | varchar(20) | No | - |  |  |
| SubAnalisis | varchar(20) | No | - |  |  |
| Epigrafe | varchar(20) | No | - |  |  |
| Partida | varchar(20) | No | - |  |  |
| SubControl | char(10) | No | - |  |  |
| Descripcion | varchar(200) | No | - |  |  |
| DEBE | money(8) | No | - |  |  |
| HABER | money(8) | No | - |  |  |
| Transito | bit(1) | No | - |  |  |
| Clasificacion | char(2) | No | - |  |  |
| Natu | bit(1) | No | - |  |  |
| Items | int(4) | No | - |  | ✅ |
| Id_ComproRef | int(4) | No | - |  |  |
| AnoRef | smallint(2) | No | - |  |  |
| MesRef | tinyint(1) | No | - |  |  |
| Id_Agrupacion | char(5) | No | - |  |  |
| Id_AgrupacionRef | char(5) | No | - |  |  |
| Marca_Conciliacion | bit(1) | No | - |  |  |
| Fecha_Conciliacion | datetime(8) | No | - |  |  |

---

#### `RH_Detalle_Comprobante_Posteos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador1 | int(4) | No | - |  |  |
| Cta | varchar(20) | No | - |  |  |
| SubCta | varchar(20) | No | - |  |  |
| Analisis | varchar(20) | No | - |  |  |
| SubAnalisis | varchar(20) | No | - |  |  |
| Epigrafe | varchar(20) | No | - |  |  |
| Partida | varchar(20) | No | - |  |  |
| SubControl | char(10) | No | - |  |  |
| DEBE | money(8) | No | - |  |  |
| HABER | money(8) | No | - |  |  |
| Items | int(4) | No | - |  | ✅ |
| Descripcion | varchar(200) | No | - |  |  |

---

#### `RH_Detalle_Devolucion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  |  |
| Id_Devolucion | int(4) | No | - |  |  |
| Id_Almacen | char(5) | No | - |  |  |
| Ano_Devolucion | smallint(2) | No | - |  |  |
| Items | smallint(2) | No | - |  |  |
| Id_Producto | char(20) | No | - |  |  |
| Id_Lote | char(20) | No | - |  |  |
| Desc_Producto | varchar(255) | No | - |  |  |
| Um_Almacen | char(5) | No | - |  |  |
| Cantidad_Devuelta | numeric(9) | No | - |  |  |
| Cantidad_Original | numeric(9) | No | - |  |  |
| Costo_DocMB | numeric(9) | No | - |  |  |
| Costo_DocMC | numeric(9) | No | - |  |  |
| Costo_NuevoMB | numeric(9) | No | - |  |  |
| Costo_NuevoMC | numeric(9) | No | - |  |  |
| ImporteDoc_MB | money(8) | No | - |  |  |
| ImporteDoc_MC | money(8) | No | - |  |  |
| ImporteCosto_MB | money(8) | No | - |  |  |
| ImporteCosto_MC | money(8) | No | - |  |  |
| Importe_MB | money(8) | No | - |  |  |
| Importe_MC | money(8) | No | - |  |  |
| Costo_FacMB | numeric(9) | No | - |  |  |
| Costo_FacMC | numeric(9) | No | - |  |  |
| Encabezado_c | bit(1) | No | - |  |  |
| Producto_Terminado_c | bit(1) | No | - |  |  |
| Producto_OServicio_c | bit(1) | No | - |  |  |
| Impuesto | numeric(5) | No | - |  |  |
| Importe_Impuesto | money(8) | No | - |  |  |
| Comision | numeric(5) | No | - |  |  |
| Importe_Comision | money(8) | No | - |  |  |
| Importe_OriginalMB | money(8) | No | - |  |  |
| Importe_OriginalMC | money(8) | No | - |  |  |
| ItemsComp | tinyint(1) | No | - |  |  |
| Id_ActivoFijo | char(20) | No | - |  |  |
| Importe_RecargoMB | money(8) | No | - |  |  |
| Importe_RecargoMC | money(8) | No | - |  |  |
| Importe_DesctoMB | money(8) | No | - |  |  |
| Importe_DesctoMC | money(8) | No | - |  |  |
| Importe_ArancelMB | money(8) | No | - |  |  |
| Importe_ArancelMC | money(8) | No | - |  |  |
| factor_Conversion | numeric(9) | No | - |  |  |
| Existencia | numeric(9) | No | - |  |  |
| ItemLink | bigint(8) | No | - |  |  |

**Índices:**
- `IX_RH_Detalle_Devolucion` (CLUSTERED)

---

#### `RH_Detalle_Factura`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  |  |
| Id_Factura | int(4) | No | - |  |  |
| Id_Almacen | char(5) | No | - |  |  |
| Ano_Factura | smallint(2) | No | - |  |  |
| Items | smallint(2) | No | - |  |  |
| Id_Producto | char(20) | No | - |  |  |
| Id_Lote | char(20) | No | - |  |  |
| Desc_Producto | varchar(255) | No | - |  |  |
| Um_Almacen | char(5) | No | - |  |  |
| Um_Factura | char(5) | No | - |  |  |
| factor_Conversion | numeric(9) | No | - |  |  |
| Precio_VentaUmAlmacenMB | numeric(9) | No | - |  |  |
| Precio_VentaUmAlmacenMC | numeric(9) | No | - |  |  |
| Precio_VentaUmFacturaMB | money(8) | No | - |  |  |
| Precio_VentaUmFacturaMC | money(8) | No | - |  |  |
| Precio_VentaTotalMB | numeric(9) | No | - |  |  |
| Precio_VentaTotalMC | numeric(9) | No | - |  |  |
| Existencia | numeric(9) | No | - |  |  |
| Disponibilidad | numeric(9) | No | - |  |  |
| Cantidad_Factura | money(8) | No | - |  |  |
| Cantidad_Almacen | numeric(9) | No | - |  |  |
| Reservadas | numeric(9) | No | - |  |  |
| DescuentoMB | numeric(5) | No | - |  |  |
| DescuentoMC | numeric(5) | No | - |  |  |
| RecargoMB | numeric(5) | No | - |  |  |
| RecargoMC | numeric(5) | No | - |  |  |
| TipoRecargoMB | tinyint(1) | No | - |  |  |
| TipoRecargoMC | tinyint(1) | No | - |  |  |
| TipoDescuentoMB | tinyint(1) | No | - |  |  |
| TipoDescuentoMC | tinyint(1) | No | - |  |  |
| ArancelMB | numeric(5) | No | - |  |  |
| ArancelMC | numeric(5) | No | - |  |  |
| Importe_MB | money(8) | No | - |  |  |
| Importe_MC | money(8) | No | - |  |  |
| Importe_MFact | money(8) | No | - |  |  |
| Impuesto | numeric(5) | No | - |  |  |
| Importe_Impuesto | money(8) | No | - |  |  |
| Tipo_Factura | smallint(2) | No | - |  |  |
| No_Serie | varchar(50) | No | - |  |  |
| Condiciones_Pago | varchar(255) | No | - |  |  |
| Cantidad_Devuelta | numeric(9) | No | - |  |  |
| Producto_OServicio_c | bit(1) | No | - |  |  |
| Arancelario | char(20) | No | - |  |  |
| Precio_CostoUmAlmacenMB | numeric(9) | No | - |  |  |
| Precio_CostoUmAlmacenMC | numeric(9) | No | - |  |  |
| Importe_CostoMB | money(8) | No | - |  |  |
| Importe_CostoMC | money(8) | No | - |  |  |
| Precio_Venta_Original | money(8) | No | - |  |  |
| Observaciones | varchar(200) | No | - |  |  |
| Paquete | numeric(9) | No | - |  |  |
| Bultos | numeric(9) | No | - |  |  |
| Comision | numeric(5) | No | - |  |  |
| Importe_Comision | money(8) | No | - |  |  |
| ItemsComp | tinyint(1) | No | - |  |  |
| Importe_DevueltoMB | money(8) | No | - |  |  |
| Importe_DevueltoMC | money(8) | No | - |  |  |
| Importe_RecargoMB | money(8) | No | - |  |  |
| Importe_RecargoMC | money(8) | No | - |  |  |
| Importe_DesctoMB | money(8) | No | - |  |  |
| Importe_DesctoMC | money(8) | No | - |  |  |
| Importe_ArancelMB | money(8) | No | - |  |  |
| Importe_ArancelMC | money(8) | No | - |  |  |
| Precio_RecargoMB | numeric(9) | No | - |  |  |
| Precio_RecargoMC | numeric(9) | No | - |  |  |
| Precio_DesctoMB | numeric(9) | No | - |  |  |
| Precio_DesctoMC | numeric(9) | No | - |  |  |
| Precio_ArancelMB | numeric(9) | No | - |  |  |
| Precio_ArancelMC | numeric(9) | No | - |  |  |
| Id_Ccosto | varchar(10) | No | - |  |  |
| Item | bigint(8) | No | - |  |  |
| LoteSM | char(20) | No | - |  |  |
| PesoBruto | money(8) | No | - |  |  |
| PesoNeto | money(8) | No | - |  |  |
| Oferta | bit(1) | No | - |  |  |
| IRConsigna | varchar(20) | No | - |  |  |
| ContaIRConsigna | int(4) | No | - |  |  |
| Desc_Ccosto | varchar(50) | No | - |  |  |
| Id_Destino | varchar(10) | No | - |  |  |
| Id_Actividad | varchar(10) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Afectados_Pago_Divisa`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Afectados_Pago_Divisa` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Afectados_Pago_Divisa` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Ausencias`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Dias | numeric(9) | No | - |  |  |
| Porciento | numeric(5) | No | - |  |  |
| A_pagar_por | tinyint(1) | No | - |  |  |
| Deducible | bit(1) | No | - |  |  |
| Afecta_Subsidio | bit(1) | No | - |  |  |
| Afecta_Vacaciones | bit(1) | No | - |  |  |
| Afecta_Vacaciones_Imp | bit(1) | No | - |  |  |
| Afecta_SNC_225 | bit(1) | No | - |  |  |
| Afecta_SNC_225_Imp | bit(1) | No | - |  |  |
| Afecta_Evaluacion_Tecnicos | bit(1) | No | - |  |  |
| Afecta_Estimulo | bit(1) | No | - |  |  |
| Prenomina_Hrs | bit(1) | No | - |  |  |
| Suma_Reporte_Ausencia | bit(1) | No | - |  |  |
| AfectaPromTrabajTot | bit(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Origen | tinyint(1) | No | - |  |  |
| Horas | numeric(5) | No | - |  |  |

**Clave primaria:** Item

**Restricciones CHECK:**
- CK_RH_Detalles_Reporte_Ausencias_Clasificacion: None
- CK_RH_Detalles_Reporte_Ausencias_A_pagar_por: None

**Índices:**
- `PK_RH_Detalles_Reporte_Ausencias` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Ausencias` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_CLA`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Horas | numeric(9) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Clasificacion_Categ_Ocupac | tinyint(1) | No | - |  |  |

**Clave primaria:** Item

**Restricciones CHECK:**
- CK_RH_Detalles_Reporte_CLA_Clasificacion: None

**Índices:**
- `PK_RH_Detalles_Reporte_CLA` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_CLA` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Descuento_Comedor`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Importe | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Descuento_Comedor` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Descuento_Comedor_Xls_Err`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  | ✅ |
| Xls_Row | bigint(8) | No | - |  |  |
| Xls_Err | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Divisa`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Divisa | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_CCosto | char(10) | No | - |  |  |
| Nivel_Nomina | tinyint(1) | No | - |  |  |
| Id_Direccion_Nomina | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Divisa` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Divisa_Xls_Err`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  | ✅ |
| Xls_Row | bigint(8) | No | - |  |  |
| Xls_Err | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Estimulacion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_CCosto | char(10) | No | - |  |  |
| Nivel_Nomina | tinyint(1) | No | - |  |  |
| Id_Direccion_Nomina | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Estimulacion` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Estimulacion_Puntos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Porc_Estimulacion | numeric(5) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_CCosto | char(10) | No | - |  |  |
| Id_Categoria | char(5) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Estimulacion_Puntos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Estimulacion_Xls_Err`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  | ✅ |
| Xls_Row | bigint(8) | No | - |  |  |
| Xls_Err | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Horas_Extra`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Horas | numeric(9) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Clasificacion_Categ_Ocupac | tinyint(1) | No | - |  |  |
| Tarifa_Divisa | money(8) | No | - |  |  |
| Importe_Divisa | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Horas_Extra` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Horas_Extra` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Idoneidad_Movil`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Puntos | numeric(5) | No | - |  |  |
| Afectacion | numeric(5) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Idoneidad_Movil` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Idoneidad_Movil` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Impuesto_CSS`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_CCosto | char(10) | No | - |  |  |
| Nivel_Nomina | tinyint(1) | No | - |  |  |
| Id_Direccion_Nomina | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Impuesto_CSS` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Impunt`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Justificada | bit(1) | No | - |  |  |
| Cantidad_Impuntualidad | smallint(2) | No | - |  |  |
| Minutos_Impuntualidad | smallint(2) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Origen | tinyint(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Impunt` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Impunt` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_MS_EE`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| CodIncidencia1 | char(3) | No | - |  |  |
| CodIncidencia2 | char(3) | No | - |  |  |
| CodIncidencia3 | char(3) | No | - |  |  |
| CodIncidencia4 | char(3) | No | - |  |  |
| CodIncidencia5 | char(3) | No | - |  |  |
| CodIncidencia6 | char(3) | No | - |  |  |
| CodIncidencia7 | char(3) | No | - |  |  |
| AusenciasJustificadas | numeric(9) | No | - |  |  |
| AusenciasInjustificadas | numeric(9) | No | - |  |  |
| Impuntualidades | smallint(2) | No | - |  |  |
| Afectacion | numeric(5) | No | - |  |  |
| Cuantia | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_MS_EE` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_MS_EE` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_MS_ET`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| CodIncidencia1 | char(3) | No | - |  |  |
| CodIncidencia2 | char(3) | No | - |  |  |
| CodIncidencia3 | char(3) | No | - |  |  |
| CodIncidencia4 | char(3) | No | - |  |  |
| CodIncidencia5 | char(3) | No | - |  |  |
| CodIncidencia6 | char(3) | No | - |  |  |
| CodIncidencia7 | char(3) | No | - |  |  |
| PorcientoCumplimiento | numeric(5) | No | - |  |  |
| PorcientoSobrecumplimiento | numeric(5) | No | - |  |  |
| EvaluacionDesempeno | numeric(5) | No | - |  |  |
| Afectacion | numeric(5) | No | - |  |  |
| Cuantia | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_MS_ET` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_MS_ET` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_MS_PM`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| CodIncidencia1 | char(3) | No | - |  |  |
| CodIncidencia2 | char(3) | No | - |  |  |
| CodIncidencia3 | char(3) | No | - |  |  |
| CodIncidencia4 | char(3) | No | - |  |  |
| CodIncidencia5 | char(3) | No | - |  |  |
| CodIncidencia6 | char(3) | No | - |  |  |
| CodIncidencia7 | char(3) | No | - |  |  |
| AusenciasJustificadas | numeric(9) | No | - |  |  |
| AusenciasInjustificadas | numeric(9) | No | - |  |  |
| Impuntualidades | smallint(2) | No | - |  |  |
| MSPagoAntiguedad | bit(1) | No | - |  |  |
| MSPagoCoeficiente | bit(1) | No | - |  |  |
| MSPagoTurno | bit(1) | No | - |  |  |
| AfectacionAntiguedad | numeric(5) | No | - |  |  |
| AfectacionCoeficiente | numeric(5) | No | - |  |  |
| AfectacionTurnos | numeric(5) | No | - |  |  |
| PagoAntiguedad | money(8) | No | - |  |  |
| PagoCoeficiente | money(8) | No | - |  |  |
| PagoTurnos | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_MS_PM` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_MS_PM` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Mov`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Regimen_Salarial | tinyint(1) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_Cargo | char(5) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Dias_Laborables | tinyint(1) | No | - |  |  |
| Tarifa_Horaria | money(8) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Porciento_Estimulo | numeric(5) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Porciento_Estimulacion | numeric(5) | No | - |  |  |
| Dias_a_Pagar | numeric(5) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Ano_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Tarjeta | tinyint(1) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Impresa | bit(1) | No | - |  |  |
| Procesada | bit(1) | No | - |  |  |
| Desc_Cargo | varchar(120) | No | - |  |  |
| FondoTiempoDia | numeric(5) | No | - |  |  |
| Impresa_Grupo | smallint(2) | No | - |  |  |
| Tarifa_Divisa | money(8) | No | - |  |  |
| Divisa_Factura | money(8) | No | - |  |  |
| Factura_Confirmada | bit(1) | No | - |  |  |
| Facturar | bit(1) | No | - |  |  |
| NoMovimiento | bigint(8) | No | - |  |  |
| Horas_a_Pagar | numeric(5) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Nominillas_Mov` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Nominillas_Mov` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Mov_Aus`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Dias | numeric(9) | No | - |  |  |
| Porciento | numeric(5) | No | - |  |  |
| A_pagar_por | tinyint(1) | No | - |  |  |
| Deducible | bit(1) | No | - |  |  |
| Afecta_Subsidio | bit(1) | No | - |  |  |
| Afecta_Vacaciones | bit(1) | No | - |  |  |
| Afecta_Vacaciones_Imp | bit(1) | No | - |  |  |
| Afecta_SNC_225 | bit(1) | No | - |  |  |
| Afecta_SNC_225_Imp | bit(1) | No | - |  |  |
| Afecta_Evaluacion_Tecnicos | bit(1) | No | - |  |  |
| Afecta_Estimulo | bit(1) | No | - |  |  |
| Prenomina_Hrs | bit(1) | No | - |  |  |
| Suma_Reporte_Ausencia | bit(1) | No | - |  |  |
| AfectaPromTrabajTot | bit(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Horas | numeric(5) | No | - |  |  |

**Clave primaria:** Item

**Restricciones CHECK:**
- CK_RH_Detalles_Reporte_Nominillas_Mov_Aus_A_pagar_por: None
- CK_RH_Detalles_Reporte_Nominillas_Mov_Aus_Clasificacion: None

**Índices:**
- `PK_RH_Detalles_Reporte_Nominillas_Mov_Aus` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Nominillas_Mov_Aus` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Mov_Imp`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Justificada | bit(1) | No | - |  |  |
| Cantidad_Impuntualidad | smallint(2) | No | - |  |  |
| Minutos_Impuntualidad | smallint(2) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Nominillas_Mov_Imp` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Nominillas_Mov_Imp` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Ret_Mov`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Del_Mark | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Nominillas_Ret_Mov` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Nominillas_Ret_Mov` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Ret_Rpt`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Del_Mark | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Nominillas_Ret_Rpt` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Nominillas_Ret_Rpt` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Rpt`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Regimen_Salarial | tinyint(1) | No | - |  |  |
| Tarifa_Horaria | money(8) | No | - |  |  |
| Dias_a_Pagar | numeric(5) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Pago_Divisa | bit(1) | No | - |  |  |
| Ano_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Tarjeta | tinyint(1) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Impresa | bit(1) | No | - |  |  |
| Procesada | bit(1) | No | - |  |  |
| ItemLink | bigint(8) | No | - |  |  |
| Tarifa_Divisa | money(8) | No | - |  |  |
| Divisa_Factura | money(8) | No | - |  |  |
| Factura_Confirmada | bit(1) | No | - |  |  |
| Facturar | bit(1) | No | - |  |  |
| Impresa_Grupo | smallint(2) | No | - |  |  |
| PreAssets | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Restricciones CHECK:**
- CK_RH_Detalles_Reporte_Nominillas_Rpt_Regimen_Salarial: None
- CK_RH_Detalles_Reporte_Nominillas_Rpt_Clasificacion: None

**Índices:**
- `PK_RH_Detalles_Reporte_Nominillas_Rpt` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Nominillas_Rpt` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Nominillas_Xls_Err`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  | ✅ |
| Xls_Row | bigint(8) | No | - |  |  |
| Xls_Err | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Nominillas_Xls_Tmp`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Otros_Pagos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Otro_Pago | char(7) | No | - |  |  |
| Valor_Otro_Pago | money(8) | No | - |  |  |
| Afecta_Ausencias | bit(1) | No | - |  |  |
| Acumula_Vacaciones | bit(1) | No | - |  |  |
| Incluir_SNC_225 | bit(1) | No | - |  |  |
| Rpt_Autom | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Otros_Pagos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Pago_Comedor`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Pago_Comedor_CUC_R | bit(1) | No | - |  |  |
| Pago_Comedor_CUC_W | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa_R | money(8) | No | - |  |  |
| Pago_Comedor_Tarifa_W | money(8) | No | - |  |  |
| Dias_Laborables | tinyint(1) | No | - |  |  |
| Dias_Ausencias_R | tinyint(1) | No | - |  |  |
| Dias_Ausencias_W | tinyint(1) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Pago_Comedor` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_PreNomina_Aus`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Dia | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Dias | numeric(9) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Horas | numeric(5) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_PreNomina_Aus` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_PreNomina_Aus` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_PreNomina_Imp`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Dia | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Minutos_Impuntualidad | smallint(2) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_PreNomina_Imp` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_PreNomina_Imp` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Reintegros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Tipo_Nomina | tinyint(1) | No | - |  |  |
| Tipo_Reintegro | tinyint(1) | No | - |  |  |
| AnoNomina | smallint(2) | No | - |  |  |
| MesNomina | tinyint(1) | No | - |  |  |
| Tipo_PagoNomina | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Cantidad_Reintegrar | numeric(5) | No | - |  |  |
| Salario_Reintegrar | money(8) | No | - |  |  |
| FechaNomina | smalldatetime(4) | No | - |  |  |
| Cantidad_Nomina | numeric(5) | No | - |  |  |
| Devengado_Nomina | money(8) | No | - |  |  |
| Cuenta_por_Cobrar | bit(1) | No | - |  |  |
| Presupuesto_Estado | bit(1) | No | - |  |  |
| Presupuesto_Estado_Tmp | bit(1) | No | - |  |  |
| Tarjeta | bit(1) | No | - |  |  |
| Horas_Extras | numeric(9) | No | - |  |  |
| Ano_Factura | smallint(2) | No | - |  |  |
| Id_Almacen | char(5) | No | - |  |  |
| Id_Factura | int(4) | No | - |  |  |
| Devolucion_Confirmada | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Reintegros` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Reintegros` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Reintegros_Sbs`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Salario_Reintegrar_Part | money(8) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Reintegros_Slr`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Salario_Reintegrar_Part | money(8) | No | - |  |  |

---

#### `RH_Detalles_Reporte_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Tipo | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Porciento | numeric(5) | No | - |  |  |
| Carencia | bit(1) | No | - |  |  |
| Dias_Naturales | numeric(5) | No | - |  |  |
| Dias_a_Pagar | numeric(5) | No | - |  |  |
| Promedio | money(8) | No | - |  |  |
| Fecha_Valido | smalldatetime(4) | No | - |  |  |
| Fecha_Pago | smalldatetime(4) | No | - |  |  |
| Fecha_Resolucion | smalldatetime(4) | No | - |  |  |
| Tipo_Certificado | tinyint(1) | No | - |  |  |
| Dias_Feriados_Periodo | tinyint(1) | No | - |  |  |
| Dias_Feriados_Adelantados | tinyint(1) | No | - |  |  |

**Clave primaria:** Item

**Restricciones CHECK:**
- CK_RH_Detalles_Reporte_Subsidios_Tipo: None
- CK_RH_Detalles_Reporte_Subsidios_Tipo_Certificado: None

**Índices:**
- `PK_RH_Detalles_Reporte_Subsidios` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Subsidios` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Subsidios_Ret`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| ItemLink | bigint(8) | No | - |  |  |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Tipo | tinyint(1) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Del_Mark | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Subsidios_Ret` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Subsidios_Ret` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Tarifa_Horaria`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Horas | numeric(9) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |
| Importe_Tarifa | money(8) | No | - |  |  |
| Porciento_Sobrecumplimiento | numeric(5) | No | - |  |  |
| Otros_Pagos | money(8) | No | - |  |  |
| Importe_Sobrecumplimiento | money(8) | No | - |  |  |
| Importe_Total | money(8) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Fecha | smalldatetime(4) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Id_Actividad | char(3) | No | - |  |  |
| Horas_Otra_Tarifa | numeric(9) | No | - |  |  |
| Otra_Tarifa | money(8) | No | - |  |  |
| Importe_Otra_Tarifa | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Tarifa_Horaria` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Tarifa_Horaria` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Turnos_Nocturnos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Horas | numeric(9) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Turnos_Nocturnos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Detalles_Reporte_Vacaciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Dias_Solicitados_Periodo | numeric(5) | No | - |  |  |
| Dias_Solicitados_Adelantados | numeric(5) | No | - |  |  |
| Dias_Solicitados | numeric(5) | No | - |  |  |
| Dias_Pagados_Periodo | numeric(5) | No | - |  |  |
| Dias_Pagados_Adelantados | numeric(5) | No | - |  |  |
| Dias_Pagados | numeric(5) | No | - |  |  |
| Importe | money(8) | No | - |  |  |
| Liquidacion | bit(1) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Origen | tinyint(1) | No | - |  |  |
| Dias_Feriados_Periodo | tinyint(1) | No | - |  |  |
| Dias_Feriados_Adelantados | tinyint(1) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Detalles_Reporte_Vacaciones` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Vacaciones` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Vacaciones_Ret`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Del_Mark | bit(1) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Vacaciones_Ret` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Vacaciones_Ret` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Vinculacion_DI`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Colectivo | char(5) | No | - |  |  |
| Id_Actividad | char(15) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Horas_Actividad | numeric(5) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Vinculacion_DI` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Vinculacion_DI` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Vinculacion_OT_AN`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Tipo | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Actividad | char(15) | No | - |  |  |
| Desc_Actividad | varchar(100) | No | - |  |  |
| UM | char(10) | No | - |  |  |
| Tasa | numeric(9) | No | - |  |  |
| Tipo_Norma | char(1) | No | - |  |  |
| Cantidad_Actividad | numeric(9) | No | - |  |  |
| Devengado_Actividad | money(8) | No | - |  |  |
| Horas_Actividad | numeric(5) | No | - |  |  |
| Devengado_Otros | money(8) | No | - |  |  |
| Horas_Multioficio | numeric(5) | No | - |  |  |
| Devengado_Multioficio | money(8) | No | - |  |  |
| CumplimNorma | numeric(9) | No | - |  |  |
| PagoSobrecumplim | numeric(5) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| IddeOrdendeTrabajo | char(25) | No | - |  |  |
| Horas_Adelantadas | numeric(5) | No | - |  |  |
| Horas_Interrupto | numeric(5) | No | - |  |  |
| Horas_Tasadas | numeric(5) | No | - |  |  |
| Horas_Real_Trabajadas | numeric(5) | No | - |  |  |
| Tarifa_Horas_Adelantadas | money(8) | No | - |  |  |
| Tarifa_Horas_Vinculacion | money(8) | No | - |  |  |
| Porciento_Interrupcion | numeric(5) | No | - |  |  |
| Porciento_Importe_Tasado | numeric(5) | No | - |  |  |
| Devengado_Horas_Adelantadas | money(8) | No | - |  |  |
| Devengado_Horas_Interrupcion | money(8) | No | - |  |  |
| Devengado_Horas_Tasadas | money(8) | No | - |  |  |
| Total_Devengado | money(8) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Vinculacion_OT_AN` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Vinculacion_OT_AN` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Vinculacion_RCD`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - | ✅ | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Colectivo | char(5) | No | - |  |  |
| Id_Actividad | char(15) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Horas_Actividad | numeric(5) | No | - |  |  |
| Cantidad_Actividad | numeric(9) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |

**Clave primaria:** Item

**Índices:**
- `PK_RH_Detalles_Reporte_Vinculacion_RCD` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Vinculacion_RCD` (NONCLUSTERED)

---

#### `RH_Detalles_Reporte_Vinculacion_RCG`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Contador | int(4) | No | - |  |  |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Colectivo | char(5) | No | - | ✅ |  |
| Id_Actividad | char(15) | No | - | ✅ |  |
| Desc_Actividad | varchar(100) | No | - |  |  |
| Tasa | numeric(9) | No | - |  |  |
| Cantidad_Actividad | numeric(9) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Colectivo, Id_Actividad

**Índices:**
- `PK_RH_Detalles_Reporte_Vinculacion_RCG` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Detalles_Reporte_Vinculacion_RCG` (NONCLUSTERED)

---

#### `RH_Devolucion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - | ✅ | ✅ |
| Confirmada | tinyint(1) | No | - |  |  |
| Id_Devolucion | int(4) | No | - |  |  |
| Id_Almacen | char(5) | No | - |  |  |
| Ano_Devolucion | smallint(2) | No | - |  |  |
| Fecha_Confirmacion | smalldatetime(4) | No | - |  |  |
| Fecha_Devolucion | smalldatetime(4) | No | - |  |  |
| Id_Empleado | char(5) | No | - |  |  |
| Desc_Empleado | varchar(60) | No | - |  |  |
| Id_Cliente | char(15) | No | - |  |  |
| Desc_Cliente | varchar(50) | No | - |  |  |
| Id_Referencia | int(4) | No | - |  |  |
| Año_Referencia | smallint(2) | No | - |  |  |
| Tipo_Devolucion | tinyint(1) | No | - |  |  |
| Devuelve_oCancela | tinyint(1) | No | - |  |  |
| Cantidad_oValor | tinyint(1) | No | - |  |  |
| ImporteTotalMB | money(8) | No | - |  |  |
| ImporteTotalMC | money(8) | No | - |  |  |
| Id_Compro | int(4) | No | - |  |  |
| Mes_Compro | tinyint(1) | No | - |  |  |
| Ano_Compro | smallint(2) | No | - |  |  |
| Nota | varchar(200) | No | - |  |  |
| Contabilizado | bit(1) | No | - |  |  |
| Marca_Conteo | bit(1) | No | - |  |  |
| Tipo_Documento | tinyint(1) | No | - |  |  |
| Xtrans | bit(1) | No | - |  |  |
| Impuesto_Total | money(8) | No | - |  |  |
| Comision_Total | money(8) | No | - |  |  |
| Desc_Almacen | varchar(50) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Doc_primario | char(20) | No | - |  |  |
| No_Prelacion | int(4) | No | - |  |  |
| ImpuestoProve | money(8) | No | - |  |  |
| ImpuestoReten | money(8) | No | - |  |  |
| IddocPago | varchar(15) | No | - |  |  |
| DescFP | varchar(50) | No | - |  |  |
| Devolucion_Nominas | tinyint(1) | No | - |  |  |

**Clave primaria:** Contador

**Índices:**
- `PK_RH_Devolucion` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Cambio_Pago`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Provincia | char(5) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_CCosto | char(10) | No | - |  |  |
| Cambiar_Pago | bit(1) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Empleados_Cambio_Pago` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Capacitacion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Id_Curso | char(10) | No | - | ✅ |  |
| Desc_Curso | varchar(80) | No | - |  |  |
| Fecha_Curso | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Id_Expediente, Id_Curso

**Índices:**
- `PK_RH_Empleados_Capacitacion` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Centro_Costo`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Id_Ccosto | char(10) | No | - | ✅ |  |
| Id_Obra | char(10) | No | - | ✅ |  |
| Desc_Ccosto | char(50) | No | - |  |  |
| Porciento_Fondo_Tiempo | numeric(5) | No | - |  |  |

**Clave primaria:** Id_Expediente, Id_Ccosto, Id_Obra

**Índices:**
- `PK_RH_Empleados_Centro_Costo` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Idiomas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Id_Idioma | char(3) | No | - | ✅ |  |
| Desc_Idioma | varchar(15) | No | - |  |  |
| Lee | tinyint(1) | No | - |  |  |
| Habla | tinyint(1) | No | - |  |  |
| Escribe | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_Expediente, Id_Idioma

**Restricciones CHECK:**
- CK_RH_Empleados_Idiomas_Lee: None
- CK_RH_Empleados_Idiomas_Habla: None
- CK_RH_Empleados_Idiomas_Escribe: None

**Índices:**
- `PK_RH_Empleados_Idiomas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Movimientos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NoMovimiento | bigint(8) | No | - |  | ✅ |
| Id_Expediente | char(15) | No | - |  |  |
| Empleado | varchar(152) | No | - |  |  |
| Id_CausaMov | char(5) | No | - |  |  |
| Id_Tipo_ContratoOld | char(3) | No | - |  |  |
| Id_Tipo_ContratoNew | char(3) | No | - |  |  |
| Regimen_SalarialOld | tinyint(1) | No | - |  |  |
| Regimen_SalarialNew | tinyint(1) | No | - |  |  |
| Tarifa_Horaria_con_ReporteOld | bit(1) | No | - |  |  |
| Tarifa_Horaria_con_ReporteNew | bit(1) | No | - |  |  |
| NivelOld | tinyint(1) | No | - |  |  |
| NivelNew | tinyint(1) | No | - |  |  |
| Id_DireccionOld | char(15) | No | - |  |  |
| Id_DireccionNew | char(15) | No | - |  |  |
| Id_CCostoOld | char(10) | No | - |  |  |
| Id_CCostoNew | char(10) | No | - |  |  |
| Id_CargoOld | char(5) | No | - |  |  |
| Id_CargoNew | char(5) | No | - |  |  |
| PlazaOld | bigint(8) | No | - |  |  |
| PlazaNew | bigint(8) | No | - |  |  |
| CalendarioOld | char(3) | No | - |  |  |
| CalendarioNew | char(3) | No | - |  |  |
| Dias_LaborablesOld | tinyint(1) | No | - |  |  |
| Dias_LaborablesNew | tinyint(1) | No | - |  |  |
| Asignacion_por_CargoOld | bit(1) | No | - |  |  |
| Asignacion_por_CargoNew | bit(1) | No | - |  |  |
| Salario_BasicoOld | money(8) | No | - |  |  |
| Salario_BasicoNew | money(8) | No | - |  |  |
| EstimuloOld | money(8) | No | - |  |  |
| EstimuloNew | money(8) | No | - |  |  |
| Porciento_EstimuloOld | numeric(5) | No | - |  |  |
| Porciento_EstimuloNew | numeric(5) | No | - |  |  |
| AntiguedadOld | money(8) | No | - |  |  |
| AntiguedadNew | money(8) | No | - |  |  |
| OtrosOld | money(8) | No | - |  |  |
| OtrosNew | money(8) | No | - |  |  |
| PlusOld | money(8) | No | - |  |  |
| PlusNew | money(8) | No | - |  |  |
| Salario_por_CargoOld | money(8) | No | - |  |  |
| Salario_por_CargoNew | money(8) | No | - |  |  |
| Porciento_PerfeccionamientoOld | numeric(5) | No | - |  |  |
| Porciento_PerfeccionamientoNew | numeric(5) | No | - |  |  |
| Valor_DivisaOld | money(8) | No | - |  |  |
| Valor_DivisaNew | money(8) | No | - |  |  |
| Porciento_Pago_DivisaOld | numeric(5) | No | - |  |  |
| Porciento_Pago_DivisaNew | numeric(5) | No | - |  |  |
| EstimulacionOld | money(8) | No | - |  |  |
| EstimulacionNew | money(8) | No | - |  |  |
| Porciento_EstimulacionOld | numeric(5) | No | - |  |  |
| Porciento_EstimulacionNew | numeric(5) | No | - |  |  |
| AlbergamientoOld | money(8) | No | - |  |  |
| AlbergamientoNew | money(8) | No | - |  |  |
| OtrasRetribucionesOld | numeric(5) | No | - |  |  |
| OtrasRetribucionesNew | numeric(5) | No | - |  |  |
| HorarioIrregularOld | money(8) | No | - |  |  |
| HorarioIrregularNew | money(8) | No | - |  |  |
| Otras_CLAOld | money(8) | No | - |  |  |
| Otras_CLANew | money(8) | No | - |  |  |
| Coeficente_Empresa_EmpleadoraOld | numeric(5) | No | - |  |  |
| Coeficente_Empresa_EmpleadoraNew | numeric(5) | No | - |  |  |
| IETerritorialOld | numeric(5) | No | - |  |  |
| IETerritorialNew | numeric(5) | No | - |  |  |
| ETSectorOld | numeric(5) | No | - |  |  |
| ETSectorNew | numeric(5) | No | - |  |  |
| Id_Tipo_ParticipacionOld | char(3) | No | - |  |  |
| Id_Tipo_ParticipacionNew | char(3) | No | - |  |  |
| Idoneidad_FijoOld | money(8) | No | - |  |  |
| Idoneidad_FijoNew | money(8) | No | - |  |  |
| Idoneidad_MovilOld | money(8) | No | - |  |  |
| Idoneidad_MovilNew | money(8) | No | - |  |  |
| Retribucion_ComplementariaOld | money(8) | No | - |  |  |
| Retribucion_ComplementariaNew | money(8) | No | - |  |  |
| Fecha_CargoOld | smalldatetime(4) | No | - |  |  |
| Fecha_CargoNew | smalldatetime(4) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Salario_DivisaOld | money(8) | No | - |  |  |
| Salario_DivisaNew | money(8) | No | - |  |  |
| Nivel_NominaOld | tinyint(1) | No | - |  |  |
| Nivel_NominaNew | tinyint(1) | No | - |  |  |
| Id_Direccion_NominaOld | char(15) | No | - |  |  |
| Id_Direccion_NominaNew | char(15) | No | - |  |  |
| NGrupoOld | tinyint(1) | No | - |  |  |
| NGrupoNew | tinyint(1) | No | - |  |  |
| Fecha_ContratacionOld | smalldatetime(4) | No | - |  |  |
| Fecha_ContratacionNew | smalldatetime(4) | No | - |  |  |
| Fecha_Efectivo | smalldatetime(4) | No | - |  |  |
| Fecha_Mov | smalldatetime(4) | No | - |  |  |
| Id_Mov | int(4) | No | - | ✅ |  |
| Agrupacion | char(5) | No | - | ✅ |  |
| Ano_Mov | int(4) | No | - | ✅ |  |

**Clave primaria:** Id_Mov, Agrupacion, Ano_Mov

**Índices:**
- `PK__RH_Emple__C97F01DD104886A7` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Nomina`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Empleado | char(15) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(50) | No | - |  |  |
| Apellido_1 | varchar(50) | No | - |  |  |
| Nomina | bit(1) | No | - |  |  |
| Seleccionado_para_Pago | bit(1) | No | - |  |  |
| Tarifa | money(8) | No | - |  |  |
| Tarifa_Diaria | money(8) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Porciento_Estimulo | numeric(5) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Acumula_Vacaciones | bit(1) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Dias_Acumulado_Temporal | numeric(5) | No | - |  |  |
| Salario_Acumulado_Temporal | money(8) | No | - |  |  |
| Nivel_Nomina | tinyint(1) | No | - |  |  |
| Id_Direccion_Nomina | char(15) | No | - |  |  |
| Invalidez_Parcial | money(8) | No | - |  |  |
| Ex_Combatientes | money(8) | No | - |  |  |
| Porciento_Perfeccionamiento | numeric(5) | No | - |  |  |
| Valor_Divisa | money(8) | No | - |  |  |
| Porciento_Pago_Divisa | numeric(5) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Porciento_Estimulacion | numeric(5) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| IETerritorial | numeric(5) | No | - |  |  |
| ETSector | numeric(5) | No | - |  |  |
| Coeficente_Empresa_Empleadora | numeric(5) | No | - |  |  |
| Id_Tipo_Participacion | char(3) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| CoeficienteTarifa | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| DescuentoMasivo | money(8) | No | - |  |  |
| Estipendio_por_Estudio | bit(1) | No | - |  |  |
| Cuantia_Estipendio | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Cta_MNac | char(16) | No | - |  |  |
| Cta_Divisa | char(16) | No | - |  |  |
| Nomb_Apell | char(25) | No | - |  |  |
| PagoMSAntig | bit(1) | No | - |  |  |
| PagoTarjetaMagnetica | bit(1) | No | - |  |  |
| Calculo_por_tarifa_diaria | bit(1) | No | - |  |  |
| CodTurno | char(3) | No | - |  |  |
| CodMSClasifEmplEstim | char(3) | No | - |  |  |
| Pago_Divisa | bit(1) | No | - |  |  |
| Importe_Vacaciones_Adelantadas | money(8) | No | - |  |  |
| Importe_Vacaciones_Mes | money(8) | No | - |  |  |
| Vacaciones_Descontadas | numeric(5) | No | - |  |  |
| Importe_Descontado | money(8) | No | - |  |  |
| Dias_Vacaciones_Adelantados | numeric(5) | No | - |  |  |
| Orden_Salidas | int(4) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| NominaSeparada | bit(1) | No | - |  |  |
| Tarifa_Divisa | money(8) | No | - |  |  |
| Salario_Divisa | money(8) | No | - |  |  |
| Pension | money(8) | No | - |  |  |
| Apellido_2 | varchar(50) | No | - |  |  |
| CUPEstimuloAcumVac | money(8) | No | - |  |  |
| Id_Beneficiario | char(15) | No | - |  |  |
| Beneficiario | varchar(50) | No | - |  |  |
| PagoTarjetaMagneticaCUC | bit(1) | No | - |  |  |
| Pago_Comedor_CUC | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Adel_Acm | money(8) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |
| Pago_Adel_Cuota | money(8) | No | - |  |  |
| Pago_Adel_Desc_Caja | money(8) | No | - |  |  |

**Clave primaria:** Id_Empleado

**Restricciones CHECK:**
- CK_RH_Empleados_Nomina_CoeficienteTarifa: None
- CK_RH_Empleados_Nomina_Porciento_Perfeccionamiento: None

**Índices:**
- `PK_Empleados_Nomina` (CLUSTERED) [unique,PRIMARY]
- `IX_Empleados_Nomina` (NONCLUSTERED) [unique]

---

#### `RH_Empleados_Organizaciones_Masas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Id_OrgMasa | char(5) | No | - | ✅ |  |
| Desc_OrgMasa | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Expediente, Id_OrgMasa

**Índices:**
- `PK_RH_Empleados_Organizaciones_Masas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Empleados_Otros_Pagos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Id_Otro_Pago | char(7) | No | - | ✅ |  |
| Valor_Otro_Pago | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente, Id_Otro_Pago

**Índices:**
- `PK_RH_Empleados_Otros_Pagos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Especialidad_Graduado`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Especialidad | char(3) | No | - | ✅ |  |
| Desc_Especialidad | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Especialidad

**Índices:**
- `PK_RH_Especialidad_Graduado` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Expedientes_Deducciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente_Deduccion | char(15) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_Deduccion | char(5) | No | - |  |  |
| Desc_Deduccion | varchar(50) | No | - |  |  |
| Beneficiario | varchar(50) | No | - |  |  |
| Direccion_Beneficiario | varchar(60) | No | - |  |  |
| Nota | varchar(60) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |
| Saldo_Inicio | money(8) | No | - |  |  |
| Saldo_Actual | money(8) | No | - |  |  |
| Recargo | money(8) | No | - |  |  |
| Fecha | smalldatetime(4) | No | - |  |  |
| Prioridad | tinyint(1) | No | - |  |  |
| Primer_Pago | bit(1) | No | - |  |  |
| Segundo_Pago | bit(1) | No | - |  |  |
| Activa | bit(1) | No | - |  |  |
| DescAutom | tinyint(1) | No | - |  |  |
| Marca | bit(1) | No | - |  |  |
| Valor_Deduccion1 | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente_Deduccion

**Índices:**
- `PK_RH_Expedientes_Deducciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Expedientes_Movimientos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NoMovExped | int(4) | No | - |  | ✅ |
| Id_ExpedienteOld | char(15) | No | - |  |  |
| Nombre | varchar(152) | No | - |  |  |
| Id_ExpedienteNew | char(15) | No | - |  |  |
| Nota | varchar(100) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

---

#### `RH_Factura`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - | ✅ | ✅ |
| Confirmada | tinyint(1) | No | - |  |  |
| Id_Factura | int(4) | No | - |  |  |
| Id_Almacen | char(5) | No | - |  |  |
| Ano_Factura | smallint(2) | No | - |  |  |
| Fecha_Confirmacion | datetime(8) | No | - |  |  |
| Fecha_Factura | datetime(8) | No | - |  |  |
| Id_Cliente | char(15) | No | - |  |  |
| Desc_Cliente | varchar(50) | No | - |  |  |
| Atte | varchar(50) | No | - |  |  |
| Id_Empleado | char(5) | No | - |  |  |
| Desc_Empleado | varchar(50) | No | - |  |  |
| Id_Pedido | int(4) | No | - |  |  |
| Ano_Oferta | smallint(2) | No | - |  |  |
| Enviado_A | varchar(50) | No | - |  |  |
| Moneda | char(5) | No | - |  |  |
| Tasa_Cambio | numeric(9) | No | - |  |  |
| ImporteTotalMB | money(8) | No | - |  |  |
| ImporteTotalMC | money(8) | No | - |  |  |
| RecargoMB | money(8) | No | - |  |  |
| RecargoMC | money(8) | No | - |  |  |
| DescuentoMB | money(8) | No | - |  |  |
| DescuentoMC | money(8) | No | - |  |  |
| ArancelMB | money(8) | No | - |  |  |
| ArancelMC | money(8) | No | - |  |  |
| RecargoMB_Porc | bit(1) | No | - |  |  |
| RecargoMC_Porc | bit(1) | No | - |  |  |
| DescuentoMB_Porc | bit(1) | No | - |  |  |
| DescuentoMC_Porc | bit(1) | No | - |  |  |
| ArancelMB_Porc | bit(1) | No | - |  |  |
| ArancelMC_Porc | bit(1) | No | - |  |  |
| AplicaArancel | bit(1) | No | - |  |  |
| AplicaPlazoCobro | bit(1) | No | - |  |  |
| EnPorciento | bit(1) | No | - |  |  |
| Nota | varchar(500) | No | - |  |  |
| Bandera | varchar(1) | No | - |  |  |
| Despachado | bit(1) | No | - |  |  |
| Referencia | varchar(20) | No | - |  |  |
| Credito | smallint(2) | No | - |  |  |
| Importe_DevueltoMB | money(8) | No | - |  |  |
| Importe_DevueltoMC | money(8) | No | - |  |  |
| Impuesto_Devuelto | money(8) | No | - |  |  |
| Forma_Pago | tinyint(1) | No | - |  |  |
| Periodo_Anterior | bit(1) | No | - |  |  |
| Id_Compro | int(4) | No | - |  |  |
| Mes_Compro | tinyint(1) | No | - |  |  |
| Ano_Compro | smallint(2) | No | - |  |  |
| Conduce | varchar(15) | No | - |  |  |
| Hora_Sal | datetime(8) | No | - |  |  |
| ChoferCI | varchar(11) | No | - |  |  |
| Despachado_Por | varchar(60) | No | - |  |  |
| Transportadopor | varchar(60) | No | - |  |  |
| Factura_Activos | bit(1) | No | - |  |  |
| Financiamiento | bit(1) | No | - |  |  |
| Agrupacion | char(5) | No | - |  |  |
| clasif_credito_factura | char(10) | No | - |  |  |
| O_Trabajo | bit(1) | No | - |  |  |
| Contabilizado | bit(1) | No | - |  |  |
| Marca_Conteo | bit(1) | No | - |  |  |
| Marca_Alertas | bit(1) | No | - |  |  |
| Xtrans | bit(1) | No | - |  |  |
| Tributable | bit(1) | No | - |  |  |
| Impuesto_Total | money(8) | No | - |  |  |
| Comision_Total | money(8) | No | - |  |  |
| Desc_Almacen | varchar(50) | No | - |  |  |
| Comision_Devuelta | money(8) | No | - |  |  |
| Cant_Art | money(8) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Contrato | varchar(20) | No | - |  |  |
| Direccion_Pto | varchar(60) | No | - |  |  |
| Id_Fpago | char(5) | No | - |  |  |
| Pais | varchar(10) | No | - |  |  |
| BL | varchar(25) | No | - |  |  |
| Naviera | varchar(30) | No | - |  |  |
| Puerto | varchar(25) | No | - |  |  |
| Buque | varchar(25) | No | - |  |  |
| Mtto | varchar(10) | No | - |  |  |
| Partida | varchar(10) | No | - |  |  |
| Bultos | varchar(10) | No | - |  |  |
| Contenedor | varchar(60) | No | - |  |  |
| Declarante | varchar(60) | No | - |  |  |
| Declaracion | char(15) | No | - |  |  |
| ContaOt | int(4) | No | - |  |  |
| Porc_Retencion | numeric(5) | No | - |  |  |
| Porc_RetencionMC | numeric(5) | No | - |  |  |
| NoServicio | varchar(20) | No | - |  |  |
| Doc_Primario | char(20) | No | - |  |  |
| No_Prelacion | int(4) | No | - |  |  |
| Factura_Nominas | tinyint(1) | No | - |  |  |

**Clave primaria:** Contador

**Índices:**
- `PK_RH_Factura` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Fundamentacion_Altas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_FundamentacionAlta | char(5) | No | - | ✅ |  |
| Desc_FundamentacionAlta | char(50) | No | - |  |  |

**Clave primaria:** Id_FundamentacionAlta

**Índices:**
- `PK_RH_Fundamentacion_Altas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Afectados_Pago_Divisa`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Afectados_Pago_Divisa_Mes: None
- CK_RH_Generales_Reporte_Afectados_Pago_Divisa_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_Afectados_Pago_Divisa` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Ajustes`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Ajustes_Mes: None
- CK_RH_Generales_Reporte_Ajustes_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_Ajustes` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Ausencias`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Ausencias_Tipo_Pago: None
- CK_RH_Generales_Reporte_Ausencias_Mes: None

**Índices:**
- `PK_RH_Generales_Reporte_Ausencias` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_CLA`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_CLA_Mes: None
- CK_RH_Generales_Reporte_CLA_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_CLA` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Descuento_Comedor`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Descuento_Comedor` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Divisa`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Confirmada | bit(1) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Divisa` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Estimulacion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| Confirmada | bit(1) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Estimulacion` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Estimulacion_Puntos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Estimulacion_Puntos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Horas_Extra`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Horas_Extra_Mes: None
- CK_RH_Generales_Reporte_Horas_Extra_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_Horas_Extra` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Idoneidad_Movil`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Idoneidad_Movil_Mes: None
- CK_RH_Generales_Reporte_Idoneidad_Movil_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_Idoneidad_Movil` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Impuesto_CSS`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Impuesto_CSS` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_MS`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_MS_Mes: None
- CK_RH_Generales_Reporte_MS_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_MS` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Nominillas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Nominillas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Otros_Pagos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Otros_Pagos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Pago_Comedor`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Pago_Comedor` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_PreNomina`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_PreNomina_Mes: None
- CK_RH_Generales_Reporte_PreNomina_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_PreNomina` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Reintegros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Reintegros_Tipo_Pago: None
- CK_RH_Generales_Reporte_Reintegros_Mes: None

**Índices:**
- `PK_RH_Generales_Reporte_Reintegros` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Índices:**
- `PK_RH_Generales_Reporte_Subsidios` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Tarifa_Horaria`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Tarifa_Horaria_Mes: None
- CK_RH_Generales_Reporte_Tarifa_Horaria_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_Tarifa_Horaria` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Vacaciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Vacaciones_Mes: None
- CK_RH_Generales_Reporte_Vacaciones_Tipo_Pago: None

**Índices:**
- `PK_RH_Generales_Reporte_Vacaciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Generales_Reporte_Vinculacion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Restricciones CHECK:**
- CK_RH_Generales_Reporte_Vinculacion_Mes: None
- CK_RH_Generales_Reporte_Vinculacion_Tipo_Pago: None

---

#### `RH_Grados_Cientificos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Grado_Cientifico | char(5) | No | - | ✅ |  |
| Desc_Grado_Cientifico | varchar(50) | No | - |  |  |
| Identificacion | char(2) | No | - |  |  |

**Clave primaria:** Id_Grado_Cientifico

**Índices:**
- `PK_RH_Grados_Cientificos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_GrpEvaluativos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_GrpEvaluativo | char(7) | No | - | ✅ |  |
| Desc_GrpEvaluativo | varchar(50) | No | - |  |  |

**Clave primaria:** Id_GrpEvaluativo

**Índices:**
- `PK_RH_GrpEvaluativos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_GrpSendRec`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_GrpSendRec | char(7) | No | - | ✅ |  |
| Desc_GrpSendRec | varchar(50) | No | - |  |  |

**Clave primaria:** Id_GrpSendRec

**Índices:**
- `PK_RH_GrpSendRec` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Grupo_Escala`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NGrupo | char(3) | No | - | ✅ |  |
| RGraduados | smallmoney(4) | No | - |  |  |
| Tecnicos_T1 | smallmoney(4) | No | - |  |  |
| Tecnicos_T2 | smallmoney(4) | No | - |  |  |
| Tecnicos_T3 | smallmoney(4) | No | - |  |  |
| Administrativos | smallmoney(4) | No | - |  |  |
| Servicios | smallmoney(4) | No | - |  |  |
| Obreros | smallmoney(4) | No | - |  |  |
| Dirigentes | smallmoney(4) | No | - |  |  |
| MSObreros | money(8) | No | - |  |  |
| MSServicios | money(8) | No | - |  |  |
| MSTecnicos | money(8) | No | - |  |  |
| MSAdministrativos | money(8) | No | - |  |  |
| MSDirigentes | money(8) | No | - |  |  |

**Clave primaria:** NGrupo

**Restricciones CHECK:**
- CK_RH_Grupo_Escala_Administrativos: None
- CK_RH_Grupo_Escala_Dirigentes: None
- CK_RH_Grupo_Escala_Obreros: None
- CK_RH_Grupo_Escala_RGraduados: None
- CK_RH_Grupo_Escala_Servicios: None
- CK_RH_Grupo_Escala_Tecnicos_T1: None
- CK_RH_Grupo_Escala_Tecnicos_T2: None
- CK_RH_Grupo_Escala_Tecnicos_T3: None

**Índices:**
- `PK_RH_Grupo_Escala` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Grupo_Escala_Bak`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NGrupo | char(3) | No | - |  |  |
| RGraduados | smallmoney(4) | No | - |  |  |
| Tecnicos_T1 | smallmoney(4) | No | - |  |  |
| Tecnicos_T2 | smallmoney(4) | No | - |  |  |
| Tecnicos_T3 | smallmoney(4) | No | - |  |  |
| Administrativos | smallmoney(4) | No | - |  |  |
| Servicios | smallmoney(4) | No | - |  |  |
| Obreros | smallmoney(4) | No | - |  |  |
| Dirigentes | smallmoney(4) | No | - |  |  |
| MSObreros | money(8) | No | - |  |  |
| MSServicios | money(8) | No | - |  |  |
| MSTecnicos | money(8) | No | - |  |  |
| MSAdministrativos | money(8) | No | - |  |  |
| MSDirigentes | money(8) | No | - |  |  |

---

#### `RH_Historico_CSS_IIP`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| CSS | money(8) | No | - |  |  |
| IIP | money(8) | No | - |  |  |
| CSS_Saldo | money(8) | No | - |  |  |
| IIP_Saldo | money(8) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Devengado_IIP | money(8) | No | - |  |  |

---

#### `RH_Historico_Empleados_Altas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  | ✅ |
| Id_Expediente | char(15) | No | - |  |  |
| No_CI | char(15) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_Cargo | char(5) | No | - |  |  |
| AnosServicio | tinyint(1) | No | - |  |  |
| Fecha_Contratacion | smalldatetime(4) | No | - |  |  |
| Id_CausaAlta | char(5) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Porciento_Estimulo | numeric(5) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Invalidez_Parcial | money(8) | No | - |  |  |
| Ex_Combatientes | money(8) | No | - |  |  |
| Porciento_Perfeccionamiento | numeric(5) | No | - |  |  |
| Valor_Divisa | money(8) | No | - |  |  |
| Porciento_Pago_Divisa | numeric(5) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Porciento_Estimulacion | numeric(5) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| IETerritorial | numeric(5) | No | - |  |  |
| ETSector | numeric(5) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| CoeficienteTarifa | money(8) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Id_Categoria | char(5) | No | - |  |  |
| Id_Provincia | char(5) | No | - |  |  |
| Id_Municipio | char(5) | No | - |  |  |
| Numero_Radicacion_Plaza | char(50) | No | - |  |  |
| Fecha_Terminacion_Contrato | smalldatetime(4) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

---

#### `RH_Historico_Empleados_Bajas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  | ✅ |
| Id_Expediente | char(15) | No | - |  |  |
| No_CI | char(15) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Id_Cargo | char(5) | No | - |  |  |
| AnosServicio | tinyint(1) | No | - |  |  |
| Fecha_Contratacion | smalldatetime(4) | No | - |  |  |
| Fecha_Baja | smalldatetime(4) | No | - |  |  |
| Id_CausaBaja | char(5) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Porciento_Estimulo | numeric(5) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Invalidez_Parcial | money(8) | No | - |  |  |
| Ex_Combatientes | money(8) | No | - |  |  |
| Porciento_Perfeccionamiento | numeric(5) | No | - |  |  |
| Valor_Divisa | money(8) | No | - |  |  |
| Porciento_Pago_Divisa | numeric(5) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Porciento_Estimulacion | numeric(5) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| IETerritorial | numeric(5) | No | - |  |  |
| ETSector | numeric(5) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| CoeficienteTarifa | money(8) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Id_Categoria | char(5) | No | - |  |  |
| Id_Provincia | char(5) | No | - |  |  |
| Id_Municipio | char(5) | No | - |  |  |
| Numero_Radicacion_Plaza | char(50) | No | - |  |  |
| Fecha_Terminacion_Contrato | smalldatetime(4) | No | - |  |  |
| Salario_Divisa | money(8) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

---

#### `RH_Historico_Empleados_Datos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_CCosto | char(10) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Nivel_Nomina | tinyint(1) | No | - |  |  |
| Id_Direccion_Nomina | char(15) | No | - |  |  |

---

#### `RH_Historico_Estimulacion_Puntos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| CUCPromIndex | money(8) | No | - |  |  |
| CUPEstimulo | money(8) | No | - |  |  |
| CUPEstimuloVac | money(8) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Historico_Estimulacion_Puntos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Historico_Inicio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Cerrado | bit(1) | No | - |  |  |
| Nomina_Cerrada | bit(1) | No | - |  |  |

---

#### `RH_Historico_Nomina_FeriadosSF`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |

---

#### `RH_Historico_Nomina_FeriadosVC`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |

---

#### `RH_Historico_Nomina_Sueldo_Fijo`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Actividad | char(3) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Salario_Basico_Medidas | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| IETerritorial | money(8) | No | - |  |  |
| ETSector | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| Dias_Trabajados | numeric(9) | No | - |  |  |
| Dias_Trabajados_para_Subsidio | numeric(9) | No | - |  |  |
| Dias_Adelantados_Rebajados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Subsidio_sin_Reporte | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interruptos_Reubicados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Suspension | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion60 | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion100 | numeric(9) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Devengado_para_Subsidio | money(8) | No | - |  |  |
| Devengado_por_Interrupcion | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| Devengado_por_Subsidio_sin_Reporte | money(8) | No | - |  |  |
| Devengado_Tarjeta | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Otros_Salarios | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| DeduccionesSalario | money(8) | No | - |  |  |
| DeduccionesReubicados | money(8) | No | - |  |  |
| DeduccionesInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosReubicados | money(8) | No | - |  |  |
| OtrosDescuentosSalario | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| SalarioResultado | money(8) | No | - |  |  |
| PerfecInterrupto | money(8) | No | - |  |  |
| PerfecReubicados | money(8) | No | - |  |  |
| PerfecSalario | money(8) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| Importe_Sobrecumplimiento | money(8) | No | - |  |  |
| Dias_Acumulado_Pago | numeric(5) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Doble_Turno | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| TarifaInterrupto | money(8) | No | - |  |  |
| Marca | bit(1) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Divisa_Factura | money(8) | No | - |  |  |
| HrsExtra_Divisa_Factura | money(8) | No | - |  |  |
| Regimen_Salarial | tinyint(1) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor_CUC | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Comedor_Dias | tinyint(1) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Otros_Pagos | money(8) | No | - |  |  |
| DescuentoMasivo | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| Hrs_Trabajadas | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Historico_Nomina_Vinculados`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Salario_Basico_Medidas | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| TarifaInterrupto | money(8) | No | - |  |  |
| Horas_Trabajadas | numeric(5) | No | - |  |  |
| Horas_Interrupto | numeric(5) | No | - |  |  |
| Horas_Actividad | numeric(5) | No | - |  |  |
| Horas_Real_Trabajadas | numeric(5) | No | - |  |  |
| Horas_Adelantadas | numeric(5) | No | - |  |  |
| Dias_a_Pagar_por_Subsidio_sin_Reporte | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interruptos_Reubicados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Suspension | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion60 | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion100 | numeric(9) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Devengado_Tarjeta | money(8) | No | - |  |  |
| DevengadoporSombrecumplimiento | money(8) | No | - |  |  |
| Devengado_Horas_Interrupcion | money(8) | No | - |  |  |
| Devengado_Horas_Tasadas | money(8) | No | - |  |  |
| Devengado_Horas_Adelantadas | money(8) | No | - |  |  |
| Devengado_Actividad | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_por_Interrupcion | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| Devengado_por_Subsidio_sin_Reporte | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| DeduccionesSalario | money(8) | No | - |  |  |
| DeduccionesReubicados | money(8) | No | - |  |  |
| DeduccionesInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosReubicados | money(8) | No | - |  |  |
| OtrosDescuentosSalario | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| PerfecInterrupto | money(8) | No | - |  |  |
| PerfecReubicados | money(8) | No | - |  |  |
| PerfecSalario | money(8) | No | - |  |  |
| Importe_Adelantado_Rebajado | money(8) | No | - |  |  |
| Dias_Acumulado_Pago | numeric(5) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor_CUC | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Comedor_Dias | tinyint(1) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Otros_Pagos | money(8) | No | - |  |  |
| DescuentoMasivo | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| Hrs_Trabajadas | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Historico_Nominilla`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Dias_a_Pagar | numeric(5) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Devengado_Tarjeta | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Ano_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Tarjeta | tinyint(1) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Pago_Divisa | bit(1) | No | - |  |  |
| Salario_BasicoMS | money(8) | No | - |  |  |
| Nominilla_Mov | bit(1) | No | - |  |  |
| Item | bigint(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Tarifa_Divisa | money(8) | No | - |  |  |
| Divisa_Factura | money(8) | No | - |  |  |
| Facturar | bit(1) | No | - |  |  |
| Impresa_Grupo | smallint(2) | No | - |  |  |
| Dias_Tarjeta | numeric(5) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |

---

#### `RH_Historico_Otros_Pagos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Otro_Pago | char(7) | No | - |  |  |
| Valor_Otro_Pago | money(8) | No | - |  |  |
| Importe_Otro_Pago | money(8) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |

---

#### `RH_Historico_Submayor_Deducciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente_Deduccion | char(15) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Deduccion | char(5) | No | - |  |  |
| RestaSaldo | bit(1) | No | - |  |  |
| Cuota | money(8) | No | - |  |  |
| Ajuste | money(8) | No | - |  |  |
| SaldoInicial | money(8) | No | - |  |  |
| SaldoFinal | money(8) | No | - |  |  |
| DeduccionesporSalario | money(8) | No | - |  |  |
| DeduccionesporVacaciones | money(8) | No | - |  |  |
| DeduccionesporSubsidios | money(8) | No | - |  |  |
| DeduccionesporEstipendio | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente_Deduccion

**Índices:**
- `PK_RH_Historico_Submayor_Deducciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Historico_Submayor_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| SaldoIni | money(8) | No | - |  |  |
| SaldoFin | money(8) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Historico_Submayor_Subsidios` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Historico_Submayor_Vacaciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| SaldoInicialDias | numeric(5) | No | - |  |  |
| SaldoInicialImporte | money(8) | No | - |  |  |
| DevengadoDias | numeric(5) | No | - |  |  |
| DevengadoImporte | money(8) | No | - |  |  |
| VacacionesDias | numeric(5) | No | - |  |  |
| VacacionesImporte | money(8) | No | - |  |  |
| AcumVacacionesDias | numeric(5) | No | - |  |  |
| AcumVacacionesImporte | money(8) | No | - |  |  |
| AjusteDias | numeric(5) | No | - |  |  |
| AjusteImporte | money(8) | No | - |  |  |
| SaldoDias | numeric(5) | No | - |  |  |
| SaldoImporte | money(8) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Historico_Submayor_Vacaciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Historico_Subsidio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Cantidad | numeric(9) | No | - |  |  |
| Importe_Pagado | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Neto_a_Cobrar | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Dias_Acumulado_Mes | numeric(5) | No | - |  |  |
| Salario_Acumulado_Mes | money(8) | No | - |  |  |
| Tipo | tinyint(1) | No | - |  |  |
| Marca | char(1) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Ano_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Tarjeta | tinyint(1) | No | - |  |  |
| Importe_Tarjeta | money(8) | No | - |  |  |
| Clasificacion_Categ_Ocupac | tinyint(1) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Historico_Vacaciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Dias_Solicitados | numeric(5) | No | - |  |  |
| Dias_Pagados | numeric(5) | No | - |  |  |
| Dias_Pagados_Adelantados | numeric(5) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Importe_Pagado | money(8) | No | - |  |  |
| Importe_Periodo | money(8) | No | - |  |  |
| Importe_Adelantado | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Neto_a_Cobrar | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Ano_Adelantado_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Adelantado_Tarjeta | tinyint(1) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_IIP_Escalas_Prog`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Escala1 | money(8) | No | - |  |  |
| Escala2 | money(8) | No | - |  |  |
| Porc_IIP | numeric(5) | No | - |  |  |

---

#### `RH_Idiomas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Idioma | char(3) | No | - | ✅ |  |
| Desc_Idioma | varchar(15) | No | - |  |  |
| ReportFlag | bit(1) | No | - |  |  |

**Clave primaria:** Id_Idioma

**Índices:**
- `PK_RH_Idiomas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Inicio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Cerrado | bit(1) | No | - |  |  |
| Titulo_Pago | char(255) | No | - |  |  |
| Nomina_Cerrada | bit(1) | No | - |  |  |

**Restricciones CHECK:**
- CK_RH_Inicio_Mes: None
- CK_RH_Inicio_Tipo_Pago: None

---

#### `RH_Jornadas_Irregulares`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Jornada | char(5) | No | - | ✅ |  |
| Desc_Jornada | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Jornada

**Índices:**
- `PK_RH_Jornadas_Irregulares` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Jornadas_Laborales`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Jornada | char(5) | No | - | ✅ |  |
| Desc_Jornada | varchar(50) | No | - |  |  |
| Lun_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lun_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Mar_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Mar_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Mie_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Mie_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Jue_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Jue_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Vie_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Vie_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Sab_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Sab_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Dom_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Dom_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Lun_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Lun_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Mar_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Mar_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Mie_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Mie_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Jue_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Jue_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Vie_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Vie_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Sab_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Sab_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Lunch_Dom_Hora_Ini | smalldatetime(4) | No | - |  |  |
| Lunch_Dom_Hora_Fin | smalldatetime(4) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

**Clave primaria:** Id_Jornada

**Índices:**
- `PK_RH_Jornadas_Laborales` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSAntiguedad`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Codigo | char(3) | No | - | ✅ |  |
| Descripcion | varchar(50) | No | - |  |  |
| LimiteInferior | tinyint(1) | No | - |  |  |
| LimiteSuperior | tinyint(1) | No | - |  |  |
| Porciento | money(8) | No | - |  |  |

**Clave primaria:** Codigo

**Índices:**
- `PK_RH_MSAntiguedad` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSAntiguedad_GS_CO`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NGrupo | tinyint(1) | No | - | ✅ |  |
| Codigo | char(3) | No | - | ✅ |  |
| Descripcion | varchar(50) | No | - |  |  |
| LimiteInferior | tinyint(1) | No | - |  |  |
| LimiteSuperior | tinyint(1) | No | - |  |  |
| Obreros | money(8) | No | - |  |  |
| Servicios | money(8) | No | - |  |  |
| Tecnicos | money(8) | No | - |  |  |
| Administrativos | money(8) | No | - |  |  |
| Dirigentes | money(8) | No | - |  |  |

**Clave primaria:** Codigo, NGrupo

**Índices:**
- `PK_RH_MSAntiguedad_GS_CO` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSClasifEmpleadosEstimulacion`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| CodMSClasifEmplEstim | char(3) | No | - | ✅ |  |
| DescMSClasifEmplEstim | char(25) | No | - |  |  |
| PorcientoCumplimiento | numeric(5) | No | - |  |  |
| PorcientoSobrecumplimiento | numeric(5) | No | - |  |  |

**Clave primaria:** CodMSClasifEmplEstim

**Índices:**
- `PK_RH_MSClasifEmpleadosEstimulacion` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSEstimuloCargosEconom`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Cargo | char(5) | No | - | ✅ |  |
| Desc_Cargo | varchar(120) | No | - |  |  |
| Cuantia | money(8) | No | - |  |  |

**Clave primaria:** Id_Cargo

**Índices:**
- `PK_RH_MSEstimuloCargosEconom` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSGruposTrabajadores`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| MSCodGrupo | char(3) | No | - | ✅ |  |
| MSDescGrupo | varchar(50) | No | - |  |  |
| MSPagoCoeficiente | bit(1) | No | - |  |  |
| MSPagoAntiguedad | bit(1) | No | - |  |  |
| MSPagoTurno | bit(1) | No | - |  |  |

**Clave primaria:** MSCodGrupo

**Índices:**
- `PK_RH_MSGruposTrabajadores` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSIncidenciasEstimulo`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| CodIncidencia | char(3) | No | - | ✅ |  |
| DescIncidencia | varchar(50) | No | - |  |  |
| PorcientoAfectacion | numeric(5) | No | - |  |  |

**Clave primaria:** CodIncidencia

**Índices:**
- `PK_RH_MSIncidenciasEstimulo` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSIncidenciasEstimuloCargosEconom`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| CodIncidencia | char(3) | No | - | ✅ |  |
| DescIncidencia | varchar(50) | No | - |  |  |
| PorcientoAfectacion | numeric(5) | No | - |  |  |
| LimiteInferior | tinyint(1) | No | - |  |  |
| LimiteSuperior | tinyint(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |

**Clave primaria:** CodIncidencia

**Índices:**
- `PK_RH_MSIncidenciasEstimuloCargosEconom` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSIncidenciasMS`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| CodIncidencia | char(3) | No | - | ✅ |  |
| DescIncidencia | varchar(50) | No | - |  |  |
| PorcientoAfectacion | numeric(5) | No | - |  |  |
| LimiteInferior | tinyint(1) | No | - |  |  |
| LimiteSuperior | tinyint(1) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| AfectaAntiguedad | bit(1) | No | - |  |  |
| AfectaCoeficiente | bit(1) | No | - |  |  |
| AfectaTurno | bit(1) | No | - |  |  |

**Clave primaria:** CodIncidencia

**Restricciones CHECK:**
- CK_RH_MSIncidenciasMS_Clasificacion: None

**Índices:**
- `PK_RH_MSIncidenciasMS` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_MSTurnosTrabajo`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| CodTurno | char(3) | No | - | ✅ |  |
| DescTurno | varchar(50) | No | - |  |  |
| Cuantia | money(8) | No | - |  |  |

**Clave primaria:** CodTurno

**Índices:**
- `PK_RH_MSTurnosTrabajo` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Municipios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Provincia | char(5) | No | - | ✅ |  |
| Id_Municipio | char(5) | No | - | ✅ |  |
| Desc_Municipio | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Provincia, Id_Municipio

**Índices:**
- `PK_RH_Municipios` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Niveles_Escolaridad`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Nivel_Escolaridad | char(3) | No | - | ✅ |  |
| Desc_Nivel_Escolaridad | varchar(50) | No | - |  |  |
| Id_Nivel_Escolaridad_Clasif | char(3) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Siglas | char(3) | No | - |  |  |

**Clave primaria:** Id_Nivel_Escolaridad

**Restricciones CHECK:**
- CK_RH_Niveles_Escolaridad_Nivel: None

**Índices:**
- `PK_RH_Niveles_Escolaridad` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Niveles_Escolaridad_Clasif`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Nivel_Escolaridad_Clasif | char(3) | No | - | ✅ |  |
| Desc_Nivel_Escolaridad_Clasif | char(15) | No | - |  |  |

**Clave primaria:** Id_Nivel_Escolaridad_Clasif

**Índices:**
- `PK_RH_Niveles_Escolaridad_Clasif` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Obras`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Obra | char(10) | No | - | ✅ |  |
| Desc_Obra | varchar(50) | No | - |  |  |

**Clave primaria:** Id_Obra

**Índices:**
- `PK_RH_Obras` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Organizaciones_Masas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_OrgMasa | char(5) | No | - | ✅ |  |
| Desc_OrgMasa | varchar(50) | No | - |  |  |

**Clave primaria:** Id_OrgMasa

**Índices:**
- `PK_RH_Organizaciones_Masas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Otros_Pagos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Otro_Pago | char(7) | No | - | ✅ |  |
| Desc_Otro_Pago | varchar(50) | No | - |  |  |
| Valor_Otro_Pago | money(8) | No | - |  |  |
| Afecta_Ausencias | bit(1) | No | - |  |  |
| Acumula_Vacaciones | bit(1) | No | - |  |  |
| Incluir_SNC_225 | bit(1) | No | - |  |  |
| Grupo | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_Otro_Pago

**Índices:**
- `PK_RH_Otros_Pagos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Parametros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Logo | image(16) | Sí | - |  |  |
| Nombre_Empresa | char(100) | No | - |  |  |
| Titulo | char(100) | No | - |  |  |
| SubTitulo | char(100) | No | - |  |  |
| Id_ClaveSabado | char(5) | No | - |  |  |
| Id_ClaveInterrupc100 | char(5) | No | - |  |  |
| Cant_Niveles | tinyint(1) | No | - |  |  |
| Nivel1 | char(25) | No | - |  |  |
| Nivel2 | char(25) | No | - |  |  |
| Nivel3 | char(25) | No | - |  |  |
| Nivel4 | char(25) | No | - |  |  |
| Nivel5 | char(25) | No | - |  |  |
| Nomina_HechoPor | char(50) | No | - |  |  |
| Nomina_AprobPor | char(50) | No | - |  |  |
| Nomina_RevPor | char(50) | No | - |  |  |
| Nomina_ContabPor | char(50) | No | - |  |  |
| NombreContratador | char(50) | No | - |  |  |
| CargoContratador | char(50) | No | - |  |  |
| Tallas_Ropa | bit(1) | No | - |  |  |
| Docencia_Investig | bit(1) | No | - |  |  |
| Defensa | bit(1) | No | - |  |  |
| Organizaciones | bit(1) | No | - |  |  |
| Idiomas | bit(1) | No | - |  |  |
| Antiguedad | bit(1) | No | - |  |  |
| Pago_Divisa | bit(1) | No | - |  |  |
| Estimulo_Salarial | bit(1) | No | - |  |  |
| PagoIdoneidad | bit(1) | No | - |  |  |
| Porc_Estimulacion_Salarial | bit(1) | No | - |  |  |
| Otros_Pagos | bit(1) | No | - |  |  |
| GeneraAutomNoExped | bit(1) | No | - |  |  |
| MaxLongAutomNoExped | tinyint(1) | No | - |  |  |
| AjustarCentavos | bit(1) | No | - |  |  |
| CalculosAutomaticos | bit(1) | No | - |  |  |
| HorasExtrasconReporte | bit(1) | No | - |  |  |
| CLAconReporte | bit(1) | No | - |  |  |
| ReportarEstimulacion | bit(1) | No | - |  |  |
| PerfeccionamientoSubsidio | bit(1) | No | - |  |  |
| PerfeccionamientoconVacaciones | bit(1) | No | - |  |  |
| MSAntigTipoPago | tinyint(1) | No | - |  |  |
| IdoneidadconAusentismo | bit(1) | No | - |  |  |
| ContratoPerfeccionamiento | bit(1) | No | - |  |  |
| NominaInterrupto | bit(1) | No | - |  |  |
| DescuentoContravalor | bit(1) | No | - |  |  |
| ControlSalario | bit(1) | No | - |  |  |
| ControlPlazas | bit(1) | No | - |  |  |
| PorcientoPerfeccionamiento | numeric(5) | No | - |  |  |
| PorcientoInterrupcion | numeric(5) | No | - |  |  |
| PorcientoTiempoTasadoaPagar | numeric(5) | No | - |  |  |
| TarifaPagoVinculacion | money(8) | No | - |  |  |
| DiasVenceReintegros | smallint(2) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |
| MSSalarioEscalaBaseCalculo | bit(1) | No | - |  |  |
| MSPlus | bit(1) | No | - |  |  |
| MSAntiguedad | bit(1) | No | - |  |  |
| MSOtros | bit(1) | No | - |  |  |
| MSSalarioporCargo | bit(1) | No | - |  |  |
| MSAlbergamiento | bit(1) | No | - |  |  |
| MSHorarioIrregular | bit(1) | No | - |  |  |
| MSCondiciones | bit(1) | No | - |  |  |
| MSIETerritorial | bit(1) | No | - |  |  |
| MSETSector | bit(1) | No | - |  |  |
| Agrupacion | char(5) | No | - |  |  |
| AjustarCentavosVacaciones | bit(1) | No | - |  |  |
| TipoReloj | tinyint(1) | No | - |  |  |
| ClaveImpunt | char(5) | No | - |  |  |
| Titulo2doFormatoNominaSalario | char(100) | No | - |  |  |
| Titulo2doFormatoNominaVacaciones | char(100) | No | - |  |  |
| Titulo2doFormatoNominaSubsidios | char(100) | No | - |  |  |
| Agencia_Empleadora | bit(1) | No | - |  |  |
| CoeficienteHorasExtras | money(8) | No | - |  |  |
| Id_Almacen_Factura | char(5) | No | - |  |  |
| Id_Clasifactura_Salario | char(10) | No | - |  |  |
| Id_Clasifactura_Indemnizacion | char(10) | No | - |  |  |
| Moneda_Factura | char(5) | No | - |  |  |
| Id_Deduccion_PagoIndebido | char(5) | No | - |  |  |
| Id_ClaveReloj | char(5) | No | - |  |  |
| Horario_Almuerzo | bit(1) | No | - |  |  |
| MSSalarioPagoActual | tinyint(1) | No | - |  |  |
| Id_ClaveDecreto_Ley_91 | char(5) | No | - |  |  |
| PerfeccionamientoSoloDevengado | bit(1) | No | - |  |  |
| MSIdoneidadFijo | bit(1) | No | - |  |  |
| MSIdoneidadMovil | bit(1) | No | - |  |  |
| Afecta_Estimulacion_Ausencias | bit(1) | No | - |  |  |
| Pago_Interrup_Tarifa_Diaria | bit(1) | No | - |  |  |
| Puerto_Serie | tinyint(1) | No | - |  |  |
| Total_Nodos | tinyint(1) | No | - |  |  |
| Tiempo_Espera | int(4) | No | - |  |  |
| MS_Pago_Nominillas | bit(1) | No | - |  |  |
| Tarifa_Hrs_Extras_Salario_Basico | bit(1) | No | - |  |  |
| MSSalarioEscalaBaseCalculo1 | bit(1) | No | - |  |  |
| MSPlus1 | bit(1) | No | - |  |  |
| MSAntiguedad1 | bit(1) | No | - |  |  |
| MSOtros1 | bit(1) | No | - |  |  |
| MSSalarioporCargo1 | bit(1) | No | - |  |  |
| MSAlbergamiento1 | bit(1) | No | - |  |  |
| MSHorarioIrregular1 | bit(1) | No | - |  |  |
| MSCondiciones1 | bit(1) | No | - |  |  |
| MSIETerritorial1 | bit(1) | No | - |  |  |
| MSETSector1 | bit(1) | No | - |  |  |
| MSIdoneidadFijo1 | bit(1) | No | - |  |  |
| MSIdoneidadMovil1 | bit(1) | No | - |  |  |
| SNC_EA_PR_Prom_Subs | bit(1) | No | - |  |  |
| MSAno | smallint(2) | No | - |  |  |
| MSMes | tinyint(1) | No | - |  |  |
| Tipo_Hrs_Extras_Reloj | tinyint(1) | No | - |  |  |
| Cant_Min_Hrs_Extras_Reloj | tinyint(1) | No | - |  |  |
| MSCoeficienteconDevengado | bit(1) | No | - |  |  |
| MSCoeficienteTipoPago | tinyint(1) | No | - |  |  |
| MSCoeficientePorciento | tinyint(1) | No | - |  |  |
| Estimulacion_Puntos | bit(1) | No | - |  |  |
| ShopConvertIndex | money(8) | No | - |  |  |
| CUCPromIndex | money(8) | No | - |  |  |
| Estimulacion_Puntos_Salario_Max | money(8) | No | - |  |  |
| Estimulacion_Puntos_Cuantia_Min | money(8) | No | - |  |  |
| Pago_Feriados_Salario_Promedio | bit(1) | No | - |  |  |
| Aplicar_Retenciones_VacacAdelant_PagoMensual | bit(1) | No | - |  |  |
| Pago_Adicional | bit(1) | No | - |  |  |
| Pago_Comedor_Desglose | bit(1) | No | - |  |  |
| Pago_Comedor_Banco | bit(1) | No | - |  |  |
| TC_People | money(8) | No | - |  |  |
| PorcientoSeguroSocialPlazoLargo | numeric(5) | No | - |  |  |
| PorcientoSeguroSocialPlazoCorto | numeric(5) | No | - |  |  |
| PorcientoUtilizaFuerzaTrabajo | numeric(5) | No | - |  |  |
| OtrosPagosconReporte | bit(1) | No | - |  |  |
| Path_Envio | varchar(200) | No | - |  |  |
| Path_Recibo | varchar(200) | No | - |  |  |
| Suc_Bancaria | char(3) | No | - |  |  |
| Centro_Pago_BPA | char(8) | No | - |  |  |
| Id_Nominilla_Xls_Dflt | tinyint(1) | No | - |  |  |
| ZeroDay | bit(1) | No | - |  |  |
| PagoEmpleadora_TH_VC_Coef | bit(1) | No | - |  |  |
| CSS | bit(1) | No | - |  |  |
| IIP | bit(1) | No | - |  |  |
| Id_Deduccion_PA | char(5) | No | - |  |  |
| OtrosPagosTributan | bit(1) | No | - |  |  |
| DivisaconReporte | bit(1) | No | - |  |  |
| DescuentoContravalorComedor | bit(1) | No | - |  |  |
| FondoHrsLun | numeric(5) | No | - |  |  |
| FondoHrsMar | numeric(5) | No | - |  |  |
| FondoHrsMie | numeric(5) | No | - |  |  |
| FondoHrsJue | numeric(5) | No | - |  |  |
| FondoHrsVie | numeric(5) | No | - |  |  |
| FondoHrsSab | numeric(5) | No | - |  |  |
| FondoHrsDom | numeric(5) | No | - |  |  |
| Mes_13_No_Subsidio_Prom | bit(1) | No | - |  |  |
| Mes_13_No_Dias_Feriado_Prom | bit(1) | No | - |  |  |
| PSP | bit(1) | No | - |  |  |
| DescAutom_POPC_Prm | bit(1) | No | - |  |  |
| DescAutom_POPC_Fld | tinyint(1) | No | - |  |  |
| DescAutom_POPC_Cfc | money(8) | No | - |  |  |

**Restricciones CHECK:**
- CK_RH_Parametros_MaxLongAutomNoExped: None
- RH_Parametros_Cant_Niveles_Values: None

---

#### `RH_Plantilla`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Nivel | tinyint(1) | No | - | ✅ |  |
| Id_Direccion | char(15) | No | - | ✅ |  |
| Desc_Direccion | varchar(100) | No | - |  |  |
| Id_Clave | char(17) | No | - |  |  |

**Clave primaria:** Nivel, Id_Direccion

**Índices:**
- `PK_RH_Plantilla` (CLUSTERED) [unique,PRIMARY]
- `IX_RH_Plantilla` (NONCLUSTERED) [unique]

---

#### `RH_Plantilla_Detalles`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Nivel | tinyint(1) | No | - | ✅ |  |
| Id_Direccion | char(15) | No | - | ✅ |  |
| Id_Cargo | char(5) | No | - | ✅ |  |
| Desc_Cargo | varchar(120) | No | - |  |  |
| Propuesta | int(4) | No | - |  |  |
| Aprobadas | int(4) | No | - |  |  |
| Exceso | int(4) | No | - |  |  |
| CantidadPlazasAnterior | int(4) | No | - |  |  |

**Clave primaria:** Nivel, Id_Direccion, Id_Cargo

**Índices:**
- `PK_RH_Plantilla_Detalles` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Plantilla_Plazas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Plaza | bigint(8) | No | - | ✅ |  |
| Nivel | tinyint(1) | No | - | ✅ |  |
| Id_Direccion | char(15) | No | - | ✅ |  |
| Id_Cargo | char(5) | No | - | ✅ |  |
| Vacante | bit(1) | No | - |  |  |
| Orden | bigint(8) | No | - |  |  |

**Clave primaria:** Plaza, Nivel, Id_Direccion, Id_Cargo

**Índices:**
- `PK_RH_Plantilla_Plazas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Profesiones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Profesion | char(5) | No | - | ✅ |  |
| Desc_Profesion | varchar(80) | No | - |  |  |
| Id_Especialidad | char(3) | No | - |  |  |

**Clave primaria:** Id_Profesion

**Índices:**
- `PK_RH_Profesiones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Profesiones_General`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Especialidad | char(3) | No | - | ✅ |  |
| Desc_Especialidad | varchar(25) | No | - |  |  |

**Clave primaria:** Id_Especialidad

**Índices:**
- `PK_RH_Profesiones_General` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Promedio_Subsidio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Tipo | tinyint(1) | No | - | ✅ |  |
| Promedio | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente, Tipo

**Restricciones CHECK:**
- CK_RH_Promedio_Subsidio_Tipo: None

**Índices:**
- `PK_RH_Promedio_Subsidio` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Provincias`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Provincia | char(5) | No | - | ✅ |  |
| Desc_Provincia | varchar(50) | No | - |  |  |
| RepMovPendular | bit(1) | No | - |  |  |

**Clave primaria:** Id_Provincia

**Índices:**
- `PK_RH_Provincias` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Reloj_Altas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(50) | No | - |  |  |
| Apellido_1 | varchar(50) | No | - |  |  |
| Apellido_2 | varchar(50) | No | - |  |  |
| Id_Tarjeta_Reloj | char(10) | No | - |  |  |
| No_CI | char(15) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Reloj_Altas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Reloj_Bajas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| No_CI | char(15) | No | - |  |  |
| Procesado | bit(1) | No | - |  |  |
| Id_Tarjeta_Reloj | char(10) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Reloj_Bajas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Reloj_Marcajes`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Nodo | tinyint(1) | No | - |  |  |
| Id_Tarjeta_Reloj | char(15) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Fecha_Hora_Lectura | datetime(8) | No | - |  |  |

---

#### `RH_Reloj_Nodos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Nodo | tinyint(1) | No | - |  | ✅ |
| Activo | bit(1) | No | - |  |  |

---

#### `RH_Reporte_Dias_Feriados`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(152) | No | - |  |  |
| Reportar | bit(1) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Reporte_Dias_Feriados` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Resumen_de_Cobros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario | money(8) | No | - |  |  |
| Dias_Trabajados | numeric(9) | No | - |  |  |
| Vacaciones | money(8) | No | - |  |  |
| Dias_Vacaciones | numeric(9) | No | - |  |  |
| Salario_para_Subsidio | money(8) | No | - |  |  |
| Dias_Trabajados_para_Subsidio | numeric(9) | No | - |  |  |
| Subsidio | money(8) | No | - |  |  |
| Dias_Subsidio | numeric(9) | No | - |  |  |
| Maternidad | money(8) | No | - |  |  |
| Semanas_Maternidad | numeric(9) | No | - |  |  |

---

#### `RH_Salarios_Adicionales`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Tipo_Participacion | char(3) | No | - | ✅ |  |
| Desc_Tipo_Participacion | varchar(50) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | numeric(5) | No | - |  |  |

**Clave primaria:** Id_Tipo_Participacion

**Índices:**
- `PK_RH_Salarios_Adicionales` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Subcategorias_Ocupacionales`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Categoria | char(5) | No | - | ✅ |  |
| Id_Subcategoria | char(5) | No | - | ✅ |  |
| Desc_Subcategoria | varchar(50) | No | - |  |  |
| Identificacion | char(2) | No | - |  |  |

**Clave primaria:** Id_Categoria, Id_Subcategoria

**Índices:**
- `PK_RH_Subcategorias_Ocupacionales` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Subsidios_Adelantados`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Id_Clave | char(5) | No | - | ✅ |  |
| Dias_Adelantados | numeric(9) | No | - |  |  |

**Clave primaria:** Id_Expediente, Id_Clave

**Índices:**
- `PK_RH_Subsidios_Adelantados` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Tablas_Comm`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| item | int(4) | No | - |  | ✅ |
| Clasificacion | tinyint(1) | No | - |  |  |
| Nombre_Tabla | char(100) | No | - |  |  |
| Enviar | bit(1) | No | - |  |  |
| Recibir | bit(1) | No | - |  |  |
| Fecha_Envio | smalldatetime(4) | No | - |  |  |
| Fecha_Recibo | smalldatetime(4) | No | - |  |  |
| Recibido | bit(1) | No | - |  |  |
| Fichero | varchar(50) | No | - |  |  |
| FicheroDetalle | varchar(50) | No | - |  |  |
| Rinner | varchar(150) | No | - |  |  |
| Rwhere | varchar(150) | No | - |  |  |
| Truncar_Tabla | bit(1) | No | - |  |  |
| OKSend | bit(1) | No | - |  |  |
| OKReceive | bit(1) | No | - |  |  |

---

#### `RH_Tarjeta_SNC225`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| EneD | numeric(5) | No | - |  |  |
| EneI | money(8) | No | - |  |  |
| EneC | char(23) | No | - |  |  |
| FebD | numeric(5) | No | - |  |  |
| FebI | money(8) | No | - |  |  |
| FebC | char(23) | No | - |  |  |
| MarD | numeric(5) | No | - |  |  |
| MarI | money(8) | No | - |  |  |
| MarC | char(23) | No | - |  |  |
| AbrD | numeric(5) | No | - |  |  |
| AbrI | money(8) | No | - |  |  |
| AbrC | char(23) | No | - |  |  |
| MayD | numeric(5) | No | - |  |  |
| MayI | money(8) | No | - |  |  |
| MayC | char(23) | No | - |  |  |
| JunD | numeric(5) | No | - |  |  |
| JunI | money(8) | No | - |  |  |
| JunC | char(23) | No | - |  |  |
| JulD | numeric(5) | No | - |  |  |
| JulI | money(8) | No | - |  |  |
| JulC | char(23) | No | - |  |  |
| AgoD | numeric(5) | No | - |  |  |
| AgoI | money(8) | No | - |  |  |
| AgoC | char(23) | No | - |  |  |
| SepD | numeric(5) | No | - |  |  |
| SepI | money(8) | No | - |  |  |
| SepC | char(23) | No | - |  |  |
| OctD | numeric(5) | No | - |  |  |
| OctI | money(8) | No | - |  |  |
| OctC | char(23) | No | - |  |  |
| NovD | numeric(5) | No | - |  |  |
| NovI | money(8) | No | - |  |  |
| NovC | char(23) | No | - |  |  |
| DicD | numeric(5) | No | - |  |  |
| DicI | money(8) | No | - |  |  |
| DicC | char(23) | No | - |  |  |

**Clave primaria:** Ano, Id_Expediente

**Índices:**
- `PK_RH_Tarjeta_SNC225` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Temporal_CSS_IIP`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| CSS | money(8) | No | - |  |  |
| IIP | money(8) | No | - |  |  |
| CSS_Saldo | money(8) | No | - |  |  |
| IIP_Saldo | money(8) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Devengado_IIP | money(8) | No | - |  |  |

---

#### `RH_Temporal_CSS_IIP_Expedientes`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| PluriEmpleo | bit(1) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Temporal_CSS_IIP_Expedientes` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Temporal_Estimulacion_Puntos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - | ✅ |  |
| Mes | tinyint(1) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| CUCPromIndex | money(8) | No | - |  |  |
| CUPEstimulo | money(8) | No | - |  |  |
| CUPEstimuloVac | money(8) | No | - |  |  |

**Clave primaria:** Ano, Mes, Tipo_Pago, Id_Expediente

**Índices:**
- `PK_RH_Temporal_Estimulacion_Puntos` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Temporal_General`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - |  |  |
| Neto_a_Cobrar | money(8) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Devengado_Subsidio | money(8) | No | - |  |  |
| Devengado_Vacaciones | money(8) | No | - |  |  |
| Salario_Acumulado_Mes | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| Dias_Salario | numeric(9) | No | - |  |  |
| Dias_Subsidio | numeric(9) | No | - |  |  |
| Dias_Vacaciones | numeric(9) | No | - |  |  |
| Dias_Acumulado_Mes | numeric(9) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Pago_Comedor_Divisa | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Hrs_Trabajadas | numeric(5) | No | - |  |  |

---

#### `RH_Temporal_Nomina_COVID_19`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Tipo_Pago | tinyint(1) | No | - | ✅ |  |
| Dias_a_Pagar_por_Interrupcion60 | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion100 | numeric(9) | No | - |  |  |
| TarifaInterrupto | money(8) | No | - |  |  |
| Devengado_por_Interrupcion_60 | money(8) | No | - |  |  |
| Devengado_por_Interrupcion_100 | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente, Tipo_Pago

**Índices:**
- `PK_RH_Temporal_Nomina_COVID_19` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Temporal_Nomina_FeriadosSF`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |

---

#### `RH_Temporal_Nomina_FeriadosVC`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |

---

#### `RH_Temporal_Nomina_Sueldo_Fijo`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Actividad | char(3) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Salario_Basico_Medidas | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| IETerritorial | money(8) | No | - |  |  |
| ETSector | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| Dias_Trabajados | numeric(9) | No | - |  |  |
| Dias_Trabajados_para_Subsidio | numeric(9) | No | - |  |  |
| Dias_Adelantados_Rebajados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Subsidio_sin_Reporte | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interruptos_Reubicados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Suspension | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion60 | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion100 | numeric(9) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Devengado_para_Subsidio | money(8) | No | - |  |  |
| Devengado_por_Interrupcion | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| Devengado_por_Subsidio_sin_Reporte | money(8) | No | - |  |  |
| Devengado_Tarjeta | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Otros_Salarios | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| DeduccionesSalario | money(8) | No | - |  |  |
| DeduccionesReubicados | money(8) | No | - |  |  |
| DeduccionesInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosReubicados | money(8) | No | - |  |  |
| OtrosDescuentosSalario | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| SalarioResultado | money(8) | No | - |  |  |
| PerfecInterrupto | money(8) | No | - |  |  |
| PerfecReubicados | money(8) | No | - |  |  |
| PerfecSalario | money(8) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| Importe_Sobrecumplimiento | money(8) | No | - |  |  |
| Dias_Acumulado_Pago | numeric(5) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Doble_Turno | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| TarifaInterrupto | money(8) | No | - |  |  |
| Marca | bit(1) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Divisa_Factura | money(8) | No | - |  |  |
| HrsExtra_Divisa_Factura | money(8) | No | - |  |  |
| Regimen_Salarial | tinyint(1) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor_CUC | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Comedor_Dias | tinyint(1) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Otros_Pagos | money(8) | No | - |  |  |
| DescuentoMasivo | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| Hrs_Trabajadas | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Temporal_Nomina_Vinculados`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Salario_Basico_Medidas | money(8) | No | - |  |  |
| Estimulo | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| TarifaInterrupto | money(8) | No | - |  |  |
| Horas_Trabajadas | numeric(5) | No | - |  |  |
| Horas_Interrupto | numeric(5) | No | - |  |  |
| Horas_Actividad | numeric(5) | No | - |  |  |
| Horas_Real_Trabajadas | numeric(5) | No | - |  |  |
| Horas_Adelantadas | numeric(5) | No | - |  |  |
| Dias_a_Pagar_por_Subsidio_sin_Reporte | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interruptos_Reubicados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Suspension | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion60 | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion100 | numeric(9) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Devengado_Tarjeta | money(8) | No | - |  |  |
| DevengadoporSombrecumplimiento | money(8) | No | - |  |  |
| Devengado_Horas_Interrupcion | money(8) | No | - |  |  |
| Devengado_Horas_Tasadas | money(8) | No | - |  |  |
| Devengado_Horas_Adelantadas | money(8) | No | - |  |  |
| Devengado_Actividad | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_por_Interrupcion | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| Devengado_por_Subsidio_sin_Reporte | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| DeduccionesSalario | money(8) | No | - |  |  |
| DeduccionesReubicados | money(8) | No | - |  |  |
| DeduccionesInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosReubicados | money(8) | No | - |  |  |
| OtrosDescuentosSalario | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| PerfecInterrupto | money(8) | No | - |  |  |
| PerfecReubicados | money(8) | No | - |  |  |
| PerfecSalario | money(8) | No | - |  |  |
| Importe_Adelantado_Rebajado | money(8) | No | - |  |  |
| Dias_Acumulado_Pago | numeric(5) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor_CUC | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Comedor_Dias | tinyint(1) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Otros_Pagos | money(8) | No | - |  |  |
| DescuentoMasivo | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| Hrs_Trabajadas | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Temporal_Nominilla`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | bigint(8) | No | - | ✅ | ✅ |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Dias_a_Pagar | numeric(5) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Devengado_Tarjeta | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Ano_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Tarjeta | tinyint(1) | No | - |  |  |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Pago_Divisa | bit(1) | No | - |  |  |
| Salario_BasicoMS | money(8) | No | - |  |  |
| Nominilla_Mov | bit(1) | No | - |  |  |
| Impresa | bit(1) | No | - |  |  |
| Item | bigint(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Tarifa_Divisa | money(8) | No | - |  |  |
| Divisa_Factura | money(8) | No | - |  |  |
| Facturar | bit(1) | No | - |  |  |
| Impresa_Grupo | smallint(2) | No | - |  |  |
| Dias_Tarjeta | numeric(5) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |

**Clave primaria:** Contador

**Índices:**
- `PK_RH_Temporal_Nominilla` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Temporal_Otros_Pagos`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Otro_Pago | char(7) | No | - |  |  |
| Valor_Otro_Pago | money(8) | No | - |  |  |
| Afecta_Ausencias | bit(1) | No | - |  |  |
| Acumula_Vacaciones | bit(1) | No | - |  |  |
| Incluir_SNC_225 | bit(1) | No | - |  |  |
| Importe_Otro_Pago | money(8) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Dias_Deducible | numeric(9) | No | - |  |  |
| Dias_Lab | tinyint(1) | No | - |  |  |
| Tarifa | numeric(9) | No | - |  |  |
| Horas_Deducible | numeric(5) | No | - |  |  |
| FondoTiempoHrs | numeric(5) | No | - |  |  |

---

#### `RH_Temporal_Salario`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Salario_Basico_Medidas | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| Otros | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| OtrasRetribuciones | numeric(5) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| IETerritorial | money(8) | No | - |  |  |
| ETSector | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| Dias_Trabajados | numeric(9) | No | - |  |  |
| Dias_por_Subsidio | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interruptos_Reubicados | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion60 | numeric(9) | No | - |  |  |
| Dias_a_Pagar_por_Interrupcion100 | numeric(9) | No | - |  |  |
| Devengado | money(8) | No | - |  |  |
| Devengado_por_Subsidio | money(8) | No | - |  |  |
| Devengado_por_Interrupcion | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| DevengadoporSombrecumplimiento | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| DeduccionesSalario | money(8) | No | - |  |  |
| DeduccionesReubicados | money(8) | No | - |  |  |
| DeduccionesInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosInterrupto | money(8) | No | - |  |  |
| OtrosDescuentosReubicados | money(8) | No | - |  |  |
| OtrosDescuentosSalario | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| PerfecInterrupto | money(8) | No | - |  |  |
| PerfecReubicados | money(8) | No | - |  |  |
| PerfecSalario | money(8) | No | - |  |  |
| Dias_Acumulado_Pago | numeric(5) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| TarifaInterrupto | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| PagoOtros | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor_CUC | bit(1) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Comedor_Dias | tinyint(1) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Otros_Pagos | money(8) | No | - |  |  |
| DescuentoMasivo | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| Hrs_Trabajadas | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Temporal_Submayor_Deducciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente_Deduccion | char(15) | No | - | ✅ |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Deduccion | char(5) | No | - |  |  |
| RestaSaldo | bit(1) | No | - |  |  |
| Cuota | money(8) | No | - |  |  |
| Ajuste | money(8) | No | - |  |  |
| SaldoInicial | money(8) | No | - |  |  |
| SaldoFinal | money(8) | No | - |  |  |
| DeduccionesPorSalario | money(8) | No | - |  |  |
| DeduccionesPorVacaciones | money(8) | No | - |  |  |
| DeduccionesPorSubsidios | money(8) | No | - |  |  |
| DeduccionesporEstipendio | money(8) | No | - |  |  |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |

**Clave primaria:** Id_Expediente_Deduccion

**Índices:**
- `PK_RH_Temporal_Submayor_Deducciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Temporal_Subsidio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  |  |
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Cantidad | numeric(9) | No | - |  |  |
| Importe_Pagado | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Neto_a_Cobrar | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Dias_Acumulado_Mes | numeric(5) | No | - |  |  |
| Salario_Acumulado_Mes | money(8) | No | - |  |  |
| Tipo | tinyint(1) | No | - |  |  |
| Marca | char(1) | No | - |  |  |
| Id_Clave | char(5) | No | - |  |  |
| Ano_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Tarjeta | tinyint(1) | No | - |  |  |
| Importe_Tarjeta | money(8) | No | - |  |  |
| Clasificacion_Categ_Ocupac | tinyint(1) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Temporal_Vacaciones`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Ano | smallint(2) | No | - |  |  |
| Mes | tinyint(1) | No | - |  |  |
| Tipo_Pago | tinyint(1) | No | - |  |  |
| Id_Expediente | char(15) | No | - | ✅ |  |
| Dias_Solicitados | numeric(5) | No | - |  |  |
| Dias_Pagados | numeric(5) | No | - |  |  |
| Dias_Pagados_Adelantados | numeric(5) | No | - |  |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Salario_Acumulado | money(8) | No | - |  |  |
| Importe_Pagado | money(8) | No | - |  |  |
| Importe_Periodo | money(8) | No | - |  |  |
| Importe_Adelantado | money(8) | No | - |  |  |
| Deducciones | money(8) | No | - |  |  |
| Neto_a_Cobrar | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Ano_Adelantado_Tarjeta | smallint(2) | No | - |  |  |
| Mes_Adelantado_Tarjeta | tinyint(1) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Temporal_Vacaciones` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Tmp_Contabilizacion_Deducc_Nominillas_Reintegros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Deducc_Nominillas_Salario`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Deducc_Nominillas_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Deducc_Nominillas_Vacation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Deducc_Salarios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Deducc_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Deducc_Vacation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - |  |  |
| Id_Expediente_Deduccion | char(15) | No | - |  |  |
| Valor_Deduccion | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Nominillas_Reintegros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Importe_Reintegro_Salario | money(8) | No | - |  |  |
| Importe_Reintegro_Subsidio | money(8) | No | - |  |  |
| Importe_Reintegro_Vacaciones | money(8) | No | - |  |  |
| Importe_Reintegro_Divisa | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Nominillas_Salario`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Otros_Salarios | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| IETerritorial | money(8) | No | - |  |  |
| ETSector | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| Importe_Sobrecumplimiento | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| Disponibles60 | money(8) | No | - |  |  |
| Disponibles100 | money(8) | No | - |  |  |
| Importe_Devolucion_Retenciones | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Id_Actividad_Id_Ccosto_Id_Obra | char(20) | No | - |  |  |
| Decreto_Ley_91 | money(8) | No | - |  |  |
| Id_Actividad | char(3) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| Indemnizacion_con_Factura | money(8) | No | - |  |  |
| Indemnizacion_sin_Factura | money(8) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Pago_Comedor_Divisa | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| Devolucion_CSS | money(8) | No | - |  |  |
| Devolucion_IIP | money(8) | No | - |  |  |
| Mes13 | money(8) | No | - |  |  |
| Pago_Adel | money(8) | No | - |  |  |
| Covid_Int60 | money(8) | No | - |  |  |
| Covid_Int100 | money(8) | No | - |  |  |
| Pago_Proyecto | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Nominillas_Subsidios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Importe_Pago_Subsidio_EnfermAccid | money(8) | No | - |  |  |
| Importe_Pago_Subsidio_Maternidad | money(8) | No | - |  |  |
| Importe_Pago_Subsidio_PrestacSocial | money(8) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Importe_Pago_Subsidio_Invalidez_Parcial | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Nominillas_Vacation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Importe_Pago_Vacaciones | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Reintegros`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Importe_Reintegro_Salario | money(8) | No | - |  |  |
| Importe_Indebido_Salario | money(8) | No | - |  |  |
| Importe_Indebido_Salario_909 | money(8) | No | - |  |  |
| Importe_909 | money(8) | No | - |  |  |
| Importe_Reintegro_Subsidio | money(8) | No | - |  |  |
| Importe_Indebido_Subsidio | money(8) | No | - |  |  |
| Importe_Reintegro_Vacaciones | money(8) | No | - |  |  |
| Importe_Indebido_Vacaciones | money(8) | No | - |  |  |
| Importe_Reintegro_Divisa | money(8) | No | - |  |  |
| Importe_Indebido_Divisa | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Salarios`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Contador | int(4) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |
| Plus | money(8) | No | - |  |  |
| Otros_Salarios | money(8) | No | - |  |  |
| Antiguedad | money(8) | No | - |  |  |
| Salario_por_Cargo | money(8) | No | - |  |  |
| IETerritorial | money(8) | No | - |  |  |
| ETSector | money(8) | No | - |  |  |
| Horas_Extra | money(8) | No | - |  |  |
| Condiciones | money(8) | No | - |  |  |
| Albergamiento | money(8) | No | - |  |  |
| HorarioIrregular | money(8) | No | - |  |  |
| Idoneidad_Fijo | money(8) | No | - |  |  |
| Idoneidad_Movil | money(8) | No | - |  |  |
| Retribucion_Complementaria | money(8) | No | - |  |  |
| OtrasRetribuciones | money(8) | No | - |  |  |
| Otras_CLA | money(8) | No | - |  |  |
| Devengado60 | money(8) | No | - |  |  |
| Devengado100 | money(8) | No | - |  |  |
| Devengado_por_Suspension | money(8) | No | - |  |  |
| DevengadoReubicados | money(8) | No | - |  |  |
| Devengado_Divisa | money(8) | No | - |  |  |
| SalarioResultado | money(8) | No | - |  |  |
| Salario_Acumulado_Pago | money(8) | No | - |  |  |
| ImporteMS | money(8) | No | - |  |  |
| Importe_Sobrecumplimiento | money(8) | No | - |  |  |
| Perfeccionamiento | money(8) | No | - |  |  |
| Estimulacion | money(8) | No | - |  |  |
| Recargo_Total | money(8) | No | - |  |  |
| Acobrar | money(8) | No | - |  |  |
| Descuento | money(8) | No | - |  |  |
| AjusteCentavos | numeric(5) | No | - |  |  |
| Porciento_Fondo | numeric(5) | No | - |  |  |
| Id_Actividad_Id_Ccosto_Id_Obra | char(20) | No | - |  |  |
| Decreto_Ley_91 | money(8) | No | - |  |  |
| Id_Actividad | char(3) | No | - |  |  |
| Id_Obra | char(10) | No | - |  |  |
| ImporteMS_ET | money(8) | No | - |  |  |
| ImporteMS_EE | money(8) | No | - |  |  |
| Pago_Comedor | money(8) | No | - |  |  |
| Pago_Comedor_Divisa | money(8) | No | - |  |  |
| Otros_Pagos1 | money(8) | No | - |  |  |
| Otros_Pagos2 | money(8) | No | - |  |  |
| Otros_Pagos3 | money(8) | No | - |  |  |
| Otros_Pagos4 | money(8) | No | - |  |  |
| Otros_Pagos5 | money(8) | No | - |  |  |
| CSS_Desc_Pago | money(8) | No | - |  |  |
| CSS_Desc_PAnt | money(8) | No | - |  |  |
| IIP_Desc_Pago | money(8) | No | - |  |  |
| IIP_Desc_PAnt | money(8) | No | - |  |  |
| CSS_Pend | money(8) | No | - |  |  |
| IIP_Pend | money(8) | No | - |  |  |
| ContraValor | money(8) | No | - |  |  |
| ContraValor_Comedor | money(8) | No | - |  |  |
| Turnos_Nocturnos | money(8) | No | - |  |  |
| Pago_Adel_Desc | money(8) | No | - |  |  |

---

#### `RH_Tmp_Contabilizacion_Salarios_Vinculados`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Item | bigint(8) | No | - |  | ✅ |
| Id_Ccosto | char(10) | No | - |  |  |
| Id_Expediente | char(15) | No | - |  |  |
| Salario_Basico | money(8) | No | - |  |  |

---

#### `RH_Tmp_Vacaciones_Sobregiradas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Dias_Acumulado | numeric(5) | No | - |  |  |
| Dias_Pagados | numeric(5) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_Tmp_Vacaciones_Sobregiradas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Ubicacion_Defensa`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Ubicacion_Defensa | char(5) | No | - | ✅ |  |
| Desc_Ubicacion_Defensa | varchar(50) | No | - |  |  |
| Siglas | char(5) | No | - |  |  |
| Clasificacion | tinyint(1) | No | - |  |  |

**Clave primaria:** Id_Ubicacion_Defensa

**Índices:**
- `PK_RH_Ubicacion_Defensa` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Unidades_Organizativas`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Nivel | tinyint(1) | No | - | ✅ |  |
| Id_Direccion | char(15) | No | - | ✅ |  |
| Desc_Direccion | varchar(100) | No | - |  |  |
| Clasificacion | varchar(5) | No | - |  |  |
| GrupoNomina | char(15) | No | - |  |  |
| GrupoDisciplinaLab | char(15) | No | - |  |  |
| CodGrpSendRec | char(7) | No | - |  |  |
| Id_Area | char(3) | No | - |  |  |
| NivelPadre | tinyint(1) | No | - |  |  |
| Id_DireccionPadre | char(15) | No | - |  |  |
| Fecha_Alta | smalldatetime(4) | No | - |  |  |
| Fecha_Baja | smalldatetime(4) | No | - |  |  |
| Nota | varchar(255) | No | - |  |  |
| Baja | bit(1) | No | - |  |  |
| Id_Provincia | char(5) | No | - |  |  |
| Id_Municipio | char(5) | No | - |  |  |

**Clave primaria:** Nivel, Id_Direccion

**Restricciones CHECK:**
- RH_Unidades_Organizativas_Nivel_Values: None

**Índices:**
- `PK_RH_Unidades_Organizativas` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Variaciones_Plantilla`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NoVariacion | bigint(8) | No | - |  | ✅ |
| Nivel | tinyint(1) | No | - |  |  |
| Id_Direccion | char(15) | No | - |  |  |
| Desc_Direccion | varchar(100) | No | - |  |  |
| Fecha_Propuesta | smalldatetime(4) | No | - |  |  |
| Fecha_Aprobada | smalldatetime(4) | No | - |  |  |
| Estado | tinyint(1) | No | - |  |  |
| Id_User | char(15) | No | - |  |  |
| Fecha_Op | smalldatetime(4) | No | - |  |  |

---

#### `RH_Variaciones_Plantilla_Detalles`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NoVariacion | bigint(8) | No | - | ✅ |  |
| Id_Cargo | char(5) | No | - | ✅ |  |
| Desc_Cargo | varchar(120) | No | - |  |  |
| Propuesta | int(4) | No | - |  |  |
| Aprobadas | int(4) | No | - |  |  |
| Exceso | int(4) | No | - |  |  |
| CantidadPlazasAnterior | int(4) | No | - |  |  |

**Clave primaria:** NoVariacion, Id_Cargo

**Índices:**
- `PK_RH_Variaciones_Plantilla_Detalles` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_Versat_Config`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| CTA | varchar(20) | No | - | ✅ |  |
| ctCuenta_Assets | tinyint(1) | No | - |  |  |
| ctCuenta_Len | tinyint(1) | No | - |  |  |
| ctSub_Cuenta_Assets | tinyint(1) | No | - |  |  |
| ctSub_Cuenta_Len | tinyint(1) | No | - |  |  |
| ctSub_Control_Assets | tinyint(1) | No | - |  |  |
| ctSub_Control_Len | tinyint(1) | No | - |  |  |
| ctAnalisis_Assets | tinyint(1) | No | - |  |  |
| ctAnalisis_Len | tinyint(1) | No | - |  |  |
| ctEspecifico_Assets | tinyint(1) | No | - |  |  |
| ctEspecifico_Len | tinyint(1) | No | - |  |  |
| ccCapitulo_Assets | tinyint(1) | No | - |  |  |
| ccCapitulo_Len | tinyint(1) | No | - |  |  |
| ccSub_Capitulo_Assets | tinyint(1) | No | - |  |  |
| ccSub_Capitulo_Len | tinyint(1) | No | - |  |  |
| ccEspecifico_Assets | tinyint(1) | No | - |  |  |
| ccEspecifico_Len | tinyint(1) | No | - |  |  |
| ccSub_Especifico_Assets | tinyint(1) | No | - |  |  |
| ccSub_Especifico_Len | tinyint(1) | No | - |  |  |
| Sub_Elemento_Assets | tinyint(1) | No | - |  |  |
| Sub_Elemento_Len | tinyint(1) | No | - |  |  |

**Clave primaria:** CTA

**Índices:**
- `PK_RH_Versat_Config` (CLUSTERED) [unique,PRIMARY]

---

#### `RH_ZeroDayAjt`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| Id_Expediente | char(15) | No | - | ✅ |  |
| Nombre | varchar(50) | No | - |  |  |
| Apellido_1 | varchar(50) | No | - |  |  |
| Apellido_2 | varchar(50) | No | - |  |  |
| Valor_Divisa | money(8) | No | - |  |  |
| Valor_Divisa_CUP | money(8) | No | - |  |  |
| Pago_Comedor_Tarifa | money(8) | No | - |  |  |
| Pago_Comedor_Tarifa_CUP | money(8) | No | - |  |  |

**Clave primaria:** Id_Expediente

**Índices:**
- `PK_RH_ZeroDayAjt` (CLUSTERED) [unique,PRIMARY]

---

#### `SysFiles_dm`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| NU | int(4) | No | - |  |  |
| _SYS_1LI | varchar(250) | No | - |  |  |
| _SYS_2LE | varchar(250) | No | - |  |  |
| _dt | smalldatetime(4) | No | - |  |  |

---

#### `SysFiles_dml`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| V_Updt | varchar(70) | No | - |  |  |
| W_Updt | varchar(70) | No | - |  |  |
| X_Updt | varchar(70) | No | - |  |  |
| Y_Updt | varchar(200) | No | - |  |  |
| Z_Updt | varchar(200) | No | - |  |  |

---

#### `SysIndexesSys`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| name | sysname(256) | Sí | - |  |  |
| id | int(4) | Sí | - |  |  |
| type | char(2) | Sí | - |  |  |
| info | smallint(2) | Sí | - |  |  |
| indid | smallint(2) | Sí | - |  |  |
| minlen | smallint(2) | Sí | - |  |  |
| rowmodctr_Bck | int(4) | Sí | - |  |  |
| rows | int(4) | Sí | - |  |  |
| schema_ver | int(4) | Sí | - |  |  |
| deltrig | int(4) | Sí | - |  |  |
| instrig | int(4) | Sí | - |  |  |
| updtrig | int(4) | Sí | - |  |  |
| seltrig | int(4) | Sí | - |  |  |
| Operacion | char(10) | Sí | - |  |  |

---

#### `SysObjectsSys`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| name | sysname(256) | No | - |  |  |
| id | int(4) | No | - |  |  |
| xtype | char(2) | No | - |  |  |
| uid | smallint(2) | No | - |  |  |
| info | smallint(2) | No | - |  |  |
| status | int(4) | No | - |  |  |
| base_schema_ver | int(4) | No | - |  |  |
| replinfo | int(4) | No | - |  |  |
| parent_obj | int(4) | No | - |  |  |
| crdate | datetime(8) | No | - |  |  |
| ftcatid | smallint(2) | No | - |  |  |
| schema_ver | int(4) | No | - |  |  |
| stats_schema_ver | int(4) | No | - |  |  |
| type | char(2) | Sí | - |  |  |
| userstat | smallint(2) | Sí | - |  |  |
| sysstat | smallint(2) | Sí | - |  |  |
| indexdel | smallint(2) | Sí | - |  |  |
| refdate | datetime(8) | Sí | - |  |  |
| version | int(4) | Sí | - |  |  |
| deltrig | int(4) | Sí | - |  |  |
| instrig | int(4) | Sí | - |  |  |
| updtrig | int(4) | Sí | - |  |  |
| seltrig | int(4) | Sí | - |  |  |
| category | int(4) | Sí | - |  |  |
| cache | smallint(2) | Sí | - |  |  |

---

#### `dtproperties`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | int(4) | No | - | ✅ | ✅ |
| objectid | int(4) | Sí | - |  |  |
| property | varchar(64) | No | - | ✅ |  |
| value | varchar(255) | Sí | - |  |  |
| uvalue | nvarchar(510) | Sí | - |  |  |
| lvalue | image(16) | Sí | - |  |  |
| version | int(4) | No | - |  |  |

**Clave primaria:** id, property

**Índices:**
- `pk_dtproperties` (CLUSTERED) [unique,PRIMARY]

---

### Vistas

- `Acceso`
- `Activo_Fijo_Tipos_Entradas`
- `Activo_Fijo_Tipos_Movim`
- `Activo_Fijo_Tipos_Salidas`
- `Almacen`
- `Areas_Geograficas`
- `Areas_Responsabilidad`
- `Assets_Licencia`
- `Canales_Distribucion`
- `Caracterizacion_Contabilidad`
- `Caracterizacion_Entidad`
- `Caracterizacion_Finanzas`
- `Categoria`
- `Causas_Ajuste_Inventario`
- `Centro_Costo`
- `Centro_Costo_Grupos`
- `Centro_Pago`
- `CH_Conceptos`
- `CH_Fondos`
- `CH_Regularidades`
- `Clasificacion_Cliente`
- `Clasificacion_Facturas`
- `Clasificacion_No_Facturar`
- `Clasificacion_producto`
- `Clasificacion_Recepciones`
- `Cliente`
- `Cliente_Puntos_Entrega`
- `Comprobante`
- `Concepto`
- `Control_ActivoFijo`
- `Control_Contabilidad`
- `Control_Inventario`
- `Control_System_Trace_L2`
- `Countries`
- `CRM_Cliente_Contactos`
- `CRM_Cliente_Productos`
- `Cuenta`
- `Cz_Module_Active`
- `Cz_Module_Active_Bck`
- `Cz_Module_Lc`
- `Detalle_Comprobante`
- `Detalle_Devolucion`
- `Detalle_Factura`
- `Devolucion`
- `Empleado`
- `Empleado_Accesos_Cancel`
- `Empleados_Gral_Externa`
- `Empleados_Rpt_Gral`
- `Equipo`
- `Especificacion_ActivoFijo`
- `Especificacion_Insumo`
- `Factura`
- `Formas_Pago`
- `Formato_XXL`
- `FzTables`
- `InfoCorporativa_RRHH`
- `Moneda`
- `Nivel_Agrupacion`
- `Nivel_Corporativo`
- `Nivel_Grupo`
- `Opciones_Sistema`
- `Opciones_Sistema_Clasif`
- `Orden_Trabajo`
- `Organismo`
- `ParametrosCom`
- `Producto`
- `Productos_Historia`
- `Regularidades_ActivoFijo`
- `Regularidades_Ajuste`
- `Regularidades_Cobros`
- `Regularidades_Factura`
- `Regularidades_FN`
- `Regularidades_Nomina`
- `Regularidades_Pagos`
- `Regularidades_Recepcion`
- `Regularidades_Utiles`
- `Regularidades_ValeSalida`
- `RH_Corporativo_CargosDirectivos_Detallado`
- `RH_Corporativo_Defensa`
- `RH_Corporativo_DirectosIndirectos_Aprob`
- `RH_Corporativo_DirectosIndirectos_Cub`
- `RH_Corporativo_Grupos_Categorias`
- `RH_Corporativo_InfoCorporativa`
- `RH_Corporativo_Plantilla_Cargos`
- `RH_Corporativo_Prom_Trabaj`
- `RH_Estimulacion_Puntos`
- `RSUMA14B`
- `Rutas_Distribucion`
- `Sg0001`
- `Subclasificacion_Contable`
- `System_Trace`
- `System_Trace_L2`
- `System_Trace_L2_Detail`
- `System_Users`
- `Tabla_NCF`
- `Tipo_Analisis_Regularidades`
- `Tipo_Epigrafe_Regularidades`
- `Tipo_Partida_Regularidades`
- `Tipo_SubAnalisis_Regularidades`
- `Tipo_SubCuentas_Regularidades`
- `Tipos_Reg_Values`
- `Unidades_Medida`
- `Util_Tool_Clasif`
- `Util_Tool_Clasif_Entradas`
- `Util_Tool_Clasif_Salidas`
- `Util_Tool_Clasif_Traslados`

### Triggers

- **`Pago_Adel_Acm_Updt`** en `RH_Detalles_Reporte_Nominillas_Rpt` ( )
- **`Fix_InsertDateTime`** en `RH_Empleados_Movimientos` ( )
---

## 2. Sigenu (`ces`)

**Servidor:** PostgreSQL `172.27.240.8` · **Base de datos:** `ces` · **Origen:** estudiantes (Sigenu).

### Tablas

#### `academic_level`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_academic_level | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_academic_level

**Índices:**
- `pk_academic_level`: CREATE UNIQUE INDEX pk_academic_level ON public.academic_level USING btree (id_academic_level)

---

#### `academic_situation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_academic_situation | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| student_status_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_academic_situation

**Claves foráneas:**
- `student_status_fk` → `student_status.id_student_status`

**Índices:**
- `pk_academic_situation`: CREATE UNIQUE INDEX pk_academic_situation ON public.academic_situation USING btree (id_academic_situation)

---

#### `activity_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| activity_type_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| sort | integer(32,0) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |

**Clave primaria:** activity_type_id

**Índices:**
- `pk_activity_type`: CREATE UNIQUE INDEX pk_activity_type ON public.activity_type USING btree (activity_type_id)

---

#### `activity_type_config`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| activity_type_config_id | character varying(1024) | No | - | ✅ |  |
| cant_hours | integer(32,0) | Sí | - |  |  |
| activity_type_fk | character varying(1024) | Sí | - |  |  |
| subject_configuration_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** activity_type_config_id

**Claves foráneas:**
- `activity_type_fk` → `activity_type.activity_type_id`
- `subject_configuration_fk` → `subject_configuration.subject_configuration_id`

**Índices:**
- `pk_activity_type_config`: CREATE UNIQUE INDEX pk_activity_type_config ON public.activity_type_config USING btree (activity_type_config_id)

---

#### `activity_types2group_plannings`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| activity_types_fk | character varying(1024) | No | - | ✅ |  |
| group_plannings_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** activity_types_fk, group_plannings_fk

**Claves foráneas:**
- `activity_types_fk` → `activity_type.activity_type_id`
- `group_plannings_fk` → `group_planning.group_planning_id`

**Índices:**
- `pk_activity_types2group_plannings`: CREATE UNIQUE INDEX pk_activity_types2group_plannings ON public.activity_types2group_plannings USING btree (activity_types_fk, group_plannings_fk)

---

#### `adjustment_subject`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| adjustment_subject_id | character varying(1024) | No | - | ✅ |  |
| real_time | integer(32,0) | No | - |  |  |
| estimated_time | integer(32,0) | No | - |  |  |
| cancelled | boolean | No | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** adjustment_subject_id

**Claves foráneas:**
- `career_fk` → `career.id_career`
- `subject_fk` → `subject.subject_id`

**Restricciones UNIQUE:** subject_fk, career_fk

**Índices:**
- `pk_adjustment_subject`: CREATE UNIQUE INDEX pk_adjustment_subject ON public.adjustment_subject USING btree (adjustment_subject_id)
- `unq_subject_career`: CREATE UNIQUE INDEX unq_subject_career ON public.adjustment_subject USING btree (subject_fk, career_fk)

---

#### `assign_study_program_motive`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assign_study_program_motive_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** assign_study_program_motive_id

**Índices:**
- `pk_assign_study_program_motive`: CREATE UNIQUE INDEX pk_assign_study_program_motive ON public.assign_study_program_motive USING btree (assign_study_program_motive_id)

---

#### `assigned_department`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assigned_department_id | character varying(1024) | No | - | ✅ |  |
| department_fk | character varying(1024) | Sí | - |  |  |
| discipline_fk | character varying(1024) | Sí | - |  |  |
| study_program_version_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** assigned_department_id

**Claves foráneas:**
- `department_fk` → `department.department_id`
- `discipline_fk` → `discipline.discipline_id`
- `study_program_version_fk` → `study_program_version.study_program_version_id`

**Índices:**
- `pk_assigned_department`: CREATE UNIQUE INDEX pk_assigned_department ON public.assigned_department USING btree (assigned_department_id)

---

#### `assigned_study_program_version`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assigned_study_program_version_id | character varying(1024) | No | - | ✅ |  |
| date | date | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| study_program_version_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| assign_study_program_motive_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** assigned_study_program_version_id

**Claves foráneas:**
- `assign_study_program_motive_fk` → `assign_study_program_motive.assign_study_program_motive_id`
- `student_fk` → `student.id_student`
- `study_program_version_fk` → `study_program_version.study_program_version_id`

**Índices:**
- `pk_assigned_study_program`: CREATE UNIQUE INDEX pk_assigned_study_program ON public.assigned_study_program_version USING btree (assigned_study_program_version_id)

---

#### `assigned_subject`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assigned_subject_id | character varying(1024) | No | - | ✅ |  |
| period | integer(32,0) | No | - |  |  |
| cancelled | boolean | No | false |  |  |
| assigned_subject_fk | character varying(1024) | Sí | - |  |  |
| assigned_subject_type_fk | character varying(1024) | Sí | - |  |  |
| year | integer(32,0) | Sí | - |  |  |
| averageable | boolean | Sí | false |  |  |
| name | character varying(1024) | Sí | - |  |  |
| to_certification | boolean | Sí | - |  |  |

**Clave primaria:** assigned_subject_id

**Claves foráneas:**
- `assigned_subject_fk` → `assigned_subject.assigned_subject_id`
- `assigned_subject_type_fk` → `assigned_subject_type.assigned_subject_type_id`

**Índices:**
- `pk_assigned_subject`: CREATE UNIQUE INDEX pk_assigned_subject ON public.assigned_subject USING btree (assigned_subject_id)

---

#### `assigned_subject_group`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assigned_subject_group_id | character varying | No | - | ✅ |  |
| department_fk | character varying | Sí | - |  |  |
| subject_group_fk | character varying | Sí | - |  |  |

**Clave primaria:** assigned_subject_group_id

**Claves foráneas:**
- `department_fk` → `department.department_id`
- `subject_group_fk` → `subject_group.id`

**Índices:**
- `pk_assigned_subject_group`: CREATE UNIQUE INDEX pk_assigned_subject_group ON public.assigned_subject_group USING btree (assigned_subject_group_id)

---

#### `assigned_subject_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assigned_subject_type_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** assigned_subject_type_id

**Índices:**
- `pk_subject_type`: CREATE UNIQUE INDEX pk_subject_type ON public.assigned_subject_type USING btree (assigned_subject_type_id)

---

#### `assigned_subjects2study_progra`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| study_program_versions_fk | character varying(1024) | No | - | ✅ |  |
| assigned_subjects_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** study_program_versions_fk, assigned_subjects_fk

**Claves foráneas:**
- `assigned_subjects_fk` → `assigned_subject.assigned_subject_id`
- `study_program_versions_fk` → `study_program_version.study_program_version_id`

**Índices:**
- `pk_assigned_subjects2study_progra`: CREATE UNIQUE INDEX pk_assigned_subjects2study_progra ON public.assigned_subjects2study_progra USING btree (study_program_versions_fk, assigned_subjects_fk)

---

#### `assistance_record`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| assistance_record_id | character varying(1024) | No | - | ✅ |  |
| date | date | Sí | - |  |  |
| week | integer(32,0) | Sí | - |  |  |
| professor_name | character varying(1024) | Sí | - |  |  |
| activity_type_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| first_assistance | boolean | Sí | false |  |  |
| second_assistance | boolean | Sí | - |  |  |

**Clave primaria:** assistance_record_id

**Claves foráneas:**
- `activity_type_fk` → `activity_type.activity_type_id`
- `professor_fk` → `professor.professor_id`
- `student_fk` → `student.id_student`
- `subject_fk` → `subject.subject_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_assistance_record`: CREATE UNIQUE INDEX pk_assistance_record ON public.assistance_record USING btree (assistance_record_id)

---

#### `assistant_student_file`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_assistant_student_file | character varying(1024) | No | - | ✅ |  |
| date | timestamp without time zone | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| assistant_student_status_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_assistant_student_file

**Claves foráneas:**
- `assistant_student_status_fk` → `assistant_student_status.id_assistant_student_status`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_assistant_student_file`: CREATE UNIQUE INDEX pk_assistant_student_file ON public.assistant_student_file USING btree (id_assistant_student_file)

---

#### `assistant_student_status`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_assistant_student_status | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |

**Clave primaria:** id_assistant_student_status

**Índices:**
- `pk_assistant_student_status`: CREATE UNIQUE INDEX pk_assistant_student_status ON public.assistant_student_status USING btree (id_assistant_student_status)

---

#### `award`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_award | character varying(1024) | No | - | ✅ |  |
| position | integer(32,0) | No | - |  |  |
| increment | real(24,None) | No | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_award

**Índices:**
- `pk_award`: CREATE UNIQUE INDEX pk_award ON public.award USING btree (id_award)

---

#### `bonus`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_bonus | character varying(1024) | No | - | ✅ |  |
| event | character varying(1024) | Sí | - |  |  |
| increment | real(24,None) | No | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_bonus

**Índices:**
- `pk_bonus`: CREATE UNIQUE INDEX pk_bonus ON public.bonus USING btree (id_bonus)

---

#### `career`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_career | character varying(1024) | No | - | ✅ |  |
| cancelled | boolean | No | - |  |  |
| course_type_fk | character varying(1024) | Sí | - |  |  |
| national_career_fk | character varying(1024) | Sí | - |  |  |
| town_university_fk | character varying(1024) | Sí | - |  |  |
| faculty_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_career

**Claves foráneas:**
- `course_type_fk` → `course_type.id_course_type`
- `faculty_fk` → `faculty.id_faculty`
- `national_career_fk` → `national_career.id_national_career`
- `town_university_fk` → `town_university.id_town_university`

**Índices:**
- `pk_career`: CREATE UNIQUE INDEX pk_career ON public.career USING btree (id_career)

---

#### `career_profile`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying | No | - | ✅ |  |
| profile | character varying | Sí | - |  |  |
| career_fk | character varying | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `career_fk` → `career.id_career`

**Índices:**
- `career_profile_pkey`: CREATE UNIQUE INDEX career_profile_pkey ON public.career_profile USING btree (id)

---

#### `config_mailserver`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | integer(32,0) | No | nextval('config_mailserver_id_seq'::regclass) | ✅ |  |
| server | character varying | Sí | - |  |  |
| account | character varying | Sí | - |  |  |
| user_name | character varying | Sí | - |  |  |
| password | character varying | Sí | - |  |  |
| port | character varying | Sí | - |  |  |
| ssl | boolean | Sí | - |  |  |
| sender_name | character varying | Sí | - |  |  |

**Clave primaria:** id

**Índices:**
- `pk_email_id`: CREATE UNIQUE INDEX pk_email_id ON public.config_mailserver USING btree (id)

---

#### `country`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_country | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| code | character varying | Sí | - |  |  |

**Clave primaria:** id_country

**Índices:**
- `pk_country`: CREATE UNIQUE INDEX pk_country ON public.country USING btree (id_country)

---

#### `course`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_course | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| matriculate_course | boolean | Sí | - |  |  |

**Clave primaria:** id_course

**Índices:**
- `pk_course`: CREATE UNIQUE INDEX pk_course ON public.course USING btree (id_course)

---

#### `course_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_course_type | character varying(1024) | No | - | ✅ |  |
| code | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| debts | integer(32,0) | No | - |  |  |
| cancelled | boolean | No | - |  |  |
| short_name | character varying(1024) | Sí | - |  |  |
| behavior | character varying(1024) | Sí | - |  |  |
| modality | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_course_type

**Índices:**
- `pk_course_type`: CREATE UNIQUE INDEX pk_course_type ON public.course_type USING btree (id_course_type)

---

#### `course_types2drop_motives`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| drop_motives_fk | character varying(1024) | No | - | ✅ |  |
| course_types_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** drop_motives_fk, course_types_fk

**Claves foráneas:**
- `course_types_fk` → `course_type.id_course_type`
- `drop_motives_fk` → `drop_motive.id_drop_motive`

**Índices:**
- `pk_course_types2drop_motives`: CREATE UNIQUE INDEX pk_course_types2drop_motives ON public.course_types2drop_motives USING btree (drop_motives_fk, course_types_fk)

---

#### `cualitative_evaluation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| cualitative_evaluation_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| abbreviation | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| priority | integer(32,0) | No | - |  |  |

**Clave primaria:** cualitative_evaluation_id

**Índices:**
- `pk_cualitative_evaluation`: CREATE UNIQUE INDEX pk_cualitative_evaluation ON public.cualitative_evaluation USING btree (cualitative_evaluation_id)

---

#### `deleted_student`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| identification | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| middle_name | character varying(1024) | Sí | - |  |  |
| last_name | character varying(1024) | Sí | - |  |  |
| id_faculty | character varying(1024) | Sí | - |  |  |
| idcareer | character varying(1024) | Sí | - |  |  |
| id_course_type | character varying(1024) | Sí | - |  |  |
| user_name | character varying(1024) | Sí | - |  |  |
| date | date | Sí | - |  |  |
| idcourse | character varying(1024) | Sí | - |  |  |
| elimination_motive | character varying(1024) | Sí | - |  |  |
| host | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Índices:**
- `pk_deleted_student`: CREATE UNIQUE INDEX pk_deleted_student ON public.deleted_student USING btree (id)

---

#### `department`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| department_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| town_university_fk | character varying(1024) | Sí | - |  |  |
| faculty_fk | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |

**Clave primaria:** department_id

**Claves foráneas:**
- `faculty_fk` → `faculty.id_faculty`
- `town_university_fk` → `town_university.id_town_university`

**Índices:**
- `pk_department`: CREATE UNIQUE INDEX pk_department ON public.department USING btree (department_id)

---

#### `discipline`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| discipline_id | character varying(1024) | No | - | ✅ |  |
| objectives | character varying(1024) | Sí | - |  |  |
| program | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| code | character varying(1024) | Sí | - |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |
| discipline_name_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** discipline_id

**Claves foráneas:**
- `career_fk` → `career.id_career`
- `discipline_name_fk` → `discipline_name.discipline_name_id`

**Índices:**
- `pk_discipline`: CREATE UNIQUE INDEX pk_discipline ON public.discipline USING btree (discipline_id)

---

#### `discipline_name`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| discipline_name_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |

**Clave primaria:** discipline_name_id

**Índices:**
- `pk_discipline_name`: CREATE UNIQUE INDEX pk_discipline_name ON public.discipline_name USING btree (discipline_name_id)

---

#### `docent_charge`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| docent_charge_id | character varying(1024) | No | - | ✅ |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |

**Clave primaria:** docent_charge_id

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `professor_fk` → `professor.professor_id`

**Índices:**
- `pk_docent_charge`: CREATE UNIQUE INDEX pk_docent_charge ON public.docent_charge USING btree (docent_charge_id)

---

#### `drop_motive`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_drop_motive | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| temporal | boolean | Sí | - |  |  |

**Clave primaria:** id_drop_motive

**Índices:**
- `pk_drop_motive`: CREATE UNIQUE INDEX pk_drop_motive ON public.drop_motive USING btree (id_drop_motive)

---

#### `entry_evaluation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_entry_evaluation | character varying(1024) | No | - | ✅ |  |
| mark | real(24,None) | No | - |  |  |
| entry_subject_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| matriculated_student_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_entry_evaluation

**Claves foráneas:**
- `entry_subject_fk` → `entry_subject.id_entry_subject`
- `matriculated_student_fk` → `matriculated_student.id_matriculated_student`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_entry_evaluation`: CREATE UNIQUE INDEX pk_entry_evaluation ON public.entry_evaluation USING btree (id_entry_evaluation)

---

#### `entry_source`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_entry_source | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_entry_source

**Índices:**
- `pk_entry_source`: CREATE UNIQUE INDEX pk_entry_source ON public.entry_source USING btree (id_entry_source)

---

#### `entry_subject`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_entry_subject | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_entry_subject

**Índices:**
- `pk_entry_subject`: CREATE UNIQUE INDEX pk_entry_subject ON public.entry_subject USING btree (id_entry_subject)

---

#### `evaluation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_evaluation | character varying(1024) | No | - | ✅ |  |
| cancelled | boolean | Sí | - |  |  |
| professor_name | character varying(1024) | Sí | - |  |  |
| examination_type_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| evaluation_value_fk | character varying(1024) | Sí | - |  |  |
| matriculated_subject_fk | character varying(1024) | Sí | - |  |  |
| user_name | character varying(1024) | Sí | - |  |  |
| registration_date | timestamp without time zone | Sí | - |  |  |
| evaluation_date | timestamp without time zone | Sí | - |  |  |
| host | character varying(1024) | Sí | - |  |  |
| deleted | boolean | Sí | - |  |  |
| motive | character varying(1024) | Sí | - |  |  |
| validated | boolean | Sí | - |  |  |
| examination_acta_fk | character varying(1024) | Sí | - |  |  |
| exam_mark_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_evaluation

**Claves foráneas:**
- `evaluation_value_fk` → `evaluation_value.id_evaluation_value`
- `exam_mark_fk` → `evaluation_value.id_evaluation_value`
- `examination_acta_fk` → `examination_acta.id_examination_acta`
- `examination_type_fk` → `examination_type.id_examination_type`
- `matriculated_subject_fk` → `matriculated_subject.matriculated_subject_id`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_evaluation`: CREATE UNIQUE INDEX pk_evaluation ON public.evaluation USING btree (id_evaluation)
- `idx_ev_matriculated_subject`: CREATE INDEX idx_ev_matriculated_subject ON public.evaluation USING btree (matriculated_subject_fk)
- `idx_ev_student`: CREATE INDEX idx_ev_student ON public.evaluation USING btree (student_fk)
- `idx_evaluation_value`: CREATE INDEX idx_evaluation_value ON public.evaluation USING btree (evaluation_value_fk)
- `idx_matriculate_value`: CREATE INDEX idx_matriculate_value ON public.evaluation USING btree (evaluation_value_fk, matriculated_subject_fk)
- `idx_matriculated_subject`: CREATE INDEX idx_matriculated_subject ON public.evaluation USING btree (matriculated_subject_fk)

---

#### `evaluation_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| evaluation_type_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** evaluation_type_id

**Índices:**
- `pk_evaluation_type`: CREATE UNIQUE INDEX pk_evaluation_type ON public.evaluation_type USING btree (evaluation_type_id)

---

#### `evaluation_value`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_evaluation_value | character varying(1024) | No | - | ✅ |  |
| value | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_evaluation_value

**Índices:**
- `pk_evaluation_value`: CREATE UNIQUE INDEX pk_evaluation_value ON public.evaluation_value USING btree (id_evaluation_value)

---

#### `evaluations_cuts`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| evaluations_cuts_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| abbreviation | character varying(1024) | Sí | - |  |  |
| week | integer(32,0) | Sí | - |  |  |
| date | date | Sí | - |  |  |
| evaluation_type | character varying(1024) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| priority | integer(32,0) | Sí | - |  |  |

**Clave primaria:** evaluations_cuts_id

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `professor_fk` → `professor.professor_id`
- `subject_fk` → `subject.subject_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_evaluations_cuts`: CREATE UNIQUE INDEX pk_evaluations_cuts ON public.evaluations_cuts USING btree (evaluations_cuts_id)

---

#### `evaluative_court_header`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| evaluative_court_header_id | character varying(1024) | No | - | ✅ |  |
| registration_date | date | Sí | - |  |  |
| delivery_date | date | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| delivered | boolean | No | - |  |  |
| group_planning_fk | character varying(1024) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| evaluations_cuts_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** evaluative_court_header_id

**Claves foráneas:**
- `evaluations_cuts_fk` → `evaluations_cuts.evaluations_cuts_id`
- `group_planning_fk` → `group_planning.group_planning_id`
- `professor_fk` → `professor.professor_id`

**Índices:**
- `pk_evaluative_court_header`: CREATE UNIQUE INDEX pk_evaluative_court_header ON public.evaluative_court_header USING btree (evaluative_court_header_id)

---

#### `examination_acta`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_examination_acta | character varying(1024) | No | - | ✅ |  |
| professor_name | character varying(1024) | Sí | - |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |
| course_type_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| examination_type_fk | character varying(1024) | Sí | - |  |  |
| subject_name_fk | character varying(1024) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| closed | boolean | Sí | - |  |  |
| validated | boolean | Sí | - |  |  |
| close_date | date | Sí | - |  |  |
| validate_date | date | Sí | - |  |  |
| examination_date | date | Sí | - |  |  |
| secretary_name | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_examination_acta

**Claves foráneas:**
- `career_fk` → `career.id_career`
- `course_fk` → `course.id_course`
- `course_type_fk` → `course_type.id_course_type`
- `examination_type_fk` → `examination_type.id_examination_type`
- `professor_fk` → `professor.professor_id`
- `subject_fk` → `subject.subject_id`
- `subject_name_fk` → `subject_name.subject_name_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_examination_acta`: CREATE UNIQUE INDEX pk_examination_acta ON public.examination_acta USING btree (id_examination_acta)

---

#### `examination_request`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| examination_request_id | character varying(1024) | No | - | ✅ |  |
| matriculated_subject_fk | character varying(1024) | Sí | - |  |  |
| examination_type_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** examination_request_id

**Índices:**
- `pk_examination_request`: CREATE UNIQUE INDEX pk_examination_request ON public.examination_request USING btree (examination_request_id)

---

#### `examination_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_examination_type | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| priority | integer(32,0) | Sí | - |  |  |
| sort | integer(32,0) | Sí | - |  |  |

**Clave primaria:** id_examination_type

**Índices:**
- `pk_examination_type`: CREATE UNIQUE INDEX pk_examination_type ON public.examination_type USING btree (id_examination_type)

---

#### `faculties2users`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| faculties_fk | character varying(1024) | No | - | ✅ |  |
| users_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** faculties_fk, users_fk

**Claves foráneas:**
- `faculties_fk` → `faculty.id_faculty`
- `users_fk` → `xuser.id`

**Índices:**
- `pk_faculties2users`: CREATE UNIQUE INDEX pk_faculties2users ON public.faculties2users USING btree (faculties_fk, users_fk)

---

#### `faculty`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_faculty | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| phone_number | character varying(1024) | Sí | - |  |  |
| dean_name | character varying(1024) | Sí | - |  |  |
| secretary_name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| university_fk | character varying(1024) | Sí | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |
| dean_email | character varying | Sí | - |  |  |

**Clave primaria:** id_faculty

**Claves foráneas:**
- `town_fk` → `town.id_town`
- `university_fk` → `university.id_university`

**Índices:**
- `pk_faculty`: CREATE UNIQUE INDEX pk_faculty ON public.faculty USING btree (id_faculty)

---

#### `father_information`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_father_information | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| salary | real(24,None) | Sí | - |  |  |
| dead | boolean | No | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| academic_level_fk | character varying(1024) | Sí | - |  |  |
| politic_org_fk | character varying(1024) | Sí | - |  |  |
| ocupation_fk | character varying(1024) | Sí | - |  |  |
| matriculated_student_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_father_information

**Claves foráneas:**
- `academic_level_fk` → `academic_level.id_academic_level`
- `matriculated_student_fk` → `matriculated_student.id_matriculated_student`
- `ocupation_fk` → `ocupation.id_ocupation`
- `politic_org_fk` → `politic_org.id_politic_org`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_father_information`: CREATE UNIQUE INDEX pk_father_information ON public.father_information USING btree (id_father_information)

---

#### `group_planning`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| group_planning_id | character varying(1024) | No | - | ✅ |  |
| assign_end_mark | boolean | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| subject_configuration_fk | character varying(1024) | Sí | - |  |  |
| docent_charge_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** group_planning_id

**Claves foráneas:**
- `docent_charge_fk` → `docent_charge.docent_charge_id`
- `subject_configuration_fk` → `subject_configuration.subject_configuration_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_group_planning`: CREATE UNIQUE INDEX pk_group_planning ON public.group_planning USING btree (group_planning_id)

---

#### `group_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_group_type | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_group_type

**Índices:**
- `pk_group_type`: CREATE UNIQUE INDEX pk_group_type ON public.group_type USING btree (id_group_type)

---

#### `groups2matriculated_students`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| matriculated_students_fk | character varying(1024) | No | - | ✅ |  |
| groups_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** matriculated_students_fk, groups_fk

**Claves foráneas:**
- `matriculated_students_fk` → `matriculated_student.id_matriculated_student`
- `groups_fk` → `xgroup.id_group`

**Índices:**
- `pk_groups2matriculated_students`: CREATE UNIQUE INDEX pk_groups2matriculated_students ON public.groups2matriculated_students USING btree (matriculated_students_fk, groups_fk)

---

#### `groups2students`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| students_fk | character varying(1024) | Sí | - |  |  |
| groups_fk | character varying(1024) | Sí | - |  |  |
| id | character varying(1024) | No | - | ✅ |  |
| consecutive | integer(32,0) | Sí | - |  |  |
| student_group_type_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `students_fk` → `student.id_student`
- `student_group_type_fk` → `student_group_type.student_group_type_id`
- `groups_fk` → `xgroup.id_group`

**Restricciones UNIQUE:** students_fk, groups_fk

**Índices:**
- `pk_groups2students`: CREATE UNIQUE INDEX pk_groups2students ON public.groups2students USING btree (id)
- `unq_group_student`: CREATE UNIQUE INDEX unq_group_student ON public.groups2students USING btree (students_fk, groups_fk)
- `idx_g2s_group`: CREATE INDEX idx_g2s_group ON public.groups2students USING btree (groups_fk)
- `idx_g2s_student`: CREATE INDEX idx_g2s_student ON public.groups2students USING btree (students_fk)

---

#### `handicap`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_handicap | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_handicap

**Índices:**
- `pk_handicap`: CREATE UNIQUE INDEX pk_handicap ON public.handicap USING btree (id_handicap)

---

#### `handicaps2matriculated_student`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| handicaps_fk | character varying(1024) | No | - | ✅ |  |
| matriculated_students_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** handicaps_fk, matriculated_students_fk

**Claves foráneas:**
- `handicaps_fk` → `handicap.id_handicap`
- `matriculated_students_fk` → `matriculated_student.id_matriculated_student`

**Índices:**
- `pk_handicaps2matriculated_student`: CREATE UNIQUE INDEX pk_handicaps2matriculated_student ON public.handicaps2matriculated_student USING btree (handicaps_fk, matriculated_students_fk)

---

#### `handicaps2students`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| handicaps_fk | character varying(1024) | No | - | ✅ |  |
| students_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** handicaps_fk, students_fk

**Claves foráneas:**
- `handicaps_fk` → `handicap.id_handicap`
- `students_fk` → `student.id_student`

**Índices:**
- `pk_handicaps2students`: CREATE UNIQUE INDEX pk_handicaps2students ON public.handicaps2students USING btree (handicaps_fk, students_fk)

---

#### `i_p_access`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| ip | character varying(1024) | Sí | - |  |  |
| faculty_fk | character varying(1024) | Sí | - |  |  |
| town_university_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `faculty_fk` → `faculty.id_faculty`
- `town_university_fk` → `town_university.id_town_university`

**Índices:**
- `pk_i_p_access`: CREATE UNIQUE INDEX pk_i_p_access ON public.i_p_access USING btree (id)

---

#### `josso_remote_password`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| username | character varying | No | - | ✅ |  |
| password_hash | character varying | No | - |  |  |

**Clave primaria:** username

**Índices:**
- `josso_remote_password_pkey`: CREATE UNIQUE INDEX josso_remote_password_pkey ON public.josso_remote_password USING btree (username)

---

#### `josso_user`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| login | character varying | Sí | - |  |  |
| password | character varying | Sí | - |  |  |
| name | character varying | Sí | - |  |  |

---

#### `josso_user_property`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| name | character varying | Sí | - |  |  |
| value | character varying | Sí | - |  |  |

---

#### `josso_user_role`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| login | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |

---

#### `laboral_information`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_laboral_information | character varying(1024) | No | - | ✅ |  |
| center_name | character varying(1024) | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| phone | character varying(1024) | Sí | - |  |  |
| salary | real(24,None) | Sí | - |  |  |
| boss_name | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| organism_fk | character varying(1024) | Sí | - |  |  |
| syndicate_fk | character varying(1024) | Sí | - |  |  |
| ocupation_fk | character varying(1024) | Sí | - |  |  |
| matriculated_student_fk | character varying(1024) | Sí | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_laboral_information

**Claves foráneas:**
- `matriculated_student_fk` → `matriculated_student.id_matriculated_student`
- `ocupation_fk` → `ocupation.id_ocupation`
- `organism_fk` → `organism.id_organism`
- `student_fk` → `student.id_student`
- `syndicate_fk` → `syndicate.id_syndicate`
- `town_fk` → `town.id_town`

**Índices:**
- `pk_laboral_information`: CREATE UNIQUE INDEX pk_laboral_information ON public.laboral_information USING btree (id_laboral_information)

---

#### `licence`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_licence | character varying(1024) | No | - | ✅ |  |
| end_date | timestamp without time zone | Sí | - |  |  |
| drop_fk | character varying(1024) | Sí | - |  |  |
| licence_motive_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_licence

**Claves foráneas:**
- `licence_motive_fk` → `licence_motive.id_licence_motive`

**Índices:**
- `pk_licence`: CREATE UNIQUE INDEX pk_licence ON public.licence USING btree (id_licence)

---

#### `licence_motive`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_licence_motive | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_licence_motive

**Índices:**
- `pk_licence_motive`: CREATE UNIQUE INDEX pk_licence_motive ON public.licence_motive USING btree (id_licence_motive)

---

#### `marital_status`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_marital_status | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_marital_status

**Índices:**
- `pk_marital_status`: CREATE UNIQUE INDEX pk_marital_status ON public.marital_status USING btree (id_marital_status)

---

#### `matriculated_student`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_matriculated_student | character varying(1024) | No | - | ✅ |  |
| identification | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| first_name | character varying(1024) | Sí | - |  |  |
| second_name | character varying(1024) | Sí | - |  |  |
| native_of | character varying(1024) | Sí | - |  |  |
| birth_date | date | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| child_number | integer(32,0) | No | - |  |  |
| phone | character varying(1024) | Sí | - |  |  |
| email | character varying(1024) | Sí | - |  |  |
| higher_education_in_date | date | Sí | - |  |  |
| university_in_date | date | Sí | - |  |  |
| inscription_date | timestamp without time zone | Sí | - |  |  |
| consecutive | integer(32,0) | Sí | - |  |  |
| scale | real(24,None) | Sí | - |  |  |
| academic_index | real(24,None) | Sí | - |  |  |
| update | boolean | No | false |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |
| scholastic_origin_fk | character varying(1024) | Sí | - |  |  |
| academic_situation_fk | character varying(1024) | Sí | - |  |  |
| orphan_fk | character varying(1024) | Sí | - |  |  |
| town_university_fk | character varying(1024) | Sí | - |  |  |
| sex_fk | character varying(1024) | Sí | - |  |  |
| faculty_fk | character varying(1024) | Sí | - |  |  |
| country_fk | character varying(1024) | Sí | - |  |  |
| course_type_fk | character varying(1024) | Sí | - |  |  |
| entry_source_fk | character varying(1024) | Sí | - |  |  |
| study_regimen_fk | character varying(1024) | Sí | - |  |  |
| marital_status_fk | character varying(1024) | Sí | - |  |  |
| student_type_fk | character varying(1024) | Sí | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |
| skin_color_fk | character varying(1024) | Sí | - |  |  |
| politic_org_fk | character varying(1024) | Sí | - |  |  |
| photo | character varying(1024) | Sí | - |  |  |
| reoffer | boolean | Sí | false |  |  |
| option | integer(32,0) | Sí | - |  |  |

**Clave primaria:** id_matriculated_student

**Claves foráneas:**
- `academic_situation_fk` → `academic_situation.id_academic_situation`
- `career_fk` → `career.id_career`
- `country_fk` → `country.id_country`
- `course_type_fk` → `course_type.id_course_type`
- `entry_source_fk` → `entry_source.id_entry_source`
- `faculty_fk` → `faculty.id_faculty`
- `marital_status_fk` → `marital_status.id_marital_status`
- `orphan_fk` → `orphan.id_orphan`
- `politic_org_fk` → `politic_org.id_politic_org`
- `scholastic_origin_fk` → `scholastic_origin.id_scholastic_origin`
- `sex_fk` → `sex.id_sex`
- `skin_color_fk` → `skin_color.id_skin_color`
- `student_type_fk` → `student_type.id_student_class`
- `study_regimen_fk` → `study_regimen.id_study_regimen`
- `town_fk` → `town.id_town`
- `town_university_fk` → `town_university.id_town_university`

**Índices:**
- `pk_matriculated_student`: CREATE UNIQUE INDEX pk_matriculated_student ON public.matriculated_student USING btree (id_matriculated_student)

---

#### `matriculated_students2o_n_gs`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| o_n_gs_fk | character varying(1024) | No | - | ✅ |  |
| matriculated_students_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** matriculated_students_fk, o_n_gs_fk

**Claves foráneas:**
- `matriculated_students_fk` → `matriculated_student.id_matriculated_student`
- `o_n_gs_fk` → `o_n_g.id_o_n_g`

**Índices:**
- `pk_matriculated_students2o_n_gs`: CREATE UNIQUE INDEX pk_matriculated_students2o_n_gs ON public.matriculated_students2o_n_gs USING btree (o_n_gs_fk, matriculated_students_fk)

---

#### `matriculated_students2popular_`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| popular_orgs_fk | character varying(1024) | No | - | ✅ |  |
| matriculated_students_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** matriculated_students_fk, popular_orgs_fk

**Claves foráneas:**
- `matriculated_students_fk` → `matriculated_student.id_matriculated_student`
- `popular_orgs_fk` → `popular_org.id_popular_org`

**Índices:**
- `pk_matriculated_students2popular_`: CREATE UNIQUE INDEX pk_matriculated_students2popular_ ON public.matriculated_students2popular_ USING btree (popular_orgs_fk, matriculated_students_fk)

---

#### `matriculated_subject`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| matriculated_subject_id | character varying(1024) | No | - | ✅ |  |
| period_number | integer(32,0) | No | - |  |  |
| approved | boolean | No | false |  |  |
| evaluated | boolean | No | false |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| year | integer(32,0) | Sí | - |  |  |
| cancelled | boolean | No | false |  |  |
| plan_year | integer(32,0) | Sí | - |  |  |
| averageable | boolean | Sí | false |  |  |
| matriculated_subject_type_fk | character varying(1024) | Sí | - |  |  |
| matriculated_subject_situat_fk | character varying(1024) | Sí | - |  |  |
| matriculated_subject_reason_fk | character varying(1024) | Sí | - |  |  |
| matriculated_student_fk | character varying(1024) | Sí | - |  |  |
| tocertification | boolean | Sí | true |  |  |

**Clave primaria:** matriculated_subject_id

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `matriculated_student_fk` → `matriculated_student.id_matriculated_student`
- `matriculated_subject_reason_fk` → `matriculated_subject_reason.matriculated_subject_reason_id`
- `matriculated_subject_situat_fk` → `matriculated_subject_situation.matriculated_subject_situation`
- `matriculated_subject_type_fk` → `matriculated_subject_type.matriculated_subject_type_id`
- `student_fk` → `student.id_student`
- `subject_fk` → `subject.subject_id`

**Índices:**
- `pk_matriculated_subject`: CREATE UNIQUE INDEX pk_matriculated_subject ON public.matriculated_subject USING btree (matriculated_subject_id)
- `idx_ms_student`: CREATE INDEX idx_ms_student ON public.matriculated_subject USING btree (student_fk)
- `idx_ms_subject`: CREATE INDEX idx_ms_subject ON public.matriculated_subject USING btree (subject_fk)

---

#### `matriculated_subject_reason`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| matriculated_subject_reason_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** matriculated_subject_reason_id

**Índices:**
- `pk_evaluation_reason`: CREATE UNIQUE INDEX pk_evaluation_reason ON public.matriculated_subject_reason USING btree (matriculated_subject_reason_id)

---

#### `matriculated_subject_situation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| matriculated_subject_situation | character varying(1024) | No | - | ✅ |  |
| situation | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| evaluation | boolean | No | - |  |  |
| abbreviation | character varying(1024) | Sí | - |  |  |

**Clave primaria:** matriculated_subject_situation

**Índices:**
- `pk_subject_situation`: CREATE UNIQUE INDEX pk_subject_situation ON public.matriculated_subject_situation USING btree (matriculated_subject_situation)

---

#### `matriculated_subject_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| matriculated_subject_type_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** matriculated_subject_type_id

**Índices:**
- `pk_matriculated_subject_type`: CREATE UNIQUE INDEX pk_matriculated_subject_type ON public.matriculated_subject_type USING btree (matriculated_subject_type_id)

---

#### `militar_grade`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_militar_grade | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_militar_grade

**Índices:**
- `pk_militar_grade`: CREATE UNIQUE INDEX pk_militar_grade ON public.militar_grade USING btree (id_militar_grade)

---

#### `militar_service`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_militar_service | character varying(1024) | No | - | ✅ |  |
| licence_date | date | Sí | - |  |  |
| militar_type_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| militar_grade_fk | character varying(1024) | Sí | - |  |  |
| matriculated_student_fk | character varying(1024) | Sí | - |  |  |
| militar_specialty_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_militar_service

**Claves foráneas:**
- `matriculated_student_fk` → `matriculated_student.id_matriculated_student`
- `militar_grade_fk` → `militar_grade.id_militar_grade`
- `militar_specialty_fk` → `militar_specialty.id_militar_specialty`
- `militar_type_fk` → `militar_type.id_militar_type`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_militar_service`: CREATE UNIQUE INDEX pk_militar_service ON public.militar_service USING btree (id_militar_service)

---

#### `militar_specialty`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_militar_specialty | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_militar_specialty

**Índices:**
- `pk_militar_specialty`: CREATE UNIQUE INDEX pk_militar_specialty ON public.militar_specialty USING btree (id_militar_specialty)

---

#### `militar_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_militar_type | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_militar_type

**Índices:**
- `pk_militar_type`: CREATE UNIQUE INDEX pk_militar_type ON public.militar_type USING btree (id_militar_type)

---

#### `mother_information`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_mother_information | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| salary | real(24,None) | Sí | - |  |  |
| dead | boolean | No | - |  |  |
| politic_org_fk | character varying(1024) | Sí | - |  |  |
| matriculated_student_fk | character varying(1024) | Sí | - |  |  |
| ocupation_fk | character varying(1024) | Sí | - |  |  |
| academic_level_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_mother_information

**Claves foráneas:**
- `academic_level_fk` → `academic_level.id_academic_level`
- `matriculated_student_fk` → `matriculated_student.id_matriculated_student`
- `ocupation_fk` → `ocupation.id_ocupation`
- `politic_org_fk` → `politic_org.id_politic_org`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_mother_information`: CREATE UNIQUE INDEX pk_mother_information ON public.mother_information USING btree (id_mother_information)

---

#### `national_career`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_national_career | character varying(1024) | No | - | ✅ |  |
| code | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| diploma | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| scienc_especialty_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_national_career

**Claves foráneas:**
- `scienc_especialty_fk` → `scienc_especialty.id_scienc_especialty`

**Restricciones UNIQUE:** code

**Índices:**
- `national_career_code_key`: CREATE UNIQUE INDEX national_career_code_key ON public.national_career USING btree (code)
- `pk_national_career`: CREATE UNIQUE INDEX pk_national_career ON public.national_career USING btree (id_national_career)

---

#### `o_n_g`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_o_n_g | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_o_n_g

**Índices:**
- `pk_o_n_g`: CREATE UNIQUE INDEX pk_o_n_g ON public.o_n_g USING btree (id_o_n_g)

---

#### `o_n_gs2students`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| o_n_gs_fk | character varying(1024) | No | - | ✅ |  |
| students_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** students_fk, o_n_gs_fk

**Claves foráneas:**
- `o_n_gs_fk` → `o_n_g.id_o_n_g`
- `students_fk` → `student.id_student`

**Índices:**
- `pk_o_n_gs2students`: CREATE UNIQUE INDEX pk_o_n_gs2students ON public.o_n_gs2students USING btree (o_n_gs_fk, students_fk)

---

#### `ocupation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_ocupation | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_ocupation

**Índices:**
- `pk_ocupation`: CREATE UNIQUE INDEX pk_ocupation ON public.ocupation USING btree (id_ocupation)

---

#### `optional_course`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| optional_course_id | character varying(1024) | No | - | ✅ |  |
| real_time | integer(32,0) | No | - |  |  |
| estimated_time | integer(32,0) | No | - |  |  |
| cancelled | boolean | No | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** optional_course_id

**Claves foráneas:**
- `subject_fk` → `subject.subject_id`

**Índices:**
- `pk_electivel_subject`: CREATE UNIQUE INDEX pk_electivel_subject ON public.optional_course USING btree (optional_course_id)

---

#### `organism`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_organism | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| code | character varying | Sí | - |  |  |
| initials | character varying | Sí | - |  |  |

**Clave primaria:** id_organism

**Índices:**
- `pk_organism`: CREATE UNIQUE INDEX pk_organism ON public.organism USING btree (id_organism)

---

#### `orphan`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_orphan | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_orphan

**Índices:**
- `pk_orphan`: CREATE UNIQUE INDEX pk_orphan ON public.orphan USING btree (id_orphan)

---

#### `periodic_evaluation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| periodic_evaluation_id | character varying(1024) | No | - | ✅ |  |
| periodic_evaluation_type_fk | character varying(1024) | Sí | - |  |  |
| user_name | character varying(1024) | Sí | - |  |  |
| host | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |
| date | date | Sí | - |  |  |
| week | integer(32,0) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| evaluation_value_fk | character varying(1024) | Sí | - |  |  |
| professor_name | character varying(1024) | Sí | - |  |  |
| deleted | boolean | Sí | - |  |  |

**Clave primaria:** periodic_evaluation_id

**Claves foráneas:**
- `evaluation_value_fk` → `evaluation_value.id_evaluation_value`
- `periodic_evaluation_type_fk` → `periodic_evaluation_type.periodic_evaluation_type_id`
- `professor_fk` → `professor.professor_id`
- `student_fk` → `student.id_student`
- `subject_fk` → `subject.subject_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_periodic_evaluation`: CREATE UNIQUE INDEX pk_periodic_evaluation ON public.periodic_evaluation USING btree (periodic_evaluation_id)

---

#### `periodic_evaluation_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| periodic_evaluation_type_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |
| priority | integer(32,0) | Sí | - |  |  |
| cancelled | boolean | Sí | - |  |  |

**Clave primaria:** periodic_evaluation_type_id

**Índices:**
- `pk_periodic_evaluation_type`: CREATE UNIQUE INDEX pk_periodic_evaluation_type ON public.periodic_evaluation_type USING btree (periodic_evaluation_type_id)

---

#### `planner_resource`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| resource_id | character varying(1024) | Sí | - |  |  |
| resource_type | integer(32,0) | No | - |  |  |
| user_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `user_fk` → `xuser.id`

**Índices:**
- `pk_planner_resource`: CREATE UNIQUE INDEX pk_planner_resource ON public.planner_resource USING btree (id)

---

#### `politic_org`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_politic_org | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_politic_org

**Índices:**
- `pk_politic_org`: CREATE UNIQUE INDEX pk_politic_org ON public.politic_org USING btree (id_politic_org)

---

#### `popular_org`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | bigint(64,0) | No | - |  |  |
| id_popular_org | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_popular_org

**Índices:**
- `pk_popular_org`: CREATE UNIQUE INDEX pk_popular_org ON public.popular_org USING btree (id_popular_org)

---

#### `popular_orgs2students`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| popular_orgs_fk | character varying(1024) | No | - | ✅ |  |
| students_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** students_fk, popular_orgs_fk

**Claves foráneas:**
- `popular_orgs_fk` → `popular_org.id_popular_org`
- `students_fk` → `student.id_student`

**Índices:**
- `pk_popular_orgs2students`: CREATE UNIQUE INDEX pk_popular_orgs2students ON public.popular_orgs2students USING btree (popular_orgs_fk, students_fk)

---

#### `preinscription_evaluation`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_evaluation | character varying(1024) | No | - | ✅ |  |
| evaluation | real(24,None) | No | - |  |  |
| entry_subject_fk | character varying(1024) | Sí | - |  |  |
| preinscription_student_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_evaluation

**Claves foráneas:**
- `entry_subject_fk` → `entry_subject.id_entry_subject`
- `preinscription_student_fk` → `preinscription_student.id_preinscription`

**Índices:**
- `pk_preinscription_evaluation`: CREATE UNIQUE INDEX pk_preinscription_evaluation ON public.preinscription_evaluation USING btree (id_evaluation)

---

#### `preinscription_student`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_preinscription | character varying(1024) | No | - | ✅ |  |
| identification | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| middle_name | character varying(1024) | Sí | - |  |  |
| last_name | character varying(1024) | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| academic_index | real(24,None) | No | - |  |  |
| scale | real(24,None) | No | - |  |  |
| option | integer(32,0) | No | '-1'::integer |  |  |
| reoffer | boolean | No | false |  |  |
| deferred | integer(32,0) | No | - |  |  |
| national_career_fk | character varying(1024) | Sí | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |
| entry_source_fk | character varying(1024) | Sí | - |  |  |
| mother_occupation_fk | character varying(1024) | Sí | - |  |  |
| country_fk | character varying(1024) | Sí | - |  |  |
| father_occupation_fk | character varying(1024) | Sí | - |  |  |
| sex_fk | character varying(1024) | Sí | - |  |  |
| father_academic_level_fk | character varying(1024) | Sí | - |  |  |
| skin_color_fk | character varying(1024) | Sí | - |  |  |
| course_type_fk | character varying(1024) | Sí | - |  |  |
| mother_academic_level_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_preinscription

**Claves foráneas:**
- `father_academic_level_fk` → `academic_level.id_academic_level`
- `mother_academic_level_fk` → `academic_level.id_academic_level`
- `country_fk` → `country.id_country`
- `course_type_fk` → `course_type.id_course_type`
- `entry_source_fk` → `entry_source.id_entry_source`
- `national_career_fk` → `national_career.id_national_career`
- `father_occupation_fk` → `ocupation.id_ocupation`
- `mother_occupation_fk` → `ocupation.id_ocupation`
- `sex_fk` → `sex.id_sex`
- `skin_color_fk` → `skin_color.id_skin_color`
- `town_fk` → `town.id_town`

**Índices:**
- `pk_preinscription_student`: CREATE UNIQUE INDEX pk_preinscription_student ON public.preinscription_student USING btree (id_preinscription)

---

#### `professor`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| professor_id | character varying(1024) | No | - | ✅ |  |
| cancelled | boolean | Sí | - |  |  |
| user_fk | character varying(1024) | Sí | - |  |  |
| department_fk | character varying(1024) | Sí | - |  |  |
| scientific_category | character varying(1024) | Sí | - |  |  |
| teaching_category | character varying(1024) | Sí | - |  |  |

**Clave primaria:** professor_id

**Claves foráneas:**
- `department_fk` → `department.department_id`
- `user_fk` → `xuser.id`

**Índices:**
- `pk_professor`: CREATE UNIQUE INDEX pk_professor ON public.professor USING btree (professor_id)

---

#### `province`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_province | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| code | character varying | Sí | - |  |  |

**Clave primaria:** id_province

**Índices:**
- `pk_province`: CREATE UNIQUE INDEX pk_province ON public.province USING btree (id_province)

---

#### `rematriculated`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| rematriculated_id | character varying(1024) | No | - | ✅ |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** rematriculated_id

**Índices:**
- `pk_rematriculated`: CREATE UNIQUE INDEX pk_rematriculated ON public.rematriculated USING btree (rematriculated_id)

---

#### `report`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| report_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| description | character varying(1024) | Sí | - |  |  |
| area | character varying(1024) | Sí | - |  |  |
| type | character varying(1024) | Sí | - |  |  |

**Clave primaria:** report_id

**Índices:**
- `pk_report`: CREATE UNIQUE INDEX pk_report ON public.report USING btree (report_id)

---

#### `scholastic_origin`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_scholastic_origin | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_scholastic_origin

**Índices:**
- `pk_scholastic_origin`: CREATE UNIQUE INDEX pk_scholastic_origin ON public.scholastic_origin USING btree (id_scholastic_origin)

---

#### `scienc_especialty`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_scienc_especialty | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_scienc_especialty

**Índices:**
- `pk_scienc_especialty`: CREATE UNIQUE INDEX pk_scienc_especialty ON public.scienc_especialty USING btree (id_scienc_especialty)

---

#### `security_level`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| description | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Índices:**
- `pk_security_level`: CREATE UNIQUE INDEX pk_security_level ON public.security_level USING btree (id)

---

#### `security_role`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| role_name | character varying(1024) | Sí | - |  |  |
| group_name | character varying(1024) | Sí | - |  |  |
| description | character varying(1024) | Sí | - |  |  |
| role_link | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id

**Índices:**
- `pk_security_role`: CREATE UNIQUE INDEX pk_security_role ON public.security_role USING btree (id)

---

#### `security_roles2users`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| security_roles_fk | character varying(1024) | No | - | ✅ |  |
| users_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** security_roles_fk, users_fk

**Claves foráneas:**
- `security_roles_fk` → `security_role.id`
- `users_fk` → `xuser.id`

**Índices:**
- `pk_security_roles2users`: CREATE UNIQUE INDEX pk_security_roles2users ON public.security_roles2users USING btree (security_roles_fk, users_fk)

---

#### `sex`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_sex | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_sex

**Índices:**
- `pk_sex`: CREATE UNIQUE INDEX pk_sex ON public.sex USING btree (id_sex)

---

#### `skin_color`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_skin_color | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_skin_color

**Índices:**
- `pk_skin_color`: CREATE UNIQUE INDEX pk_skin_color ON public.skin_color USING btree (id_skin_color)

---

#### `student`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_student | character varying(1024) | No | - | ✅ |  |
| identification | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| middle_name | character varying(1024) | Sí | - |  |  |
| last_name | character varying(1024) | Sí | - |  |  |
| native_of | character varying(1024) | Sí | - |  |  |
| birth_date | date | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| son_count | integer(32,0) | Sí | - |  |  |
| phone | character varying(1024) | Sí | - |  |  |
| email | character varying(1024) | Sí | - |  |  |
| higher_education_in_date | date | Sí | - |  |  |
| university_in_date | date | Sí | - |  |  |
| register_date | timestamp without time zone | Sí | - |  |  |
| scale | real(24,None) | Sí | - |  |  |
| academic_index | real(24,None) | Sí | - |  |  |
| scholastic_origin_fk | character varying(1024) | No | - |  |  |
| country_fk | character varying(1024) | No | - |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |
| study_regimen_fk | character varying(1024) | No | - |  |  |
| skin_color_fk | character varying(1024) | No | - |  |  |
| student_type_fk | character varying(1024) | No | - |  |  |
| entry_source_fk | character varying(1024) | No | - |  |  |
| sex_fk | character varying(1024) | No | - |  |  |
| orphan_fk | character varying(1024) | No | - |  |  |
| faculty_fk | character varying(1024) | Sí | - |  |  |
| politic_org_fk | character varying(1024) | No | - |  |  |
| marital_status_fk | character varying(1024) | No | - |  |  |
| course_type_fk | character varying(1024) | No | - |  |  |
| town_university_fk | character varying(1024) | Sí | - |  |  |
| academic_situation_fk | character varying(1024) | No | - |  |  |
| student_status_fk | character varying(1024) | Sí | - |  |  |
| photo | character varying(1024) | Sí | - |  |  |
| reoffer | boolean | Sí | false |  |  |
| option | integer(32,0) | Sí | - |  |  |
| block | boolean | Sí | false |  |  |
| gold_title | boolean | Sí | false |  |  |
| gold_title_resolution | character varying | Sí | - |  |  |
| gold_title_date | timestamp without time zone | Sí | - |  |  |
| scientific_merit_award | boolean | Sí | false |  |  |

**Clave primaria:** id_student

**Claves foráneas:**
- `academic_situation_fk` → `academic_situation.id_academic_situation`
- `career_fk` → `career.id_career`
- `country_fk` → `country.id_country`
- `course_type_fk` → `course_type.id_course_type`
- `entry_source_fk` → `entry_source.id_entry_source`
- `faculty_fk` → `faculty.id_faculty`
- `marital_status_fk` → `marital_status.id_marital_status`
- `orphan_fk` → `orphan.id_orphan`
- `politic_org_fk` → `politic_org.id_politic_org`
- `scholastic_origin_fk` → `scholastic_origin.id_scholastic_origin`
- `sex_fk` → `sex.id_sex`
- `skin_color_fk` → `skin_color.id_skin_color`
- `student_status_fk` → `student_status.id_student_status`
- `student_type_fk` → `student_type.id_student_class`
- `study_regimen_fk` → `study_regimen.id_study_regimen`
- `town_fk` → `town.id_town`
- `town_university_fk` → `town_university.id_town_university`

**Índices:**
- `pk_student`: CREATE UNIQUE INDEX pk_student ON public.student USING btree (id_student)

---

#### `student2career_profiles`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| student_id | character varying | No | - | ✅ |  |
| career_profile_id | character varying | No | - | ✅ |  |

**Clave primaria:** career_profile_id, student_id

**Claves foráneas:**
- `career_profile_id` → `career_profile.id`
- `student_id` → `student.id_student`

**Índices:**
- `student2career_profiles_pkey`: CREATE UNIQUE INDEX student2career_profiles_pkey ON public.student2career_profiles USING btree (student_id, career_profile_id)

---

#### `student_award`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_award_student | character varying(1024) | No | - | ✅ |  |
| matriculated_subject_fk | character varying(1024) | Sí | - |  |  |
| award_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| create_date | timestamp without time zone | Sí | - |  |  |
| user_name | character varying(1024) | Sí | - |  |  |
| host | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| assigned_date | timestamp without time zone | Sí | - |  |  |

**Clave primaria:** id_award_student

**Claves foráneas:**
- `award_fk` → `award.id_award`
- `course_fk` → `course.id_course`
- `matriculated_subject_fk` → `matriculated_subject.matriculated_subject_id`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_student_award`: CREATE UNIQUE INDEX pk_student_award ON public.student_award USING btree (id_award_student)

---

#### `student_bonus`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_bonus_student | character varying(1024) | No | - | ✅ |  |
| period | integer(32,0) | No | - |  |  |
| create_date | timestamp without time zone | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| bonus_fk | character varying(1024) | Sí | - |  |  |
| user_name | character varying(1024) | Sí | - |  |  |
| host | character varying(1024) | Sí | - |  |  |
| assigned_date | timestamp without time zone | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| description | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_bonus_student

**Claves foráneas:**
- `bonus_fk` → `bonus.id_bonus`
- `course_fk` → `course.id_course`
- `student_fk` → `student.id_student`

**Índices:**
- `pk_student_bonus`: CREATE UNIQUE INDEX pk_student_bonus ON public.student_bonus USING btree (id_bonus_student)

---

#### `student_cut`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| student_cut_id | character varying(1024) | No | - | ✅ |  |
| cant_hours_ausent | integer(32,0) | No | - |  |  |
| ausent_percent | real(24,None) | No | - |  |  |
| date | date | Sí | - |  |  |
| evaluations_cuts_fk | character varying(1024) | Sí | - |  |  |
| cualitative_evaluation_fk | character varying(1024) | Sí | - |  |  |
| professor_fk | character varying(1024) | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |
| consecutive | integer(32,0) | Sí | - |  |  |
| evaluative_court_header_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** student_cut_id

**Claves foráneas:**
- `cualitative_evaluation_fk` → `cualitative_evaluation.cualitative_evaluation_id`
- `evaluations_cuts_fk` → `evaluations_cuts.evaluations_cuts_id`
- `evaluative_court_header_fk` → `evaluative_court_header.evaluative_court_header_id`
- `professor_fk` → `professor.professor_id`
- `student_fk` → `student.id_student`
- `subject_fk` → `subject.subject_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_student_cut`: CREATE UNIQUE INDEX pk_student_cut ON public.student_cut USING btree (student_cut_id)

---

#### `student_group_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| student_group_type_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| uniqued | boolean | No | - |  |  |

**Clave primaria:** student_group_type_id

**Índices:**
- `pk_student_group_type`: CREATE UNIQUE INDEX pk_student_group_type ON public.student_group_type USING btree (student_group_type_id)

---

#### `student_status`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_student_status | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_student_status

**Índices:**
- `pk_student_status`: CREATE UNIQUE INDEX pk_student_status ON public.student_status USING btree (id_student_status)

---

#### `student_status_history`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_student_status_history | character varying(1024) | No | - | ✅ |  |
| date | timestamp without time zone | Sí | - |  |  |
| comment | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |
| student_status_fk | character varying(1024) | Sí | - |  |  |
| end_date | timestamp without time zone | Sí | - |  |  |
| previous_history_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_student_status_history

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `student_fk` → `student.id_student`
- `student_status_fk` → `student_status.id_student_status`
- `previous_history_fk` → `student_status_history.id_student_status_history`

**Índices:**
- `pk_student_status_history`: CREATE UNIQUE INDEX pk_student_status_history ON public.student_status_history USING btree (id_student_status_history)

---

#### `student_type`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_student_class | character varying(1024) | No | - | ✅ |  |
| kind | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_student_class

**Índices:**
- `pk_student_type`: CREATE UNIQUE INDEX pk_student_type ON public.student_type USING btree (id_student_class)

---

#### `student_volume_folio`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | integer(32,0) | No | nextval('student_volume_folio_id_seq'::regclass) | ✅ |  |
| volume_faculty | integer(32,0) | Sí | - |  |  |
| volume_institute | integer(32,0) | Sí | - |  |  |
| folio_faculty | integer(32,0) | Sí | - |  |  |
| folio_institute | integer(32,0) | Sí | - |  |  |
| student_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `student_fk` → `student.id_student`

**Índices:**
- `students_volume_folio_pkey`: CREATE UNIQUE INDEX students_volume_folio_pkey ON public.student_volume_folio USING btree (id)

---

#### `study_program`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| study_program_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| periods_amount | integer(32,0) | No | - |  |  |
| description | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |
| study_program_name_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| approved | boolean | No | - |  |  |
| years_amount | integer(32,0) | Sí | - |  |  |

**Clave primaria:** study_program_id

**Claves foráneas:**
- `career_fk` → `career.id_career`
- `course_fk` → `course.id_course`
- `study_program_name_fk` → `study_program_name.study_program_name_id`

**Índices:**
- `pk_custom_study_program`: CREATE UNIQUE INDEX pk_custom_study_program ON public.study_program USING btree (study_program_id)

---

#### `study_program_name`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| study_program_name_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** study_program_name_id

**Índices:**
- `pk_study_program_name`: CREATE UNIQUE INDEX pk_study_program_name ON public.study_program_name USING btree (study_program_name_id)

---

#### `study_program_version`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| study_program_version_id | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | false |  |  |
| study_program_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** study_program_version_id

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `study_program_fk` → `study_program.study_program_id`

**Índices:**
- `pk_study_program_version`: CREATE UNIQUE INDEX pk_study_program_version ON public.study_program_version USING btree (study_program_version_id)

---

#### `study_regimen`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_study_regimen | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_study_regimen

**Índices:**
- `pk_study_regimen`: CREATE UNIQUE INDEX pk_study_regimen ON public.study_regimen USING btree (id_study_regimen)

---

#### `subject`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| subject_id | character varying(1024) | No | - | ✅ |  |
| topics_program | text | Sí | - |  |  |
| analytical_program | text | Sí | - |  |  |
| period | integer(32,0) | Sí | - |  |  |
| hours | integer(32,0) | No | - |  |  |
| cancelled | boolean | No | false |  |  |
| basic | boolean | No | false |  |  |
| year | integer(32,0) | Sí | - |  |  |
| subject_name_fk | character varying(1024) | Sí | - |  |  |
| discipline_fk | character varying(1024) | Sí | - |  |  |
| evaluation_type_fk | character varying(1024) | Sí | - |  |  |
| assigned_subject_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** subject_id

**Claves foráneas:**
- `assigned_subject_fk` → `assigned_subject.assigned_subject_id`
- `discipline_fk` → `discipline.discipline_id`
- `evaluation_type_fk` → `evaluation_type.evaluation_type_id`
- `subject_name_fk` → `subject_name.subject_name_id`

**Índices:**
- `pk_subject`: CREATE UNIQUE INDEX pk_subject ON public.subject USING btree (subject_id)
- `idx_s_asigned_subject`: CREATE INDEX idx_s_asigned_subject ON public.subject USING btree (assigned_subject_fk)

---

#### `subject_configuration`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| subject_configuration_id | character varying(1024) | No | - | ✅ |  |
| cancelled | boolean | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| evaluations_registry_start_date | date | Sí | - |  |  |
| evaluations_registry_end_date | date | Sí | - |  |  |

**Clave primaria:** subject_configuration_id

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `subject_fk` → `subject.subject_id`

**Índices:**
- `pk_subject_configuration`: CREATE UNIQUE INDEX pk_subject_configuration ON public.subject_configuration USING btree (subject_configuration_id)

---

#### `subject_group`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| averageable | boolean | No | true |  |  |
| matriculated_subject_type_fk | character varying(1024) | Sí | - |  |  |
| subject_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `matriculated_subject_type_fk` → `matriculated_subject_type.matriculated_subject_type_id`
- `subject_fk` → `subject.subject_id`
- `group_fk` → `xgroup.id_group`

**Restricciones UNIQUE:** group_fk, subject_fk

**Índices:**
- `pk_subject_group`: CREATE UNIQUE INDEX pk_subject_group ON public.subject_group USING btree (id)
- `unq_subject_group`: CREATE UNIQUE INDEX unq_subject_group ON public.subject_group USING btree (subject_fk, group_fk)

---

#### `subject_name`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| subject_name_id | character varying(1024) | No | - | ✅ |  |
| code | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| abbreviation | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | false |  |  |

**Clave primaria:** subject_name_id

**Índices:**
- `pk_subject_name`: CREATE UNIQUE INDEX pk_subject_name ON public.subject_name USING btree (subject_name_id)

---

#### `syndicate`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_syndicate | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |

**Clave primaria:** id_syndicate

**Índices:**
- `pk_syndicate`: CREATE UNIQUE INDEX pk_syndicate ON public.syndicate USING btree (id_syndicate)

---

#### `town`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_town | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| province_fk | character varying(1024) | Sí | - |  |  |
| code | character varying | Sí | - |  |  |

**Clave primaria:** id_town

**Claves foráneas:**
- `province_fk` → `province.id_province`

**Índices:**
- `pk_town`: CREATE UNIQUE INDEX pk_town ON public.town USING btree (id_town)

---

#### `town_universities2users`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| town_universities_fk | character varying(1024) | No | - | ✅ |  |
| users_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** users_fk, town_universities_fk

**Claves foráneas:**
- `town_universities_fk` → `town_university.id_town_university`
- `users_fk` → `xuser.id`

**Índices:**
- `pk_town_universities2users`: CREATE UNIQUE INDEX pk_town_universities2users ON public.town_universities2users USING btree (town_universities_fk, users_fk)

---

#### `town_university`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_town_university | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| initial | character varying(1024) | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| phone_number | character varying(1024) | Sí | - |  |  |
| fax | character varying(1024) | Sí | - |  |  |
| rector_name | character varying(1024) | Sí | - |  |  |
| general_secretary_name | character varying(1024) | Sí | - |  |  |
| graduation_date | date | Sí | - |  |  |
| matriculation_end_date | date | Sí | - |  |  |
| rematriculation_begin_date | date | Sí | - |  |  |
| rematriculation_end_date | date | Sí | - |  |  |
| matriculation_begin_date | date | Sí | - |  |  |
| activities | character varying(1024) | Sí | - |  |  |
| logo | character varying(1024) | Sí | - |  |  |
| bylaw | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |
| university_fk | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_town_university

**Claves foráneas:**
- `town_fk` → `town.id_town`
- `university_fk` → `university.id_university`

**Índices:**
- `pk_town_university`: CREATE UNIQUE INDEX pk_town_university ON public.town_university USING btree (id_town_university)

---

#### `transfer`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_transfer | character varying(1024) | No | - | ✅ |  |
| target_career_fk | character varying(1024) | Sí | - |  |  |
| source_career_fk | character varying(1024) | Sí | - |  |  |
| drop_fk | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_transfer

**Claves foráneas:**
- `source_career_fk` → `career.id_career`
- `target_career_fk` → `career.id_career`
- `drop_fk` → `xdrop.id_drop`
- `drop_fk` → `xdrop.id_drop`

**Índices:**
- `pk_transfer`: CREATE UNIQUE INDEX pk_transfer ON public.transfer USING btree (id_transfer)

---

#### `universities2users`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| universities_fk | character varying(1024) | No | - | ✅ |  |
| users_fk | character varying(1024) | No | - | ✅ |  |

**Clave primaria:** users_fk, universities_fk

**Claves foráneas:**
- `universities_fk` → `university.id_university`
- `users_fk` → `xuser.id`

**Índices:**
- `pk_universities2users`: CREATE UNIQUE INDEX pk_universities2users ON public.universities2users USING btree (universities_fk, users_fk)

---

#### `university`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_university | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| initial | character varying(1024) | Sí | - |  |  |
| address | character varying(1024) | Sí | - |  |  |
| phone_number | character varying(1024) | Sí | - |  |  |
| fax | character varying(1024) | Sí | - |  |  |
| rector_name | character varying(1024) | Sí | - |  |  |
| general_secretary_name | character varying(1024) | Sí | - |  |  |
| graduation_date | date | Sí | - |  |  |
| matriculation_begin_date | date | Sí | - |  |  |
| matriculation_end_date | date | Sí | - |  |  |
| rematriculation_begin_date | date | Sí | - |  |  |
| rematriculation_end_date | date | Sí | - |  |  |
| activities | character varying(1024) | Sí | - |  |  |
| logo | character varying(1024) | Sí | - |  |  |
| bylaw | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| town_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| code | character varying(1024) | Sí | - |  |  |
| closure | boolean | Sí | - |  |  |
| start | boolean | Sí | - |  |  |
| promote | boolean | Sí | - |  |  |

**Clave primaria:** id_university

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `town_fk` → `town.id_town`

**Índices:**
- `pk_university`: CREATE UNIQUE INDEX pk_university ON public.university USING btree (id_university)

---

#### `w_s_connection`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| wsdl_url | character varying(1024) | Sí | - |  |  |
| enabled | boolean | No | - |  |  |
| secured | boolean | No | - |  |  |
| username | character varying(1024) | Sí | - |  |  |
| password | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Índices:**
- `pk_w_s_connection`: CREATE UNIQUE INDEX pk_w_s_connection ON public.w_s_connection USING btree (id)

---

#### `xdrop`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_drop | character varying(1024) | No | - | ✅ |  |
| begin_date | timestamp without time zone | Sí | - |  |  |
| student_status_history_fk | character varying(1024) | Sí | - |  |  |
| drop_motive_fk | character varying(1024) | Sí | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| comment | character varying(1024) | Sí | - |  |  |
| year | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id_drop

**Claves foráneas:**
- `course_fk` → `course.id_course`
- `drop_motive_fk` → `drop_motive.id_drop_motive`

**Índices:**
- `pk_drop`: CREATE UNIQUE INDEX pk_drop ON public.xdrop USING btree (id_drop)

---

#### `xgroup`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id_group | character varying(1024) | No | - | ✅ |  |
| name | character varying(1024) | Sí | - |  |  |
| cancelled | boolean | No | - |  |  |
| course_fk | character varying(1024) | Sí | - |  |  |
| group_type_fk | character varying(1024) | Sí | - |  |  |
| study_program_version_fk | character varying(1024) | Sí | - |  |  |
| group_fk | character varying(1024) | Sí | - |  |  |
| career_fk | character varying(1024) | Sí | - |  |  |
| period_ini | integer(32,0) | Sí | - |  |  |
| period_end | integer(32,0) | Sí | - |  |  |
| year | integer(32,0) | Sí | - |  |  |
| terminal | boolean | Sí | - |  |  |

**Clave primaria:** id_group

**Claves foráneas:**
- `career_fk` → `career.id_career`
- `course_fk` → `course.id_course`
- `group_type_fk` → `group_type.id_group_type`
- `study_program_version_fk` → `study_program_version.study_program_version_id`
- `group_fk` → `xgroup.id_group`

**Índices:**
- `pk_group`: CREATE UNIQUE INDEX pk_group ON public.xgroup USING btree (id_group)

---

#### `xuser`

| Columna | Tipo | Null | Default | PK | Identity |
|---|---|---|---|---|---|
| id | character varying(1024) | No | - | ✅ |  |
| username | character varying(1024) | Sí | - |  |  |
| password | character varying(1024) | Sí | - |  |  |
| identification | character varying(1024) | Sí | - |  |  |
| name | character varying(1024) | Sí | - |  |  |
| surname | character varying(1024) | Sí | - |  |  |
| last_surname | character varying(1024) | Sí | - |  |  |
| email | character varying(1024) | Sí | - |  |  |
| description | character varying(1024) | Sí | - |  |  |
| blocked | boolean | No | - |  |  |
| cancelled | boolean | No | - |  |  |
| security_level_fk | character varying(1024) | Sí | - |  |  |
| remote_user | boolean | No | - |  |  |
| last_login_ip | character varying(1024) | Sí | - |  |  |
| last_login_date | timestamp without time zone | Sí | - |  |  |
| question | character varying(1024) | Sí | - |  |  |

**Clave primaria:** id

**Claves foráneas:**
- `security_level_fk` → `security_level.id`

**Restricciones UNIQUE:** username

**Índices:**
- `pk_user`: CREATE UNIQUE INDEX pk_user ON public.xuser USING btree (id)
- `xuser_username_key`: CREATE UNIQUE INDEX xuser_username_key ON public.xuser USING btree (username)

---

### Vistas

- `josso_user`
- `josso_user_property`
- `josso_user_role`

### Triggers

- **`propagate_update`** en `assigned_subject` (AFTER UPDATE)
  ```sql
  EXECUTE PROCEDURE propagate_assigned_subject_update()
  ```
- **`no_duplicados`** en `evaluation` (BEFORE INSERT)
  ```sql
  EXECUTE PROCEDURE no_evaluar_doble()
  ```
- **`no_duplicados`** en `evaluation` (BEFORE UPDATE)
  ```sql
  EXECUTE PROCEDURE no_evaluar_doble()
  ```
- **`create_privilege_to_adm`** en `faculty` (AFTER INSERT)
  ```sql
  EXECUTE PROCEDURE assign_faculty_privilege_to_adm()
  ```
- **`no_duplicados`** en `matriculated_subject` (BEFORE UPDATE)
  ```sql
  EXECUTE PROCEDURE no_matricular_doble()
  ```
- **`no_duplicados`** en `matriculated_subject` (BEFORE INSERT)
  ```sql
  EXECUTE PROCEDURE no_matricular_doble()
  ```
- **`create_privilege_to_adm`** en `town_university` (AFTER INSERT)
  ```sql
  EXECUTE PROCEDURE assign_cum_privilege_to_adm()
  ```
- **`trac_trigger_delete_into_trac_user`** en `xuser` (AFTER DELETE)
  ```sql
  EXECUTE PROCEDURE trac_trigger_function_delete_into_trac_user()
  ```
- **`trac_trigger_insert_into_trac_user`** en `xuser` (AFTER INSERT)
  ```sql
  EXECUTE PROCEDURE trac_trigger_function_insert_into_trac_user()
  ```
- **`trac_trigger_update_into_trac_user`** en `xuser` (AFTER UPDATE)
  ```sql
  EXECUTE PROCEDURE trac_trigger_function_update_into_trac_user()
  ```