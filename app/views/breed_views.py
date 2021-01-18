from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.services.http import build_api_response
from app.models.breed_model import Breed, BreedSchema


import csv
import os
from environs import Env

env = Env()
env.read_env()


bp_breed = Blueprint('bp_breed', __name__, url_prefix='/breed')


@bp_breed.route('/', methods=['GET'])
@jwt_required
def get():
    breed = Breed.query.all()

    return {'data': BreedSchema(many=True).dump(breed)}, HTTPStatus.OK


@bp_breed.route('/', methods=['POST'])
@jwt_required
def create():
    
    with open(env('BREEDS_CSV')) as f:

        reader = csv.DictReader(f)
        for breed in reader:
            record = Breed(**{"name":breed['Breed']})
            db.session.add(record)

    try:
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
