from pydantic import BaseModel


class Purchases(BaseModel):
    id: int
    item: str
    price: float


class User(BaseModel):
    name: str
    email: str
    purchases: list[Purchases]


class UserResponse(BaseModel):
    message: str
    data: User
