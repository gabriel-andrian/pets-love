from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.services.http import build_api_response
from app.models.interest_model import Interest


bp_interest = Blueprint('api_interest', __name__, url_prefix='/interest')

@bp_interest.route('/', methods=['POST'])
def create():
    data = request.get_json()
    
    interest = Interest(
        gender=data["gender"],
        dog_id=data["dog_id"],
        breed_id=data["breed_id"]
    )

    try:
        db.session.add(interest)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_interest.route('/<int:interest_id>', methods=['DELETE'])
def delete(interest_id: int):
    interest_id_selected = Interest.query.filter_by(id = interest_id).delete()
    db.session.commit()
    return build_api_response(HTTPStatus.OK)