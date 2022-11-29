import os
from dotenv import load_dotenv
from sys import exit

load_dotenv()

BOT_API_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_API_TOKEN:
    exit("Error: no token provided")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    exit("Error: no API key provided")
CURRENT_WEATHER_API_CALL = os.getenv("WEATHER_API_CALL_1") + os.getenv("WEATHER_API_KEY") \
                           + os.getenv("WEATHER_API_CALL_2")
if not CURRENT_WEATHER_API_CALL:
    exit("Error: no API call provided")
