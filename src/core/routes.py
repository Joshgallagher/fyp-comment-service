from src.comment.resource.comment import CommentResource
from src.comment.resource.article_comments_resource import ArticleCommentsResource


def register_routes(api):
    api.add_resource(ArticleCommentsResource, '/comments/article/<int:id>')
    api.add_resource(CommentResource, '/comments', '/comments/<string:id>')
