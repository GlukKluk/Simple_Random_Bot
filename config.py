import os
from dataclasses import dataclass

import dotenv


@dataclass
class TgBot:
    bot_token: str


@dataclass
class RedisConnect:
    local_ip: str
    local_port: int


@dataclass
class WebhookSettings:
    base_url: str
    path: str
    host: str
    port: int
    secret: str


@dataclass
class Config:
    tg_connect: TgBot
    redis_connect: RedisConnect
    webhook_setting: WebhookSettings


def load_config():
    dotenv.load_dotenv()

    return Config(
        tg_connect=TgBot(
            bot_token=os.getenv("BOT_TOKEN")
        ),

        redis_connect=RedisConnect(
            local_ip=os.getenv("REDIS_LOCAL_IP"),
            local_port=int(os.getenv("REDIS_LOCAL_PORT"))
        ),

        webhook_setting=WebhookSettings(
            base_url=os.getenv("WEBHOOK_BASE_URL"),
            path=os.getenv("WEBHOOK_PATH"),
            host=os.getenv("WEBHOOK_HOST"),
            port=int(os.getenv("WEBHOOK_PORT")),
            secret=os.getenv("WEBHOOK_SECRET")
        )
    )
