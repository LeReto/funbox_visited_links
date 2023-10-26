from dependency_injector import containers, providers
from .services import Service

import redis


def redis_connection(host, port) -> redis.Redis:
    pool = redis.ConnectionPool(host=host, port=port)
    return redis.Redis(connection_pool=pool, decode_responses=True)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    redis_conn = providers.Resource(
        redis_connection,
        host=config.redis_host,
        port=config.redis_port
    )

    redis_service = providers.Factory(
        Service,
        redis=redis_conn,
        collection=config.redis_collection
    )
