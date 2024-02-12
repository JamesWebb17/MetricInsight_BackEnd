"""
@package routes
@file contact.py
@brief This file is the entry point for the MetricInsight contact.
@details This file is the entry point for the MetricInsight contact. It defines the routes and the functions to send a message to the MetricInsight team.
@version 1.0
@date 2024-02-12
"""

from flask import Blueprint, request, redirect

contact_blueprint = Blueprint('contact', __name__, url_prefix='/contact')

@contact_blueprint.route('/send_message', methods=['POST'])
#TODO: Add the decorator to allow the server to receive the data
def send_message():
    """
    Send a message to the server
    :return:
    """
    # Recovering form data
    form_data = request.form

    return redirect("http://148.60.220.43:3000/")