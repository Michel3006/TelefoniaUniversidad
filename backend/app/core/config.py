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


settings = Settings()