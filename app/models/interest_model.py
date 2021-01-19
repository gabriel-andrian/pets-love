from app.models import db, ma
from marshmallow import fields

from app.models.dog_model import DogSchema
from app.models.breed_model import BreedSchema


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'), nullable=False, unique=True)
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)
    gender_interest = db.Column(db.Boolean, nullable=False)

class InterestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Interest

    id = ma.auto_field()

    dog_id = ma.auto_field()
    breed_id = ma.auto_field()
    gender_interest = ma.auto_field()
    