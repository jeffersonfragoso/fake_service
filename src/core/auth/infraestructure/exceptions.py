from dataclasses import dataclass
from src.core._shared.exceptions import CustomException


@dataclass
class UnauthorizedException(CustomException):
    title: str = "Could not validate credentials"

@dataclass
class ForbiddenException(CustomException):
    title: str = "Not enough permissions"
