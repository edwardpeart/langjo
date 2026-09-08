import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_URL: str = os.getenv("DATABASE_URL") or os.getenv(
        "DB_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/langjo",
    )
    SECRET_KEY: str = os.getenv(
        "LANGJO_SECRET_KEY",
        "langjo-demo-secret-key-32-bytes-long",
    )
    ALGORITHM: str = os.getenv("LANGJO_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("LANGJO_ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    )
    DEMO_MODE: bool = os.getenv("LANGJO_DEMO") == "1"


config = Config()
DEMO_MODE = config.DEMO_MODE
