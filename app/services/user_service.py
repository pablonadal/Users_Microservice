from app.models import User
from app.repositories import UserRepository
from app.services.security_service import SecurityService
from app import cache

class UserService:
    """
    En este servicio van todas las funciones referidas al usuario.
    Buscar todos los usuarios, buscar un usuario por id, crear un usuario, actualizar un usuario, eliminar un usuario.
    """

    def __init__(self):
        self.__repo = UserRepository()
    
    def create(self, entity: User) -> User:
        entity.password = SecurityService.generate_password(entity.password)
        user = self.__repo.create(entity)
        cache.set(f'{user.id}', user, timeout=50)
        return user
    
    def update(self, entity: User, id: int) -> User:
        entity.password = SecurityService.generate_password(entity.password)
        user = cache.get(f'{id}')
        if user:
            cache.update(f'{user.id}', entity, timeout=50)
            user = self.__repo.update(entity, id)
        else:
            user = self.__repo.update(entity, id)
            cache.set(f'{user.id}', user, timeout=50)
        return user
    
    def delete(self, id: int) -> User:
        user = cache.get(f'{id}')
        if user:
            cache.delete(f'{user.id}')
        return self.__repo.delete(id)
    
    @cache.memoize(timeout=50)
    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> User:
        user = cache.get(f'{id}')
        if user is None:
            user = self.__repo.find_by_id(id)
            if not user:
                return None
            cache.set(f'{user.id}', user, timeout=50)
        return user
    
    def find_by_email(self, email: str) -> User:
        user = cache.get(f'{email}')
        if not user:
            user = self.__repo.find_by_email(email)
            if not user:
                return None
            cache.set(f'{user.email}', user, timeout=50)
        return user
    
    def check_password(self, mail: str, password: str) -> bool:
        user = self.__repo.find_by_email(mail)
        return SecurityService.check_password(user.password, password)