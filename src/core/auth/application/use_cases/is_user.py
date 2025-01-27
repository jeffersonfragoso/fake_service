from src.core.auth.infraestructure.fastapi_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface


class AuthenticationException(BaseException):
    pass


class IsUser():
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, token: str) -> None:
        try:
            decoded_token = JwtAuthAdapter.decode_token(token)
            user_name = decoded_token.get("sub", None)
            user_entity = self.repository.user_of_name(user_name)

            if not user_entity:
                raise AuthenticationException()

            if not user_entity.is_user():
                raise AuthenticationException()

        except Exception as e:
            pass
