from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .middlewares import SessionMiddleware
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

# run openssl rand -hex 32 and put it in .env SECRET_KEY
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
assert SECRET_KEY is not None, "Set SECRET_KEY in .env"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static/"), name="static")

templates = Jinja2Templates(directory="app/templates")

from .admin import *  # noqa
from . import routes  # noqa
