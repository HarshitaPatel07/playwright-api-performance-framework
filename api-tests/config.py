import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# API Configuration
BASE_URL = os.getenv("BASE_URL", "https://gorest.co.in/public/v2")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # DEBUG, INFO, WARNING, ERROR, CRITICAL
