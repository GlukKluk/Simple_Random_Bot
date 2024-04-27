import os
import asyncio

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from config import load_config
from utils.redis_main import create_redis_connect

from handlers.user_handlers import user_handler_router
from handlers.other_handlers import other_handler_router
from callback_query_handlers.user_callback import user_callback_router


async def main():

    config = load_config()
    tunnel, redis_conn = create_redis_connect()

    bot = Bot(token=config.tg_connect.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=RedisStorage(redis=redis_conn))

    dp.include_routers(
        user_handler_router,
        other_handler_router,
        user_callback_router
    )

    try:
        await dp.start_polling(bot)

    finally:
        tunnel.close()

if __name__ == "__main__":
    asyncio.run(main())
