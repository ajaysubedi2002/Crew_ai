from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MODEL: str    
    
    base_url : str

    class Config:
        env_file = ".env"
        extra = "ignore"  # Allow extra fields from .env without errors


# Instantiate the settings
settings = Settings()