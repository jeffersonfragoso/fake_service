from fastapi import FastAPI

from src.core._shared.infraestructure.database import create_db_and_tables
from src.entrypoints.web.v1 import v1_routers

def register_routes(app: FastAPI):
    app.include_router(v1_routers)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Fake Api",
        description="Fake Api",
    )

    create_db_and_tables()
    register_routes(app)

    return app
