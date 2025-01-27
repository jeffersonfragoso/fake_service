from src.core._shared.infraestructure.database import factory_session
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core.user_purchases.infraestructure.repository.sqlmodel.user_purchase_adapter import SqlModelUserPurchaseRepository
from src.core.admin_reports.infraestructure.repository.sqlmodel.admin_report_adapter import SqlModelAdminReportRepository


def factory_user_purchase_repository() -> RepositoryInterface:
  session = factory_session()
  return SqlModelUserPurchaseRepository(session)

def factory_admin_report_repository() -> RepositoryInterface:
  session = factory_session()
  return SqlModelAdminReportRepository(session)
