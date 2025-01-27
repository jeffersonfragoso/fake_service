from typing import Any


class UserPurchaseEntity:
    def __init__(
        self,
        name: str,
        email: str,
        purchases: list[Any] | None = None,
    ):
       self.name = name
       self.email = email
       self.purchases: list[Any] | None= purchases

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("name cannot be empty")
        if not self.email:
            raise ValueError("email cannot be empty")
        if not self.purchases:
            raise ValueError("purchases cannot be empty")
