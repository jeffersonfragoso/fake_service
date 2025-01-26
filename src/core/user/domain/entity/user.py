from typing import Any


class UserEntity:
    def __init__(
        self,
        name: str,
        email: str,
        encrypted_password: str | None = None,
        purchases: list[Any] | None = None,
        reports: list[Any] | None = None,
    ):
       self.name = name
       self.email = email
       self.encrypted_password = encrypted_password
       self.purchases: list[Any] | None= purchases
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

        if not any([self.purchases, self.reports]):
            raise ValueError("email cannot be empty")
