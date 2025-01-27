from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.core.auth.application.use_cases.is_user import IsUser
from src.core.auth.infraestructure.exceptions import ForbiddenException
from src.core.auth.infraestructure.jwt_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface
from src.core.user_purchases.application.use_cases.get_user_purchases import GetUserPurchases
from src.core.user_purchases.application.use_cases.create_user_purchases import CreateUserPurchases
from src.core.user_purchases.application.use_cases.dto import UserPurchaseDto
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.entrypoints.web.api_exceptions import ApiForbiddenException, ApiInternalServerException
from src.entrypoints.web.v1.dependencies import factory_user_purchase_repository, factory_user_repository
from src.entrypoints.web.v1.user_purchase.schemas import UserPurchasesResponse

user_router = APIRouter()


@user_router.get("/", response_model=UserPurchasesResponse)
async def get(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    user_repository: UserRepositoryInterface = Depends(factory_user_repository),
    purcahse_repository: RepositoryInterface = Depends(factory_user_purchase_repository)
):
    try:
        is_user = IsUser(user_repository)
        is_user.execute(credentials.credentials)

        use_case = GetUserPurchases(purcahse_repository)
        output = use_case.execute()
    except ForbiddenException:
        raise ApiForbiddenException()
    except Exception:
        raise ApiInternalServerException()

    return UserPurchasesResponse(
        message="Hello, user!",
        data=output
    )

@user_router.post("/")
async def post(
    input_create: UserPurchaseDto.InputNewUserPurchase,
    purcahse_repository: RepositoryInterface = Depends(factory_user_purchase_repository)
):
    try:
        use_case = CreateUserPurchases(purcahse_repository)
        use_case.execute(input_create)
    except Exception:
        raise ApiInternalServerException()
