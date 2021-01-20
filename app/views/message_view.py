from flask import Blueprint
from flask.globals import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.http import build_api_response
from app.models import db
from app.models.dog_model import Dog, Message, MessageSchema

bp_message = Blueprint(
    'bp_message', __name__, url_prefix='/msg')


@bp_message.route('/', methods=['POST'])
@jwt_required
def create_msg():
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    message_text = request.json.get('message_text')

    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id)
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    msg = Message(
        message=message_text,
        dog_id=dog_id,
    )

    db.session.add(msg)
    db.session.commit()

    return {'data': MessageSchema().dump(msg)}, HTTPStatus.CREATED


@jwt_required
@bp_message.route('/msg/<int:msg_id>', methods=['GET'])
def get_one_msg(msg_id):

    data = Message.query.filter_by(id=msg_id)[0]
    if not data:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {"data": MessageSchema().dump(data)}, HTTPStatus.FOUND


@jwt_required
@bp_message.route('/msg', methods=['DELETE'])
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
