# this file should contain utility functions, personally i prefered class based utility functions where each method is live as staticmethod, but function based utility functions are also supported, feel free to modify

# see example below
from app import pwd_context


class Utils1:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subs(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


class Hashing:
    # check how fastapi implement hashing in this
    # https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords
    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password_input: str, hashed_password: str):
        return pwd_context.verify(password_input, hashed_password)
