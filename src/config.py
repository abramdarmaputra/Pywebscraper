from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()

@dataclass(frozen=True)
class Settings:
    database_url: str
    base_url: str
    pages: int

    @staticmethod
    def load():
        return Settings(
            database_url=os.getenv("DATABASE_URL"),
            base_url=os.getenv("BASE_URL"),
            pages=int(os.getenv("PAGES", 3))
        )
        