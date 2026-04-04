import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "34446649"))
    API_HASH = os.getenv("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8337679965:AAFyI31rSKDe7dzNAlvD-lDQsdwfO_TlqPs")
    
    # Database
    MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    
    # Admin
    ADMIN_STR = os.getenv("ADMINS", "7892805795")
    ADMINS = [int(x) for x in ADMIN_STR.split()] if ADMIN_STR else []
    
    # Channel
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "-1003515041061") # username or ID
    
    # UI
    START_PIC = os.getenv("START_PIC", "https://ibb.co/XZZhqDs0") # Default image
    
    # Log Channel
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", "-1003515041061") # Channel ID (e.g. -100xxxx)

