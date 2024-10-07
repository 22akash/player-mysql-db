from marshmallow import Schema,fields

class PlayerSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    sport = fields.Str(required=True)
    country = fields.Str(required=True)
    gender = fields.Str(required=True)
