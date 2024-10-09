from flask import Blueprint

newsapi_bp = Blueprint(
    "newsapi_bp", __name__, template_folder="templates", url_prefix="/newsapi"
)

from . import routes
