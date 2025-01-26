from pydantic import BaseModel

from src.core.user.application.use_cases.dto import UserDto

class UserResponse(BaseModel):
    message: str
    data: UserDto.OutPutGetUser
