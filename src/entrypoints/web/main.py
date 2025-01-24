from fastapi import FastAPI

from src.entrypoints.web.v1 import v1_routers

def register_routes(app: FastAPI):
    app.include_router(v1_routers)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Fake Api",
        description="Fake Api",
    )

    register_routes(app)

    return app
