from flask import Blueprint, request
from app.models.owner_model import Owner

bp_authorization = Blueprint('authorization', __name__, '/auth')


@bp_authorization.route('/signup', methods = ['POST'])
def signup():
    data = request.get_json()
    owner = Owner(
        name = data['name']
        surname = data['surname']
        document = data['document']
        email = data['email']
        address = data['name']
        password = sha256(data['name'])
    )
    return {'msg': f'created: {owner}'}


@bp_authorization.route('/login', methods = ['POST'])
def login():
    ...