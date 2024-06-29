import logging

from aiohttp import web

from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.update_type import UpdateType
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from database.setup import create_db_engine, create_session_pool, init_models
from tgbot.config import load_config
from tgbot.handlers.bot_commands import UserCommands
from utils.redis_main import create_redis_connect

from tgbot.handlers.admin_handlers import router as admin_handler_router
from tgbot.handlers.user_handlers import router as user_handler_router
from tgbot.handlers.other_handlers import router as other_handler_router
from tgbot.callback_query_handlers.admin_callback import router as admin_callback_router
from tgbot.callback_query_handlers.user_callback import router as user_callback_router
from tgbot.middlewares.db_middlewares import DatabaseMiddleware


config = load_config()


async def on_startup(bot: Bot, engine) -> None:
    await bot.set_webhook(
        url=f"{config.webhook_setting.base_url}{config.webhook_setting.path}",
        secret_token=config.webhook_setting.secret,
        allowed_updates=list(UpdateType)
    )
    await init_models(engine=engine)

    await bot.set_my_commands(commands=[UserCommands.start])


def main():

    # redis_conn = create_redis_connect()

    bot = Bot(
        token=config.tg_connect.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    # dp = Dispatcher(storage=RedisStorage(redis=redis_conn))
    dp = Dispatcher(storage=MemoryStorage())

    engine = create_db_engine(echo=True)
    session_pool = create_session_pool(engine=engine)

    dp.startup.register(on_startup)

    dp.include_routers(
        admin_handler_router,
        user_handler_router,
        other_handler_router,

        admin_callback_router,
        user_callback_router
    )

    dp.update.outer_middleware(DatabaseMiddleware(session_pool))  # реєструємо мідлвар
    
    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=config.webhook_setting.secret,
    )
    webhook_requests_handler.register(app, path=config.webhook_setting.path)

    setup_application(app, dp, bot=bot, engine=engine)

    web.run_app(app, host=config.webhook_setting.host, port=config.webhook_setting.port)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот був зупинений")
