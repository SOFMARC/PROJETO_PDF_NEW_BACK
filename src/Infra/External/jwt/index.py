import jwt 
from jwt.exceptions import DecodeError, ExpiredSignatureError


class JwtFactory:
    
    @staticmethod
    def jwt():
        return jwt
    
    @staticmethod
    def DecodeError():
        return DecodeError

    @staticmethod
    def ExpiredSignatureError():
        return ExpiredSignatureError

