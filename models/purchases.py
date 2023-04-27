from datetime import datetime

from db import db
from models.enums import PurchaseStatus


class Purchase(db.Model):
    __tablename__ = "purchases"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')
    concert_id = db.Column(db.Integer, db.ForeignKey('concerts.id'), nullable=False)
    concert = db.relationship('Concert')
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    status = db.Column(db.Enum(PurchaseStatus), default=PurchaseStatus.pending, nullable=False)
