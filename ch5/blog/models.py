# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func

from database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(name='id', type_=Integer, primary_key=True, index=True)
    title = Column(name='title', type_=String, index=True)
    body = Column(name='body', type_=Text)
    published = Column(name='published', type_=Boolean)
    created_at = Column(name='created_at', type_=DateTime(
        timezone=True), server_default=func.now())
    updated_at = Column(name='updated_at', type_=DateTime(
        timezone=True), onupdate=func.now())
