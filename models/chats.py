#!/usr/bin/python3
"""Chat class models chats table"""
from models.base_model import BaseModel


class Chat(BaseModel):
    member_1 = ''
    member_2 = ''
    messages = ''
