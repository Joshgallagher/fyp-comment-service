from flask import Flask


def create_app(config_object=None):
    app = Flask(__name__)

    return app
