from flask import Blueprint
from flask.globals import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.http import build_api_response
from app.models import db
from app.models.dog_model import Dog, Message, MessageSchema

bp_message = Blueprint(
    'bp_message', __name__)


@bp_message.route('/dog/<int:dog_id>/msg', methods=['POST'])
@jwt_required
def create_msg(dog_id):
    owner_id = get_jwt_identity()
    conv_id = request.json.get('conv_id')
    message_text = request.json.get('message_text')

    dog = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not dog:
        return build_api_response(HTTPStatus.NOT_FOUND)

    msg = Message(
        message=message_text,
        dog_id=dog_id,
        conversation_id=conv_id
    )

    db.session.add(msg)
    db.session.commit()

    return {'data': MessageSchema().dump(msg)}, HTTPStatus.CREATED


@bp_message.route('/dog/<int:dog_id>/msg/<int:msg_id>', methods=['GET'])
@jwt_required
def get_one_msg(dog_id, msg_id):
    owner_id = get_jwt_identity()
    dog = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not dog:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Message.query.filter_by(dog_id=dog_id, id=msg_id).first()
    if not data:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {"data": MessageSchema().dump(data)}, HTTPStatus.OK


@bp_message.route('/dog/<int:dog_id>/msg/<int:msg_id>', methods=['DELETE'])
@jwt_required
def delete_msg(dog_id, msg_id):
    owner_id = get_jwt_identity()
    dog = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not dog:
        return {"dog": build_api_response(HTTPStatus.NOT_FOUND)}

    msg = Message.query.filter_by(id=msg_id, dog_id=dog_id)
    if not msg.first():
        return {"msg": build_api_response(HTTPStatus.NOT_FOUND)}

    msg.delete()
    db.session.commit()
    return build_api_response(HTTPStatus.OK)
