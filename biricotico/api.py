from webob import Request, Response


class API:
    def __init__(self):
        self.taps = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()

        for path, handler in self.taps.items():
            if path == request.path:
                handler(request, response)
                return response

    def tap(self, path):
        def wrapper(handler):
            self.taps[path] = handler
            return handler

        return wrapper
