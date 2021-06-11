# -*- coding: utf-8 -*-
import graphene
from graphql.execution.executors.asyncio import AsyncioExecutor
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
import queries
import mutations


import models
import database
from routers import flashcards, categories

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(flashcards.router)
app.include_router(categories.router)

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=queries.Query,
              mutation=mutations.APIMutations), executor_class=AsyncioExecutor))
