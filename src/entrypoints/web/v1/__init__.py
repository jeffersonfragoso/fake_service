from fastapi import APIRouter

from .admin_report.controllers import admin_reports_router
from .auth.controllers import auth_router
from .health_check.controllers import health_check_router
from .user_purchase.controllers import user_router

v1_routers = APIRouter(prefix="/v1")

v1_routers.include_router(health_check_router, prefix="/health", tags=["health"])
v1_routers.include_router(user_router, prefix="/user", tags=["user"])
v1_routers.include_router(admin_reports_router, prefix="/admin", tags=["admin"])
v1_routers.include_router(auth_router, prefix="/token", tags=["auth"])
