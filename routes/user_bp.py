from flask import Blueprint, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate

from services.user_service import UserService

user_bp = Blueprint("user_bp", __name__)

user_service = UserService()


class UserModel(BaseModel):
    username: str
    password: str


@user_bp.route('/register', methods=['POST'])
@validate(body=UserModel)
def register_user():
    data = request.body_params
    result = user_service.register_user(data.username, data.password)
    return jsonify(result)
