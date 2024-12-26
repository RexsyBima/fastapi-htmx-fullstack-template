# for using sqladmin, check how to implement here, https://aminalaee.dev/sqladmin/
# note you should have database in order to use sqladmin (obviously)


from datetime import datetime, timedelta
from .models import engine, User, session
from sqlmodel import select
from . import app
from sqladmin import Admin, ModelView
from starlette.requests import Request
from sqladmin.authentication import AuthenticationBackend
from .utils import Hashing, JwtDecodeEncode, Authentication
from .enums import UserRole
from app import SECRET_KEY
assert SECRET_KEY is not None, "Set SECRET_KEY in .env"


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        assert isinstance(
            password, str), "Invalid password datatype, it should be a string"
        user = session.exec(select(User).where(
            User.username == username)).first()
        if user is None or user.role != UserRole.ADMIN:
            return False
        if Hashing.verify_password(password, user.password):
            exp_date = int(
                (datetime.now() + timedelta(minutes=30)).timestamp())
            payload = Authentication.TokenAuth(
                # NOTE: you could do that, but why, why would you do that?
                **{"sub": user.username, "exp": exp_date})
            token = JwtDecodeEncode.encode(payload)
            request.session.update({"token": token, })
            return True
        else:
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not isinstance(token, str):
            return False
        decoded_token = JwtDecodeEncode.decode(token)
        # log out user if token expired
        if int(datetime.now().timestamp()) > decoded_token.exp:
            request.session.clear()
            return False
        user = session.exec(select(User).where(
            User.username == decoded_token.sub)).first()
        if token is None or user is None or user.role != UserRole.ADMIN:
            return False
        return True


authentication_backend = AdminAuth(secret_key=SECRET_KEY)
admin = Admin(app, engine, authentication_backend=authentication_backend)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username,
                   User.email, User.role]  # type: ignore


admin.add_view(UserAdmin)
