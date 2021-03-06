from marshmallow import Schema, fields, validate


class CommentSchema(Schema):
    comment = fields.String(required=True, validate=validate.Length(min=1))
