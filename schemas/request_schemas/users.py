from marshmallow import Schema, fields


class UserSignUpRequestSchema(Schema):
    email = fields.Email(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True)
    favourite_genres = fields.String()
    city = fields.String(required=True)
    card_number = fields.Integer()

class UserSignInRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)