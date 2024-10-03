import re


def has_ascii_letter(s):
    return bool(re.match(r"^[^a-zA-Z]*[a-zA-Z][^a-zA-Z]*|^[a-zA-Z]+$", s))


def has_digit(s):
    return bool(re.match(r".*\d.*", s))


def has_punctuation(s):
    return bool(re.search(r"[^\w\s]", s))


def password_has_uppercase_or_lowercase(password: str, param: str):
    for p in password:
        if p in param:
            return True  # Password punya paramacter asciiletter minimal 1

    return False
