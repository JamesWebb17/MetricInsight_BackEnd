from flask import Flask
from flask_cors import CORS
from routes import contact, metricInsight, api

app = Flask(__name__)

CORS(app)

app.register_blueprint(contact.contact_blueprint, url_prefix='/contact')
app.register_blueprint(metricInsight.MetricInsight_blueprint, url_prefix='/MetricInsight')
app.register_blueprint(api.api_blueprint, url_prefix='/api')


if __name__ == '__main__':
    app.run()
