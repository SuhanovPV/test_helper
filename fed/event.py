from fed import db_data_processor
import datetime


class Event:
    def __init__(self, **kwargs):
        self.id = 1
        self.allow_record = True
        self._channel = db_data_processor.get_channel(kwargs['channel_id'])
        self.channel = self._get_channel_id()
        self.transport_stream = self._get_transport_stream()
        self.start = self._get_time(kwargs['start_time'])
        self.end = self._get_time(kwargs['end_time'])
        self.descriptions = self._get_description(**kwargs)
        if kwargs['content']:
            self.content = self._get_genre(kwargs['content'])
        if kwargs['episode_number']:
            self.episode_number = kwargs['episode_number']
        if kwargs['parental_rating']:
            self.parental_rating = int(kwargs['parental_rating'])
        if kwargs['production_date']:
            self.production_date = kwargs['production_date']
        if kwargs['star_rating']:
            self.star_rating = kwargs['star_rating']


    def _get_transport_stream(self):
        ts = {'original_network_id': self._channel.original_network_id,
              'service_id': self._channel.s_id,
              'transport_stream_id': self._channel.transport_stream_id}
        return ts

    def _get_channel_id(self):
        return self._channel.epg_id

    def _get_genre(self, id):
        print(id)
        genre = db_data_processor.get_genre(id)
        return genre.code

    def _get_time(self, time):
        time -= datetime.timedelta(hours=3)
        return 'T'.join(str(time).split(' ')) + '+00:00'

    def _get_description(self, **kwargs):
        desc = dict()
        required = ['title', 'language']
        optional = ['actors', 'directors', 'full_description', 'presenters', 'producers', 'production_country',
                    'short_description', 'writers']
        for key in required:
            desc[key] = kwargs[key]
        for key in optional:
            if kwargs[key]:
                desc[key] = kwargs[key]
        return desc

    def get_event(self):
        event = dict()
        for key in self.__dict__:
            if key[0] != '_':
                event[key] = self.__dict__[key]
        return event
