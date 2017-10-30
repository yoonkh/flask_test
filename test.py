import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Shell
from flask_moment import Moment
from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for, flash

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
