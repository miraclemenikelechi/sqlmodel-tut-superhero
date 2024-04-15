from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config: SettingsConfigDict = {
        "extra": "ignore",
        "env_file": ".env",
        "env_ignore_empty": True,
    }

    CURRENT_API_URL: str = "/api/v1"

    DOMAIN: str = "localhost"

    ENVIRONMENT: Literal["local", "staging", "production"] = "local"


server_config: AppSettings = AppSettings()
