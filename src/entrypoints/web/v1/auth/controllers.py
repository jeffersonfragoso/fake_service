from fastapi import APIRouter, Depends

from src.entrypoints.web.v1.auth.schemas import AuthTokenResponse, InputCredentials

auth_router = APIRouter()


@auth_router.post("/", response_model=AuthTokenResponse)
async def token(credentials: InputCredentials = Depends()):
    return AuthTokenResponse(access_token="123", token_type="bearer")
