from marshmallow import Schema, fields

from managers.purchases import PurchaseManager


class PurchaseResponseSchema(Schema):
    user_id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
