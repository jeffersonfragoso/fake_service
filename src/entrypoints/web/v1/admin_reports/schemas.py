from pydantic import BaseModel


class Report(BaseModel):
    id: int
    title: str
    status: str


class AdminReport(BaseModel):
    name: str
    email: str
    reports: list[Report]


class AdminReportsResponse(BaseModel):
    message: str
    data: AdminReport
