import string

with open("password.txt", "r") as f:
    password_list = f.read().splitlines()
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
