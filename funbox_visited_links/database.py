import redis


def redis_connection(host, port) -> redis.Redis:
    pool = redis.ConnectionPool(host=host, port=port)
    session = redis.Redis(connection_pool=pool, decode_responses=True)
    yield session
    session.close()
