from flask import Blueprint, request, redirect, jsonify

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/get_update', methods=['GET'])
def get_update():
    return jsonify({'data': 'Hello World!'})

