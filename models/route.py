from models.models import Channels


def get_channels():
    return Channels.query.all()
