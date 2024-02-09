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