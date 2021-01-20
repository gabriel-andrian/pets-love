from flask import Blueprint
from flask.globals import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.http import build_api_response
from app.models import db
from app.models.dog_model import Dog, Conversation, ConversationSchema


bp_conversation = Blueprint(
    'bp_conversation', __name__, url_prefix='/conversation')


@bp_conversation.route('/', methods=['POST'])
@jwt_required
def create_conversation():
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    dog_to_data = request.json.get('dog_to')

    found_dog = Dog.filter_by(id=dog_id, owner_id=owner_id)
    if not found_dog:
        return {"Not found": "dog_id is incorrect or does not belong to authenticated user."}, HTTPStatus.NOT_FOUND

    dog_to = Dog.filter_by(id=dog_to_data)
    if not found_dog:
        return {"Not found": "dog_to does not exist in database."}, HTTPStatus.NOT_FOUND

    dogs = Dog.query.filter(Dog.id.in_([found_dog, dog_to])).all()

    new_conversation = Conversation(dogs=dogs)
    db.session.add(new_conversation)
    db.session.commit()

    return {'data': ConversationSchema().dump(new_conversation)}, HTTPStatus.CREATED


@bp_conversation.route('/<int:conv_id>', methods=['PUT'])
@jwt_required
def update_conversation(conv_id):
    owner_id = get_jwt_identity()

    found_dog = Dog.filter_by(id=dog_id, owner_id=owner_id)
    if not found_dog:
        return {"Not found": "dog_id is incorrect or dog does not belong to authenticated user."}, HTTPStatus.NOT_FOUND

    msg = Message.query.filter_by(id=request.json.get('msg_id')).first()

    conversation = Conversation.filter_by(id=conv_id).first()
    conversation.messages.append(msg)

    db.session.commit()

    return build_api_response(HTTPStatus.OK)


@bp_conversation.route('/', methods=['GET'])
@jwt_required
def get_all_conversations():
    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')

    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Conversation.query.filter_by(dog_id=found.id)

    return {'data': ConversationSchema(many=True).dump(data)}, HTTPStatus.FOUND


@bp_conversation.route('/<int:conv_id>', methods=['GET'])
@jwt_required
def get_one_conversation(conv_id):

    owner_id = get_jwt_identity()
    dog_id = request.json.get('dog_id')
    found = Dog.query.filter_by(owner_id=owner_id, id=dog_id).first()
    if not found:
        return build_api_response(HTTPStatus.NOT_FOUND)

    data = Conversation.query.filter_by(id=conv_id).first(
    ) if conv_id else Conversation.query.filter_by(dog_id=found.id).all()
    return {'data': ConversationSchema().dump(data) if conv_id else ConversationSchema(many=True).dump(data)}, HTTPStatus.FOUND
