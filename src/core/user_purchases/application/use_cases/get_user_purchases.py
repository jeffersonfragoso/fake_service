from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core.user_purchases.application.use_cases.dto import UserPurchaseDto


class GetUserPurchases:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self) -> UserPurchaseDto.OutPutGetUserPurchases | None:
        entity = self.repository.first()

        if entity:
            purchases = [
                UserPurchaseDto.PurchaseDto(**item.__dict__) for item in entity.purchases
            ]

            output = UserPurchaseDto.OutPutGetUserPurchases(
                name=entity.name, email=entity.email, purchases=purchases
            )
            return output
