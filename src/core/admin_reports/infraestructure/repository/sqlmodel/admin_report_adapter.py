from src.core._shared.infraestructure.orm import AdminReportModel, ReportModel, select
from src.core.admin_reports.domain.entity.admin_report import AdeminReportEntity
from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core._shared.infraestructure.database import Session


class SqlModelAdminReportRepository(RepositoryInterface):
    def __init__(self, session: Session):
        super().__init__()
        self.session =  session

    def save(self, entity: AdeminReportEntity):
        try:
            self.session.add(self._to_orm(entity))
            self.commit()
        except Exception as e:
            print(e)
            self.rollback()

    def first(self) -> AdeminReportEntity:
        try:
            statement = select(AdminReportModel).where(AdminReportModel.role == "admin")
            user_db = self.session.exec(statement).first()

            if user_db:
                return self.to_entity(user_db)
            else:
                return None
        except Exception as e:
            print(e)

    def _to_orm(self, entity: AdeminReportEntity):
        reports_model = [ReportModel(**item.model_dump()) for item in entity.reports]

        user_model = AdminReportModel(
            name=entity.name,
            email=entity.email,
            role=entity.role,
            encrypted_password=entity.encrypted_password,
            reports=reports_model
        )
        return user_model

    def to_entity(self, model: AdminReportModel):
        return AdeminReportEntity(
            name=model.name,
            email=model.email,
            role=model.role,
            reports=model.reports
        )

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
