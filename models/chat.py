#!/usr/bin/python3
"""Chat class models chats table"""
from models.base_model import BaseModel, Base
from models.conversation import conversation

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Chat(BaseModel, Base):
    __tablename__ = 'chats'
    user_1 = Column(String(128), ForeignKey('users.id'), nullable=False) 
    user_2 = Column(String(128), ForeignKey('users.id'), nullable=False)
    messages = Column(Text, nullable=False)

    # Relationship
    users = relationship('User', secondary=conversation, back_populates='chats')
