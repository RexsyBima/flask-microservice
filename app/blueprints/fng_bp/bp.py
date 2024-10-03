from flask import Blueprint


fng_bp = Blueprint("fng_bp", __name__, template_folder="templates", url_prefix="/fng")

from . import routes
