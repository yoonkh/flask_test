from flask import Flask, request, app

app = Flask(__name__)


## HTTP method : import request

@app.route('/method')
def method():
    return 'Method used : %s' % request.method


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'

    else:
        return 'You are probably using GET'


if __name__ == '__main__':
    app.run()
