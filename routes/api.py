"""!
@brief This file is the entry point for the MetricInsight api route.

@details The api blueprint is created and the api route is registered.

@section package File Information
- package : routes
- name : api.py

@section author Author(s)
- Created by Simon Faucher on 2023-10-01.
- Modified by Simon Faucher on 2024-02-19.

@section libraries_main Libraries/Modules
- flask (https://flask.palletsprojects.com/en/2.0.x/)
--> Access to Blueprint and jsonify classes.

@section version Current Version
- 1.0

@section date Date
- 2024-02-12

@section copyright Copyright
- Copyright (c) 2024 MetricInsight  All rights reserved.
"""

# Import the required packages
from flask import Blueprint, jsonify

## @var api_blueprint
# Create the blueprint for the api route
api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/hello', methods=['GET'])
def hello():
    """!Send a message to the server
        @return Message for the server : "Hello World!"
    """
    return jsonify({'data': 'Hello World!'})