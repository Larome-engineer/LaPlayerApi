import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BASE_URL = '/api/v1'

DB_URL = os.getenv('DB_URL')
yandex_client_id = os.getenv('YA_CL_ID')

mp3_root = os.getenv('MP3')
wav_root = os.getenv('WAV')
logo_path = os.getenv('LOGO')
