import os
from dotenv import load_dotenv

load_dotenv()
print("Loading environment variables from .env file...")
print(os.environ.get("password"))
print(os.environ.get("login"))