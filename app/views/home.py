from flask import Blueprint

bp_home = Blueprint('bp_home', __name__, url_prefix='/home')


@bp_home.route('/')
def status():
    return {'msg': 'ok'}
