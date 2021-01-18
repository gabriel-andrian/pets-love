from flask import Blueprint, request
from app.models import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.owner_model import Owner, OwnerSchema
from app.models.dog_model import Dog
from http import HTTPStatus
from app.services.http import build_api_response

bp_owner = Blueprint("api_owner", __name__, url_prefix="/owner")


@bp_owner.route("/", methods=["PATCH"])
@jwt_required
def update():
    owner_id = get_jwt_identity()

    data = request.get_json()
    owner = Owner.query.get_or_404(owner_id)

    owner.name = data['name'] if data.get('name') else owner.name
    owner.surname = data['surname'] if data.get('surname') else owner.surname
    owner.document = data['document'] if data.get(
        'document') else owner.document
    owner.email = data['email'] if data.get('email') else owner.email
    owner.address = data['address'] if data.get('address') else owner.address
    owner.password = data['password'] if data.get(
        'password') else owner.password

    db.session.commit()
    return {'data': OwnerSchema().dump(owner)}, HTTPStatus.OK


@bp_owner.route("/", methods=["DELETE"])
@jwt_required
def delete():
    owner_id = get_jwt_identity()

    Owner.query.get_or_404(owner_id)
    Dog.query.filter_by(owner_id=owner_id).delete()
    Owner.query.filter_by(id=owner_id).delete()

    db.session.commit()
    return build_api_response(HTTPStatus.OK)
