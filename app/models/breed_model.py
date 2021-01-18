from app.models import db, ma


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
