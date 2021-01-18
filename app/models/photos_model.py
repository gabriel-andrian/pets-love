from app.models import db, ma


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_account_id = db.Column(db.Integer,  db.ForeignKey('dog.id'))
    link = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Photo {self.id} />"


class PhotoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Photo

    id = ma.auto_field()
    dog_account_id = ma.auto_field()
    link = ma.auto_field()
