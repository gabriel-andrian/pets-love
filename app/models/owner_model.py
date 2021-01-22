from app.models import db, ma, dog_model
from marshmallow import fields


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=True)
    document = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    address = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    dogs = db.relationship("Dog", backref="owner",
                           cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"<Owner {self.name} {self.surname} />"


class OwnerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Owner

    id = ma.auto_field()
    name = ma.auto_field()
    surname = ma.auto_field()
    document = ma.auto_field()
    email = ma.auto_field()
    address = ma.auto_field()

    dogs = fields.Nested(dog_model.DogSchema, many=True)
