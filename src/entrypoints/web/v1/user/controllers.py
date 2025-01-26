from fastapi import APIRouter, Depends

from src.core._shared.infraestructure.fastapi_auth_adapter import FastApiAuthAdapter
from src.core.user.application.use_cases.get_user import GetUser
from src.core.user.application.use_cases.create_user import CreateUser
from src.core.user.application.use_cases.dto import UserDto
from src.entrypoints.web.v1.user.schemas import UserResponse

user_router = APIRouter()


@user_router.get(
    "/",
    response_model=UserResponse,
    dependencies=[Depends(FastApiAuthAdapter.has_role(role="user"))]
)
async def get():
    use_case = GetUser()
    output = use_case.execute()

    return UserResponse(
        message="Hello, user!",
        data=output
    )

@user_router.post("/")
async def post(input_create: UserDto.InputCreateUser):
    use_case = CreateUser()
    use_case.execute(input_create)
