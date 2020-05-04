from flask_restful import Resource


class ArticleCommentsResource(Resource):
    def get(self, id):
        return {}, 200
