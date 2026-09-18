from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Sistema de Gestion de Telefonia"
    api_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/telefonia"
    secret_key: str = "cambiar-en-produccion"
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"

    moneda: str = "CUP"
    locale: str = "es-CU"

    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    assets_rrhh_habilitado: bool = False
    assets_rrhh_server: str = "10.8.6.191"
    assets_rrhh_database: str = "ASSETS_RH"
    assets_rrhh_username: str = ""
    assets_rrhh_password: str = ""
    assets_rrhh_driver: str = "ODBC Driver 17 for SQL Server"


settings = Settings()