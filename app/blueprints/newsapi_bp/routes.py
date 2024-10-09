from .bp import newsapi_bp
from flask import request
from datetime import datetime
import os
import requests
from .models import NewsApiArticle
from app import mail
from flask_mail import Message


@newsapi_bp.route("/")
def index():
    return "Hello world from newsapi_bp"


@newsapi_bp.route("/get_news", methods=["POST"])
def get_news():
    email = request.form.get("email")
    resp = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv('NEWS_API_KEY')}"
    ).json()
    output = []
    for news in resp["articles"]:
        news = NewsApiArticle(**news)
        if news.url == "https://removed.com":
            continue
        output.append(news)
    news_string_output = ""
    for n in output:
        news_string_output = (
            news_string_output + f"{n.title} - {n.url} - {n.author} - {n.source}" + "\n"
        )
    message = Message(
        f"Top news for today - {datetime.now().strftime('%Y-%m-%d')}",
        recipients=[email if email is not None else "rexsyflaskportofolio@gmail.com"],
        body="""
Dear Rexsy, here is current US top news for today:

        """
        + news_string_output,
    )
    mail.send(message)
    return {"status_code": 200}
