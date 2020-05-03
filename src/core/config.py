import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = 'production'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = 'development'

    MONGODB_SETTINGS = {
        'host': 'mongodb://root:example@rating-service-db:27017/rating?authSource=admin'
    }


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = 'testing'

    MONGODB_SETTINGS = {
        'host': 'mongodb://root:example@rating-service-db:27017/rating-test?authSource=admin'
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
