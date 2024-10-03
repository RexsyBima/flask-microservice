from .bp import sentiment_analysis_bp as sa_bp
from textblob import TextBlob
from flask import request

testimonial = TextBlob("I kinda like Python")
print(testimonial.sentiment, testimonial.sentiment.polarity)


@sa_bp.route("/")
def index():
    return "Hello World from sentimen analysis"


@sa_bp.route("/do_analysis", methods=["POST"])
def do_analysis():
    text = request.form.get("text")
    testimonial = TextBlob(text)
    if testimonial.sentiment.polarity > 0:
        return {"sentiment": "positive"}
    elif testimonial.sentiment.polarity < 0:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}
