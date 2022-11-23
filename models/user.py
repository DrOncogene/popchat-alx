#!/usr/bin/python3
"""User class models chats table"""
from models.base_model import BaseModel, Base
from models.conversation import conversation

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'users'
    username = Column(String(60), nullable=False, unique=True) 
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    # Relationship
    chats = relationship('Chat', secondary=conversation, back_populates='users')
