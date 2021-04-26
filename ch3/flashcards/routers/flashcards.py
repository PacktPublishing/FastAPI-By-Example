from fastapi import APIRouter, HTTPException, status, Depends
import crud, database, models, schemas
from typing import Optional, List
from utils import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/api/v1', tags=['Flashcards'])

@router.get('/flashcards/{id}', response_model=schemas.ListFlashcard)
async def get_flashcard(id:int, db:Session=Depends(get_db)):
    return crud.get_flashcard(db=db, id=id)

@router.get('/flashcards/', response_model=List[schemas.ListFlashcard])
async def get_flashcards(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    return crud.get_flashcards(skip=skip, limit=limit, db=db)

@router.post('/flashcards/', response_model=schemas.ListFlashcard)
async def create_flashcard(flashcard:schemas.CreateFlashcard, db:Session=Depends(get_db)):
    return crud.create_flashcard(flashcard=flashcard, db=db)

@router.put('/flashcards/{id}', response_model=schemas.ListFlashcard)
async def update_flashcard(id:int, flashcard:schemas.UpdateFlashcard, db:Session=Depends(get_db)):
    return crud.update_flashcard(db=db, flashcard=flashcard, id=id)

@router.delete('/flashcards/{id}/', response_model=schemas.ListFlashcard)
async def delete_flashcard(id:int, db:Session=Depends(get_db)):
    return crud.delete_flashcard(id=id, db=db)


