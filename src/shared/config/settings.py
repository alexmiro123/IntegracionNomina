from pydantic_settings import BaseSettings
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_SERVICE: str

    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int

    PRIVATE_KEY: str
    PUBLIC_KEY: str

    AES_SECRET_KEY: str

    LOG_LEVEL: str
    ORACLE_CLIENT_PATH: str

    APP_HOST: str
    APP_PORT: int

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()