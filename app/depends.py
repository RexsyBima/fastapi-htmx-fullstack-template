# this file should be used to define dependency functions, wether its function dependencies, or class dependencies
# https://fastapi.tiangolo.com/tutorial/dependencies/
from fastapi import Request
from sqlmodel import select
from .models import session
from .models import User
from .utils import JwtDecodeEncode, Authentication


def get_current_user(request: Request) -> Authentication.TokenAuth | None:
    token = request.session.get("token")
    if not isinstance(token, str):
        return None
    decoded_token = JwtDecodeEncode.decode(token)
    user = session.exec(select(User).where(
        User.username == decoded_token.sub)).first()
    if user:
        return decoded_token
