from unittest import TestCase
from marshmallow import ValidationError
from src.comment.schema.comment_schema import CommentSchema


class CommentSchemaTest(TestCase):
    def test_comment_schema_validation_pass(self):
        comment = 'This is a comment.'

        try:
            CommentSchema().load({'comment': comment})
        except ValidationError:
            self.fail('Comment Schema validation failed.')

    def test_comment_schema_validation_fail(self):
        comment_min_one = ''

        try:
            CommentSchema().load({'comment': comment_min_one})
        except ValidationError as e:
            self.assertEqual(e.valid_data, {})
            self.assertEqual(
                e.messages, {'comment': ['Shorter than minimum length 1.']})

        self.assertRaises(ValidationError)

        comment_none = None

        try:
            CommentSchema().load({'comment': comment_none})
        except ValidationError as e:
            self.assertEqual(e.valid_data, {})
            self.assertEqual(
                e.messages, {'comment': ['Field may not be null.']})

        self.assertRaises(ValidationError)
