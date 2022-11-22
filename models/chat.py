#!/usr/bin/python3
"""Chat class models chats table"""
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Chat(BaseModel, Base):
    __tablename__ = 'chats'
    sender = Column(String(128), ForeignKey('users.id'), nullable=False) 
    recipient = Column(String(128), ForeignKey('users.id'), nullable=False)
    messages = Column(Text, nullable=False)

    # Relationship
    user = relationship('User', back_populates='chats')
