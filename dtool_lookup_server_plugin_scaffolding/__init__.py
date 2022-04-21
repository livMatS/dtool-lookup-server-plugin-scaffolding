from flask import (
    abort,
    jsonify,
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from flask_smorest import Blueprint

from dtool_lookup_server import AuthenticationError
from dtool_lookup_server.schemas import ConfigSchema

try:
    from importlib.metadata import version, PackageNotFoundError
except ModuleNotFoundError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass

from .utils import config_to_dict

scaffolding_bp = Blueprint("scaffolding", __name__, url_prefix="/scaffolding")


@scaffolding_bp.route("/config", methods=["GET"])
@scaffolding_bp.response(200, ConfigSchema)
@jwt_required()
def plugin_config():
    """Return the JSON-serialized plugin configuration."""
    username = get_jwt_identity()
    try:
        config = config_to_dict(username)
    except AuthenticationError:
        abort(401)
    return jsonify(config)
