from flask import Blueprint, render_template, request
from fed.form_schedule import CompositeForm
from fed import data_formatter

fed = Blueprint('fed', __name__)

# TODO Перенести получение меню в отдельный модуль

menu = [{'title': 'Главная', 'url': 'index'},
        {'title': 'Создать json для контета дня', 'url': 'fed.index'}]


@fed.route('/', methods=["POST", "GET"])
def index():
    form = CompositeForm()

    for f in form:
        if f.name[:8] == 'schedule':
            f.channel_id.choices = data_formatter.get_channel_list()
            f.content.choices = data_formatter.get_genres_list()

    if request.method == 'POST':
        is_valid = True
        for f in form:
            if not f.validate(f) and f.name not in ['submit', 'csrf_token']:
                is_valid = False
        if is_valid:
            return "ПРИВЕТ"

    if request.method == 'GET':
        form.schedule1.form.visible.process_data(True)
    return render_template('fed/fed_index.html', menu=menu, form=form)
