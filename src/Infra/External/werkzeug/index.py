from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

class WerkzeugFactory:
    @staticmethod
    def secure_filename(file_name):
        return secure_filename(file_name)

    @staticmethod
    def generate_password_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password_hash(password, password2):
        return check_password_hash(password, password2)
