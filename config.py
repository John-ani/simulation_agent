import os

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    raise ValueError("API key not set in environment variables.")