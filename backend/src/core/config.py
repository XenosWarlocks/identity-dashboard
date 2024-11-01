from pydantic import BaseSettings, Field, EmailStr
from typing import Optional

class Settings(BaseSettings):
    # General App Settings
    APP_NAME: str = Field("MyApp", env="APP_NAME")
    DEBUG: bool = Field(False, env="DEBUG")
    
    # Database Settings
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    DATABASE_USERNAME: Optional[str] = Field(None, env="DATABASE_USERNAME")
    DATABASE_PASSWORD: Optional[str] = Field(None, env="DATABASE_PASSWORD")

    # Security Settings
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field("HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # Email Settings (if applicable)
    SMTP_SERVER: Optional[str] = Field(None, env="SMTP_SERVER")
    SMTP_PORT: Optional[int] = Field(None, env="SMTP_PORT")
    EMAIL_FROM: Optional[EmailStr] = Field(None, env="EMAIL_FROM")
    EMAIL_PASSWORD: Optional[str] = Field(None, env="EMAIL_PASSWORD")

    # Other APIs and Integrations
    THIRD_PARTY_API_KEY: Optional[str] = Field(None, env="THIRD_PARTY_API_KEY")
    THIRD_PARTY_API_URL: Optional[str] = Field(None, env="THIRD_PARTY_API_URL")

    class Config:
        env_file = ".env"  # Path to the environment file
        env_file_encoding = "utf-8"  # Encoding for .env file

# Instantiate settings object for use across the application
settings = Settings()
