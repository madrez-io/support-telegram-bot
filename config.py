import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") if os.getenv("BOT_TOKEN") else None
ADMIN_ID = int(os.getenv("ADMIN_ID")) if os.getenv("ADMIN_ID") else None

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in .env file")

if not ADMIN_ID:
    raise ValueError("ADMIN_ID not found in .env file")
