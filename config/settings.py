# File: config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "gemini-3.8-flash"

ALLOWED_IMAGE_TYPES = ["png", "jpg", "jpeg"]
RESPONSE_OPTIONS = ["Hints", "Solution with code"]

PAGE_TITLE = "AI Code Debugger"
PAGE_ICON = "🐞"
