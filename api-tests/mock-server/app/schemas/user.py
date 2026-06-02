from pydantic import BaseModel, EmailStr, Field

from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    gender: Gender
    age: int = Field(ge=1, le=120)


class UserResponse(UserCreate):
    id: int

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    gender: Gender | None = None
    age: int | None = Field(default=None, ge=1, le=120)
