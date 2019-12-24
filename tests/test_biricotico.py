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

