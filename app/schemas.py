from pydantic import BaseModel
from datetime import datetime
from auth.schemas import UserOut
from typing import List


class Blog(BaseModel):
    id:int
    title:str
    body:str
    created:datetime


class BlogIn(BaseModel):
    title:str
    body:str


class BlogOut(BaseModel):
    id:int
    title:str
    body:str
    created:datetime
    author:UserOut
    comments :List[str] = None


class CommentIn(BaseModel):
    blog_id:int
    body:str