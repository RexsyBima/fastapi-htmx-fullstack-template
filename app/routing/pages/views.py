from . import router
from app import templates
from fastapi import Request


@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="pages/homepage.html")
