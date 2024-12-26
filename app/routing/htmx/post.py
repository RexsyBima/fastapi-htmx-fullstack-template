from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Depends, Response
from app.models import User, session
from app.utils import Hashing, Authentication
from sqlmodel import select
from . import router


@router.post("/auth/login")
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response, request: Request):
    user = session.exec(select(User).where(
        User.username == form.username)).first()
    if user and Hashing.verify_password(form.password, user.password):
        token = Authentication.create_access_token(data={"sub": user.username})
        print(token)
        # response.set_cookie(key="token", value=token, httponly=True)
        request.session.update({"token": token})
        return HTMLResponse("<div>Login success</div>")

    return HTMLResponse("<div>Login failed</div>")
