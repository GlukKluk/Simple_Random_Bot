from redis.asyncio import Redis

from config import load_config


config = load_config()


def create_redis_connect():
    redis_object = Redis(
        host=config.redis_connect.local_ip,
        port=config.redis_connect.local_port,
        db=2,
        decode_responses=True
    )

    return redis_object

