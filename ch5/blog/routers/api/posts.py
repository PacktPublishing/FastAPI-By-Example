# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.orm import Session
from typing import Optional, List

import crud
import models
import schemas
import database
from utils.db_utils import get_db

router = APIRouter(prefix='/v1/api/blog', tags=['API Posts'])


@router.post("/posts/", response_model=schemas.PostOut)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(post=post, db=db)


@router.get("/posts/", response_model=List[schemas.PostOut])
async def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_posts(skip=skip, limit=limit, db=db)


@router.get("/posts/{id}/", response_model=schemas.PostOut)
async def get_post(id: int, db: Session = Depends(get_db)):
    return crud.get_post(db=db, id=id)


@router.delete("/posts/{id}/", response_model=schemas.PostOut)
async def delete_post(id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db=db, id=id)


@router.put("/posts/{id}", response_model=schemas.PostOut)
async def update_post(id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    return crud.update_post(db=db, id=id, post=post)
