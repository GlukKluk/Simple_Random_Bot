import logging

from aiohttp import web
import betterlogging as bl

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.update_type import UpdateType
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from database.setup import create_db_engine, create_session_pool, init_models
from tgbot.config import load_config
from tgbot.handlers.bot_commands import UserCommands
from utils.redis_main import create_redis_connect

from tgbot.dialogs import dialogs_list

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
        allowed_updates=list(UpdateType),
    )
    await init_models(engine=engine)

    await bot.set_my_commands(commands=[UserCommands.start])


def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")

    sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
    sqlalchemy_logger.setLevel(log_level)


def get_storage() -> RedisStorage | MemoryStorage:
    """
    Return storage based on the provided configuration.


    Returns:
        Storage: The storage object based on the configuration.

    """

    if config.tg_bot.use_redis:
        redis_conn = create_redis_connect()

        return RedisStorage(
            redis=redis_conn,
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True)
        )
    else:
        return MemoryStorage()


def main():
    setup_logging()
    storage = get_storage()

    bot = Bot(
        token=config.tg_bot.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=storage, admin_ids=config.tg_bot.admins_id)

    engine = create_db_engine()
    session_pool = create_session_pool(engine=engine)

    dp.startup.register(on_startup)

    dp.include_routers(
        user_handler_router,
        *dialogs_list,
        # admin_handler_router,
        # other_handler_router,
        #
        # admin_callback_router,
        # user_callback_router
    )

    setup_dialogs(dp)

    dp.update.outer_middleware(DatabaseMiddleware(session_pool))

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
