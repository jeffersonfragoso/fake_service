import structlog
from fastapi import APIRouter

from src.entrypoints.web.v1.health_check.schemas import HealthCheckResponse


log = structlog.stdlib.get_logger()
health_check_router = APIRouter()


@health_check_router.get("/", response_model=HealthCheckResponse)
async def health_check():
    log.info("Log HealthCheck")
    return HealthCheckResponse(status=200, message="API is healthy")
