from flask import Blueprint, render_template, request, session
from fed.form_schedule import CompositeForm
from fed import data_formatter

fed = Blueprint('fed', __name__)


@fed.route('/', methods=["POST", "GET"])
def index():
    form = CompositeForm()
    channel_list = data_formatter.get_channel_list()
    genres_list = data_formatter.get_genres_list()
    language_list = data_formatter.get_language_list()

    for f in form:
        if f.name[:8] == 'schedule':
            f.channel_id.choices = channel_list
            f.content.choices = genres_list
            f.language.choices = language_list

    if request.method == 'POST':
        is_valid = True
        for f in form:
            if not f.validate(f) and f.name not in ['submit', 'csrf_token']:
                is_valid = False

        if is_valid:
            return "ПРИВЕТ"

    if request.method == 'GET':
        form.schedule1.form.visible.process_data(True)

    return render_template('fed/fed_index.html', menu=session.menu, form=form)
