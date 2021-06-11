# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
import crud
import models
import database
import schemas
from utils import get_db
from typing import Optional, List

router = APIRouter(prefix='/api/v1', tags=['Categories'])


@router.get('/category/{id}/', response_model=schemas.ListCategory)
async def get_category(id: int, db: Session = Depends(get_db)):
    return crud.get_category(id=id, db=db)


@router.get('/category/', response_model=List[schemas.ListCategory])
async def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(skip=skip, limit=limit, db=db)


@router.post('/category/', response_model=schemas.ListCategory)
async def create_category(category: schemas.CreateCategory, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@router.put('/category/{id}', response_model=schemas.ListCategory)
async def update_category(id: int, category: schemas.UpdateCategory, db: Session = Depends(get_db)):
    return crud.update_category(id=id, db=db, category=category)


@router.delete('/category/{id}/', response_model=schemas.ListCategory)
async def delete_category(id: int, db: Session = Depends(get_db)):
    return crud.delete_category(id=id, db=db)
