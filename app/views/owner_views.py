from flask import Blueprint, request
from app.models import db
from app.models.owner_model import Owner, OwnerSchema
from http import HTTPStatus

bp_owner = Blueprint("api_owner", __name__, url_prefix="/owner")


@bp_owner.route("/<int:owner_id>", methods=["PATCH"])
def update(owner_id: int):
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


@bp_owner.route("/<int:owner_id>", methods=["DELETE"])
def delete(owner_id: int):
    Owner.query.get_or_404(owner_id)

    Owner.query.filter_by(id=owner_id).delete()
    db.session.commit()
    return {"msg": f'Dono com id {owner_id} deletado'}, HTTPStatus.OK
