import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    JWT_LEEWAY = 600


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = 'production'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = 'development'

    JWT_ISSUER = 'http://127.0.0.1:4455/'
    JWT_AUDIENCE = 'vue'
    JWKS_URL = 'http://oathkeeper-api:4456'

    MONGODB_SETTINGS = {
        'host': 'mongodb://root:example@comment-service-db:27017/comment?authSource=admin'
    }


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = 'testing'

    JWT_ISSUER = 'http://127.0.0.1:4455/'
    JWT_AUDIENCE = 'vue'
    JWKS_URL = 'http://oathkeeper-api:4456'

    MONGODB_SETTINGS = {
        'host': 'mongodb://root:example@comment-service-db:27017/comment-test?authSource=admin'
    }


config = {
    'default': 'src.core.config.DevelopmentConfig',
    'production': 'src.core.config.ProductionConfig',
    'development': 'src.core.config.DevelopmentConfig',
    'testing': 'src.core.config.TestingConfig',
}


def init_config(app):
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config[config_name])
