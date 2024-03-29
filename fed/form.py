from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SelectField, TextAreaField, FormField, SubmitField, \
    BooleanField, DateTimeLocalField
from wtforms.validators import NumberRange, ValidationError
from wtforms.widgets import DateTimeLocalInput
from datetime import datetime, timedelta


def required_if_visible(form, field):
    if form.visible.data and not field.data:
        raise ValidationError("Поле не может быть пустым")


def value_in_range_if_set(min_val, max_val):
    message = f"Значение должно быть в диапазоне от {min_val} до {max_val} включительно"

    def _value_in_range_if_set(form, field):
        if form.visible.data and field.data is not None:
            if field.data > max_val or field.data < min_val:
                raise ValidationError(message)

    return _value_in_range_if_set


class Schedule(FlaskForm):
    # .replace(second=0, microsecond=0)
    visible = BooleanField("Visible")
    title = StringField("Заголовок*:", validators=[required_if_visible])
    start_time = DateTimeLocalField("Начало", format='%Y-%m-%dT%H:%M',
                                    default=datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=5),
                                    validators=[required_if_visible], widget=DateTimeLocalInput())
    end_time = DateTimeLocalField("Конец", format='%Y-%m-%dT%H:%M',
                                  default=datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=10),
                                  validators=[required_if_visible], widget=DateTimeLocalInput())
    channel_id = SelectField("Канал*:", choices=[])
    content = SelectField("Категория:", choices=[])
    parental_rating = IntegerField("ВО:", default=0,
                                   validators=[NumberRange(min=0, max=18)])
    language = SelectField("Язык:*", choices=[])
    episode_number = StringField("Номер эпизода: ")
    production_date = StringField("Год выпуска")
    star_rating = StringField("Рейтинг:")

    production_country = StringField("Страна:")
    actors = StringField("Актеры:")
    directors = StringField("Режиссеры:")
    presenters = StringField("Ведущие:")
    producers = StringField("Продюсеры:")
    writers = StringField("Сценаристы:")
    short_description = TextAreaField("Краткое описание:")
    full_description = TextAreaField("Полное описание:")


class Version(FlaskForm):
    build = IntegerField("Version", default=2, validators=[NumberRange(min=2, max=2)])
    subversion = IntegerField("Subversion", default=0, validators=[NumberRange(min=0)])
    version = IntegerField("Build", default=0, validators=[NumberRange(min=0)])


class CompositeForm(FlaskForm):
    schedule1 = FormField(Schedule)
    schedule2 = FormField(Schedule)
    schedule3 = FormField(Schedule)
    schedule4 = FormField(Schedule)
    schedule5 = FormField(Schedule)
    schedule6 = FormField(Schedule)
    schedule7 = FormField(Schedule)
    schedule8 = FormField(Schedule)
    schedule9 = FormField(Schedule)
    schedule10 = FormField(Schedule)
    version = FormField(Version)
    submit = SubmitField("Создать")
