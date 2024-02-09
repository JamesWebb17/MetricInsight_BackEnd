from flask import Blueprint, request, redirect, jsonify
import time
from flask_sse import sse

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/hello', methods=['GET'])
def get_update():
    """
    Send a message to the server
    :return:
    """
    return jsonify({'data': 'Hello World!'})