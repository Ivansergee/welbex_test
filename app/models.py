from dataclasses import dataclass
from datetime import datetime
from app import db


@dataclass
class Record(db.Model):

    id: int
    date: datetime
    title: str
    amount: int
    distance: int

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date())
    title = db.Column(db.String(50))
    amount = db.Column(db.Integer())
    distance = db.Column(db.Integer())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
