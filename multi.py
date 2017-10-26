from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/multi')
@app.route('/multi/<user>')
def multi(user=None):  # None by default
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run()
