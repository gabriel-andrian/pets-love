from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.models import db
from http import HTTPStatus

from app.models.like_model import Like

bp_like = Blueprint('api_like', __name__, url_prefix="/like")


@bp_like.route('/', methods=["POST"])
@jwt_required
def give_like():
    # Cria um novo like com os dados recebidos
    data = request.get_json()

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

    # Se o dislike for --False--, verificar se possui algum like dado a ele
    if not like.dislike:
        # Se sim, verificar se o id do dog dado o like está entre os que deram
        # o like para ele e o dislike for --False--
        like_received = Like.query.filter_by(
            dog_id_receive=like.dog_id_give,
            dog_id_give=like.dog_id_receive,
            dislike=False).first()

        if like_received is not None:
            # Se sim, modificar o match de ambos como --True--
            like.match = True
            like_received.match = True

    db.session.add(like)
    db.session.commit()
    return {'data': {'match': like.match}}, HTTPStatus.CREATED


@bp_like.route(
    "/dog/<int:dog_id>/has_match_with/<int:other_dog_id>", methods=["GET"])
@jwt_required
def has_match(dog_id: int, other_dog_id: int):
    like = Like.query.filter_by(
        dog_id_give=dog_id, dog_id_receive=other_dog_id).first()
    if like is None:
        return {'msg': "Like não existente!"}, HTTPStatus.NOT_FOUND
    return {'data': {'match': like.match}}, HTTPStatus.OK
