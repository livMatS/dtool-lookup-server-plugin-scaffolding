from flask import (
    abort,
    Blueprint,
    jsonify,
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from dtool_lookup_server import AuthenticationError

from .utils import config_to_dict

__version__ = "0.1.0"


scaffolding_bp = Blueprint("scaffolding", __name__, url_prefix="/scaffolding")

@scaffolding_bp.route("/config", methods=["GET"])
@jwt_required
def plugin_config():
    """Return the JSON-serialized plugin configuration."""
    username = get_jwt_identity()
    try:
        config = config_to_dict(username)
    except AuthenticationError:
        abort(401)
    return jsonify(config)
