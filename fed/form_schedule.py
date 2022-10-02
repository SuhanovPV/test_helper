from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime, timedelta


class Schedule(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired(message="Поле не может быть пустым")])
    start_time = DateTimeField("Начало", default=datetime.now() + timedelta(minutes=10),
                               validators=[DataRequired(message="Поле не может быть пустым")])
    end_time = DateTimeField("Начало", default=datetime.now() + timedelta(minutes=5),
                             validators=[DataRequired(message="Поле не может быть пустым")])
    channel_id = IntegerField("Канал", validators=[DataRequired(message="Поле не может быть пустым")])
    content = IntegerField("Категория")
    parental_rating = IntegerField("Возрастное ограничение", default=None,
                                   validators=[NumberRange(min=0, max=18, message="Значения могут быть от 0 до 18")])
    episode_number = StringField("Номер эпизода: ")
    production_date = StringField("Дата выпуска программы")
    star_rating = StringField("Рейтинг события")
    language = SelectField("Язык", choices=[('ru', 'Russian '), ('en', 'English'), ('zu', 'Zulu')])
    actors = StringField("Актеры программы")
    directors = StringField("Режиссеры программы")
    presenters = StringField("Имена ведущих программы")
    producers = StringField("Продюсеры программы")
    production_country = StringField("Страна производства программы")
    writers = StringField("Сценаристы программы")
    short_description = TextAreaField("Краткое описание события")
    full_description = TextAreaField("Полное описание события")
