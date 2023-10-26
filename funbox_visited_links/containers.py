from dependency_injector import containers, providers
from .services import Service
from .database import redis_connection


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
