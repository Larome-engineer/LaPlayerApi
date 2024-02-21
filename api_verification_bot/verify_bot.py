import asyncio, logging, sys
from verify_handler import verify
from verify_bot_create import dp, verify_bot


async def main():
    dp.include_router(
        verify
    )
    await dp.start_polling(verify_bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
