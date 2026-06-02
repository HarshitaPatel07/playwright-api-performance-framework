from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    gender: str
    age: int


class UserResponse(UserCreate):
    id: int

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    gender: str | None = None
    age: int | None = None
