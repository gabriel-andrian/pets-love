from __future__ import annotations
from app.models import db, ma
from app.models.conversation_model import ConversationSchema, dog_conversation
from marshmallow import fields


class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    details = db.Column(db.String(1024), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
    gender = db.Column(db.Boolean, nullable=False)

    # Relationship
    # photos = db.relationship("DogPhoto", back_populates="dog")

    conversations = db.relationship('Conversation', secondary=dog_conversation,
                                    back_populates='dogs')

    messages = db.relationship('Message', back_populates='dogs')

    def __repr__(self):
        return f"<Dog {self.name} />"


class DogSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Dog

    id = ma.auto_field()
    name = ma.auto_field()
    details = ma.auto_field()
    owner_id = ma.auto_field()
    breed_id = ma.auto_field()
    gender = ma.auto_field()
    conversations = fields.Nested(ConversationSchema, many=True)
    messages = fields.Nested(MessageSchema, many=True)
