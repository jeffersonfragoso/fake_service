import pytest
from src.core.admin_reports.domain.entity.admin_report import AdminReportEntity
from src.core.admin_reports.application.use_cases.dto import AdminReportDto


class TestAdminReportEntity:
    def test_username_cannot_be_empty(self):
        """
        Dado solicitar criar um novo Admin Report
        Quando não for informado o campo "name"
        Então deve lançar um ValueError com a mensagem "name cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            AdminReportEntity(
                name=None,
                email="admin@example.com",
                reports=[]
            )

        assert str(exc_info.value) == "name cannot be empty"

    def test_encrypted_password_cannot_be_empty(self):
        """
        Dado solicitar criar um novo Admin Report
        Quando não for informado o campo "email"
        Então deve lançar um ValueError com a mensagem "email cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            AdminReportEntity(
                name="Admin Master",
                email=None,
                reports=[]
            )

        assert str(exc_info.value) == "email cannot be empty"

    def test_role_cannot_be_empty(self):
        """
        Dado solicitar criar um novo Admin Report
        Quando não for informado o campo "reports"
        Então deve retornar lançar um ValueError com a mensagem "reports cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            AdminReportEntity(
                name="Admin Master",
                email="admin@example.com",
                reports=None
            )

        assert str(exc_info.value) == "reports cannot be empty"
