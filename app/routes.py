# this file is used to import all the routes from folder routing/
from . import app
from .routing import pages, htmx, apis

app.include_router(pages.router)
app.include_router(htmx.router)
app.include_router(apis.router)
