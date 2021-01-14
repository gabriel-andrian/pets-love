from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<Breed {self.name} />"


class BreedSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Breed

    id = ma.auto_field()
    name = ma.auto_field()
