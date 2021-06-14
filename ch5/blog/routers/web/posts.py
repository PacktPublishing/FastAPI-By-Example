# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from utils.db_utils import get_db
import crud
import schemas

router = APIRouter(prefix='/web/blog', tags=['Web Posts'])

templates = Jinja2Templates(directory='templates')


@router.get('/index', response_class=HTMLResponse)
async def index(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db=db, skip=skip, limit=limit)
    return templates.TemplateResponse('index.html', {'request': request, 'posts': posts})


@router.get('/new_post')
async def new_post(request: Request):
    return templates.TemplateResponse('create_post.html', {'request': request})


@router.post('/new_post')
async def new_post(request: Request, title: str = Form(...), body: str = Form(...), published: bool = Form(...), db: Session = Depends(get_db)):
    post = schemas.PostCreate(title=title, body=body, published=published)
    crud.create_post(db=db, post=post)
    return RedirectResponse(url='index', status_code=status.HTTP_303_SEE_OTHER)


@router.get('/{id}', response_class=HTMLResponse)
async def post(request: Request, id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db=db, id=id)
    return templates.TemplateResponse('post.html', {'request': request, 'post': post})
