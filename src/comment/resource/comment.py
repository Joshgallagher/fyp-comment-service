from flask import g, request
from flask_restful import Resource
from src.comment.model.comment import Comment
from src.middleware.get_subject import get_subject
# from src.middleware.authorise import authorise
from src.comment.schema.comment_schema import CommentSchema
from marshmallow import ValidationError


class CommentResource(Resource):
    # method_decorators = [authorise, get_subject]
    method_decorators = [get_subject]

    def post(self):
        user_id = g.current_user_id

        try:
            req_body = request.get_json()
        except Exception:
            req_body = None

        try:
            CommentSchema().load(
                {'articleId': req_body['articleId'],
                 'comment': req_body['comment']})
        except ValidationError as e:
            return e.messages, 422

        comment = Comment(user_id=user_id,
                          article_id=req_body['articleId'],
                          comment=req_body['comment']).save()
        id = str(comment.id)

        return {'id': id}, 201

    def put(self):
        return {}, 200

    def delete(self):
        return {}, 204
