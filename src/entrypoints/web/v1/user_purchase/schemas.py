from pydantic import BaseModel

from src.core.user.application.use_cases.dto import UserPurchaseDto

class UserResponse(BaseModel):
    message: str
    data: UserPurchaseDto.OutPutGetUserPurchases
