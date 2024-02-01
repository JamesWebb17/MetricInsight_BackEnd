from flask import Blueprint, request, redirect, jsonify
import time
from flask_sse import sse

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/get_update', methods=['GET'])
def get_update():
    return jsonify({'data': 'Hello World!'})


@api_blueprint.route('/sse-endpoint')
def start_events():
    for _ in range(10):  # Envoyer des événements toutes les secondes pendant 10 secondes
        time.sleep(1)
        sse.publish({"message": "coucou"}, type='event-type')
        print("Event sent!")

    return "Événements envoyés avec succès!"