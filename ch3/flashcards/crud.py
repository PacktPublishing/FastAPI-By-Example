from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
import database, models, schemas
from typing import Optional, List

def get_category(db:Session, id:int):
    db_category = db.query(models.Category).filter(models.Category.id==id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Category not found!')
    return db_category

def get_categories(db:Session, skip:int=0, limit:int=100):
    db_categories = db.query(models.Category).offset(skip).limit(limit).all()
    if not db_categories:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='No categories were found!')
    return db_categories

def create_category(db:Session, category:schemas.CreateCategory):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(id:int, db:Session, category:schemas.UpdateCategory):
    db_category = db.query(models.Category).filter(models.Category.id==id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Category does not exist!')
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db:Session, id:int):
    db_category = db.query(models.Category).filter(models.Category.id==id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Category does not exist!')
    db.delete(db_category)
    db.commit()
    return db_category

def get_flashcard(db:Session, id:int):
    db_flashcard = db.query(models.Flashcard).filter(models.Flashcard.id==id).first()
    if not db_flashcard:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Flashcard not found!')
    return db_flashcard

def get_flashcards(db:Session, skip:int=0, limit:int=100):
    db_flashcards = db.query(models.Flashcard).offset(skip).limit(limit).all()
    if not db_flashcards:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Flashcards not found!')
    return db_flashcards

def create_flashcard(db:Session, flashcard:schemas.CreateFlashcard):
    db_flashcard = models.Flashcard(question=flashcard.question, answer=flashcard.answer, category_id=flashcard.category_id)
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard

def update_flashcard(id:int, db:Session, flashcard:schemas.UpdateFlashcard):
    db_flashcard = db.query(models.Flashcard).filter(models.Flashcard.id==id).first()
    if not db_flashcard:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Flashcard not found!')
    if flashcard.category:
        db_flashcard.category = flashcard.category
    if flashcard.question:
        db_flashcard.question = flashcard.question
    if flashcard.answer:
        db_flashcard.answer = flashcard.answer
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard

def delete_flashcard(db:Session, id:int):
    db_flashcard = db.query(models.Flashcard).filter(models.Flashcard.id==id).first()
    if not db_flashcard:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Flashcard not found!')
    db.delete(db_flashcard)
    db.commit()
    return db_flashcard
