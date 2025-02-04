from pydantic import BaseModel
from typing import Optional
class LoginModel(BaseModel):
    email:str
    userName:Optional[str]=""
    password:str