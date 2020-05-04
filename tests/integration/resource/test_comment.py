import json

from tests.integration.integration_base_test import IntegrationBaseTest
from unittest.mock import patch
from src.comment.model.comment import Comment


class RatingTest(IntegrationBaseTest):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer {}'.format(self.token)}

        super().setUp()

    def test_create_rating(self):
        with patch('src.middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            comment = 'This is a comment.'

            payload = json.dumps(
                {'articleId': 1, 'comment': comment})
            request = self.app.post(
                '/comments', headers=self.headers, data=payload)

            new_comment = Comment.objects.get(comment=comment)

            self.assertEqual(comment, new_comment.comment)

            self.assertEqual(str(new_comment.id), request.json['id'])
            self.assertEqual(201, request.status_code)

    def test_create_rating_validation(self):
        with patch('src.middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            payload = json.dumps(
                {'articleId': None, 'comment': 'This is a comment.'})
            request = self.app.post(
                '/comments', headers=self.headers, data=payload)

            self.assertEqual('Something went wrong.', request.json['message'])
            self.assertEqual(500, request.status_code)

            payload = json.dumps(
                {'articleId': 1, 'comment': None})
            request = self.app.post(
                '/comments', headers=self.headers, data=payload)

            self.assertEqual('Field may not be null.',
                             request.json['comment'][0])
            self.assertEqual(422, request.status_code)

            payload = json.dumps(
                {'articleId': 1, 'comment': ''})
            request = self.app.post(
                '/comments', headers=self.headers, data=payload)

            self.assertEqual('Shorter than minimum length 1.',
                             request.json['comment'][0])
            self.assertEqual(422, request.status_code)
