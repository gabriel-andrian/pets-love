from flask import Blueprint, request
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.services.http import build_api_response
from app.models.interest_model import Interest, InterestSchema
from app.services.owner_services import owner_required
from app.services.dog_auth import verify_auth


bp_interest = Blueprint('api_interest', __name__, url_prefix='/interest')


@bp_interest.route('/<int:interest_id>', methods=['GET'])
@jwt_required
def get_dog_id(interest_id: int):

    dog_verify = verify_auth(interest_id)

    if not dog_verify:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    dog = Interest.query.get(interest_id)

    if not dog:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {'data': InterestSchema().dump(dog)}, HTTPStatus.OK


@bp_interest.route('/', methods=['POST'])
@owner_required
def created_new_interest():

    data = request.get_json()

    interest = Interest(
        dog_id=data["dog_id"],
        breed_id=data["breed_id"],
        gender_interest=data["gender_interest"]
    )

    try:
        db.session.add(interest)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_interest.route('/<int:interest_id>', methods=['PATCH'])
@jwt_required
def update_interest(interest_id: int):

    dog_verify = verify_auth(interest_id)

    if not dog_verify:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    data = request.get_json()

    dog = Interest.query.get_or_404(interest_id)

    if not dog:
        return build_api_response(HTTPStatus.NOT_FOUND)

    dog.breed_id = data['breed_id'] if data.get(
        'breed_id') else dog.breed_id
    dog.gender_interest = data['gender_interest'] if data.get(
        'gender_interest') else dog.gender_interest

    try:
        db.session.commit()
        return build_api_response(HTTPStatus.OK)
    except IntegrityError:
        return build_api_response(HTTPStatus.NOT_FOUND)
