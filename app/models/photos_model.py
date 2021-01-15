from app.models import db, ma


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_account_id = db.Column(db.Integer,  db.foreignKey('dog.id'))
    link = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=True)
    time_added = db.Column(db.DateTime(), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Photo {self.id} />"


class PhotoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Photo

    id = ma.auto_field()
    dog_account_id = ma.auto_field()
    link = ma.auto_field()
    details = ma.auto_field()
    time_added = ma.auto_field()
    active = ma.auto_field()
