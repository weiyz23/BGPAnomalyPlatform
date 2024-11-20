# Import the built-in libraries
import os
import sys
import time
import zipfile
import glob

# Import external libraries
import numpy as np
from flask import Flask, render_template, url_for, request, send_file, abort
from flask_socketio import SocketIO, emit, disconnect

# Import customized libraries
from config import flask_config, flask_folder
from src.utils.geolocator import geolocator
from routes import my_routes

# Load Flask configuration
async_mode, app, socketio, thread, thread_lock = flask_config()
flask_folder()

# register the routes
app.register_blueprint(my_routes)

# You can use socketio to create websockets

"""
## Launch app
"""
if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
    # app.run(debug=True)