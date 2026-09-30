from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


class StudentBase(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str
    department: str
    phone: Optional[str] = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    course: Optional[str] = None
    department: Optional[str] = None
    phone: Optional[str] = None


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)