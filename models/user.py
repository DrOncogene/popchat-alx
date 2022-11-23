#!/usr/bin/python3
"""User class models users table"""

from models.base_model import BaseModel, Base
from models.joining_tables import conference, conversation
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    User extends BaseModel and maps users table
    Args:
        BaseModel: superclass
        Base: stores a class and its corresponding mapped table
    """
    __tablename__ = 'users'
    username = Column(String(60), nullable=False, unique=True) 
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    # Relationships:
    #: list of obj: stores list of chats between two users
    chats = relationship('Chat', secondary=conversation, back_populates='users')
    #: list of obj: stores list of rooms a user belong
    rooms = relationship('Room', secondary=conference, back_populates='members')
