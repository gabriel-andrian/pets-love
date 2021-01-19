from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.services.http import build_api_response
from app.models.interest_model import Interest, InterestSchema


bp_interest = Blueprint('api_interest', __name__, url_prefix='/interest')


@bp_interest.route('/<int:interest_id>', methods=['GET'])
def get_dog_id(interest_id: int):

    dog_interest = Interest.query.get_or_404(interest_id)

    return {'data': InterestSchema().dump(dog_interest)}, HTTPStatus.OK


@bp_interest.route('/', methods=['POST'])
def create():
    data = request.get_json()

    interest = Interest(
        dog_id=data["dog_id"],
        breed_id=data["breed_id"]
    )

    try:
        db.session.add(interest)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_interest.route('/<int:interest_id>', methods=['PATCH'])
def update(interest_id: int):

    data = request.get_json()

    interest = Interest.query.get_or_404(interest_id)

    interest.dog_id = data['dog_id'] if data.get('dog_id') else interest.dog_id
    interest.breed_id = data['breed_id'] if data.get(
        'breed_id') else interest.breed_id

    db.session.commit()
    return build_api_response(HTTPStatus.CREATED)
