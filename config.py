# Import the built-in libraries
import os

# Import the external libraries
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from threading import Lock


def flask_config():
    async_mode = None
    # Declare a Flask app
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins = '*')
    thread = None
    thread_lock = Lock()

    return async_mode, app, socketio, thread, thread_lock


# build the directories
def flask_folder():
    data_folder = './data'
    data_bgp_folder = './data/bgp'
    data_geo_folder = './data/geolocation'
    
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    if not os.path.exists(data_bgp_folder):
        os.makedirs(data_bgp_folder)
    if not os.path.exists(data_geo_folder):
        os.makedirs(data_geo_folder)
    return None