from fastapi.testclient import TestClient

from funbox_visited_links.app import apps

client = TestClient(apps)


def test_visited_links(service_mock):
    with apps.container.redis_service.override(service_mock):
        response = client.post(
            "/visited_links",
            json={"links": ["https://ya.ru"]}
        )

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_visited_links_empty_body(service_mock):
    with apps.container.redis_service.override(service_mock):
        response = client.post(
            "/visited_links",
            json={"links": []}
        )

    assert response.status_code == 422
