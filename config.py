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
    DATABASE_URL = 'postgresql://postgres:12345678@localhost/capstone_q3'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345678@localhost/capstone_q3'


class ProductionConfig(Config):
    ENV = 'production'
    DATABASE_URL = env.str('DATABASE_URL')
    BREEDS_CSV = env.str('BREEDS_CSV')
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')
