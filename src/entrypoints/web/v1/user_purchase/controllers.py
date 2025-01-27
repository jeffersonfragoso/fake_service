from fastapi import APIRouter, Depends

from src.core._shared.infraestructure.fastapi_auth_adapter import FastApiAuthAdapter
from src.core.user.application.use_cases.get_user_purchases import GetUserPurchases
from src.core.user.application.use_cases.create_user_purchases import CreateUserPurchases
from src.core.user.application.use_cases.dto import UserPurchaseDto
from src.core.user.infraestructure.repository_interface import RepositoryInterface
from src.entrypoints.web.v1.dependencies import factory_user_repository
from src.entrypoints.web.v1.user_purchase.schemas import UserResponse

user_router = APIRouter()


@user_router.get(
    "/",
    response_model=UserResponse,
    dependencies=[Depends(FastApiAuthAdapter.has_role(role="user"))]
)
async def get(
    repository: RepositoryInterface = Depends(factory_user_repository)
):
    use_case = GetUserPurchases(repository)
    output = use_case.execute()

    return UserResponse(
        message="Hello, user!",
        data=output
    )

@user_router.post("/")
async def post(
    input_create: UserPurchaseDto.InputNewUserPurchase,
    repository: RepositoryInterface = Depends(factory_user_repository)
):
    use_case = CreateUserPurchases(repository)
    use_case.execute(input_create)
