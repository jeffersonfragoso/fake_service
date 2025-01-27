from fastapi import APIRouter, Depends

from src.core._shared.infraestructure.fastapi_auth_adapter import FastApiAuthAdapter
from src.core.admin_reports.application.use_cases.create_admin_reports import CreateAdminReports
from src.core.admin_reports.application.use_cases.dto import AdminReportDto
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.entrypoints.web.v1.admin_report.schemas import AdminReportsResponse
from src.entrypoints.web.v1.dependencies import factory_admin_report_repository
from src.core.admin_reports.application.use_cases.get_admin_reports import GetAdminReports

admin_reports_router = APIRouter()


@admin_reports_router.get(
    "/",
    response_model=AdminReportsResponse,
    dependencies=[Depends(FastApiAuthAdapter.has_role(role="admin"))])
async def admin(
    repository: RepositoryInterface = Depends(factory_admin_report_repository)
):
    use_case = GetAdminReports(repository)
    output = use_case.execute()

    return AdminReportsResponse(
        message="Hello, admin!",
        data=output
    )


@admin_reports_router.post("/")
async def post(
    input_create: AdminReportDto.InputNewAdminReports,
    repository: RepositoryInterface = Depends(factory_admin_report_repository)
):
    use_case = CreateAdminReports(repository)
    use_case.execute(input_create)
