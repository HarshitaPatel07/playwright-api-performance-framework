import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

BASE_URL = os.getenv("BASE_URL", "https://gorest.co.in/public/v2")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")