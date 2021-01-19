from flask import Blueprint, request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from sqlalchemy import join

from app.models import db
from app.services.http import build_api_response
from app.models.interest_model import Interest, InterestSchema
from app.models.dog_model import Dog
from app.models.owner_model import Owner, OwnerSchema


bp_interest = Blueprint('api_interest', __name__, url_prefix='/interest')


@bp_interest.route('/<int:interest_id>', methods=['GET'])
#@jwt_required
def get_dog_id(interest_id: int):

    dog_interest = Interest.query.get_or_404(interest_id)

    return {'data': InterestSchema().dump(dog_interest)}, HTTPStatus.OK


@bp_interest.route('/', methods=['POST'])
#@jwt_required
def created_new_interest():
    owner_id = get_jwt_identity()

    data = request.get_json()
    dog_interest = Dog.query.get_or_404(data['dog_id'])

    result = InterestSchema().dump(dog_interest)

    print("*************", result)

    # # interest = Interest(**{
    # #     "dog_id":data["dog_id"],
    # #     "breed_id":data["breed_id"],
    # #     "gender_interest":data["gender_interest"]
    # # })

    # try:
    #     db.session.add(interest)
    #     db.session.commit()
    #     return build_api_response(HTTPStatus.CREATED)
    # except IntegrityError:
    #     return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_interest.route('/<int:interest_id>', methods=['PATCH'])
def update_interest(interest_id: int):

    data = request.get_json()

    interest = Interest.query.get_or_404(interest_id)

    interest.breed_id = data['breed_id'] if data.get(
        'breed_id') else interest.breed_id
    interest.gender_interest = data['gender_interest'] if data.get(
        'gender_interest') else interest.gender_interest

    db.session.commit()
    return build_api_response(HTTPStatus.CREATED)
