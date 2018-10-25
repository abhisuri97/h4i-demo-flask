from flask import current_app
from .. import db

class Club(db.Model):
    __tablename__ = 'clubs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    club_reviews = db.relationship('Review', back_populates='club')
