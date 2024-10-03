from flask import Blueprint
from jinja2 import TemplateNotFound

password_bp = Blueprint(
    "password_bp", __name__, template_folder="templates", url_prefix="/password"
)

from . import routes
