from datetime import datetime
from random import choices
from string import ascii_letters
from . import db

SHORT_LEN = 6


def get_short():
    while True:
        short_url = "".join(choices(ascii_letters + ascii_letters, k=SHORT_LEN))
        if URLModel.query.filter(URLModel.short_url == short_url).first():
            continue

        return short_url


class URLModel(db.Model):
    url_id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255))
    short_url = db.Column(db.String(6), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
