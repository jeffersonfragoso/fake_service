
from pydantic import BaseModel


class UserPurchaseDto:
    class PurchaseDto(BaseModel):
        id: int
        item: str
        price: float

    class OutPutGetUserPurchases(BaseModel):
        name: str
        email: str
        purchases: list["PurchaseDto"]

    class InputNewUserPurchase(BaseModel):
        name: str
        email: str
        password: str
        purchases: list["PurchaseDto"] | None = None


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
