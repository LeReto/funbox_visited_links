FROM python:3.11-buster

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY funbox_visited_links ./funbox_visited_links

RUN poetry install --without test

ENTRYPOINT ["poetry", "run", "python", "-m", "funbox_visited_links.app"]