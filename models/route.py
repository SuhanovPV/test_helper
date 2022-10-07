from models.models import Channels, Genres, Menu, Language

def get_channels():
    return Channels.query.all()


def get_genres():
    return Genres.query.all()


def get_menu():
    return Menu.query.all()

def get_language():
    return Language.query.all()
