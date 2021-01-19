from app.models.dog_model import Dog
from flask_jwt_extended import get_jwt_identity


def verify_auth(dog_id):
    current_owner = get_jwt_identity()
    dog = Dog.query.filter_by(
        id=dog_id, owner_id=current_owner).first()

    return dog
