# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
from typing import Optional, List


class BasePost(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

    class Config:
        orm_mode = True


class CreatePost(BasePost):
    pass


class ShowPost(BasePost):
    author: ShowUser
