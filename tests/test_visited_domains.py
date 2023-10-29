from fastapi.testclient import TestClient

from funbox_visited_links.app import apps

client = TestClient(apps)


def test_visited_domains(service_mock):
    service_mock.get.return_value = [
        "funbox.ru"
    ]

    with apps.container.redis_service.override(service_mock):
        response = client.get("/visited_domains?from=0&to=1")

    assert response.status_code == 200
    assert response.json() == {"domains": ["funbox.ru"], "status": "ok"}


def test_visited_domains_empty(service_mock):
    service_mock.get.return_value = []

    with apps.container.redis_service.override(service_mock):
        response = client.get("/visited_domains?from=0&to=1")

    assert response.status_code == 200
    assert response.json() == {"domains": [], "status": "ok"}


def test_visited_domain_with_incorrect_parameters():
    response = client.get("/visited_domains?from=-1&to=1")
    assert response.status_code == 422
