# this file should contain utility functions, personally i prefered class based utility functions where each method is live as staticmethod, but function based utility functions are also supported, feel free to modify
# see example below
from app import pwd_context
from .exc import credentials_exception
from pydantic import BaseModel
from jwt.exceptions import InvalidTokenError
from app import ALGORITHM, SECRET_KEY
from datetime import datetime, timedelta
import jwt


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
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password_input: str, hashed_password: str) -> bool:
        return pwd_context.verify(password_input, hashed_password)


class JwtDecodeEncode:
    @staticmethod
    def encode(payload: "Authentication.TokenAuth") -> str:
        return jwt.encode(payload.model_dump(), key=SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    # why the f is this working?? i mean the use of "" to declare class datatype
    def decode(token: str) -> "Authentication.TokenAuth":
        # TODO: maybe check the expiration token here? or it should live as dependency injection?
        try:
            decoded = Authentication.TokenAuth(
                **jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM]))
        except InvalidTokenError:
            raise credentials_exception
        return decoded


class Authentication:
    # How authentication works, please check this video by fireship https://www.youtube.com/watch?v=UBUNrFtufWo
    # Below is cool, but is it necessary?? NOTE :
    class TokenAuth(BaseModel):
        sub: str
        exp: int

    @staticmethod
    def create_access_token(data: dict):
        expired_date = int((datetime.now() + timedelta(days=7)).timestamp())
        data = data.copy()
        data.update({"exp": expired_date})
        return JwtDecodeEncode.encode(Authentication.TokenAuth(**data))

    @staticmethod
    def validate_token(token: str):
        # token = JwtDecodeEncode.decode(token)
        # token.copy()
        raise NotImplementedError
