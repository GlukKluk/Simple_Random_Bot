import os
import asyncio

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from handlers.user_handlers import user_handler_router
from handlers.other_handlers import other_handler_router
from callback_query_handlers.user_callback import user_callback_router


async def main():

    dotenv.load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        user_handler_router,
        other_handler_router,
        user_callback_router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
