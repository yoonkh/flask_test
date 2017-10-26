from os import environ

from flask import Flask, request

app = Flask(__name__)

with app.request_context(environ):
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run()
