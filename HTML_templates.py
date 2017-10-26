from flask import Flask, request, render_template, app

app = Flask(__name__)

# need packeges : templates, static

@app.route('/profile/<name>')
def profileWithTemplate(name):
    return render_template('profile.html', name=name)


if __name__ == '__main__':
    app.run()
