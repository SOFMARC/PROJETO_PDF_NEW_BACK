from typing import Optional
from Domain.Extrator import NotaFiscal
from App.Repositories.user_repository import UserRepository

class CadastrarUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def save(self, name: str, email:str, password:str):
        return self.user_repository.save(name, email, password)
    
    def check_user_login(self, email: str, password:str):
        return self.user_repository.check_user_login(email, password)
    
    def get_user(self, email:str):
        return self.user_repository.get_user(email)
    
