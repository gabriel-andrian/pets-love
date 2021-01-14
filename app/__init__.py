from flask import Flask
from flask-jwt-extended import JWTManager
from secrets import token_hex
from app.views.home import bp_home
from environs import Env
from app.views.authorization_view import bp_authorization


def create_app():

    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")
    app.config['JWT_SECRET_KEY'] = token_hex(16)

    JWTManager(app)

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_authorization)

    return app