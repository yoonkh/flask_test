from flask import Flask, request, render_template, app

app = Flask(__name__)

# need packeges : templates, static

@app.route('/layout/')
def profileWithTemplate():
    return render_template('layout_1.html')


if __name__ == '__main__':
    app.run()
