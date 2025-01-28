from pydantic import BaseModel


class AdminReportDto:

    class ReportDto(BaseModel):
        id: int
        title: str
        status: str

    class OutPutGetAdminReports(BaseModel):
        name: str
        email: str
        reports: list["ReportDto"]  # noqa: F821

    class InputNewAdminReports(BaseModel):
        name: str
        email: str
        reports: list["ReportDto"] | None = None  # noqa: F821
