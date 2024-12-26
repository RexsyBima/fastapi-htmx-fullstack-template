# this file is used to import all the routes from folder routing/
from . import SECRET_KEY, app
from .routing import pages, htmx, apis
from .middlewares import SessionMiddleware
assert SECRET_KEY is not None, "Set SECRET_KEY in .env"

app.include_router(pages.router)
app.include_router(htmx.router)
app.include_router(apis.router)


app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
