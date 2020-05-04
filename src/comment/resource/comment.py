from datetime import datetime
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
            article_id = request.get_json()['articleId']
        except Exception:
            article_id = None

        if article_id is None:
            return {'message': 'Something went wrong.'}, 500

        try:
            comment = request.get_json()['comment']
        except Exception:
            comment = None

        try:
            CommentSchema().load({'comment': comment})
        except ValidationError as e:
            return e.messages, 422

        comment = Comment(
            user_id=user_id, article_id=article_id, comment=comment).save()
        id = str(comment.id)

        return {'id': id}, 201

    def put(self, id):
        try:
            comment = request.get_json()['comment']
        except Exception:
            comment = None

        try:
            CommentSchema().load({'comment': comment})
        except ValidationError as e:
            return e.messages, 422

        comment = Comment.objects.get(id=id).update(
            comment=comment, updated_at=datetime.now())

        return {}, 204

    def delete(self):
        return {}, 204
