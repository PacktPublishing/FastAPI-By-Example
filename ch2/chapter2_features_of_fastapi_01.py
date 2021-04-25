import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


def get_db():
    db = 'fakedatabaseconnection'
    return db

app = FastAPI()

@app.get('/')
async def index(db:Session=Depends(get_db)):
    return f'Fake database connection: {db}'

uvicorn.run(app, host='127.0.0.1', port=8080)
