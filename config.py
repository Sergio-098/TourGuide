# app/config.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY is not set in the environment!")
