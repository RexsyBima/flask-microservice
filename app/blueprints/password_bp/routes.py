from .bp import password_bp
from . import password_list, lowercase, uppercase
from flask import render_template, request, jsonify
from app.utils import (
    has_digit,
    has_punctuation,
    password_has_uppercase_or_lowercase,
)
import random
import string
import re


@password_bp.route("/")
def index():
    return render_template("password_bp/helloworld.html")  # return index.html


@password_bp.route("/get_random_password")
def get_random_password():
    password = ""
    while True:
        for i in range(random.randint(8, 16)):
            password += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=-{};:'<>,./?])[A-Za-z\d!@#$%^&*()_+=-{};:'<>,./?]+$"
        if bool(re.search(pattern, password)):
            return jsonify(
                output={"password": password, "length": len(password)}, staus=200
            )  # return password
        else:
            password = ""


@password_bp.route("/check_password", methods=["POST"])
def check_password():
    password = request.form.get("password")
    check1 = has_digit(password)
    check2 = password_has_uppercase_or_lowercase(password, lowercase)
    check3 = has_punctuation(password)
    check4 = password_has_uppercase_or_lowercase(password, uppercase)
    status = [check1, check2, check3, check4]
    status = [s for s in status if s is True]
    if len(password) < 8:
        return {"password": "very weak"}
    elif len(status) == 4:
        return {"password": "strong"}
    elif len(status) == 3:
        return {"password": "medium"}
    elif len(status) == 2:
        return {"password": "weak"}
    else:
        return {"password": "very weak"}


@password_bp.route("/password_common_checker", methods=["POST"])
def common_password():
    password = request.form.get("password")
    if password in password_list:
        return {"is_password_common": True}
    else:
        return {"is_password_common": False}
