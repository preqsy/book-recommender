from pydantic_settings import BaseSettings
from pathlib import Path

env_path = Path.cwd() / ".env"


class Settings(BaseSettings):
    DATABASE_URL: str
    DB_NAME: str
    SECRET_KEY: str = ""
    ALGORITHM: str = ""
    ACCESS_TOKEN_EXPIRY_TIME: int

    class Config:
        env_file = env_path


settings = Settings()
