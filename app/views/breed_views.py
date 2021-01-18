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
    
    # with open(env('BREEDS_CSV')) as f:

    #     reader = csv.DictReader(f)

    #     reader.to_sql('Breed', con=engine, index= False, if_exists= 'append')
    #     query = db.update(finaltable).where(finaltable.DataSource == None).values(DataSource == f[i])

    #     connection.execute(query)



    data = request.get_json()

    breed = Breed(
        name=data["name"]
    )

    try:
        db.session.add(breed)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
