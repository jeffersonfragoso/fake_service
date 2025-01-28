import pytest
from src.core.user_purchases.domain.entity.user_purchase import UserPurchaseEntity


class TestUserPurchaseEntity:
    def test_name_cannot_be_empty(self):
        """
        Dado solicitar criar um novo User Purchase
        Quando não for informado o campo "name"
        Então deve lançar um ValueError com a mensagem "name cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            UserPurchaseEntity(
                name=None,
                email="john@example.com",
                purchases=[{}]
            )

        assert str(exc_info.value) == "name cannot be empty"

    def test_email_cannot_be_empty(self):
        """
        Dado solicitar criar um novo User Purchase
        Quando não for informado o campo "email"
        Então deve lançar um ValueError com a mensagem "email cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            UserPurchaseEntity(
                name="John Doe",
                email=None,
                purchases=[{}]
            )

        assert str(exc_info.value) == "email cannot be empty"

    def test_purchases_cannot_be_empty(self):
        """
        Dado solicitar criar um novo User Purchase
        Quando não for informado o campo "purchases"
        Então deve retornar lançar um ValueError com a mensagem "purchases cannot be empty"
        """
        with pytest.raises(ValueError) as exc_info:
            UserPurchaseEntity(
                name="John Doe",
                email="john@example.com",
                purchases=None
            )

        assert str(exc_info.value) == "purchases cannot be empty"
