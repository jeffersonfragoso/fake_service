from src.core._shared.infraestructure.crypt import Crypt
from src.core.admin_reports.application.use_cases.dto import AdminReportDto
from src.core.admin_reports.domain.entity.admin_report import AdminReportEntity
from src.core._shared.infraestructure.repository_interface import RepositoryInterface


class CreateAdminReports():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, input_create: AdminReportDto.InputNewAdminReports) -> None:
        new_report = AdminReportEntity(
            name=input_create.name,
            email=input_create.email,
            reports=input_create.reports
        )
        self.repository.save(new_report)
