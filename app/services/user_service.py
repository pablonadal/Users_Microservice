from app.models import User
from app.repositories import UserRepository


class UserService:
    """
    En este servicio van todas las funciones referidas al usuario.
    Buscar todos los usuarios, buscar un usuario por id, crear un usuario, actualizar un usuario, eliminar un usuario.
    """

    def __init__(self):
        self.__repo = UserRepository()
    
    def create(self, entity: User) -> User:
        return self.__repo.create(entity)
    
    def update(self, entity: User, id: int) -> User:
        from app.services import SecurityService
        entity.password = SecurityService.generate_password(entity.password)
        return self.__repo.update(entity, id)
    
    def delete(self, id: int) -> User:
        return self.__repo.delete(id)
    
    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> User:
        return self.__repo.find_by_id(id)
    
    def find_by_email(self, email: str) -> User:
        return self.__repo.find_by_email(email)