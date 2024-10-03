from flask import Flask
from dotenv import load_dotenv
from flask_mail import Mail
import os

load_dotenv()

app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv("EMAIL")
app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("EMAIL")
mail = Mail(app)
from . import routes
