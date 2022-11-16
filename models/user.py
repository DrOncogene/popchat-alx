#!/usr/bin/python3
"""Chat class models chats table"""
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = 'users'
    username = Column(String(128), nullable=False) 
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    chats = Column(String(128), nullable=True)
    rooms = Column(String(128), nullable=True)
