from dataclasses import dataclass
from app import db


@dataclass
class Record(db.Model):

    id: int
    date: str
    title: str
    amount: int
    distance: int

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(10))
    title = db.Column(db.String(50))
    amount = db.Column(db.Integer())
    distance = db.Column(db.Integer())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
