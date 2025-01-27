from src.core._shared.exceptions import catch_exceptions
from src.core.auth.infraestructure.exceptions import ForbiddenException
from src.core.auth.infraestructure.jwt_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import UserRepositoryInterface


class IsUser():
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    @catch_exceptions(exceptions=[ForbiddenException])
    def execute(self, token: str) -> None:
        decoded_token = JwtAuthAdapter.decode_token(token)
        user_name = decoded_token.get("sub", None)
        user_entity = self.repository.user_of_name(user_name)

        if not user_entity:
            raise ForbiddenException(detail="Not found")

        if not user_entity.is_user():
            raise ForbiddenException(detail="Role [user] not found")
