from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    NAME_PROJECT: str = 'fastapi_zero'
    VERSION: str = '0.1.0'
    DESCRIPTION: str = 'A minimal FastAPI application with zero dependencies.'
    ROOT_PATH: str = '/api/v1'
    IS_PRODUCTION: bool
    SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    EXPIRE: int = 1

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
