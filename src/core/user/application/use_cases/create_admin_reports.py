from src.core._shared.infraestructure.crypt import Crypt
from src.core.user.application.use_cases.dto import AdminReportDto
from src.core.user.domain.entity.user import UserEntity
from src.core.user.infraestructure.repository_interface import RepositoryInterface


class CreateAdminReports():
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, input_create: AdminReportDto.InputNewAdminReports) -> None:
        try:
            new_user = UserEntity(
                name=input_create.name,
                email=input_create.email,
                role=input_create.role,
                encrypted_password=Crypt.encrypt_secret(input_create.password),
                reports=input_create.reports
            )
        except Exception as e:
            pass

        self.repository.save(new_user)
