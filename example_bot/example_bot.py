import asyncio
import logging
import sys
import requests

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, URLInputFile, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = ''
BASE_URL = ''
LP_API_TOKEN = ''

example_bot = Bot(TOKEN)
dp = Dispatcher()

download_router = Router()
explore_router = Router()


@explore_router.message(F.text)
async def explore(msg: Message):
    search_result = requests.get(f'{BASE_URL}/search?name={msg.text}&token={LP_API_TOKEN}')
    btn_list = []

    for name, link in search_result.json().items():
        btn_list.append(InlineKeyboardButton(text=name, callback_data=f"val_{link}"))
    opt_builder = InlineKeyboardBuilder().row(*btn_list, width=1)

    await example_bot.send_message(
        chat_id=msg.from_user.id,
        text="Выберите трек",
        reply_markup=opt_builder.as_markup()
    )


@download_router.callback_query(F.data.startswith("val"))
async def download(call: CallbackQuery):
    call_data = call.data.split("_")[1]
    await example_bot.send_audio(
        chat_id=call.from_user.id,
        audio=URLInputFile(f"{BASE_URL}/download?link={call_data}&token={LP_API_TOKEN}")
    )


async def main():
    dp.include_routers(
        download_router,
        explore_router
    )
    await dp.start_polling(example_bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
