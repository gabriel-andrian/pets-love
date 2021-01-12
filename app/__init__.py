from flask import Flask
from app.views.home import bp_home
from environs import Env


def create_app():

    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")

    app.register_blueprint(bp_home)

    return app