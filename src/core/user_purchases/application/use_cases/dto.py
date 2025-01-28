from pydantic import BaseModel


class UserPurchaseDto:
    class PurchaseDto(BaseModel):
        id: int
        item: str
        price: float

    class OutPutGetUserPurchases(BaseModel):
        name: str
        email: str
        purchases: list["PurchaseDto"]  # noqa: F821

    class InputNewUserPurchase(BaseModel):
        name: str
        email: str
        purchases: list["PurchaseDto"] | None = None  # noqa: F821
