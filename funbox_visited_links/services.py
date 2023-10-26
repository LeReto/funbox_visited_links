import redis as r


class Service:
    def __init__(self, redis: r.Redis, collection: str) -> None:
        self._redis = redis
        self._collection = collection

    def set(self, domains: set, unix_timestamp: int):
        self._redis.zadd(self._collection, {
            name: unix_timestamp
            for name in domains
        })

    def get(self, _from: int, to: int) -> str:
        return self._redis.zrangebyscore(
            self._collection,
            _from,
            to
        )
