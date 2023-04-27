from marshmallow import Schema, fields

from models import PurchaseStatus


class PurchaseRequestSchema(Schema):
    concert_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    status = fields.Enum(PurchaseStatus)
