from models.models import Channels, Genres


def get_channels():
    return Channels.query.all()


def get_genres():
    return Genres.query.all()
