# this file is used to import all the routes from folder routing/
from . import SECRET_KEY, app
from .routing import pages, htmx, apis
from .middlewares import SessionMiddleware
assert SECRET_KEY is not None, "Set SECRET_KEY in .env"

app.include_router(pages.router)
app.include_router(htmx.router)
app.include_router(apis.router)


# This is used so we can do things with request.session
# You must use .add_middleware method after defining or including all router above
# check here https://github.com/fastapi/fastapi/issues/4746#issuecomment-1141134939
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
