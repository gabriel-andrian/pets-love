from __future__ import annotations
from app.models import db, ma, col
# from app.models.conversation_model import ConversationSchema, dog_conversation
from marshmallow import fields
from datetime import datetime

dog_conversation = db.Table(
    'dog_conversation',
    col('dog_id', db.Integer, db.ForeignKey(
        'dog.id'), primary_key=True),
    col('conversation_id', db.Integer, db.ForeignKey(
        'conversation.id'), primary_key=True)
)


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


class Conversation(db.Model):
    __tablename__ = 'conversation'
    id = col(db.Integer, primary_key=True)
    time_started = col(db.Time, default=datetime.utcnow)
    messages = db.relationship('Message', back_populates='conversations')
    dogs = db.relationship('Dog', secondary=dog_conversation,
                           back_populates='conversations')


class Message(db.Model):
    __tablename__ = 'message'
    id = col(db.Integer, primary_key=True)
    message = col(db.Text, nullable=False)
    ts = col(db.DateTime, default=datetime.utcnow)
    dog_id = col(db.Integer, db.ForeignKey('dog.id'), nullable=False)
    dog_to = col(db.Integer, db.ForeignKey('dog.id'), nullable=False)
    conversation_id = col(db.Integer, db.ForeignKey(
        'conversation.id'), nullable=False)

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
