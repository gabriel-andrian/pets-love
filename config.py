from environs import Env
from secrets import token_hex

env = Env()
env.read_env()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = token_hex(32)
    SECRET_KEY = token_hex(32)
    JWT_ACCESS_TOKEN_EXPIRES = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    DATABASE_URL = env.str('DATABASE_URL')
    BREEDS_CSV = env.str('BREEDS_CSV')
