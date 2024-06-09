import logging

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from database.repo.requests import RequestRepo
from database.setup import create_db_engine, create_session_pool, create_tables
from tgbot.config import load_config
from utils.redis_main import create_redis_connect

from tgbot.handlers.user_handlers import router as user_handler_router
from tgbot.handlers.other_handlers import router as other_handler_router
from tgbot.callback_query_handlers.user_callback import router as user_callback_router
from tgbot.middlewares.database import DatabaseMiddleware


config = load_config()


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        url=f"{config.webhook_setting.base_url}{config.webhook_setting.path}",
        secret_token=config.webhook_setting.secret
    )


def main():

    redis_conn = create_redis_connect()

    bot = Bot(
        token=config.tg_connect.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=RedisStorage(redis=redis_conn))

    engine = create_db_engine()
    session_pool = create_session_pool(engine=engine)

    create_tables(engine)

    dp.startup.register(on_startup)

    dp.include_routers(
        user_handler_router,
        other_handler_router,
        user_callback_router
    )

    dp.update.outer_middleware(DatabaseMiddleware(ssession_pool))  # реєструємо мідлвар
    
    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=config.webhook_setting.secret,
        repo=repo
    )
    webhook_requests_handler.register(app, path=config.webhook_setting.path)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=config.webhook_setting.host, port=config.webhook_setting.port)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот був зупинений")
