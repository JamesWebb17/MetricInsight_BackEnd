"""
@package app.py
@file app.py
@brief This file is the entry point for the Flask app. It creates the app and registers the blueprints.
@details The app is created and the blueprints are registered. The app is then run.
@version 1.0
@date 2020-11-20
"""

# Import the required packages
import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from routes import contact, metricInsight, api

# Load the environment variables
load_dotenv()

# Set the environment variables for the back-end IP and port
back_end_ip = os.getenv("BACKEND_IP")
port = os.getenv("PORT")

print(f"BACKEND_IP: {back_end_ip}")
print(f"PORT: {port}")

# Create the Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Register the blueprints
app.register_blueprint(contact.contact_blueprint, url_prefix='/contact')
app.register_blueprint(metricInsight.MetricInsight_blueprint, url_prefix='/MetricInsight')
app.register_blueprint(api.api_blueprint, url_prefix='/api')

# Run the app
if __name__ == '__main__':
    app.run(port=port, host=back_end_ip, debug=True)
