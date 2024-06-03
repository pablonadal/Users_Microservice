from werkzeug.security import generate_password_hash, check_password_hash

class SecurityService:
    """
    En este servicio van todas las funciones referidas a la seguridad.
    Generar un hash de una contraseña, comparar una contraseña con un hash.
    """

    @staticmethod
    def generate_password(password: str) -> str:
        """Genera un hash de una contraseña pasada por parámetro."""
        return generate_password_hash(password)
    
    @staticmethod
    def check_password(pwhash: str, password: str) -> bool:
        """Compara el hash de la contraseña con la contraseña ingresada."""
        return check_password_hash(pwhash, password)