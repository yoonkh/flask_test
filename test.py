from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


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
#
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
# @app.route('/user')
# def user():
#     return render_template('user.html')
#
#
# @app.route('/test/<username>')
# def variable(username):
#     return render_template('test.html', username=username)

# @app.route('/user/comment/')
# def comments():
#     return 'comment_set'
#
# @app.route('/')
# def index():
#     return render_template('index.html', current_time=datetime.utcnow())

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
