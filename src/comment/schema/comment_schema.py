from marshmallow import Schema, fields, validate


class CommentSchema(Schema):
    article_id = fields.Integer(
        required=True, validate=validate.Range(min=1), data_key='articleId')
    comment = fields.String(required=True, validate=validate.Length(min=1))
