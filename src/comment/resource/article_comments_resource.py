from flask_restful import Resource
from src.comment.model.comment import Comment


class ArticleCommentsResource(Resource):
    def get(self, id):
        pipeline = [
            {
                '$project': {
                    '_id': 0,
                    'id': {
                        '$toString': '$_id'
                    },
                    'userId': '$user_id',
                    'comment': 1,
                    'createdAt': {
                        '$dateToString': {
                            'date': '$created_at',
                        }
                    }
                }
            }
        ]
        comments = Comment.objects(article_id=id).aggregate(pipeline)

        return list(comments), 200
