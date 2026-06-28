from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    # ==========================
    # Database Configuration
    # ==========================
    DATABASE_URL: str

    # ==========================
    # JWT Authentication
    # ==========================
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # ==========================
    # GPS Simulator Configuration
    # ==========================
    GPS_UPDATE_INTERVAL: int = 3

    DEFAULT_BUS_ID: int = 2

    SIMULATED_BUS_COUNT: int = 5

    DEFAULT_SPEED: int = 40

    DEFAULT_HEADING: int = 180

    DESTINATION_LATITUDE: float = 18.5800

    DESTINATION_LONGITUDE: float = 73.9100

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )


settings = Settings()