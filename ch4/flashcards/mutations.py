import graphene
from graphql import GraphQLError
import graphql_schemas, crud, schemas, database

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    success = graphene.Boolean()
    category = graphene.Field(graphql_schemas.Category)

    async def mutate(root, info, name):
        try:
            category_schema = schemas.CreateCategory(name=name)
            category = crud.create_category(db=database.SessionLocal(), category=category_schema)
            return CreateCategory(success=True, category=category)
        except:
            raise GraphQLError('The category could not be created!')


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
    
    success = graphene.Boolean()
    category = graphene.Field(graphql_schemas.Category)

    async def mutate(root, info, id, name):
        try:
            category_schema = schemas.UpdateCategory(name=name)
            category = crud.update_category(db=database.SessionLocal(), id=id, category=category_schema)
            return UpdateCategory(success=True, category=category)
        except:
            raise GraphQLError('The category could not be updated!')


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()
    category = graphene.Field(graphql_schemas.Category)

    async def mutate(root, info, id):
        try:
            category = crud.delete_category(db=database.SessionLocal(), id=id)
            return DeleteCategory(success=True, category=category)
        except:
            raise GraphQLError('The category could not be deleted!')



class CreateFlashcard(graphene.Mutation):
    class Arguments:
        question = graphene.String()
        answer = graphene.String()
        category_id = graphene.Int()

    success = graphene.Boolean()
    flashcard = graphene.Field(graphql_schemas.Flashcard)

    async def mutate(root, info, question, answer, category_id):
        try:
            flashcard_schema = schemas.CreateFlashcard(question=question, answer=answer, category_id=category_id)
            flashcard = crud.create_flashcard(db=database.SessionLocal(), flashcard=flashcard_schema)
            return CreateFlashcard(success=True, flashcard=flashcard)
        except:
            raise GraphQLError('The flashcard could not be created!')


class UpdateFlashcard(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        question = graphene.String()
        answer = graphene.String()
        category_id = graphene.Int()

    success = graphene.Boolean()
    flashcard = graphene.Field(graphql_schemas.Flashcard)

    async def mutate(root, info, id, question, answer, category_id):
        try:
            flashcard_schema = schemas.UpdateFlashcard(question=question, answer=answer, category_id=category_id)
            flashcard = crud.update_flashcard(db=database.SessionLocal(), id=id, flashcard=flashcard_schema)
            return UpdateFlashcard(success=True, flashcard=flashcard)
        except: 
            raise GraphQLError('The flashcard could not be updated!')



class DeleteFlashcard(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
    
    success = graphene.Boolean()
    flashcard = graphene.Field(graphql_schemas.Flashcard)

    async def mutate(root, info, id):
        try:
            flashcard = crud.delete_flashcard(db=database.SessionLocal(), id=id)
            return DeleteFlashcard(success=True, flashcard=flashcard)
        except:
            raise GraphQLError('The flashcard could not be deleted!')

class APIMutations(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_flashcard = CreateFlashcard.Field()
    update_flashcard = UpdateFlashcard.Field()
    delete_flashcard = DeleteFlashcard.Field()
