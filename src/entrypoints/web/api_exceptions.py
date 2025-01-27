from dataclasses import dataclass
from typing import Any

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder


class CustomHttpErrorException(HTTPException):
    status_code: int
    detail: Any | None = None

    def __init__(self):
        super().__init__(self.status_code, self.detail, None)
        self.status_code = self.status_code
        self.detail = self.detail

    def as_json(self) -> dict:
        return {
            "status_code": self.status_code,
            "content": jsonable_encoder(
                {
                    "detail": self.detail,
                }
            ),
        }


class ApiAuthenticationException(CustomHttpErrorException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Could not validate credentials"


class ApiForbiddenException(CustomHttpErrorException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Not enough permissions"


class ApiInternalServerException(CustomHttpErrorException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal Server Error"
