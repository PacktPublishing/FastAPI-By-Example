# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
from typing import Optional, List


class BasePost(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

    class Config:
        orm_mode = True


class PostCreate(BasePost):
    pass


class PostUpdate(BasePost):
    pass


class PostOut(BasePost):
    class Config:
        orm_mode = True


class Post(BasePost):
    id: int

    class Config:
        orm_mode = True
