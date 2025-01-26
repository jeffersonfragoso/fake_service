from src.core.user.application.use_cases.dto import UserDto
from src.core.user.domain.entity.user import UserEntity
from src.core.user.infraestructure.repository_interface import RepositoryInterface


class CreateUser():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, input_create: UserDto.InputNewUser) -> None:
        try:
            new_user = UserEntity(
                name=input_create.name,
                email=input_create.email,
                password=input_create.password,
                purchases=input_create.purchases
            )
        except Exception:
            pass

        self.repository.save(new_user)
