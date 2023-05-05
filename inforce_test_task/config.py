import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_PORT: int = os.getenv("DATABASE_PORT")
    BUILD_VERSION: str = 'v1.0'


settings = Settings()
