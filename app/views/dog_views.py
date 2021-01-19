from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.models import db
from app.models.dog_model import Dog, DogSchema
from app.services.http import build_api_response
from flask_jwt_extended import jwt_required, get_jwt_identity


bp_dogs = Blueprint("api_dogs", __name__, url_prefix="/dog")

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)


@bp_dogs.route('/', methods=['POST'])
@jwt_required
def create():
    data = request.get_json()
    owner_id = get_jwt_identity()

    dog = Dog(
        name=data['name'],
        details=data['details'],
        owner_id=data['owner_id'],
        breed_id=data['breed_id'],
        gender=data['gender'])

    try:
        db.session.add(dog)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@ bp_dogs.route('/', methods=['GET'])
def list_all():
    dogs = Dog.query.all()

    return {'data': dogs_schema.dump(dogs)}, HTTPStatus.OK


@ bp_dogs.route('/<int:dog_id>', methods=['GET'])
@jwt_required
def get(dog_id: int):
    dog = Dog.query.get_or_404(dog_id)

    return {'data': dog_schema.dump(dog)}, HTTPStatus.OK


@bp_dogs.route("/<int:dog_id>", methods=["PATCH"])
@jwt_required
def update(dog_id: int):
    data = request.get_json()
    dog = Dog.query.get_or_404(dog_id)

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
    Dog.query.get_or_404(dog_id)

    Dog.query.filter_by(id=dog_id).delete()
    db.session.commit()

    return {"msg": f'Dog com id {dog_id} deletado'}, HTTPStatus.OK


@ bp_dogs.route('/matches', methods=['GET'])
def get_matches():
    ...
