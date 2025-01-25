import functools
from typing import Annotated
import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.core._shared.infraestructure.auth_interface import AuthInterface, InputDataToEncode, OutputAccesToken


SECRET_KEY = "secret"


class FastApiAuthAdapter(AuthInterface):

    @classmethod
    def _decode_token(cls, token: str) -> dict:
        try:
            return jwt.decode(jwt=token, key=SECRET_KEY, algorithms=["HS256"])
        except jwt.PyJWTError:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

    @classmethod
    def _check_role(
        cls,
        role: str,
        credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]
    ) -> bool:
        token = credentials.credentials
        decoded_token = cls._decode_token(token)
        required_hole = role == decoded_token.get("role", None)
        if not required_hole:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )

    @classmethod
    def create_access_token(cls, data: InputDataToEncode) -> OutputAccesToken:
        access_token = jwt.encode(payload=data.model_dump(), key=SECRET_KEY, algorithm="HS256")
        return OutputAccesToken(
            access_token=access_token
        )

    @classmethod
    def has_role(
        cls,
        role: str,
    ) -> bool:
        return functools.partial(cls._check_role, role)
