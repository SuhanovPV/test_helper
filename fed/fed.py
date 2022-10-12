from flask import Blueprint, render_template, request, session, redirect, url_for

import fed.form_data_processor
import utils
from fed.form import CompositeForm
from fed import db_data_processor, form_data_processor

fed = Blueprint('fed', __name__)


@fed.route('/', methods=["POST", "GET"])
def index():
    form = CompositeForm()
    channel_list = db_data_processor.get_channel_list()
    genres_list = db_data_processor.get_genres_list()
    language_list = db_data_processor.get_language_list()

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
            form_data_processor.get_data_from_forms([f for f in form if f.name not in ['submit', 'csrf_token']])
            return redirect(url_for('index'))

    if request.method == 'GET':
        form.schedule1.form.visible.process_data(True)

    return render_template('fed/fed_index.html', menu=session.menu, form=form)
