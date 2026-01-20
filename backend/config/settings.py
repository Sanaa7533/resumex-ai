import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class Settings:
    APP_NAME: str = "RESUMEX AI"
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/resumexdb")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")

settings = Settings()
