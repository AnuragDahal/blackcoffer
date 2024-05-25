from dotenv import load_dotenv
import os
load_dotenv()


class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    FLASK_ENV = os.environ.get("FLASK_ENV")
