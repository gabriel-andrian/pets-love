from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.models import db
from app.models.photos_model import Photo
from app.services.http import build_api_response
from flask_jwt_extended import jwt_required, get_jwt_identity


bp_photo = Blueprint('api_photo', __name__, url_prefix='/photo')


@bp_photo.route('/', methods=['POST'])
@jwt_required
def create():
    data = request.get_json()
    photo = Photo(
        dog_account_id=data['dog_account_id'],
        link=data['link'])

    try:
        db.session.add(photo)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_photo.route("/<photo_id>", methods=["DELETE"])
@jwt_required
def delete(photo_id):

    # owner_id = get_jwt_identity()
    # Logica de se a foto é do dog e se o dog é do dono (ID)
    # result = db.session.query(Photo).join(Dog).join(Owner). \
    #   filter(Owner.id == owner_id).all()

    Photo.query.get_or_404(photo_id)
    Photo.query.filter_by(id=photo_id).delete()

    db.session.commit()
    return {"msg": f'Foto com id {photo_id} deletado'}, HTTPStatus.OK
