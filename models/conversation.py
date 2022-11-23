#!/usr/bin/python3
"""Conversation table models joining table for user_chat table"""
from models.base_model import Base

from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.sql.schema import Table

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
