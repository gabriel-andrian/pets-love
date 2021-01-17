from datetime import datetime
from app.models import db, ma

col = db.Column

dog_conversation = db.Table(
    'dog_conversation',
    col('dog_id', db.Integer, db.ForeignKey('conversation.id'), primary_key = True),
    col('conversation_id', db.Integer, db.ForeignKey('dog.id'), primary_key = True)
)


class Conversation(db.Model):
    __tablename__ = 'conversation'
    id = col(db.Integer, primary_key = True)
    time_started = col(db.Time)

    messages = db.relationship('Message', back_populates='conversations')
    dogs = db.relationship('Dog', secondary = dog_conversation, backref = 'conversations')


class Message(db.Model):
    __tablename__ = 'message'
    id = col(db.Integer, primary_key = True)
    message = col(db.Text, nullable = False)
    ts = col(db.DateTime, default = datetime.utcnow())
    
    dog_id = col(db.Integer, db.ForeignKey('dog.id'), nullable = False)
    conversation_id = col(db.Integer, db.ForeignKey('conversation.id'), nullable=False)

    conversations = db.relationship('Conversation', back_populates='messages')


class ConversationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Conversation

    id = ma.auto_field()
    time_started = ma.auto_field()
    messages = ma.auto_field()
    dogs = ma.auto_field()


class MessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Message

    id = ma.auto_field()
    message = ma.auto_field()
    ts = ma.auto_field()
    dog_id = ma.auto_field()
    conversations = ma.auto_field()
    conversation_id = ma.auto_field()
    