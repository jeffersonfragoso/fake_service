import jwt

from src.core.auth.application.use_cases.dto import AuthDto
from src.core.auth.infraestructure.auth_interface import AuthInterface
from src.core.auth.infraestructure.exceptions import ForbiddenException, UnauthorizedException

SECRET_KEY = "secret"


class JwtAuthAdapter(AuthInterface):

    @classmethod
    def decode_token(cls, token: str) -> dict:
        try:
            return jwt.decode(jwt=token, key=SECRET_KEY, algorithms=["HS256"])
        except Exception as e:
            raise ForbiddenException(detail=str(e))

    @classmethod
    def create_access_token(cls, data: AuthDto.InputDataToEncode) -> str:
        try:
            return jwt.encode(payload=data.model_dump(), key=SECRET_KEY, algorithm="HS256")
        except Exception as e:
            raise UnauthorizedException(detail=str(e))
