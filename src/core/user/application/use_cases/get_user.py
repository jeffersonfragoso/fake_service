from src.core.user.infraestructure.repository_interface import RepositoryInterface
from src.core.user.application.use_cases.dto import UserDto

class GetUser():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self) -> UserDto.OutPutGetUser:
        try:
            entity = self.repository.first()
            purchases = [UserDto.PurchaseDto(**item.__dict__) for item in entity.purchases]

            output = UserDto.OutPutGetUser(
                name=entity.name,
                email=entity.email,
                purchases=purchases
            )

            return output
        except Exception as e:
            pass
