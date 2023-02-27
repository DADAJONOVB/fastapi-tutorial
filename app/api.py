from fastapi import APIRouter, Security
from .models import Blog, Comment
from .schemas import BlogIn, BlogOut
from fastapi_jwt import JwtAuthorizationCredentials
from auth.auth_backend import access_security

app_router = APIRouter()



@app_router.get('/blogs/', response_model=BlogOut)
async def get_blogs():
    blogs = await Blog.objects.all()
    return blogs



@app_router.get('/blog/deatil/{id}/', response_model=BlogOut)
async def get_blog(id:int):
    blog = await Blog.objects.get(id=id)
    return blog



@app_router.post('/blog/create/')
async def create_blog(
    blog:BlogIn,
    credentials: JwtAuthorizationCredentials = Security(access_security)
    ):
    print(blog)
    print(credentials)
    return True