from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, SelectField, TextAreaField, FormField, SubmitField, \
    BooleanField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from wtforms.widgets import DateTimeLocalInput
from datetime import datetime, timedelta

def required_if_visible(form, field):
    if form.visible.data and not field.data:
        raise ValidationError("Поле не может быть пустым")


class Schedule(FlaskForm):
    visible = BooleanField("Visible")
    title = StringField("Заголовок", validators=[required_if_visible])
    start_time = DateTimeField("Начало", default=datetime.now() + timedelta(minutes=5),
                               validators=[required_if_visible], widget=DateTimeLocalInput())
    end_time = DateTimeField("Конец", default=datetime.now() + timedelta(minutes=10),
                             validators=[required_if_visible], widget=DateTimeLocalInput())
    channel_id = SelectField("Канал", choices=[])
    # content = IntegerField("Категория")
    # parental_rating = IntegerField("Возрастное ограничение", default=None,
    #                                validators=[NumberRange(min=0, max=18, message="Значения могут быть от 0 до 18")])
    # episode_number = StringField("Номер эпизода: ")
    # production_date = StringField("Дата выпуска программы")
    # star_rating = StringField("Рейтинг события")
    # language = SelectField("Язык", choices=[('ru', 'Russian '), ('en', 'English'), ('zu', 'Zulu')])
    # actors = StringField("Актеры программы")
    # directors = StringField("Режиссеры программы")
    # presenters = StringField("Имена ведущих программы")
    # producers = StringField("Продюсеры программы")
    # production_country = StringField("Страна производства программы")
    # writers = StringField("Сценаристы программы")
    # short_description = TextAreaField("Краткое описание события")
    # full_description = TextAreaField("Полное описание события")

    # def __init__(self, formdata, **kwargs):
    #     super().__init__(formdata=formdata, **kwargs)
    #     self.channels = route.get_channels()


class Version(FlaskForm):
    build = IntegerField("Version", validators=[NumberRange(min=0)])
    subversion = IntegerField("Subversion", validators=[NumberRange(min=0)])
    version = IntegerField("Build", validators=[NumberRange(min=0)])


class CompositeForm(FlaskForm):
    schedule1 = FormField(Schedule)
    schedule2 = FormField(Schedule)
    version = FormField(Version)
    submit = SubmitField("Создать")
