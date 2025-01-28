from dataclasses import dataclass
from functools import wraps
from typing import Any


@dataclass
class CustomException(Exception):
    title: str
    detail: Any | None = None

    def __str__(self) -> str:
        return f"{self.title}: {self.detail}"


def handle_exception(exc: CustomException, raise_errors: bool):
    print(f"[Domain exception handler] {str(exc)}")
    if raise_errors:
        raise exc


def catch_exceptions(exceptions: list[CustomException], raise_errors: bool = True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except tuple(exceptions) as exc:
                handle_exception(exc, raise_errors)

        return wrapper

    return decorator
