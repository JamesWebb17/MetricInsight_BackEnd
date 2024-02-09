import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from routes import contact, metricInsight, api

# Load the environment variables
load_dotenv()

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
    app.run()
