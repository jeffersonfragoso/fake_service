from fastapi import APIRouter

from src.entrypoints.web.v1.health_check.schemas import HealthCheckResponse

health_check_router = APIRouter()


@health_check_router.get("/", response_model=HealthCheckResponse)
async def health_check():
    return HealthCheckResponse(status=200, message="API is healthy")
