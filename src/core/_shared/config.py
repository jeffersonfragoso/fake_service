import structlog
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

log = structlog.stdlib.get_logger()

class Settings(BaseSettings):
    ENV_NAME: str = "Local"
    DB_URL: str = "sqlite:///database.db"
    SECRET_KEY: str
    DEFAULT_USER: str
    DEFAULT_USER_PASSWORD: str
    DEFAULT_ADMIN: str
    DEFAULT_ADMIN_PASSWORD: str

    LOG_LEVEL: str = "INFO"
    ENABLE_JSON_LOGS: bool = False

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        case_sensitive=True,
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    log.info(f"Loading settings for: {settings.ENV_NAME}")
    return settings
