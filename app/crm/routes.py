from aiohttp.abc import Application

from app.crm.views import index


def setup_routes(app: Application):
    app.router.add_get('/index', index)