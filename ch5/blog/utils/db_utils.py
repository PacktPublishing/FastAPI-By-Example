# -*- coding: utf-8 -*-
from database import SessionLocal


async def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
