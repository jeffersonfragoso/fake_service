from src.core._shared.infraestructure.database import factory_session
from src.core.user.infraestructure.repository_interface import RepositoryInterface
from src.core.user.infraestructure.repository_sqlmodel_adapter import SqlModelUserRepository


def factory_user_repository() -> RepositoryInterface:
  session = factory_session()
  return SqlModelUserRepository(session)
