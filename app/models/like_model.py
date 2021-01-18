from app.models import db, ma


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_id_give = db.Column(
        db.Integer, db.ForeignKey("dog.id"), nullable=False)
    dog_id_receive = db.Column(
        db.Integer, db.ForeignKey("dog.id"), nullable=False)
    dislike = db.Column(db.Boolean, nullable=False)
    match = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Like from {self.dog_id_give} to {self.dog_id_receive} >"


class LikeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Like

    dog_id_give = ma.auto_field()
    dog_id_receive = ma.auto_field()
    match = ma.auto_field()
