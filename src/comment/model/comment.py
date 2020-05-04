from datetime import datetime
from src.core.database import database


class Comment(database.Document):
    user_id = database.UUIDField(binary=False, required=True)
    article_id = database.IntField(required=True)
    comment = database.StringField()
    created_at = database.DateTimeField(
        required=True, default=datetime.now())
    updated_at = database.DateTimeField(
        required=True, default=datetime.now())
