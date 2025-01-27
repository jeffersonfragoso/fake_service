from typing import Any


class AdeminReportEntity:
    def __init__(
        self,
        name: str,
        email: str,
        role: str | None = None,
        encrypted_password: str | None = None,
        reports: list[Any] | None = None,
    ):
       self.name = name
       self.email = email
       self.role = role
       self.encrypted_password = encrypted_password
       self.reports: list[Any] | None = reports

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("name cannot be empty")

        if not self.email:
            raise ValueError("email cannot be empty")

        if not self.encrypted_password:
            raise ValueError("password cannot be empty")

        if not self.reports:
            raise ValueError("reports cannot be empty")

    def assign_hole(self):
        self.role = "admin"
