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
