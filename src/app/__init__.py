from flask import Blueprint, jsonify

from .routes import routes
from ..common.AppException import AppException

blueprint = Blueprint('example', __name__)


@blueprint.errorhandler(AppException)
def handle_app_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

for route in routes:
    blueprint.add_url_rule(route['path'], methods=route['methods'], view_func=route['handler'])
