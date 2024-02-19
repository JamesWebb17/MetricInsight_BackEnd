"""!
@brief This file is the entry point for the Flask app. It creates the app and registers the blueprints.

@details The app is created and the blueprints are registered. The app is then run.

@section package File Information
- name : app.py

@section author Author(s)
- Created by Simon Faucher on 2023-10-01.
- Modified by Simon Faucher on 2024-02-19.

@section libraries_main Libraries/Modules
- os standard library (https://docs.python.org/3/library/os.html)
--> Access to getenv function.
- flask (https://flask.palletsprojects.com/en/2.0.x/)
--> Access to Flask class.
- flask_cors (https://flask-cors.readthedocs.io/en/latest/)
--> Access to CORS class.
- dotenv (https://pypi.org/project/python-dotenv/)
--> Access to load_dotenv function.
- routes module (local)
--> Access to contact, metricInsight, and api blueprints.

@section version Current Version
- 1.0

@section date Date
- 2024-02-12

@section copyright Copyright
- Copyright (c) 2024 MetricInsight  All rights reserved.
"""

##
# @mainpage MetricInsight Backend Documentation
#
# @section description_main Description
# This is the backend for the MetricInsight project. It is a Flask app that serves as the API for the front-end.
# This Backend must be installed on the device that you want to monitor.
#
# @section notes_main Possibilities
# - It can start and stop MetricInsight
# - It can send data to the front-end
#
# Copyright (c) 2024 Simon Faucher  All rights reserved.

# Imports
import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from routes import contact, metricInsight, api

# Load the environment variables
load_dotenv()

# Global Variables
## Set the environment variables for the back-end IP
back_end_ip = os.getenv("BACKEND_IP")
print(f"BACKEND_IP: {back_end_ip}")

## Set the environment variables for the back-end port
port = os.getenv("PORT")
print(f"PORT: {port}")

## Create the Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

## Register the blueprints
# - contact
app.register_blueprint(contact.contact_blueprint, url_prefix='/contact')

## Register the blueprints
# - metricInsight
app.register_blueprint(metricInsight.MetricInsight_blueprint, url_prefix='/MetricInsight')

## Register the blueprints
# - api
app.register_blueprint(api.api_blueprint, url_prefix='/api')

# Run the app
if __name__ == '__main__':
    """! Start the Backend."""
    app.run(port=port, host=back_end_ip, debug=True)
