from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "TeamPixel"  # App name in swagger docs
    DEBUG: bool  # Show error preview
    SECRET_KEY: str  # Key for JWT generate
    CORS_ALLOWED_ORIGINS: str  # CORS middleware
    VERSION: str = "1.0 BETA"


settings = Settings()  # type: ignore
