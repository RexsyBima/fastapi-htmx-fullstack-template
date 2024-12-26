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
    # How authentication works, please check this video by fireship https://www.youtube.com/watch?v=UBUNrFtufWo
    user = session.exec(select(User).where(
        User.username == form.username)).first()
    if user and Hashing.verify_password(form.password, user.password):
        token = Authentication.create_access_token(data={"sub": user.username})
        request.session.update({"token": token})  # this just works....
        return HTMLResponse("<div>Login success</div>")
    return HTMLResponse("<div>Login failed</div>")
