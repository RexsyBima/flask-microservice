from flask import Blueprint


sentiment_analysis_bp = Blueprint(
    "sentiment_analysis_bp",
    __name__,
    template_folder="templates",
    url_prefix="/sentiment_analysis",
)

from . import routes
