from parse import parse
from webob import Request, Response


class API:
    def __init__(self):
        self.taps = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def find_handler(self, request):
        for path, handler in self.taps.items():
            parse_result = parse(path, request.path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request):
        response = Response()

        handler, kwargs = self.find_handler(request)

        if handler is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response

    def default_response(self, response):
        response.status = 404
        response.text = "Not found."


    def tap(self, path):
        def wrapper(handler):
            self.taps[path] = handler
            return handler

        return wrapper
