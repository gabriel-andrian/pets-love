from flask import Blueprint
from datetime import datetime
from flask.globals import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.http import build_api_response
from app.models import db
from app.models.dog_model import Conversation, Message, ConversationSchema, MessageSchema


bp_conversation = Blueprint(
    'bp_conversation', __name__, url_prefix='/conversation')


@bp_conversation.route('/', methods=['POST'])
@jwt_required
def create_conversation():
    owner_id = get_jwt_identity()

    new_conversation = Conversation(dogs=[], messages=[])
    db.add(new_conversation)
    db.commit()
    return build_api_response(HTTPStatus.CREATED)


@bp_conversation.route('/', methods=['GET'])
@jwt_required
def get_all_conversation():

    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Conversation.query.filter_by(dog_id=dog_id)
    return {'data': MessageSchema().dump(data)}, HTTPStatus.FOUND


@bp_conversation.route('/<int:conv_id>', methods=['GET'])
@jwt_required
def get_one_conversation(conv_id):

    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Conversation.query.filter_by(id=conv_id)
    return {'data': ConversationSchema().dump(data)}, HTTPStatus.FOUND


@bp_conversation.route('/<int:conv_id>/msg', methods=['POST'])
@jwt_required
def create_msg(conv_id):
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    message_text = request.json.get('message_text')

    msg = Message(
        message_text=message_text,
        dog_id=dog_id,
        conversation_id=conv_id
    )

    db.session.add(msg)
    db.session.commit()

    return {'data': MessageSchema().dump(msg)}, HTTPStatus.CREATED


@jwt_required
@bp_conversation.route('<int:conv_id>/msg', methods=['GET'])
def get_all_msg(conv_id):
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Message.query.filter_by(conversation_id=conv_id)
    return {'data': MessageSchema().dump(data)}, HTTPStatus.FOUND


@jwt_required
@bp_conversation.route('/msg', methods=['GET'])
def get_one_msg():
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    msg_id = request.get_or_404('msg_id')
    data = Message.query.filter_by(id=msg_id)[0]
    if not data:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {"data": MessageSchema().dump(data)}, HTTPStatus.FOUND


@jwt_required
@bp_conversation.route('/msg', methods=['DELETE'])
def delete_msg():
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    msg_id = request.get_or_404('msg_id')
    msg_found = Message.query.filter_by(id=msg_id, dog_id=dog_id).first()
    if not msg_found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    msg_found.delete()
    db.session.commit()
    return build_api_response(HTTPStatus.OK)
