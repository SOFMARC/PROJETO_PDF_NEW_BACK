from abc import ABC, abstractmethod
from src.Domain.Clients.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, name: str, email:str, password:str) -> User:
        pass

    @abstractmethod
    def check_user_login(self, email: str, password:str):
        pass

    @abstractmethod
    def get_user(self, email: str):
        pass
    
