from models import route


def get_channel_list():
    return [(x.id, x.title) for x in route.get_channels()]


def get_genres_list():
    return [(x.id, x.title) for x in route.get_genres()]


def get_language_list():
    return [(x.code, x.title) for x in route.get_language()]


def get_channel(channel_id):
    return route.get_channel(int(channel_id))


def get_genre(genre_id):
    return route.get_genre(str(genre_id))
