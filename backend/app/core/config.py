import json

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Sistema de Gestion de Telefonia"
    api_prefix: str = "/api/v1"
    environment: str = "development"  # development | production

    database_url: str = "sqlite:///./dev.db"
    secret_key: str = "cambiar-en-produccion"
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"

    moneda: str = "CUP"
    locale: str = "es-CU"

    # Password inicial del admin creado por el seed (nunca por defecto).
    admin_initial_password: str = ""

    # Politica de contrasenas.
    password_min_length: int = 10
    password_max_bytes: int = 72  # bcrypt trunca silenciosamente
    password_max_chars: int = 128

    # Rate limiting del login (por IP y por usuario).
    login_max_intentos: int = 5
    login_ventana_minutos: int = 1
    login_bloqueo_minutos: int = 15
    login_rate_limit_habilitado: bool = True

    # Origenes permitidos para CORS (separados por coma o JSON).
    cors_origins: str = "http://localhost:5173,http://localhost:3000"

    assets_rrhh_habilitado: bool = False
    assets_rrhh_server: str = ""
    assets_rrhh_database: str = "ASSETS_RH"
    assets_rrhh_username: str = ""
    assets_rrhh_password: str = ""
    assets_rrhh_driver: str = "ODBC Driver 17 for SQL Server"
    assets_rrhh_encrypt: bool = True
    assets_rrhh_trust_server_certificate: bool = False
    assets_rrhh_timeout: int = 15

    @property
    def cors_origins_list(self) -> list[str]:
        valor = (self.cors_origins or "").strip()
        if not valor:
            return []
        try:
            parsed = json.loads(valor)
            if isinstance(parsed, list):
                return [str(o).strip() for o in parsed if str(o).strip()]
        except ValueError:
            pass
        return [o.strip() for o in valor.split(",") if o.strip()]

    def validar_entorno(self) -> None:
        """Fail-closed: en produccion exige claves y URL de BD seguras."""
        if self.environment != "production":
            return
        if not self.secret_key or self.secret_key == "cambiar-en-produccion":
            raise ValueError("SECRET_KEY no definida o con el valor por defecto en produccion")
        if len(self.secret_key) < 32:
            raise ValueError("SECRET_KEY debe tener al menos 32 caracteres en produccion")
        if not self.database_url or self.database_url.startswith("sqlite"):
            raise ValueError("DATABASE_URL es obligatoria y no puede ser SQLite en produccion")


settings = Settings()
settings.validar_entorno()