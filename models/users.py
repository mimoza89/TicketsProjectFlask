from db import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(25), nullable=False, unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String, nullable=False)
    favourite_genres = db.Column(db.String(255))
    city = db.Column(db.String(20), nullable=False)
    card_number = db.Column(db.Integer)