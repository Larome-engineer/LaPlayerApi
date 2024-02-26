import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = "http://127.0.0.1:5000/api/v1"
BOT_TOKEN = os.getenv('TOKEN')
