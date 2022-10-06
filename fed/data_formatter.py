from models import models, route


def get_channel_list():
    return [(x.id, x.title) for x in route.get_channels()]