# from __future__ import annotations
# from datetime import datetime
# from app.models import db, ma, col
# from marshmallow import fields


# dog_conversation = db.Table(
#     'dog_conversation',
#     col('dog_id', db.Integer, db.ForeignKey(
#         'dog.id'), primary_key=True),
#     col('conversation_id', db.Integer, db.ForeignKey(
#         'conversation.id'), primary_key=True)
# )


# class Conversation(db.Model):
#     __tablename__ = 'conversation'
#     id = col(db.Integer, primary_key=True)
#     time_started = col(db.Time, default=datetime.utcnow)
#     messages = db.relationship('Message', back_populates='conversations')
#     dogs = db.relationship('Dog', secondary=dog_conversation,
#                            back_populates='conversations')


# class Message(db.Model):
#     __tablename__ = 'message'
#     id = col(db.Integer, primary_key=True)
#     message = col(db.Text, nullable=False)
#     ts = col(db.DateTime, default=datetime.utcnow)
#     dog_id = col(db.Integer, db.ForeignKey('dog.id'), nullable=False)
#     conversation_id = col(db.Integer, db.ForeignKey(
#         'conversation.id'), nullable=False)

#     conversations = db.relationship('Conversation', back_populates='messages')
#     dogs = db.relationship('Dog', back_populates='messages')


# class ConversationSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Conversation

#     id = ma.auto_field()
#     time_started = ma.auto_field()
#     messages = fields.Nested(MessageSchema, many=True)
#     dogs = fields.Nested(DogSchema, many=True)


# class MessageSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Message

#     id = ma.auto_field()
#     message = ma.auto_field()
#     ts = ma.auto_field()
#     dog_id = ma.auto_field()
#     conversation_id = ma.auto_field()
