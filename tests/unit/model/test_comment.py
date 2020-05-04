from unittest import TestCase
from src.comment.model.comment import Comment


class CommentTest(TestCase):
    def test_create_comment(self):
        expected_user_id = '854c9a9b-4a4a-410f-867c-9985c17878d8'
        expected_article_id = 1
        expected_comment = 'This is a comment.'

        comment = Comment(user_id=expected_user_id,
                          article_id=expected_article_id,
                          comment=expected_comment)

        self.assertEqual(str(comment.user_id), expected_user_id)
        self.assertEqual(comment.article_id, expected_article_id)
        self.assertEqual(comment.comment, expected_comment)
