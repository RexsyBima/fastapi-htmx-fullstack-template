from fastapi import APIRouter

router = APIRouter(prefix="/htmx", tags=["htmx"])

from . import delete, get, post, put, patch  # noqa
