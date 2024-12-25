from fastapi import APIRouter

router = APIRouter(tags=["pages"])

from . import views  # noqa
