import pytest


def test_basic_route_adding(api):
    @api.tap("/home")
    def home(req, resp):
        resp.text = "TEST"

        with pytest.raises(AssertionError):
            @api.tap("/home")
            def home2(req, resp):
                resp.text = "TEST"


def test_biricotico_test_client_can_send_requests(api, client):
    expected_response = 'THIS IS COOL'

    @api.tap('/hey')
    def cool(req, resp):
        resp.text = expected_response

    assert client.get('http://testserver/hey').text == expected_response


def test_parameterized_routes(api, client):
    @api.tap("/{name}")
    def hello(req, resp, name):
        resp.text = f"hello, {name}"


    assert client.get("http://testserver/rhenan").text == "hello, rhenan"


def test_get_default_404_response(api, client):
    resp = client.get("http://testserver/doesnotexists")

    assert resp.status_code == 404
    assert resp.text == "Not found."


def test_class_based_view(api, client):
    @api.tap("/home")
    class HomeView:
        def get(self, req, resp):
            resp.text = "Home"

    assert client.get("http://testserver/home").text == "Home"


def test_post_method(api, client):
    @api.tap("/book")
    class BookView:
        def post(self, req, resp):
            resp.text = "Book Added"

    assert client.post("http://testserver/book").text == "Book Added"


def test_method_not_allowed(api, client):
    @api.tap("/book")
    class BookView:
        def post(self, req, resp):
            resp.text = "Book Added"

    with pytest.raises(AttributeError):
        client.get("http://testserver/book")


def test_alternative_rout(api, client):
    expected_response = "Another way to add route"

    def home(req, resp):
        resp.text = expected_response

    api.add_tap("/home", home)

    assert client.get("http://testserver/home").text == expected_response

