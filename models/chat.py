#!/usr/bin/python3
"""Chat class models chats table"""
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Chat(BaseModel, Base):
    __tablename__ = 'chats'
    member_1 = Column(String(128), ForeignKey('users.id'), nullable=False) 
    member_2 = Column(String(128), ForeignKey('users.id'), nullable=False)
    messages = Column(String(128), nullable=False)
