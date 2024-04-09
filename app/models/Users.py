from app import db
from sqlalchemy.ext.hybrid import hybrid_property
# from .relationships import association_table

class User(db.Model): 
    __tablename__ ='users'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String(100))
    __lastname = db.Column('lastname', db.String(100))
    __phone_number = db.Column('phone_number', db.String(15))
    __email_address = db.Column('email_address', db.String(100), unique=True)
    __password = db.Column('password', db.String(255))
    # roles = db.relationship('Role', secondary=association_table, back_populates='users')
    # user_bookings = db.relationship('Booking', backref='user')

    """ Constructor
    Atributos: 
        name (str): Nombre del usuario, máximo 100 caracteres.
        lastname (str): Apellido del usuario, máximo 100 caracteres.
        phone_number (str): Número de teléfono del usuario, máximo 15 dígitos.
        email_address (str): Dirección de correo electrónico del usuario.
        password (str): Contraseña del usuario, hash encriptado.
    """

    def __init__(self, name: str, lastname: str, phone_number: str, email_address: str, password: str):
        self.__name = name
        self.__lastname = lastname
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__password = password

    @hybrid_property
    def id(self)->str:
        return self.__id
    
    @id.setter
    def code(self, id:str):
        self.__id = id

    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name

    @hybrid_property
    def lastname(self)->str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname:str):
        self.__lastname = lastname

    @hybrid_property
    def phone_number(self)->str:
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number:str):
        self.__phone_number = phone_number
    
    @hybrid_property
    def email_address(self)->str:
        return self.__email_address
    
    @email_address.setter
    def email_address(self, email_address:str):
        self.__email_address = email_address
    
    @hybrid_property
    def password(self)->str:
        return self.__password
    
    @password.setter
    def password(self, password:str):
        self.__password = password

    def __repr__(self) -> str:
        return f'User (code={self.__code}, name={self.__name}, lastname={self.__lastname}, phone_number={self.__phone_number}, email_address={self.__email_address})'

    def __eq__(self, __value: object) -> bool:
        return self.__email_address == __value.email_address  