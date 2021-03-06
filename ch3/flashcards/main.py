# -*- coding: utf-8 -*-
from fastapi import FastAPI

import models
import database
from routers import flashcards, categories

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(flashcards.router)
app.include_router(categories.router)
