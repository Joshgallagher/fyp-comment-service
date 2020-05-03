from flask_mongoengine import MongoEngine

database = MongoEngine()


def init_connection(app):
    database.init_app(app)
