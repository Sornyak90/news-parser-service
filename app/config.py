from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = Field(default=True, description="Enable debug mode")

    database_url: str

    BOT_TOKEN: str
    CHANNEL_ID: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    PARSING_INTERVAL_MINUTES: int
    DEBUG: bool


settings = Settings()  # type: ignore
