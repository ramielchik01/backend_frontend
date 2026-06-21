from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    name: str
    