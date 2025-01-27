from typing import List
from sqlmodel import Field, SQLModel, Relationship, select

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
    email: str = Field(index=True)
    encrypted_password: str
    purchases: List[PurchaseModel] = Relationship(back_populates="user")
    reports: List[ReportModel] = Relationship(back_populates="user")
    role: str = Field(index=True)


class SqlModelUserRepository(RepositoryInterface):
    def __init__(self, session: Session):
        super().__init__()
        self.session =  session

    def save(self, user: UserEntity):
        try:
            self.session.add(self._to_orm(user))
            self.commit()
        except Exception as e:
            print(e)
            self.rollback()

    def first_of_role(self, role: str) -> UserEntity:
        try:
            statement = select(UserModel).where(UserModel.role == role)
            user_db = self.session.exec(statement).first()

            if user_db:
                return self.to_entity(user_db)
            else:
                return None
        except Exception as e:
            print(e)

    def _to_orm(self, entity: UserEntity):
        purchases_model = []
        reports_model = []

        if entity.purchases:
            purchases_model = [PurchaseModel(**item.model_dump()) for item in entity.purchases]
        else:
            reports_model = [ReportModel(**item.model_dump()) for item in entity.reports]

        user_model = UserModel(
            name=entity.name,
            email=entity.email,
            role=entity.role,
            encrypted_password=entity.encrypted_password,
            purchases=purchases_model,
            reports=reports_model
        )
        return user_model


    def to_entity(self, model: UserModel):
        return UserEntity(
            name=model.name,
            email=model.email,
            role=model.role,
            purchases=model.purchases,
            reports=model.reports
        )


    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
