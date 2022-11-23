#!/usr/bin/python3
"""Define joining tables each appropriate many-to-many relationship"""

from models.base_model import Base
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.sql.schema import Table

# store user_chat joining table
conversation = Table(
    'user_chat',
    Base.metadata,
    Column(
        'user_id',
        String(60),
        ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'chat_id',
        String(60),
        ForeignKey('chats.id'),
        primary_key=True,
        nullable=False
    )
)

# store user_room joining table
conference = Table(
    'user_room',
    Base.metadata,
    Column(
        'user_id',
        String(60),
        ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'room_id',
        String(60),
        ForeignKey('rooms.id'),
        primary_key=True,
        nullable=False
    )
)
