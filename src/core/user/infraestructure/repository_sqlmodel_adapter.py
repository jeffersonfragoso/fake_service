from typing import List
from sqlmodel import Field, SQLModel, Relationship

from src.core.user.infraestructure.repository_interface import RepositoryInterface
from src.core._shared.infraestructure.database import Session
from src.core.user.domain.entity.user import UserEntity


class ReportModel(SQLModel, table=True):
    __tablename__ = "report"

    id: int = Field(primary_key=True)
    title: str
    status: str
    user_id: int = Field(foreign_key="user.id")
    user: "UserModel" = Relationship(back_populates="reports")


class PurchaseModel(SQLModel, table=True):
    __tablename__ = "purchase"

    id: int = Field(primary_key=True)
    item: str
    price: float
    user_id: int = Field(foreign_key="user.id")
    user: "UserModel" = Relationship(back_populates="purchases")


class UserModel(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    hashed_password: str
    purchases: List[PurchaseModel] | None = Relationship(back_populates="user")
    reports: List[ReportModel] | None = Relationship(back_populates="user")


class SqlModelUserRepository(RepositoryInterface):
    def __init__(self, session: Session):
        super().__init__()
        self.session =  session

    def save(self, user: UserEntity):
        try:
            self.session.add(self._to_orm(user))
            self.commit()
        except Exception:
            self.rollback()


    def list(self, user: UserEntity) -> None:
        raise NotImplementedError

    def _to_orm(self, entity: UserEntity):
        purchases = [PurchaseModel(**item.model_dump()) for item in entity.purchases]
        user_model = UserModel(
            name=entity.name,
            email=entity.email,
            hashed_password=entity.password,
            purchases=purchases
        )
        return user_model

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
