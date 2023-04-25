from datetime import datetime

from db import db


class Concert(db.Model):
    __tablename__ = "concerts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    hosted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    host = db.relationship('User')
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

