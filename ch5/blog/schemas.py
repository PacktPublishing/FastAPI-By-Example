# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
from typing import Optional, List


class BaseUser(BaseModel):
    name: str
    email: str


class CreateUser(BaseUser):
    password: str


class BasePost(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False
    
    class Config:
        orm_mode = True

class ShowUser(BaseUser):
    posts: List[BasePost] = []

    class Config:
        orm_mode = True

class CreatePost(BasePost):
    pass

class ShowPost(BasePost):
    author: ShowUser

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

