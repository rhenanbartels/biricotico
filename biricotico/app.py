"""
WSGI-compatible interface
"""
from biricotico.api import API


app = API()


@app.tap('/home')
def home(request, response):
    response.text = 'Hello from the HOME page'


@app.tap('/about')
def about(request, response):
    response.text = 'Hello from the ABOUT page'


@app.tap('/greetings/{name}')
def greetings(request, response, name):
    response.text = f'Hello, {name}'


@app.tap('/sum/{int1:d}/{int2:d}')
def sum(request, response, int1, int2):
    response.text = str(int1 + int2)


@app.tap('/')
class LandingPage:
    def get(self, request, response):
        response.text = 'GET method using CBV'

    def post(self, requst, response):
        response.text = 'POST method using CBV'
