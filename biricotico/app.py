"""
WSGI-compatible interface
"""
from biricotico.api import API


app = API()


@app.tap('/')
def landing_page(request, response):
    response.text = 'Welcome!'


@app.tap('/home')
def home(request, response):
    response.text = 'Hello from the HOME page'


@app.tap('/about')
def about(request, response):
    response.text = 'Hello from the ABOUT page'
