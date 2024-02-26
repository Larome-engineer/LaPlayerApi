import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = '/api/v1'
TOKEN = os.getenv('EXP_TOKEN')
LP_API_TOKEN = os.getenv('LP_API_TOKEN')
