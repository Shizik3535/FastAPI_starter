from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # Debug
    DEBUG: bool

    # Config
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
