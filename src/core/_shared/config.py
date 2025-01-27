from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV_NAME: str = "Local"
    DB_URL: str = "sqlite:///database.db"
    SECRET_KEY: str
    DEFAULT_USER: str
    DEFAULT_USER_PASSWORD: str
    DEFAULT_ADMIN: str
    DEFAULT_ADMIN_PASSWORD: str

    model_config = SettingsConfigDict(
        extra="ignore", env_file=".env",
        case_sensitive=True,
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.ENV_NAME}")
    return settings
