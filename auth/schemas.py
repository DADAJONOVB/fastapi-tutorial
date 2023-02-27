from pydantic import BaseModel
from datetime import datetime


class UserOut(BaseModel):
    id:int
    username:str
    password:str
    data_register:datetime



class UserIn(BaseModel):
    username:str
    password:str