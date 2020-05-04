from tests.integration.integration_base_test import IntegrationBaseTest
from src.comment.model.comment import Comment


class CommentTest(IntegrationBaseTest):
    def test_create_comment(self):
        user_id = self.token_subject
        article_id = 1
        comment = 'This is a comment.'

        Comment(user_id=user_id, article_id=article_id, comment=comment).save()

        new_comment = Comment.objects.get(
            user_id=user_id, article_id=article_id, comment=comment)

        self.assertEqual(article_id, new_comment.article_id)
        self.assertEqual(comment, new_comment.comment)
        self.assertIsNotNone(new_comment)
