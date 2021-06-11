# -*- coding: utf-8 -*-
from fastapi import FastAPI
import models
import database

app = FastAPI()


@app.on_event('startup')
def startup():
    models.Base.metadata.create_all(bind=database.engine)
