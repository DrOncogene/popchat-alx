"""
init file
"""
from os import path

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from dotenv import load_dotenv

curr_dir = path.abspath(path.dirname(__name__))
load_dotenv(path.join(curr_dir, '..', '.env'))

app = Flask(__name__)
sio = SocketIO()
cors = CORS()

app.config.update(
    DEBUG=True,
    ENV='development',
    JSONIFY_PRETTYPRINT_REGULAR=True,
)
cors.init_app(app, resources={r'/auth/*': {'origins': '*'},
                r'/api/v1/*': {'origins': '*'}})
sio.init_app(app, async_mode='eventlet', cors_allowed_origins=r'*')
