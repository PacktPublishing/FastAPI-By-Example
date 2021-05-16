from graphene_sqlalchemy import SQLAlchemyObjectType
import models

class Flashcard(SQLAlchemyObjectType):
    class Meta:
        model = models.Flashcard


class Category(SQLAlchemyObjectType):
    class Meta:
        model = models.Category
