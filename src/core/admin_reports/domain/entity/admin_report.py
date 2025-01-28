from typing import Any


class AdminReportEntity:
    def __init__(
        self,
        name: str,
        email: str,
        reports: list[Any],
    ):
        self.name = name
        self.email = email
        self.reports: list[Any] | None = reports
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("name cannot be empty")

        if not self.email:
            raise ValueError("email cannot be empty")

        if not self.reports:
            raise ValueError("reports cannot be empty")
