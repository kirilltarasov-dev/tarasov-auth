from uuid import UUID
from enum import Enum
from datetime import datetime

from pydantic import BaseModel, EmailStr


class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID
    role: RoleEnum
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
