from app.models import db, ma


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_id_give = db.Column(
        db.Integer, nullable=False)
    dog_id_receive = db.Column(
        db.Integer, nullable=False)
    dislike = db.Column(db.Boolean, nullable=False)
    match = db.Column(db.Boolean, default=False)


class LikeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Like

    id = ma.auto_field()
    dog_id_give = ma.auto_field()
    dog_id_receive = ma.auto_field()
    dislike = ma.auto_field()
    match = ma.auto_field()
