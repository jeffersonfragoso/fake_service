from src.core.user.infraestructure.repository_interface import RepositoryInterface
from src.core.user.application.use_cases.dto import UserPurchaseDto

class GetUserPurchases():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self) -> UserPurchaseDto.OutPutGetUserPurchases:
        try:
            entity = self.repository.first_of_role(role="user")
            purchases = [UserPurchaseDto.PurchaseDto(**item.__dict__) for item in entity.purchases]

            output = UserPurchaseDto.OutPutGetUserPurchases(
                name=entity.name,
                email=entity.email,
                purchases=purchases
            )
            return output
        except Exception as e:
            pass
