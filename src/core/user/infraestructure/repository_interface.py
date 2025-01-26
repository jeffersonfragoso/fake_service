from abc import ABC, abstractmethod


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
    def list(self, entity) -> None:
        raise NotImplementedError
