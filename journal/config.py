import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_URL: str = os.getenv(
        "DB_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/langjo",
    )
    DEMO_MODE: bool = os.getenv("LANGJO_DEMO") == "1"


config = Config()
