from flask import Blueprint
from http import HTTPStatus
from app.models.breed_model import Breed, BreedSchema

bp_breed = Blueprint('bp_breed', __name__, url_prefix='/breed')


@bp_breed.route('/', methods=['GET'])
def get():
    breed = Breed.query.all()

    return {'data': BreedSchema(many=True).dump(breed)}, HTTPStatus.OK
