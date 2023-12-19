# marine_routes.py
from flask import Blueprint, jsonify, request
from handlers import sports_handler
from redis_config import redis  # Import the 'redis' object
import json

sports_bp = Blueprint('sports', __name__)


@sports_bp.route('/register', methods=['POST'])
def post_user_city_registration():
    data = request.json
    if data:
        email = data.get('email')
        city_name = data.get('city')
        print(city_name)
        print(email)
        response_data = sports_handler.create_registration(data)
        return jsonify({'message': response_data})



@sports_bp.route('/register/<email>', methods=['GET'])
def get_user_city_registration_by_email(email):

    response_data = sports_handler.get_user_city_registration_by_email(email)
    return response_data


@sports_bp.route('/register/<int:id>', methods=['DELETE'])
def delete_user_city_registration(id):
    response_data = sports_handler.delete_registration_by_id(id)
    return jsonify({"message": response_data})

