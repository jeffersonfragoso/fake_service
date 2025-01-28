from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi.middleware.cors import CORSMiddleware
import structlog


from src.core._shared.config import get_settings
from src.core._shared.infraestructure.database import create_db_and_tables, seed_database
from src.core._shared.infraestructure.struct_log import setup_logging
from src.entrypoints.web.api_exceptions import CustomHttpErrorException
from src.entrypoints.web.middlewares.access_logger import RequestAccessLoggerMiddleware
from src.entrypoints.web.middlewares.timer import RequestTimeMiddleware
from src.entrypoints.web.v1 import v1_routers


LOG_LEVEL = get_settings().LOG_LEVEL
ENABLE_JSON_LOGS = get_settings().ENABLE_JSON_LOGS
log = structlog.stdlib.get_logger()


async def custom_exception_handler(_: Request, exc: CustomHttpErrorException) -> JSONResponse:
    log.error(f"[Web Api exception handler] The execution resulted in an error {str(exc)}")
    return JSONResponse(**exc.as_json())


def register_routes(app: FastAPI):
    app.include_router(v1_routers)


def register_exceptions(app: FastAPI):
    app.add_exception_handler(CustomHttpErrorException, custom_exception_handler)


def register_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["X-Request-ID"],
        expose_headers=["X-Request-ID"],
    )
    app.add_middleware(
        CorrelationIdMiddleware,
        header_name="X-Request-ID",
        update_request_header=True,
    )
    app.add_middleware(RequestTimeMiddleware)
    app.add_middleware(RequestAccessLoggerMiddleware)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging(LOG_LEVEL, ENABLE_JSON_LOGS)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="Fake Api",
        description="Fake Api",
        lifespan=lifespan
    )

    create_db_and_tables()
    seed_database()
    register_routes(app)
    register_exceptions(app)
    register_middlewares(app)

    return app
