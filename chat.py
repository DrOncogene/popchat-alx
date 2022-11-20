"""
module for dynamically generating sockeio 
envent handlers and other helper methods
"""
from datetime import datetime

from flask import request
from flask_socketio import join_room, send

from app import sio
from storage import db


def handle_chat(payload):
    """
    sends a message to the appropriate room
    :param payload: The message sent by the client
    """
    send(payload['message'], to=payload['room'], include_self=False)
    print(payload)


def load_handlers(user: dict):
    """
    load all handlers for a newly connected user
    :param user: The dictionary containing the user data
    """
    for room in user['rooms']:
        join_room(room)
        sio.on_event(f'{room}_event', handle_chat)


@sio.on('connected')
def handle_connect(payload):
    """
    handles the connection event
    :param auth: Authentication dict
        passed by the client
    """
    load_handlers(payload.get('user'))
    print(payload.get('user'))


def parse_messages(blob: str) -> list:
    """
    parses a message string and return a list of
    the messages
    :param msg: The string blob for all messages
        in a chat
    """
    messages: list = []
    all_msg = blob.split(';')
    for message in all_msg:
        sender, when, text = message.split('|')
        msg = {}
        msg['sender'] = sender
        msg['when'] = datetime.strptime(when, '%d-%B-%Y %H:%M')
        msg['text'] = text
        messages.append(msg)

    return messages


def add_message(which: str, chat_id: str, msg: 'dict[str]') -> bool:
    """
    adds a new message to a room/chat
    :param which: the type of chat (private or a room/channel)
        valid values are room and chat
    :param chat_id: private chat id or room id
    :param msg: new message to add
    Return: True is success, False otherwise
    """
    if which not in ['room', 'chat']:
        return False

    if which == 'chat':
        chat = db.get_one('Chat', chat_id)
    else:
        chat = db.get_one('Room', chat_id)

    user = msg['sender']
    when = msg['when']
    text = msg['text']
    msg_str = f'{user}|{when}|{text};'
    chat.messages.append(msg_str)
    db.save()

    return True
    