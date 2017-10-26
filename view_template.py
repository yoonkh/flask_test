from flask import render_template, Flask

app = Flask(__name__)


@app.route('/test/')
@app.route('/test/<name>')
def test(name=None):
    return render_template('test.html', name=name)


if __name__ == '__main__':
    app.run()