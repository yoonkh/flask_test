from flask import Flask, render_template

app = Flask(__name__)


# from flask.ext.script import Manager
# from flask import Flask
#
# app = Flask(__name__)
#
# manager = Manager(app)


# @app.route('/')
# def test():
#     return 'tesing'

# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# @app.route('/test')
# def test():
#     return 'Testing'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id

# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'

# @app.route('/')
# def index():
#     return '<h1>test</h1>'
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
