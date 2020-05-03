from flask import Flask
from flask_restful import Api
from src.core.database import init_connection
from src.core.routes import register_routes
from src.core.config import init_config


def create_app(config_object=None):
    app = Flask(__name__)
    api = Api(app)

    if config_object is not None:
        app.config.from_object(config_object)
    else:
        init_config(app)

    init_connection(app)
    register_routes(api)

    return app
