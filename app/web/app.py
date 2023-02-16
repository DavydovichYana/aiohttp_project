from aiohttp.web import Application, run_app as aiohttp_run_app

from app.web.routes import setup_routes

app = Application()

def run_app():
    setup_routes(app)
    aiohttp_run_app(app)