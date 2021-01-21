from flask import Blueprint
from flask.globals import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.http import build_api_response
from app.models import db
from app.models.dog_model import Dog, Conversation, ConversationSchema


bp_conversation = Blueprint(
    'bp_conversation', __name__)


@bp_conversation.route('/dog/<int:dog_id>/conversation', methods=['POST'])
@jwt_required
def create_conversation(dog_id):
    owner_id = get_jwt_identity()
    dog_to_data = request.json.get('dog_to')

    found_dog = Dog.query.filter_by(id=dog_id, owner_id=owner_id).first()
    if not found_dog:
        return {"Not found": "dog_id is incorrect or does not belong to authenticated user."}, HTTPStatus.NOT_FOUND

    dog_to = Dog.query.filter_by(id=dog_to_data).first()
    if not dog_to:
        return {"Not found": "dog_to does not exist in database."}, HTTPStatus.NOT_FOUND

    conversation = Conversation()
    conversation.dogs.append(found_dog)
    conversation.dogs.append(dog_to)
    db.session.add(conversation)
    db.session.commit()

    return {'data': ConversationSchema().dump(conversation)}, HTTPStatus.CREATED


@bp_conversation.route('/dog/<int:dog_id>/conversation', methods=['GET'])
@jwt_required
def get_all_conversations(dog_id):
    owner_id = get_jwt_identity()

    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Conversation.query.filter(
        Conversation.dogs.any(id=dog_id)).all()

    return {'data': ConversationSchema(many=True).dump(data)}, HTTPStatus.FOUND


@bp_conversation.route('/dog/<int:dog_id>/conversation/<int:conv_id>', methods=['GET'])
@jwt_required
def get_one_conversation(dog_id, conv_id):

    owner_id = get_jwt_identity()
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Conversation.query.filter_by(id=conv_id).first()
    if not data:
        return build_api_response(HTTPStatus.NOT_FOUND)

    if found in data.dogs:
        return {'data': ConversationSchema().dump(data)}, HTTPStatus.FOUND

    return build_api_response(HTTPStatus.UNAUTHORIZED)
