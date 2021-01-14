from flask import Flask
from app.views.home import bp_home
from app.views.breed_view import bp_breed

from app.models.breed_model import db, mg, ma

from environs import Env


def create_app():

    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_breed)


    return app