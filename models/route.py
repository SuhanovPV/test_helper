from models.models import Channels, Genres, Menu, Language


def get_channels():
    return Channels.query.all()


def get_genres():
    return Genres.query.all()


def get_menu():
    return Menu.query.all()


def get_language():
    return Language.query.all()


def get_channel(channel_id):
    return Channels.query.get(channel_id)


def get_genre(genre_id):
    return Genres.query.get(genre_id)
