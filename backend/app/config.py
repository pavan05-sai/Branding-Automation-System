"""
BrandCraft Configuration Module
Loads and validates environment variables for the application.
"""

import os
from typing import Optional
from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file (override ensures fresh values on reload)
load_dotenv(override=True)


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Groq Cloud Configuration
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    model_name: str = os.getenv("MODEL_NAME", "llama3-70b-8192") # Modified default model name
    
    # Optional Image Generation
    hf_api_token: Optional[str] = os.getenv("HF_API_TOKEN", None)
    sdxl_model: str = os.getenv("SDXL_MODEL", "stabilityai/stable-diffusion-xl-base-1.0")
    stability_api_key: Optional[str] = os.getenv("STABILITY_API_KEY", None)
    
    api_prefix: str = "/api"
    
    # Server Configuration
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # API Configuration
    api_prefix: str = "/api"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    Uses lru_cache to avoid reloading settings on every call.
    """
    return Settings()


def validate_settings() -> bool:
    """
    Validate that required settings are configured.
    Returns True if valid, raises ValueError if not.
    """
    settings = get_settings()
    
    if not settings.groq_api_key or settings.groq_api_key == "your_groq_api_key_here":
        raise ValueError(
            "GROQ_API_KEY is not configured. "
            "Please set it in your .env file."
        )
    
    return True
