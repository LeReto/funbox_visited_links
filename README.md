**Зачем**: Решил попробовать FastAPI

Нашел вот [это](https://funbox.ru/q/python.pdf) тестовое задание


Реализуйте web-приложение для простого учета посещенных (неважно, как, кем и когда) ссылок

- [x] Приложение написано на языке Python версии > 3.7
- [x] Приложение предоставляет JSON API по HTTP
- [x] Приложение предоставляет два HTTP ресурса
- [x] Первый ресурс служит для передачи в сервис массива ссылок в POST-запросе. Временем их посещения считается время получения запроса сервисом.
- [x] Второй ресурс служит для получения GET-запросом списка уникальных доменов, посещенных за переданный интервал времени.
- [x] Поле status ответа служит для передачи любых возникающих при обработке запроса ошибок.
- [x] Для хранения данных сервис должен использовать REDIS.
- [x] Код должен быть покрыт тестами.
- [x] Инструкции по запуску должны находиться в README

**Ресурс загрузки посещений**:

POST /visited_links

```json
{
    "links": [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
}
```

Response:

```json
{
  "status": "ok"
}
```

GET visited_domains?from=1698153709&to=1698153709

Response:

```json
{
    "domains": [
        "ya.ru",
        "funbox.ru",
        "stackoverflow.com"
    ],
    "status": "ok"
}
```

**Инструкция по запуску:**

Запуск приложения в docker
```bash
docker-compose -f docker-compose.yaml up -d
```

Для локальной разработки:
1. Устанавливаем зависимости `poetry install`
2. Запуск тестов `pytest`
3. Запуск API, предварительно должен быть запущен Redis `REDIS_HOST=localhost REDIS_PORT=6379 REDIS_COLLECTION=links uvicorn funbox_visited_links.app:apps --reload`