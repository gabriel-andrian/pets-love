from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask import request
from functools import wraps
from http import HTTPStatus
from .http import build_api_response

from app.models.dog_model import Dog
from app.models.interest_model import Interest
from app.models.owner_model import Owner
from app.models.like_model import Like
from app.models.photos_model import Photo


def owner_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()

        owner_id = get_jwt_identity()

        data = request.get_json()

        found_dog = Dog.query.get(data["dog_id"])
        if found_dog.owner_id == owner_id:
            return function(*args, **kwargs)

        return build_api_response(HTTPStatus.UNAUTHORIZED)

    return wrapper
