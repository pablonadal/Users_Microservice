from flask import jsonify, Blueprint, request
from app.dto import ResponseBuilder
from app.mapping import UserSchema
from app.services import AuthService
from app.validators import validate_with

auth = Blueprint('auth', __name__)
user_schema = UserSchema()
auth_service = AuthService()
response = ResponseBuilder()

@auth.route('/register', methods=['POST'])
@validate_with(UserSchema)
def register(validated_data):
    user = validated_data
    register = auth_service.register(user)
    if not register:
        response.add_data(user_schema.dump(user)).add_message('Error de registro. Ya existe un usuario con ese email.').add_status_code(400)
        return jsonify(response.build()), response.status_code
    else:
        response.add_data(user_schema.dump(register)).add_message('Usuario registrado con éxito.').add_status_code(200)
        return jsonify(response.build()), response.status_code

@auth.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    login = auth_service.login(email, password)
    if not login:
        response.add_data({"email": email, "password": password}).add_message('El email o la contraseña no son correctos.').add_status_code(400)
        return jsonify(response.build()), response.status_code
    else:
        response.add_data({'token': login}).add_message('Inicio de sesion exitoso').add_status_code(200)
        return jsonify(response.build()), response.status_code