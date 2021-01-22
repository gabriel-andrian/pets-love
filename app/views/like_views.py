from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from http import HTTPStatus

from app.models.like_model import Like, LikeSchema
from app.models.owner_model import Owner

from app.services.like_services import verify_match

bp_like = Blueprint('api_like', __name__, url_prefix="/like")


@bp_like.route('/', methods=["POST"])
@jwt_required
def give_like():
    data = request.get_json()

    owner = Owner.query.get(get_jwt_identity())

    if data['dog_id_give'] in [dog.id for dog in owner.dogs]:
        if Like.query.filter_by(
            dog_id_give=data['dog_id_give'],
            dog_id_receive=data['dog_id_receive']
        ).first() is not None:
            return {'msg': "Like alredy exists!"}, HTTPStatus.BAD_REQUEST

        like = Like(
            dog_id_give=data['dog_id_give'],
            dog_id_receive=data['dog_id_receive'],
            dislike=data['dislike']
        )

        verify_match(like)

        db.session.add(like)
        db.session.commit()
        return {'data': {'match': LikeSchema().dump(like)}}, \
            HTTPStatus.CREATED

    msg = f"Dog with id {data['dog_id_give']} not exists, or is not your dog!"
    return {'msg': msg}, HTTPStatus.NOT_FOUND
