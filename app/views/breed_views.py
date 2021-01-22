from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.services.http import build_api_response
from app.models.breed_model import Breed, BreedSchema
from app.services.insert_list_breeds import insert_list_csv_breed


bp_breed = Blueprint('api_breed', __name__, url_prefix='/breed')


@bp_breed.route('/', methods=['GET'])
@jwt_required
def get():
    breed = Breed.query.all()

    return {'data': BreedSchema(many=True).dump(breed)}, HTTPStatus.OK


@bp_breed.route('/', methods=['POST'])
@jwt_required
def create():

    insert_list_csv_breed()

    try:
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
