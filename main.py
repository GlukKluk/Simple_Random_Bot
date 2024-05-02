import logging

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from config import load_config
from utils.redis_main import create_redis_connect

from handlers.user_handlers import user_handler_router
from handlers.other_handlers import other_handler_router
from callback_query_handlers.user_callback import user_callback_router


config = load_config()


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        url=f"{config.webhook_setting.base_url}{config.webhook_setting.path}",
        secret_token=config.webhook_setting.secret
    )


def main():

    # redis_conn = create_redis_connect()

    bot = Bot(
        token=config.tg_connect.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    # dp = Dispatcher(storage=RedisStorage(redis=redis_conn))
    dp = Dispatcher(storage=MemoryStorage())

    dp.startup.register(on_startup)

    dp.include_routers(
        user_handler_router,
        other_handler_router,
        user_callback_router
    )

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=config.webhook_setting.secret,
    )
    webhook_requests_handler.register(app, path=config.webhook_setting.path)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=config.webhook_setting.host, port=config.webhook_setting.port)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот був зупинений")
