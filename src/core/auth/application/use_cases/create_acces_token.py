from src.core._shared.exceptions import catch_exceptions
from src.core._shared.infraestructure.crypt import Crypt
from src.core.auth.application.use_cases.dto import AuthDto
from src.core.auth.infraestructure.exceptions import UnauthorizedException
from src.core.auth.infraestructure.jwt_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import (
    UserRepositoryInterface,
)


class AuthenticationException(BaseException):
    pass


class CreateAccesToken:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    @catch_exceptions(exceptions=[UnauthorizedException])
    def execute(self, credentials: AuthDto.InputCredentials) -> AuthDto.OutputAccesToken:
        user_in_db = self.repository.user_of_name(credentials.username)

        if not user_in_db:
            raise UnauthorizedException(detail="Not found")

        Crypt.verify_secret(credentials.password, user_in_db.encrypted_password)

        data_to_encode = AuthDto.InputDataToEncode(
            sub=credentials.username,
        )

        access_token = JwtAuthAdapter.create_access_token(data_to_encode)
        return AuthDto.OutputAccesToken(access_token=access_token)
