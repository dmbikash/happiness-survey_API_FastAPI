from pydantic import BaseModel
from datetime import datetime


class UserDataSchema(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime


class UpdateUserDataSchema(BaseModel):
    name: str
    email: str


class UserInfo(BaseModel):
    name: str
    email: str
    password: str


class ShowUserInfo(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

# -----------------------------------------------------


class HappySchema(BaseModel):

    index : int
    employeeID : str
    rated_at : datetime


