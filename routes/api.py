"""
@package routes
@file api.py
@brief This file is the entry point for the MetricInsight api.
@details
@version 1.0
@date 2020-11-20
"""

# Import the required packages
from flask import Blueprint, jsonify

# Create the blueprint
api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/hello', methods=['GET'])
def get_update():
    """
    Send a message to the server
    :return:
    """
    return jsonify({'data': 'Hello World!'})