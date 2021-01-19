from flask import Blueprint, request
from http import HTTPStatus
from datetime import timedelta
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from app.services.http import build_api_response
from hashlib import sha256

from app.models import db
from app.models.owner_model import Owner

bp_authorization = Blueprint('authorization', __name__, url_prefix='/auth')


def crypto(value):
    return sha256(value.encode()).hexdigest()


@bp_authorization.route('/signup', methods=['POST'])
def signup():

    name = request.json.get('name')
    surname = request.json.get('surname')
    document = request.json.get('document')
    email = request.json.get('email')
    address = request.json.get('address')
    password = crypto(request.json.get('password'))

    email_error = Owner.query.filter_by(email=email).first()
    if email_error:
        return {'Error': 'Email already taken. Try another one.'}, HTTPStatus.UNAUTHORIZED

    document_error = Owner.query.filter_by(document=document).first()
    if document_error:
        return {'Error': 'Document alredy exists in DB. Please check your data and try again.'}, HTTPStatus.UNAUTHORIZED

    owner = Owner(
        name=name,
        surname=surname,
        document=document,
        email=email,
        address=address,
        password=password
    )

    try:
        db.session.add(owner)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_authorization.route('/login', methods=['POST'])
def login():

    email = request.json.get('email')
    password = crypto(request.json.get('password'))
    owner = Owner.query.filter_by(
        email=email, password=password).first() or None
    if not owner:
        return build_api_response(HTTPStatus.NOT_FOUND)

    access_token = create_access_token(
        identity=owner.id,
        expires_delta=timedelta(days=10)
    )

    return {
        "data": {
            "name": owner.name,
            "owner_id": owner.id,
            "token": access_token
        }
    }, HTTPStatus.ACCEPTED
