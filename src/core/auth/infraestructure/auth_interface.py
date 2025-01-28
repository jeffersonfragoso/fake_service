from abc import ABC, abstractmethod

from src.core.auth.application.use_cases.dto import AuthDto


class AuthInterface(ABC):

    @classmethod
    @abstractmethod
    def create_access_token(self, data: AuthDto.InputDataToEncode) -> AuthDto.OutputAccesToken:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def decode_token(self, token: str) -> dict:
        raise NotImplementedError
