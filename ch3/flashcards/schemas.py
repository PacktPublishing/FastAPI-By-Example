# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Optional, List


class BaseCategory(BaseModel):
    name: str


class CreateCategory(BaseCategory):
    pass


class UpdateCategory(BaseCategory):
    pass


class BaseFlashcard(BaseModel):
    question: str
    answer: str


class CreateFlashcard(BaseFlashcard):
    category_id: int


class UpdateFlashcard(BaseFlashcard):
    category_id: int


class ListFlashcard(BaseFlashcard):
    class Config:
        orm_mode = True


class ListCategory(BaseCategory):
    flashcard: List[ListFlashcard] = []

    class Config:
        orm_mode = True
