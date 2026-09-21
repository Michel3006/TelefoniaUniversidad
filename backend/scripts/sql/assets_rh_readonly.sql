-- A4: usuario de solo lectura para ASSETS_RH que usa el backend en
-- `backend/app/services/institucional.py` (conexion ODBC). El backend solo
-- ejecuta SELECT sobre estas tablas/columnas, de ahi que los permisos se
-- limiten a esa operacion.
--
-- Ejecutar como administrador de la instancia de SQL Server.
-- Ajustar login/password y el nombre de la base antes de aplicar.

USE master;
GO

IF NOT EXISTS (SELECT 1 FROM sys.sql_logins WHERE name = N'troncal_rrhh_ro')
    CREATE LOGIN troncal_rrhh_ro WITH PASSWORD = N'CAMBIAR_PASSWORD_FUERTE', CHECK_POLICY = ON;
GO

USE ASSETS_RH;
GO

IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = N'troncal_rrhh_ro')
    CREATE USER troncal_rrhh_ro FOR LOGIN troncal_rrhh_ro;
GO

ALTER ROLE db_datareader ADD MEMBER troncal_rrhh_ro;
GO

-- El backend consulta unicamente estas tablas; db_datareader cubre la lectura.
-- Si la politica exige permiso explicito por tabla:
--   GRANT SELECT ON EMpLEADO_Gral TO troncal_rrhh_ro; etc.
GO

-- Alternativa estricta (recomendado): quitar db_datareader y otorgar solo lo necesario
-- ALTER ROLE db_datareader DROP MEMBER troncal_rrhh_ro;
-- GRANT SELECT ON RH_Cargos TO troncal_rrhh_ro;
-- GRANT SELECT ON RH_Area_Trabajo_Actual TO troncal_rrhh_ro;
-- GRANT SELECT ON RH_Unidades_Organizativas TO troncal_rrhh_ro;
-- GRANT SELECT ON Empleados_Gral TO troncal_rrhh_ro;
GO