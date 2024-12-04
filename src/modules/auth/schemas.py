from datetime import datetime

from pydantic import BaseModel, validator


class CreateAccount(BaseModel):
    email: str
    password: str
    account_type_id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str
    exp: datetime
    authenticated: bool = True


class PasswordBase(BaseModel):
    password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v
