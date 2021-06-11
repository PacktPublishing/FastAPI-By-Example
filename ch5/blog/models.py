# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(name='id', type_=Integer, primary_key=True, index=True)
    title = Column(name='title', type_=String, index=True)
    body = Column(name='body', type_=Text)
    published = Column(name='published', type_=Boolean)
    author = relationship('User', back_populates='posts')
    author_id = Column(ForeignKey('users.id'),
                       name='creator_id', type_=Integer)
    created_at = Column(name='created_at', type_=DateTime(
        timezone=True), server_default=func.now())
    updated_at = Column(name='updated_at', type_=DateTime(
        timezone=True), onupdate=func.now())


class User(Base):
    __tablename__ = "users"
    id = Column(name='id', type_=Integer, primary_key=True, index=True)
    name = Column(name='name', type_=String, index=True)
    email = Column(name='email', type_=String, unique=True)
    password = Column(name='password', type_=String)
    posts = relationship('Post', back_populates='author')
