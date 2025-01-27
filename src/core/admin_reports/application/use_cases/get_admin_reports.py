from src.core._shared.infraestructure.repository_interface import RepositoryInterface
from src.core.admin_reports.application.use_cases.dto import AdminReportDto

class GetAdminReports():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self) -> AdminReportDto.OutPutGetAdminReports:
        try:
            entity = self.repository.first()
            reports = [AdminReportDto.ReportDto(**item.__dict__) for item in entity.reports]

            output = AdminReportDto.OutPutGetAdminReports(
                name=entity.name,
                email=entity.email,
                reports=reports
            )
            return output
        except Exception as e:
            pass
