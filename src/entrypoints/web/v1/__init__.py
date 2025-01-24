from fastapi import APIRouter

from .health_check.controllers import health_check_router

v1_routers = APIRouter(prefix="/v1")

v1_routers.include_router(health_check_router, prefix="/health", tags=["health"])
