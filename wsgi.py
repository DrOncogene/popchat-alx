"""
server entry point
"""
from os import environ

from app import app, sio


if __name__ == '__main__':
    HOST = environ.get('HOST') or 'localhost'
    PORT = environ.get('PORT') or 5000

    sio.run(app, host=HOST, port=PORT)
