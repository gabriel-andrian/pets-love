from __future__ import annotations
from app.models import db, ma, col
from marshmallow import fields
from datetime import datetime
from app.models.breed_model import BreedSchema
from app.models.photos_model import PhotoSchema
from app.models.interest_model import InterestSchema

dog_conversation = db.Table(
    'dog_conversation',
    col('dog_id', db.Integer, db.ForeignKey(
        'dog.id', ondelete="CASCADE")),
    col('conversation_id', db.Integer, db.ForeignKey(
        'conversation.id', ondelete="CASCADE"))
)


class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    details = db.Column(db.String(300), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(
        'owner.id', ondelete="CASCADE"))
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
    gender = db.Column(db.Boolean, nullable=False)

    breed = db.relationship("Breed", backref="dog",
                            cascade="all, delete")
    photos = db.relationship("Photo", backref="dog",
                             cascade="all, delete", passive_deletes=True)
    interest = db.relationship(
        "Interest", backref="dog", cascade="all, delete")

    conversations = db.relationship('Conversation',
                                    secondary=dog_conversation,
                                    back_populates='dogs',
                                    cascade="all, delete")

    messages = db.relationship(
        'Message', back_populates='dogs', cascade="all, delete",
        passive_deletes=True)

    def __repr__(self):
        return f"<Dog {self.name} />"


class Conversation(db.Model):
    __tablename__ = 'conversation'
    id = col(db.Integer, primary_key=True)
    time_started = col(db.DateTime, default=datetime.utcnow)
    messages = db.relationship('Message', back_populates='conversations')
    dogs = db.relationship('Dog', secondary=dog_conversation,
                           back_populates='conversations',
                           passive_deletes=True)


class Message(db.Model):
    __tablename__ = 'message'
    id = col(db.Integer, primary_key=True)
    message = col(db.Text, nullable=False)
    ts = col(db.DateTime, default=datetime.utcnow)
    dog_id = col(db.Integer, db.ForeignKey(
        'dog.id', ondelete="CASCADE"), nullable=False)
    conversation_id = col(db.Integer, db.ForeignKey(
        'conversation.id'))

    conversations = db.relationship('Conversation', back_populates='messages')
    dogs = db.relationship('Dog', back_populates='messages')


class MessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Message

    id = ma.auto_field()
    message = ma.auto_field()
    ts = ma.auto_field()
    dog_id = ma.auto_field()
    conversation_id = ma.auto_field()


class ConversationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Conversation

    id = ma.auto_field()
    time_started = ma.auto_field()
    messages = fields.Nested(MessageSchema, many=True)
    dogs = ma.auto_field()


class DogSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Dog

    id = ma.auto_field()
    name = ma.auto_field()
    details = ma.auto_field()
    owner_id = ma.auto_field()
    breed = fields.Nested(BreedSchema)
    gender = ma.auto_field()
    conversations = fields.Nested(ConversationSchema, many=True)
    photos = fields.Nested(PhotoSchema, many=True)
    interest = fields.Nested(InterestSchema, many=True)
