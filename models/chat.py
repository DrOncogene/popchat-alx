#!/usr/bin/python3
"""Chat class models chats table"""

from models.base_model import BaseModel, Base
from models.joining_tables import conversation
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Chat(BaseModel, Base):
    """
    Chat extends BaseModel and maps chats table
    Args:
        BaseModel: superclass
        Base: stores a class and its corresponding mapped table
    """
    __tablename__ = 'chats'
    user_1 = Column(String(128), ForeignKey('users.id'), nullable=False) 
    user_2 = Column(String(128), ForeignKey('users.id'), nullable=False)
    messages = Column(Text, nullable=False)

    # Relationship
    users = relationship('User', secondary=conversation, back_populates='chats')
