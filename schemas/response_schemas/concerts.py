from marshmallow import Schema, fields


class ConcertResponseSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    city = fields.String(required=True)
    artist = fields.String(required=True)
    price = fields.Float(required=True)
    hosted_by = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
