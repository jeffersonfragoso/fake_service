from fastapi import APIRouter

from src.entrypoints.web.v1.admin_reports.schemas import AdminReportsResponse, AdminReport, Report

admin_reports_router = APIRouter()


@admin_reports_router.get("/", response_model=AdminReportsResponse)
async def get():
    return AdminReportsResponse(
        message="Hello, admin!",
        data=AdminReport(
            name="Admin Master",
            email="admin@example.com",
            reports=[
                Report(id=1, title="Monthly Sales", status="Completed"),
                Report(id=2, title="User Activity", status="Pending"),
            ]
        )
    )
