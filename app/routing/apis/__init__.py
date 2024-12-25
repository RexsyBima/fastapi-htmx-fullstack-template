from fastapi import APIRouter

router = APIRouter(prefix="/apis", tags=["apis"])

from . import delete, get, post, put, patch  # noqa
