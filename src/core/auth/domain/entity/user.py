
class UserEntity:
    def __init__(
        self,
        username: str,
        encrypted_password: str,
        role: str,
    ):
       self.username = username
       self.encrypted_password = encrypted_password
       self.role = role

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.username:
            raise ValueError("username cannot be empty")

        if not self.encrypted_password:
            raise ValueError("encrypted_password cannot be empty")

        if not self.role:
            raise ValueError("role cannot be empty")

    def is_admin(self) -> bool:
        return bool(self.role == "admin")

    def is_user(self) -> bool:
        return bool(self.role == "user")
