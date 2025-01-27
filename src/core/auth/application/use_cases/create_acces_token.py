from src.core._shared.infraestructure.crypt import Crypt
from src.core.auth.application.use_cases.dto import AuthDto
from src.core.auth.infraestructure.fastapi_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface


class AuthenticationException(BaseException):
    pass


class CreateAccesToken():
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, credentials: AuthDto.InputCredentials) -> AuthDto.OutputAccesToken:
        try:
            user_in_db = self.repository.user_of_name(credentials.username)

            if not user_in_db:
                raise AuthenticationException()

            if not Crypt.verify_secret(credentials.password, user_in_db.encrypted_password):
                raise AuthenticationException()

            data_to_encode = AuthDto.InputDataToEncode(
                sub=credentials.username,
            )

            access_token = JwtAuthAdapter.create_access_token(data_to_encode)
            return AuthDto.OutputAccesToken(access_token=access_token)
        except Exception as e:
            pass
