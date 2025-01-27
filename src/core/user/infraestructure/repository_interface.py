from abc import ABC, abstractmethod
from typing import Any


class RepositoryInterface(ABC):
    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def save(self, entity) -> None:
        raise NotImplementedError

    @abstractmethod
    def first_of_role(self, role: str) -> Any:
        raise NotImplementedError
