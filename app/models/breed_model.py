from app.models import db, ma


class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class BreedSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Breed

    id = ma.auto_field()
    name = ma.auto_field()
