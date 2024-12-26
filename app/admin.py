# for using sqladmin, check how to implement here,
# https: // aminalaee.dev/sqladmin/
# note you should have database in order to use sqladmin (obviously)

import os
from typing import Any
from sqladmin import authentication
from .enums import UserRole
from .utils import Hashing
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from sqladmin import Admin, ModelView
from . import app
from sqlmodel import select
from .models import engine, User, session


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        assert isinstance(
            password, str), "Invalid password datatype, it should be a string"
        user = session.exec(select(User).where(
            User.username == username)).first()
        assert isinstance(user, User), "User not found"
        if user.role != UserRole.ADMIN:
            return False
        if Hashing.verify_password(password, user.password):
            # TODO: do jwt authentication??
            request.session.update({"token": user.username})
            return True
        else:
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        # TODO: do jwt authentication??
        token = request.session.get("token")
        user = session.exec(select(User).where(User.username == token)).first()
        if user is None:
            return False
        if token is None or user.role != UserRole.ADMIN:
            return False
        return True


secret_key = os.getenv("SECRET_KEY")
assert secret_key is not None, "Set SECRET_KEY in .env"
authentication_backend = AdminAuth(secret_key=secret_key)
admin = Admin(app, engine, authentication_backend=authentication_backend)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username,
                   User.email, User.role]  # type: ignore


admin.add_view(UserAdmin)
