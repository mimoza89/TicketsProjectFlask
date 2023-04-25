from marshmallow import Schema, fields


class ConcertCreateRequestSchema(Schema):
    title = fields.String(required=True)
    city = fields.String(required=True)
    artist = fields.String(required=True)
    price = fields.Float(required=True)

