from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    affiliation: str
    role: str = "worker"

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    affiliation: str
    role: str

    class Config:
        orm_mode = True
