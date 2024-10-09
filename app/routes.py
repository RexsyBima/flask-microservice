from . import app
import string
import requests
from .blueprints.password_bp.bp import password_bp
from .blueprints.sentiment_analysis_bp.bp import sentiment_analysis_bp
from .blueprints.fng_bp.bp import fng_bp
from .blueprints.btc_getter.bp import btc_getter
from .blueprints.newsapi_bp.bp import newsapi_bp


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
app.register_blueprint(password_bp)
app.register_blueprint(sentiment_analysis_bp)
app.register_blueprint(fng_bp)
app.register_blueprint(btc_getter)
app.register_blueprint(newsapi_bp)


@app.route("/")
def index():
    return "Hello World"


@app.route("/get_fng")
def get_fng():
    resp = requests.get("https://api.alternative.me/fng/")
    return resp.json()
