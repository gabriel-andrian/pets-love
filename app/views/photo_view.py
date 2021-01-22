from flask import Blueprint, request
from http import HTTPStatus
from app.models import db
from app.models.photos_model import Photo, PhotoSchema
from app.models.dog_model import Dog
from app.services.http import build_api_response
from flask_jwt_extended import jwt_required
from app.services.photo_auth import verify_auth_delete, verify_auth_create

bp_photo = Blueprint('api_photo', __name__, url_prefix='/photo')


@bp_photo.route('/', methods=['POST'])
@jwt_required
def create():
    data = request.get_json()
    photo = Photo(
        dog_account_id=data['dog_account_id'],
        link=data['link'])

    Dog.query.get_or_404(data['dog_account_id'])

    result = verify_auth_create(data)

    if not result:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    db.session.add(photo)
    db.session.commit()
    return {"data": PhotoSchema().dump(photo)}, HTTPStatus.CREATED


@bp_photo.route("/<photo_id>", methods=["DELETE"])
@jwt_required
def delete(photo_id):

    Photo.query.get_or_404(photo_id)
    result = verify_auth_delete(photo_id)

    if not result:
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    Photo.query.filter_by(id=photo_id).delete()

    db.session.commit()
    return build_api_response(HTTPStatus.OK)
