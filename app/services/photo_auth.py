from app.models.dog_model import Dog
from app.models.photos_model import Photo
from flask_jwt_extended import get_jwt_identity
from app.models import db


def verify_auth_delete(photo_id):
    current_owner = get_jwt_identity()

    result = db.session.query(Photo, Dog).filter(
        Photo.dog_account_id == Dog.id,
        Photo.id == photo_id,
        Dog.owner_id == current_owner).first()

    return result


def verify_auth_create(data):
    current_owner = get_jwt_identity()
    result = db.session().query(Dog).filter(
        Dog.owner_id == current_owner,
        Dog.id == data['dog_account_id']).first()

    return result
