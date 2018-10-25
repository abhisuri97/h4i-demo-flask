from flask import current_app
from .. import db

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship("User", back_populates="reviews")
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))
    club = db.relationship("Club", back_populates="club_reviews")
    good = db.Column(db.Integer)
