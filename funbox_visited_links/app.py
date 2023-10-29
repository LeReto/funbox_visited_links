from fastapi import FastAPI

from funbox_visited_links import endpoints
from funbox_visited_links.containers import Container
from funbox_visited_links.exception_handlers import exception_handler


def create_app() -> FastAPI:
    container = Container()
    container.config.redis_host.from_env("REDIS_HOST")
    container.config.redis_port.from_env("REDIS_PORT")
    container.config.redis_collection.from_env("REDIS_COLLECTION")
    container.wire([endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    app.add_exception_handler(Exception, exception_handler)
    return app


apps = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(apps, host="0.0.0.0", port=8000)
