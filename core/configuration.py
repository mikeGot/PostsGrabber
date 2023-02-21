from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    username: str
    api_id: str
    api_hash: str
    sites: dict = Field(default={"yandex_market": "https://t.me/market_marketplace",
                                 "ozon": "https://t.me/ozonmarketplace"})
    secret_key: str

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
