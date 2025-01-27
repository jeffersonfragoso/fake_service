
from pydantic import BaseModel


class AdminReportDto:

    class ReportDto(BaseModel):
        id: int
        title: str
        status: str

    class OutPutGetAdminReports(BaseModel):
        name: str
        email: str
        reports: list["ReportDto"]

    class InputNewAdminReports(BaseModel):
        name: str
        email: str
        password: str
        reports: list["ReportDto"] | None = None
