from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(name='id', type_=Integer, primary_key=True, nullable=False, unique=True, index=True)
    name = Column(name='name', type_=String(64), index=True, nullable=False, unique=True)
    flashcard = relationship('Flashcard', back_populates='category')
    time_created = Column(name='time_created', type_=DateTime(timezone=True), server_default=func.now())
    time_updated = Column(name='time_updated', type_=DateTime(timezone=True), onupdate=func.now())


class Flashcard(Base):
    __tablename__ = 'flashcards'
    id = Column(name='id', type_=Integer, primary_key=True, index=True, nullable=False, unique=True)
    category_id = Column(ForeignKey('categories.id'), name='category_id', type_=Integer, nullable=True)
    question = Column(name='question', type_=String, nullable=True)
    answer = Column(name='answer', type_=String, nullable=True)
    category = relationship('Category', back_populates='flashcard')
    time_created = Column(name='time_created', type_=DateTime(timezone=True), server_default=func.now())
    time_updated = Column(name='time_updated', type_=DateTime(timezone=True), onupdate=func.now())
