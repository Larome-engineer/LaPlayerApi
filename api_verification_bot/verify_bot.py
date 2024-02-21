from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.state import StatesGroup, State

TOKEN = ""
BASE_URL = ""

verify_bot = Bot(TOKEN)
dp = Dispatcher()

verify = Router()


class User(StatesGroup):
    username = State()
    email = State()
    pwd = State()


@verify.message(CommandStart())
def start_verify():
    pass
