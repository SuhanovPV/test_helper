from models import route


def get_channel_list():
    return [(x.id, x.title) for x in route.get_channels()]


def get_genres_list():
    return [(x.id, x.title) for x in route.get_genres()]
