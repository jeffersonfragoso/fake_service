from src.core._shared.exceptions import catch_exceptions
from src.core.auth.infraestructure.exceptions import ForbiddenException
from src.core.auth.infraestructure.jwt_auth_adapter import JwtAuthAdapter
from src.core.auth.infraestructure.repository.sqlmodel.user_adapter import (
    UserRepositoryInterface,
)


class IsAdmin:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    @catch_exceptions(exceptions=[ForbiddenException])
    def execute(self, token: str) -> None:
        decoded_token = JwtAuthAdapter.decode_token(token)
        user_name = decoded_token.get("sub", None)
        user_in_db = self.repository.user_of_name(user_name)

        if not user_in_db:
            raise ForbiddenException(detail="Not found")

        if not user_in_db.role == "admin":
            raise ForbiddenException(detail="Role [admin] not found")
