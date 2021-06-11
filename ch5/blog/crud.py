from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import models, schemas
from utils import security #generate_hash, verify_password_hash

def get_post(db:Session, id:int):
    db_post = db.query(models.Post).filter(models.Post.id==id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No post found!')
    return db_post

def get_posts(db:Session, skip:int=0, limit:int=100):
    db_posts = db.query(models.Post).offset(skip).limit(limit).all()
    if not db_posts:
        raise HTTPEXception(status_code=status.HTTP_404_NOT_FOUND, detail='No posts were found!')
    return db_posts

def create_post(db:Session, post:schemas.CreatePost):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(id:int,  post:schemas.BasePost, db:Session):
    db_post = db.query(models.Post).filter(models.Post.id == id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post does not exist!')
    db(**post.dict()).commit()
    db.refresh(db_post)
    return db_post
    

def delete_post(id:int, db:Session):
    db_post = db.query(models.Post).filter(models.Post.id == id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post does not exist!')
    db.delete(db_post)
    db.commit()
    return db_post
