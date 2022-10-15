import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

class DevelopmentConfig(Config):
    DEBUG = True

class StagingConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False

class TestConfig(Config):
    TESTING = True
