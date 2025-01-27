from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.core.auth.infraestructure.exceptions import ForbiddenException
from src.core.auth.infraestructure.jwt_auth_adapter import JwtAuthAdapter
from src.core.admin_reports.application.use_cases.create_admin_reports import CreateAdminReports
from src.core.admin_reports.application.use_cases.dto import AdminReportDto
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface
from src.entrypoints.web.api_exceptions import ApiForbiddenException, ApiInternalServerException
from src.entrypoints.web.v1.admin_report.schemas import AdminReportsResponse
from src.entrypoints.web.v1.dependencies import factory_admin_report_repository, factory_user_repository
from src.core.admin_reports.application.use_cases.get_admin_reports import GetAdminReports
from src.core.auth.application.use_cases.is_admin import IsAdmin

admin_reports_router = APIRouter()


@admin_reports_router.get("/", response_model=AdminReportsResponse)
async def admin(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    user_repository: UserRepositoryInterface = Depends(factory_user_repository),
    report_repository: RepositoryInterface = Depends(factory_admin_report_repository)
):
    try:
        is_admin = IsAdmin(user_repository)
        is_admin.execute(credentials.credentials)

        use_case = GetAdminReports(report_repository)
        output = use_case.execute()
    except ForbiddenException:
        raise ApiForbiddenException()
    except Exception:
        raise ApiInternalServerException()

    return AdminReportsResponse(
        message="Hello, admin!",
        data=output if output else {}
    )


@admin_reports_router.post("/")
async def post(
    input_create: AdminReportDto.InputNewAdminReports,
    report_repository: RepositoryInterface = Depends(factory_admin_report_repository)
):
    try:
        use_case = CreateAdminReports(report_repository)
        use_case.execute(input_create)
    except Exception:
        raise ApiInternalServerException()
