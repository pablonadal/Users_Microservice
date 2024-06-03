from flask import Blueprint, jsonify, request
from app.services import UserService
from app.mapping import UserSchema
from app.dto import ResponseBuilder
from app.validators import validate_with, validate_exists

ps = UserSchema(many=True) # Para devolver varios usuarios
user = Blueprint('user', __name__)

user_schema = UserSchema() # Para devolver un usuario
user_service = UserService()
response = ResponseBuilder()

@user.route('/', methods=['GET'])
def index():
    response.add_status_code(200).add_message('OK this is User resource').add_data({"message": "OK this is User resource"})
    return jsonify(response.build()), response.status_code


@user.route('/create', methods=['POST'])
@validate_with(UserSchema)
def create(validated_data):
    user = validated_data
    response.add_status_code(201).add_message('User created!').add_data({"User created": user_schema.dump(user_service.create(user))})
    return jsonify(response.build()), response.status_code


@user.route('/findall', methods=['GET'])
def find_all():
    if not user_service.find_all():
        response.add_status_code(400).add_message('There are no users created!').add_data()
        return jsonify(response.build()), response.status_code
    response.add_status_code(200).add_message('Users found!').add_data({"Users": ps.dump(user_service.find_all())})
    return jsonify(response.build()), response.status_code
    

@user.route('/findbyid/<int:id>', methods=['GET'])
@validate_exists(user_service, response)
def find_by_id(id):
    response.add_status_code(200).add_message('User found!').add_data({"User": user_schema.dump(user_service.find_by_id(id))})
    return jsonify(response.build()), response.status_code
    
    
@user.route('/update/<int:id>', methods=['PUT'])
@validate_with(UserSchema)
@validate_exists(user_service, response)
def update(validated_data, id):
    user = validated_data
    response.add_status_code(200).add_message('User updated!').add_data(
        {"user updated": user_schema.dump(user_service.update(user, id))}
    )
    return jsonify(response.build()), response.status_code


@user.route('/delete/<int:id>', methods=['DELETE'])
@validate_exists(user_service, response)
def delete(id):
    response.add_status_code(200).add_message('User deleted!').add_data({"User deleted": user_schema.dump(user_service.delete(id))})
    return jsonify(response.build()), response.status_code


@user.route('/findbymail/<string:mail>', methods=['GET'])
def find_by_mail(mail):
    try:
        response.add_status_code(200).add_message('User found!').add_data({"User": user_schema.dump(user_service.find_by_email(mail))})
        return jsonify(response.build()), response.status_code
    except:
        response.add_status_code(400).add_message('User not found.').add_data()
        return jsonify(response.build()), response.status_code