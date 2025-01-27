from src.core.user_purchases.application.use_cases.dto import UserPurchaseDto
from src.core.user_purchases.domain.entity.user_purchase import UserPurchaseEntity
from src.core._shared.infraestructure.repository_interface import RepositoryInterface


class CreateUserPurchases():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, input_create: UserPurchaseDto.InputNewUserPurchase) -> None:
        try:
            new_purchase = UserPurchaseEntity(
                name=input_create.name,
                email=input_create.email,
                purchases=input_create.purchases,
            )
        except Exception:
            pass

        self.repository.save(new_purchase)
