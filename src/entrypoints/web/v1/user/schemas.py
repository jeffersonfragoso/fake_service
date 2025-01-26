from pydantic import BaseModel

from src.entrypoints.web.v1.admin_reports.schemas import Report


class PurchaseSchema(BaseModel):
    id: int
    item: str
    price: float


class UserSchema(BaseModel):
    name: str
    email: str
    purchases: list[PurchaseSchema]


class UserResponse(BaseModel):
    message: str
    data: UserSchema

class InputCreateUser(BaseModel):
    name: str
    email: str
    password: str
    purchases: list[PurchaseSchema] | None = None
    reports: list[Report] | None = None
