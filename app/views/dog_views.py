from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.models import db
from app.models.dog_model import Dog, DogSchema
from app.models.like_model import Like
from app.services.http import build_api_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.dog_auth import verify_auth

bp_dogs = Blueprint("api_dogs", __name__, url_prefix="/dog")

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)


@bp_dogs.route('/', methods=['POST'])
@jwt_required
def create():
    owner_id = get_jwt_identity()
    data = request.get_json()
    current_owner = get_jwt_identity()

    if current_owner is not data['owner_id']:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    dog = Dog(
        name=data['name'],
        details=data['details'],
        owner_id=owner_id,
        breed_id=data['breed_id'],
        gender=data['gender'])

    try:
        db.session.add(dog)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@ bp_dogs.route('/', methods=['GET'])
@jwt_required
def list_all():
    dogs = Dog.query.all()

    return {'data': dogs_schema.dump(dogs)}, HTTPStatus.OK


@ bp_dogs.route('/<int:dog_id>', methods=['GET'])
@jwt_required
def get(dog_id: int):
    dog = Dog.query.get(dog_id)

    if not dog:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {'data': dog_schema.dump(dog)}, HTTPStatus.OK


@bp_dogs.route("/<int:dog_id>", methods=["PATCH"])
@jwt_required
def update(dog_id: int):
    data = request.get_json()
    dog = verify_auth(dog_id)

    if not dog:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    dog.name = data['name'] if data.get('name') else dog.name
    dog.details = data['details'] if data.get('details') else dog.details
    dog.breed_id = data['breed_id'] if data.get(
        'breed_id') else dog.breed_id
    dog.gender = data['gender'] if data.get('gender') else dog.gender

    db.session.commit()
    return {'data': dog_schema.dump(dog)}, HTTPStatus.OK


@bp_dogs.route("/<int:dog_id>", methods=["DELETE"])
@jwt_required
def delete(dog_id: int):
    dog = verify_auth(dog_id)
    if not dog:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    Dog.query.filter_by(id=dog.id).delete()
    db.session.commit()
    return build_api_response(HTTPStatus.OK)


@bp_dogs.route('/<int:dog_id>/matches', methods=['GET'])
@jwt_required
def get_matches(dog_id: int):
    owner_id = get_jwt_identity()

    found_dog = Dog.query.get(dog_id)

    if not found_dog.owner_id or found_dog.owner_id != owner_id:
        return build_api_response(HTTPStatus.NOT_FOUND)

    likes = Like.query.filter_by(dog_id_give=found_dog.id, match=True).all()

    dogs = []
    for like in likes:
        dogs.append(Dog.query.get(like.dog_id_receive))

    return {'data': DogSchema(many=True).dump(dogs)}, HTTPStatus.OK
