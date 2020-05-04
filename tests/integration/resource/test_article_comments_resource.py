import json

from tests.integration.integration_base_test import IntegrationBaseTest
from unittest.mock import patch
from src.comment.model.comment import Comment
from mongoengine import DoesNotExist


class RatingTest(IntegrationBaseTest):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer {}'.format(self.token)}

        super().setUp()

    def test_get_article_comments(self):
        with patch('src.middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            expected_article_comments = 1

            Comment(user_id=self.token_subject, article_id=1,
                    comment='This is a comment.').save()
            Comment(user_id=self.token_subject, article_id=1,
                    comment='This is a comment.').save()
            Comment(user_id=self.token_subject, article_id=2,
                    comment='This is a comment.').save()

            request = self.app.get(
                '/comments/article/{}'.format(expected_article_comments),
                headers=self.headers)

            self.assertEqual(2, len(request.json))
            self.assertEqual(200, request.status_code)
