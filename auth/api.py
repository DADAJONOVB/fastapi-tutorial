from .models import User
from .schemas import UserIn, UserOut
from passlib.hash import pbkdf2_sha256
from fastapi import APIRouter, Security
from fastapi_jwt import JwtAuthorizationCredentials,  JwtAccessBearer
from .auth_backend import secret_key, access_security



auth_api = APIRouter()


@auth_api.get("/users/me")
async def read_current_user(
    credentials: JwtAuthorizationCredentials = Security(access_security),
):
    return {"username": credentials["username"], "role": credentials["role"]}



@auth_api.post('/user/register/')
async def register_user(data:UserIn):   
    # data = data.dict()
    user = await User.objects.create(**data)
    return user



@auth_api.post('/user/login/')
async def login(user:UserIn):
    data = {}
    try:
        auth =  await User.objects.get(username=user.username)
        if pbkdf2_sha256.verify(user.password, auth.password):
            subject = {"username": user.username, "role": "user"}
            data["access_token"]=access_security.create_access_token(subject=subject)
        else:
            data['success']=False
            data['detail']='user is none'
    except:
        data['success']=False
        data['detail']='user is none'

    return data