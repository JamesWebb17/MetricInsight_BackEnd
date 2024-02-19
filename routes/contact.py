"""!
@brief This file is the entry point for the MetricInsight contact route.

@details The contact blueprint is created and the contact route is registered.

@section author Author(s)
- Created by Simon Faucher on 2023-10-01.
- Modified by Simon Faucher on 2024-02-19.

@section libraries_main Libraries/Modules
- flask (https://flask.palletsprojects.com/en/2.0.x/)
--> Access to Blueprint request and redirect classes.

@section version Current Version
- 1.0

@section date Date
- 2024-02-12

@section copyright Copyright
- Copyright (c) 2024 MetricInsight  All rights reserved.
"""

from flask import Blueprint, request, redirect

contact_blueprint = Blueprint('contact', __name__, url_prefix='/contact')

@contact_blueprint.route('/send_message', methods=['POST'])
#TODO: Add the decorator to allow the server to receive the data
def send_message():
    """!
    Send a message to the server
    @return:
    """
    # Recovering form data
    form_data = request.form

    return redirect("http://148.60.220.43:3000/")