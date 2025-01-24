from fastapi import Query
from pydantic import BaseModel


class InputCredentials(BaseModel):
    username: str = Query(None, description="Username")
    password: str = Query(None, description="Password")


class AuthTokenResponse(BaseModel):
    access_token: str
    token_type: str
