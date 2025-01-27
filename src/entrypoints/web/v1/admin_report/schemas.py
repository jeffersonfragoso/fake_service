from pydantic import BaseModel
from src.core.user.application.use_cases.dto import AdminReportDto


class AdminReportsResponse(BaseModel):
    message: str
    data: AdminReportDto.OutPutGetAdminReports
