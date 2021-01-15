from app.models import db, ma
from marshmallow import fields

from app.models.dog_model import DogSchema
from app.models.breed_model import BreedSchema



class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    gender = db.Column(db.Boolean, db.ForeignKey('dog.gender'), nullable=False)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)

    def __repr__(self):
        return f"<Interest number {self.id} />"


class InterestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Interest
    
    id = ma.auto_field()

    gender = fields.Nested(DogSchema)
    dog_id = fields.Nested(DogSchema)
    breed_id = fields.Nested(BreedSchema)