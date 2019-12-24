import pytest

from biricotico.api import API


@pytest.fixture
def api():
    return API()


@pytest.fixture
def client(api):
    return api.test_session()
