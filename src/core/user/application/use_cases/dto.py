
from pydantic import BaseModel


class UserDto:
    class PurchaseDto(BaseModel):
        id: int
        item: str
        price: float

    class ReportDto(BaseModel):
        id: int
        title: str
        status: str

    class OutPutGetUser(BaseModel):
        name: str
        email: str
        purchases: list["PurchaseDto"]

    class InputNewUser(BaseModel):
        name: str
        email: str
        password: str
        purchases: list["PurchaseDto"] | None = None
        reports: list["ReportDto"] | None = None
