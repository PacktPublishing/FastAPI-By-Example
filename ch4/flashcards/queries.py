import graphene
from graphql import GraphQLError
import graphql_schemas, crud, models, schemas, database

class Query(graphene.ObjectType):
    get_flashcard = graphene.Field(graphql_schemas.Flashcard, id=graphene.Int())
    get_flashcards = graphene.List(graphql_schemas.Flashcard)
    get_category = graphene.Field(graphql_schemas.Category, id=graphene.Int())
    get_categories = graphene.List(graphql_schemas.Category)

    async def resolve_get_flashcard(root, info, id):
        try:
            flashcard = crud.get_flashcard(db=database.SessionLocal(), id=id)
            return flashcard
        except:
            raise GraphQLError('Flashcard not found!')

    async def resolve_get_flashcards(root, info):
        try:
            flashcards = crud.get_flashcards(db=database.SessionLocal())
            return flashcards
        except:
            raise GraphQLError('Flashcards not found!')

    async def resolve_get_category(root, info, id):
        try:
            category = crud.get_category(db=database.SessionLocal(), id=id)
            return category
        except:
            raise GraphQLError('Category not found')

    async def resolve_get_categories(root, info):
        try:
            categories = crud.get_categories(db=database.SessionLocal())
            return categories
        except:
            raise GraphQLError('Categories not found!')
