import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = "/api/v1"
BOT_TOKEN = os.getenv('TOKEN')
