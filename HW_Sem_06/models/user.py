from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    name: str = Field(..., title="First Name", max_length=30)
    surname: str = Field(..., title="Last Name", max_length=30)
    email: EmailStr = Field(..., title="Email", max_length=30)


class UserIn(BaseModel):
    name: str = Field(..., title="First Name", max_length=30)
    surname: str = Field(..., title="Last Name", max_length=30)
    email: EmailStr = Field(..., title="Email", max_length=30)
    password: str = Field(..., title="Password", min_length=6, max_length=20)
