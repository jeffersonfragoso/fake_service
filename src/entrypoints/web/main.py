from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from src.core._shared.infraestructure.database import create_db_and_tables, seed_database
from src.entrypoints.web.api_exceptions import CustomHttpErrorException
from src.entrypoints.web.v1 import v1_routers


async def custom_exception_handler(_: Request, exc: CustomHttpErrorException) -> JSONResponse:
    print(f"[Web Api exception handler] The execution resulted in an error {str(exc)}")
    return JSONResponse(**exc.as_json())


def register_routes(app: FastAPI):
    app.include_router(v1_routers)


def register_exceptions(app: FastAPI):
    app.add_exception_handler(CustomHttpErrorException, custom_exception_handler)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Fake Api",
        description="Fake Api",
    )

    create_db_and_tables()
    seed_database()
    register_routes(app)
    register_exceptions(app)

    return app
