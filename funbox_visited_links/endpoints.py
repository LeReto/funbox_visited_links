from datetime import datetime
from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import Query, Depends, APIRouter

from .containers import Container
from .services import Service
from .models import LinksValidator

router = APIRouter()


@router.post("/visited_links")
@inject
def visited_links(
        json_data: LinksValidator,
        service: Service = Depends(Provide[Container.redis_service])
):
    unix_timestamp = int(datetime.timestamp(datetime.now()))
    domains = json_data.extract_domains()
    service.set(domains, unix_timestamp)

    return {"status": "ok"}


@router.get("/visited_domains")
@inject
def visited_domains(
        _from: Annotated[int, Query(alias="from")],
        to: int,
        service: Service = Depends(Provide[Container.redis_service])
):
    domains = service.get(_from, to)

    return {
        "domains": domains,
        "status": "ok"
    }
