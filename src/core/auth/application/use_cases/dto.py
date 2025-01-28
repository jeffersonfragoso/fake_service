from pydantic import BaseModel


class AuthDto:
    class InputCredentials(BaseModel):
        username: str
        password: str

    class InputDataToEncode(BaseModel):
        sub: str

    class OutputAccesToken(BaseModel):
        access_token: str
        token_type: str = "bearer"
