from . import router
from typing import Annotated
from app import templates
from fastapi import Depends
from app.depends import get_current_user
from app.models import User
from app.utils import JwtDecodeEncode
from app.utils import Authentication

from fastapi import Request, Response


@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="pages/homepage.html")


@router.get("/auth/login")
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="pages/login.html")


@router.get("/get_token")
# TODO: implement this somewhere else?
async def get_token(request: Request, user: Annotated[Authentication.TokenAuth, Depends(get_current_user)]):
    return user


@router.get("/del_token")
async def del_token(request: Request, ):
    request.session.pop("token")
    return Response(status_code=200)
