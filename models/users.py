from db import db
from models.enums import RoleType


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String, nullable=False)
    favourite_genres = db.Column(db.String(255))
    city = db.Column(db.String(20), nullable=False)
    role = db.Column(
        db.Enum(RoleType),
        default = RoleType.simple_user,
        nullable=False,
    )
    purchased_tickets = db.Column(db.Integer)
