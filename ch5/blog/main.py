# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.api.posts import router as api_router
from routers.web.posts import router as web_router
import models
import database

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name='static')


@app.on_event('startup')
def startup():
    models.Base.metadata.create_all(bind=database.engine)


app.include_router(api_router)
app.include_router(web_router)
