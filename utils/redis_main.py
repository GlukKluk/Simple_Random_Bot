from sshtunnel import SSHTunnelForwarder
from redis.asyncio import Redis

from config import load_config


config = load_config()


def create_ssh_tunnel():
    return SSHTunnelForwarder(
        (config.ssh_connect.server, config.ssh_connect.port),
        ssh_username=config.ssh_connect.username,
        # ssh_password=config.ssh_connect.password,
        ssh_pkey=config.ssh_connect.pkey_path,
        remote_bind_address=(config.redis_connect.local_ip, config.redis_connect.local_port)
    )


def create_redis_connect():
    tunnel = create_ssh_tunnel()
    tunnel.start()

    redis_object = Redis(
        host=config.redis_connect.local_ip,
        port=tunnel.local_bind_port,
        db=2,
        # decode_responses=True,
    )

    return tunnel, redis_object

