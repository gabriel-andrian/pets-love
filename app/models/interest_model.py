from app.models import db, ma


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    dog_id = db.Column(db.Integer, db.ForeignKey(
        'dog.id'), nullable=False, unique=True)
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)
    gender_interest = db.Column(db.Boolean, nullable=False)


class InterestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Interest

    id = ma.auto_field()

    dog_id = ma.auto_field()
    breed_id = ma.auto_field()
    gender_interest = ma.auto_field()
