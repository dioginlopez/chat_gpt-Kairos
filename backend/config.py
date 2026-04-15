import os
from dotenv import load_dotenv

load_dotenv()

# Configuration from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
CONTEXT_MEMORY_SIZE = int(os.getenv("CONTEXT_MEMORY_SIZE", "10"))

