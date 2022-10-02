from flask import Blueprint, render_template
from fed.form_schedule import Schedule

fed = Blueprint('fed', __name__)

# TODO Перенести получение меню в отдельный модуль

menu = [{'title': 'Главная', 'url': 'index'},
        {'title': 'Создать json для контета дня', 'url': 'fed.index'}]


@fed.route('/')
def index():
    form = Schedule()
    return render_template('fed/fed_index.html', menu=menu, form=form)
