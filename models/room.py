#!/usr/bin/python3
"""Room class models rooms table"""

from models.base_model import BaseModel, Base
from models.joining_tables import conference
from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship


class Room(BaseModel, Base):
    """
    Room extends BaseModel class and maps rooms table
    Args:
        BaseModel: superclass
        Base: stores a class and its corresponding mapped table
    """
    __tablename__ = 'rooms'
    name = Column(String(60), nullable=False)
    created_by = Column(String(128), ForeignKey('users.id'), nullable=False)
    messages = Column(Text, nullable=False)
    
    #: list of obj: stores list of users belong to a room
    members = relationship('User', secondary=conference, back_populates='rooms')
