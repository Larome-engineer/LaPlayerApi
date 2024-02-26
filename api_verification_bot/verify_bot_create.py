from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

verify_bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()
