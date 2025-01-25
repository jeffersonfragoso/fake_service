from fastapi import APIRouter, Depends

from src.core._shared.infraestructure.fastapi_auth_adapter import InputDataToEncode, FastApiAuthAdapter
from src.entrypoints.web.v1.auth.schemas import AuthTokenResponse, InputCredentials

auth_router = APIRouter()


@auth_router.post("/", response_model=AuthTokenResponse)
async def token(credentials: InputCredentials = Depends()):
    role = "user" if credentials.username == "user" else "admin"
    data_to_encode = InputDataToEncode(
        sub=credentials.username,
        role=role
    )
    output = FastApiAuthAdapter.create_access_token(data_to_encode)
    return AuthTokenResponse(
        access_token=output.access_token,
        token_type=output.token_type
    )
