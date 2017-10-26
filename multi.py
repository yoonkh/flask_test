from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/shopping')
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template('shopping.html', food=food)


if __name__ == '__main__':
    app.run()
