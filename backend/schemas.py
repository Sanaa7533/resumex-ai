from pydantic import BaseModel, EmailStr

# --- Request Schemas ---
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

# --- Response Schemas ---
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
