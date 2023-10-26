import redis


def redis_connection(host, port) -> redis.Redis:
    pool = redis.ConnectionPool(host=host, port=port)
    return redis.Redis(connection_pool=pool, decode_responses=True)