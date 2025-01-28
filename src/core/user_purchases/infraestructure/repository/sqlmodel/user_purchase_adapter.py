import structlog
from src.core._shared.infraestructure.database import Session
from src.core._shared.infraestructure.orm import PurchaseModel, UserPurchaseModel, select
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core.user_purchases.domain.entity.user_purchase import UserPurchaseEntity

log = structlog.stdlib.get_logger()

class SqlModelUserPurchaseRepository(RepositoryInterface):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def save(self, entity: UserPurchaseEntity):
        try:
            self.session.add(self._to_orm(entity))
            self.commit()
        except Exception as e:
            log.error(e)
            self.rollback()

    def first(self) -> UserPurchaseEntity:
        try:
            statement = select(UserPurchaseModel)
            user_db = self.session.exec(statement).first()

            if user_db:
                return self.to_entity(user_db)
            else:
                return None
        except Exception as e:
            log.error(e)

    def _to_orm(self, entity: UserPurchaseEntity):
        purchases_model = [PurchaseModel(**item.model_dump()) for item in entity.purchases]
        user_model = UserPurchaseModel(
            name=entity.name,
            email=entity.email,
            purchases=purchases_model,
        )
        return user_model

    def to_entity(self, model: UserPurchaseModel):
        return UserPurchaseEntity(
            name=model.name,
            email=model.email,
            purchases=model.purchases,
        )

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
