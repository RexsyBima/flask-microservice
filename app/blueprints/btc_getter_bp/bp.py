from flask import Blueprint


btc_getter_bp = Blueprint(
    "btc_getter_bp", __name__, template_folder="templates", url_prefix="/btc_getter"
)

from . import routes
