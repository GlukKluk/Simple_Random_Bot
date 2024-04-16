import os
import dotenv

import asyncio

from aiogram import Bot, Dispatcher

from handlers.user_handlers import user_handler_router
from handlers.other_handlers import other_handler_router


async def main():

    dotenv.load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")

    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_router(user_handler_router)
    dp.include_router(other_handler_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
