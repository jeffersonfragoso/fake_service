from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


class InputDataToEncode(BaseModel):
    sub: str
    role: str


class OutputAccesToken(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AuthInterface(ABC):

    @classmethod
    def create_access_token(self, data: InputDataToEncode) -> OutputAccesToken:
        raise NotImplementedError

    @classmethod
    def has_role(self, role: str, credentials: Any) -> bool:
        raise NotImplementedError
