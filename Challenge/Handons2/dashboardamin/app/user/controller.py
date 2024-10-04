from flask import Blueprint, request, jsonify
from app.user.service import UserService
from flask_cors import CORS

user_bp = Blueprint('users_api', __name__)
CORS(user_bp)


@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users])


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user.to_dict()) if user else ('', 404)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # validate username length > 5 and < 9
    if len(data['username']) < 5 or len(data['username']) > 9:
        return 'Username must be between 5 and 9 characters', 400

    # validate email using regex
    import re
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data['email']):
        return 'Invalid email', 400

    user = UserService.create_user(data)
    return jsonify(user.to_dict()), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data)
    return jsonify(user.to_dict()) if user else ('', 404)


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserService.delete_user(user_id)
    return ('', 204) if user else ('', 404)