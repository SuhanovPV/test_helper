from models_db import db


class Channels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    epg_id = db.Column(db.Integer, nullable=False)
    s_id = db.Column(db.Integer, nullable=False)
    original_network_id = db.Column(db.Integer, nullable=False)
    transport_stream_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<channels: {self.id}>"


class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    code = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<genres: {self.id}>"
