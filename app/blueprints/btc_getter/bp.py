from flask import Blueprint


btc_getter = Blueprint(
    "btc_getter", __name__, template_folder="templates", url_prefix="/btc_getter"
)

from . import routes
