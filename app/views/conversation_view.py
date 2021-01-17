from flask import Blueprint
from datetime import datetime
from flask.globals import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.http import build_api_response
from app.models import db
from app.models.conversation_model import Conversation, Message, ConversationSchema, MessageSchema


bp_conversation = Blueprint('bp_conversation', __name__, url_prefix='/conversation')


@bp_conversation.route('/', methods = ['POST'])
@jwt_required
def create_conversation():
    owner_id = get_jwt_identity()
    new_conversation = Conversation()
    db.add(new_conversation)
    db.commit()
    return build_api_response(HTTPStatus.CREATED)


@bp_conversation.route('/', methods = ['GET'])
@jwt_required
def get_all_conversation():
    owner_id = get_jwt_identity()
    data = Conversation.query.all()
    return {'data': data}


# @jwt_required
# @bp_conversation.route('/<int:conv_id>', methods = ['GET'])
# def get_one_conversation(conv_id):
#     owner_id = get_jwt_identity()

#     Conversation.query.filter_by(id = id)
#     ...


@bp_conversation.route('/<int:conv_id>/msg', methods = ['POST'])
@jwt_required
def create_msg(conv_id):
    owner_id = get_jwt_identity()
    data = request.json.get('message_text')
    dog_id = request.json.get('dog_id')

    # testar se o cachorro pertence ao owner...

    msg = Message(
        message_text = data['message_text'],
        dog_id = data['dog_id'],
        ts = datetime.now(),
        conversation_id = conv_id
    )

    db.session.add(msg)
    db.session.commit()

    return {'data': MessageSchema().dump(msg)}, HTTPStatus.CREATED

# @jwt_required
# @bp_conversation.route('<int:conv_id>/msg', methods = ['GET'])
# def get_all_msg(conv_id):
#     owner_id = get_jwt_identity()
#     pass


# @jwt_required
# @bp_conversation.route('/msg', methods = ['GET'])
# def get_one_msg():
#     owner_id = get_jwt_identity()
#     pass