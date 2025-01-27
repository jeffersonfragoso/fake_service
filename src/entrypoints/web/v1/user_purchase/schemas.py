from pydantic import BaseModel

from src.core.user_purchases.application.use_cases.dto import UserPurchaseDto

class UserPurchasesResponse(BaseModel):
    message: str
    data: UserPurchaseDto.OutPutGetUserPurchases | dict
