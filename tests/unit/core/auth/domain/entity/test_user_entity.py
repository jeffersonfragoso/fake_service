import pytest
from src.core.auth.domain.entity.user import UserEntity

stub_user = UserEntity(
  username="user",
  encrypted_password="123",
  role="user"
)

stub_admin = UserEntity(
  username="admin",
  encrypted_password="123",
  role="admin"
)

class TestUserEntity:
    def test_is_user_role(self):
        """
        Dado um usuário com o papel "user"
        Quando solicitar a verificação de papel
        Então deve retornar True para "is_user"
        E deve retornar "False" para "is_admin"
        """
        assert stub_user.is_user() is True
        assert stub_user.is_admin() is False

    def test_is_admin_role(self):
        """
        Dado um usuário com o papel "admin"
        Quando solicitar a verificação de papel
        Então deve retornar True para "is_admin"
        E deve retornar "False" para "is_user"
        """
        assert stub_admin.is_admin() is True
        assert stub_admin.is_user() is False

    def test_username_cannot_be_empty(self):
        """
        Dado um usuário
        Quando não for informado o campo "username"
        Então deve retornar lançar um ValueError com a mensagem "username cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            UserEntity(
                username=None,
                encrypted_password="123",
                role="user"
            )

        assert str(exc_info.value) == "username cannot be empty"

    def test_encrypted_password_cannot_be_empty(self):
        """
        Dado um usuário
        Quando não for informado o campo "encrypted_password"
        Então deve retornar lançar um ValueError com a mensagem "encrypted_password cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            UserEntity(
                username="user",
                encrypted_password=None,
                role="user"
            )

        assert str(exc_info.value) == "encrypted_password cannot be empty"

    def test_role_cannot_be_empty(self):
        """
        Dado um usuário
        Quando não for informado o campo "role"
        Então deve retornar lançar um ValueError com a mensagem "role cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            UserEntity(
                username="user",
                encrypted_password="123",
                role=None
            )

        assert str(exc_info.value) == "role cannot be empty"
