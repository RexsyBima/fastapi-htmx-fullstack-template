# This file is used to generate superadmin account into the database
from dotenv import load_dotenv
import os
from app.models import User, session
from app.enums import UserRole
from app.utils import Hashing

load_dotenv()

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
assert ADMIN_PASSWORD is not None, "Set ADMIN_PASSWORD in .env"

password = input("Login: ")
if password != ADMIN_PASSWORD:
    raise Exception("Wrong password")

username = input("Input username : ")
password = input("Input admin password: ")
# TODO: implement hashing in utils.py
pw_hash = Hashing.hash_password(password)


user = User(username=username, email="superadmin@gmail.com",
            password=pw_hash, role=UserRole.ADMIN)

session.add(user)
session.commit()
