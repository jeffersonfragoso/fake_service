from abc import abstractmethod

from src.core._shared.infraestructure.database import Session
from src.core._shared.infraestructure.orm import UserModel, select
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core.auth.domain.entity.user import UserEntity


class UserRepositoryInterface(RepositoryInterface):
    @abstractmethod
    def user_of_name(self, username: str) -> UserEntity:
        raise NotImplementedError


class SqlModelUserRepository(UserRepositoryInterface):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def save(self, entity: UserEntity):
        try:
            self.session.add(self._to_orm(entity))
            self.commit()
        except Exception as e:
            print(e)
            self.rollback()

    def first(self) -> UserEntity:
        try:
            statement = select(UserModel)
            user_db = self.session.exec(statement).first()

            if user_db:
                return self.to_entity(user_db)
            else:
                return None
        except Exception as e:
            print(e)

    def user_of_name(self, username: str) -> UserEntity | None:
        try:
            statement = select(UserModel).where(UserModel.username == username)
            user_db = self.session.exec(statement).first()

            if user_db:
                return self.to_entity(user_db)
            else:
                return None
        except Exception as e:
            print(e)

    def _to_orm(self, entity: UserEntity):
        user_model = UserModel(
            username=entity.username,
            encrypted_password=entity.encrypted_password,
            role=entity.role,
        )
        return user_model

    def to_entity(self, model: UserModel):
        return UserEntity(
            username=model.username,
            encrypted_password=model.encrypted_password,
            role=model.role,
        )

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
