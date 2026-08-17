from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    BOT_TOKEN: str
    CHANNEL_ID: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    PARSING_INTERVAL_MINUTES: int
    DEBUG: bool

    


settings = Settings()  