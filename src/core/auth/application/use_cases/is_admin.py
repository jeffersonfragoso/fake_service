from src.core.auth.infraestructure.fastapi_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface


class AuthenticationException(BaseException):
    pass


class IsAdmin():
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, token: str) -> None:
        try:
            decoded_token = JwtAuthAdapter.decode_token(token)
            user_name = decoded_token.get("sub", None)
            user_in_db = self.repository.user_of_name(user_name)

            if not user_in_db:
                raise AuthenticationException()

            if not user_in_db.role == "admin":
                raise AuthenticationException()

        except Exception as e:
            pass
