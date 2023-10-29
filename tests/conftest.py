from unittest import mock

import pytest

from funbox_visited_links.services import Service


@pytest.fixture(scope="module")
def service_mock():
    return mock.Mock(spec=Service)
