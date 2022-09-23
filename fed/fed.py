from flask import Blueprint

fed = Blueprint('fed', __name__, template_folder='templates', static_folder='static')


@fed.route('/')
def index():
    return "HELLO"
