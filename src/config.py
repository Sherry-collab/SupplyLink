from pydantic_settings import BaseSettings, SettingsConfigDict

class settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = settings()