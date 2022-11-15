"""
init file
"""
from os import environ

from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=r'*')

app.config.update(
    SECRET_KEY='c6e88c23a381ac802fbcaa09938f56a80042d30850b27b71db00ced777ecd64e',
    JSONIFY_PRETTYPRINT_REGULAR=True,
    DEBUG=True,
    ENV='development',
)


if __name__ == '__main__':
    HOST = environ.get('HOST') or 'localhost'
    PORT = environ.get('PORT') or 5000

    socketio.run(app, host=HOST, port=PORT)
