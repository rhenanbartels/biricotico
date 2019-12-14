from wsgiref.simple_server import make_server

from webapp import application


if __name__ == "__main__":
    server = make_server('localhost', 8000, app=application)
    server.serve_forever()
