from flask import Blueprint, request, redirect

contact_blueprint = Blueprint('contact', __name__, url_prefix='/contact')

@contact_blueprint.route('/send_message', methods=['POST'])
def send_message():
    # Accédez aux données du formulaire à partir de request.form
    form_data = request.form

    print(form_data)

    # Faites quelque chose avec les données du formulaire
    result = {'data': form_data}

    return redirect("http://148.60.220.43:3000/")