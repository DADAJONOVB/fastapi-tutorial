from fastapi import APIRouter, Security, Body

from auth.models import User
from .models import Blog, Comment
from .schemas import BlogIn, BlogOut, CommentIn
from fastapi_jwt import JwtAuthorizationCredentials
from auth.auth_backend import access_security
from typing import List


app_router = APIRouter()



@app_router.get('/blogs/', response_model=List[BlogOut])
async def get_blogs():
    blogs = await Blog.objects.all()
    return blogs


@app_router.get('/blog/detail/{id}/')
async def get_blog(id:int):
    blog = await Blog.objects.get(id=id)
    return blog



@app_router.post('/blog/create/')
async def create_blog(
    blog: BlogIn,
    credentials: JwtAuthorizationCredentials = Security(access_security)
    ):
    user = await User.objects.get(username=credentials['username'])
    object = await Blog.objects.create(
        title=blog.title,
        body=blog.body,
        author=user
    )
    return object



@app_router.post('/comment/create/')
async def create_comment(
    comment:CommentIn,
    credentials: JwtAuthorizationCredentials = Security(access_security)
    ):
    blog = await Blog.objects.get(id=comment.blog_id)    
    user = await User.objects.get(username=credentials['username'])
    await Comment.objects.create(blog=blog, body=comment.body, user=user)
    return True