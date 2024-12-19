from redis.asyncio import Redis

from tgbot.config import load_config


config = load_config()


def create_redis_connect():
    redis_object = Redis(
        host=config.redis_connect.local_ip,
        port=config.redis_connect.local_port,
        password=config.redis_connect.local_password,
        db=config.redis_connect.local_db,
        decode_responses=True
    )

    return redis_object

