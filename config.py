import os
from dataclasses import dataclass

import dotenv


@dataclass
class TgBot:
    bot_token: str


@dataclass
class SSHConnect:
    server: str
    port: int
    username: str
    password: str
    pkey_path: str


@dataclass
class RedisConnect:
    local_ip: str
    local_port: int


@dataclass
class Config:
    tg_connect: TgBot
    ssh_connect: SSHConnect
    redis_connect: RedisConnect


def load_config():
    dotenv.load_dotenv()

    return Config(
        tg_connect=TgBot(
            bot_token=os.getenv("BOT_TOKEN")
        ),

        ssh_connect=SSHConnect(
            server=os.getenv("SSH_SERVER"),
            port=int(os.getenv("SSH_PORT")),
            username=os.getenv("SSH_USERNAME"),
            password=os.getenv("SSH_PASSWORD"),
            pkey_path=os.getenv("SSH_PKEY_PATH")
        ),

        redis_connect=RedisConnect(
            local_ip=os.getenv("REDIS_LOCAL_IP"),
            local_port=int(os.getenv("REDIS_LOCAL_PORT"))
        )
    )
