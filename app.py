import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from routes import contact, metricInsight, api

load_dotenv()

app = Flask(__name__)


CORS(app)

app.register_blueprint(contact.contact_blueprint, url_prefix='/contact')
app.register_blueprint(metricInsight.MetricInsight_blueprint, url_prefix='/MetricInsight')
app.register_blueprint(api.api_blueprint, url_prefix='/api')



if __name__ == '__main__':

    host = os.getenv("SERVER_IP", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))

    print(f"Server running on {host}:{port}")

    app.run(host="148.60.220.43", port=port)
