from fastapi import APIRouter, Depends

from src.core.auth.infraestructure.exceptions import UnauthorizedException
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface
from src.entrypoints.web.api_exceptions import ApiAuthenticationException, ApiInternalServerException
from src.entrypoints.web.v1.auth.schemas import AuthTokenResponse, InputCredentials
from src.core.auth.application.use_cases.create_acces_token import CreateAccesToken
from src.entrypoints.web.v1.dependencies import factory_user_repository

auth_router = APIRouter()


@auth_router.post("/", response_model=AuthTokenResponse)
async def token(
    credentials: InputCredentials = Depends(),
    repository: UserRepositoryInterface = Depends(factory_user_repository)
):
    try:
        use_case = CreateAccesToken(repository)
        output = use_case.execute(credentials)
        return AuthTokenResponse(**output.model_dump())
    except UnauthorizedException:
        raise ApiAuthenticationException()
    except Exception:
        raise ApiInternalServerException()
