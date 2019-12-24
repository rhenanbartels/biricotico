import pytest

from biricotico.api import API


@pytest.fixture
def api():
    return API()


def test_basic_route_adding(api):
    @api.tap("/home")
    def home(req, resp):
        resp.text = "TEST"
