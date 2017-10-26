from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def test():
#     return 'tesing'

@app.route('/')
def index():
    return 'Index Page'


@app.route('/test')
def test():
    return 'Testing'


if __name__ == '__main__':
    app.run()
