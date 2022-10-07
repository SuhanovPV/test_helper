from flask import Flask, render_template, session
from models.models import db
from fed.fed import fed
import utils
from models import route

# https://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue/9695045#9695045
DEBUG = True
SECRET_KEY = '73af89c9e2e8acc3977817dcc1b718e403754051a983f65ad0470048e66b'
SQLALCHEMY_DATABASE_URI = 'sqlite:///helper.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

menu = [{'title': 'Главная', 'url': 'index'},
        {'title': 'Создать json для контета дня', 'url': 'fed.index'}]

app = Flask(__name__)
app.config.from_object(__name__)

db.init_app(app=app)
app.register_blueprint(fed, url_prefix='/fed', template_folder='tepmlates', static_folder='static')


@app.before_request
def preset():
    session.menu = utils.get_menu(route.get_menu())


@app.route('/')
def index():
    return render_template('index.html', title="Главная", menu=session.menu)


if __name__ == "__main__":
    app.run()
