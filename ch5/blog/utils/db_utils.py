# -*- coding: utf-8 -*-
from .. import database


async def get_db():
    db_session = database.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
