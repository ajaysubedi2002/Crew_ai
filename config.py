from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MODEL: str    
    
    base_url : str

    class Config:
        # Load environment variables from the package .env file
        # (relative to the project root where you run Python)
        env_file = "agent_blog_writing/.env"
        extra = "ignore"  # Allow extra fields from .env without errors


# Instantiate the settings
settings = Settings()