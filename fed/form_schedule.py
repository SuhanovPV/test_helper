from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FormField, SubmitField, \
    BooleanField, DateTimeLocalField
from wtforms.validators import NumberRange, ValidationError
from wtforms.widgets import DateTimeLocalInput
from datetime import datetime, timedelta


def required_if_visible(form, field):
    if form.visible.data and not field.data:
        raise ValidationError("Поле не может быть пустым")


def value_in_range_if_set(form, field, min_val, max_val):
    if form.visible.data and not field.data:
        if field.data > max_val or field.data < min_val:
            raise ValidationError(f"Значение должно быть в диапазоне от {min_val} до {max_val} включительно")


class Schedule(FlaskForm):
    visible = BooleanField("Visible")
    title = StringField("Заголовок", validators=[required_if_visible])
    start_time = DateTimeLocalField("Начало", default=datetime.now() + timedelta(minutes=5),
                                    validators=[required_if_visible], widget=DateTimeLocalInput())
    end_time = DateTimeLocalField("Конец", default=datetime.now() + timedelta(minutes=10),
                                  validators=[required_if_visible], widget=DateTimeLocalInput())
    channel_id = SelectField("Канал", choices=[])
    content = SelectField("Категория", choices=[])
    # parental_rating = IntegerField("Возрастное ограничение", default=0,
    #                                validators=[value_in_range_if_set(min_val=0, max_val=18)])
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
