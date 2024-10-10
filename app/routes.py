from . import app
import string
from .blueprints.password_bp.bp import password_bp
from .blueprints.sentiment_analysis_bp.bp import sentiment_analysis_bp
from .blueprints.fng_bp.bp import fng_bp
from .blueprints.btc_getter_bp.bp import btc_getter_bp
from .blueprints.newsapi_bp.bp import newsapi_bp
from flask import render_template

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
app.register_blueprint(password_bp)
app.register_blueprint(sentiment_analysis_bp)
app.register_blueprint(fng_bp)
app.register_blueprint(btc_getter_bp)
app.register_blueprint(newsapi_bp)
GithubLink = "pass"

homepage = f"""
Welcome to my Rexsy Microservice App
Contact me: { GithubLink }
endpoint features:

1. Password Generator to access -> /password/
2. Sentiment Analysis -> /sentiment_analysis/
3. Fear and Greed BTc -> /fng/
4. News API -> /newsapi/
5. Bitcoin Getter -> /btc_getter/
"""


@app.route("/")
def index():
    return render_template("homepage.html")
