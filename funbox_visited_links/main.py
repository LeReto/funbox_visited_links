import re
import redis

from fastapi import FastAPI, Query
from pydantic import BaseModel, constr
from datetime import datetime
from typing import Annotated

import logging

logger = logging.getLogger(__name__)

app = FastAPI()


class JSONValidator(BaseModel):
    _regexp: str = r"(?:https?:\/\/)?([a-zA-Z0-9.-]+\.[a-z]+)"
    links: list[constr(pattern=_regexp)]

    def extract_domains(self):
        return {
            re.match(self._regexp, link).group(1)
            for link in self.links
        }


@app.post("/visited_links")
def visited_links(json_data: JSONValidator):
    redis_key = 'links'
    unix_timestamp = int(datetime.timestamp(datetime.now()))

    print(f"unix_timestamp {unix_timestamp}")

    domains = json_data.extract_domains()

    r = redis.Redis()
    r.zadd(redis_key, {
        domain: unix_timestamp
        for domain in domains
    })

    return {"status": "ok"}


@app.get("/visited_domains")
def visited_domains(_from: Annotated[int, Query(alias="from")], to: int):
    logger.info(f"request / endpoint!")
    redis_key = 'links'
    r = redis.Redis()

    domains = r.zrangebyscore(redis_key, _from, to)

    return {
        "domains": domains,
        "status": "ok"
    }