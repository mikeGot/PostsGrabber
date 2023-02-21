from pathlib import Path

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    username: str
    api_id: str
    api_hash: str
    sites: dict = Field(
        default={
            "yandex_market": "https://t.me/market_marketplace",
            "ozon": "https://t.me/ozonmarketplace",
        }
    )
    secret_key: str
    debug: bool = Field(default=True)
    sqlite_dsn: str = Field(default="sqlite:///Django_Admin/db.sqlite3")

    class Config:
        case_sensitive = False
        env_file = f"{Path(__file__).resolve().parent.parent}/.env"


settings = Settings()
