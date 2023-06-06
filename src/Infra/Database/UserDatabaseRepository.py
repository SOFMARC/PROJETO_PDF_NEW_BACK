from src.App.Repositories.user_repository import UserRepository
from src.Infra.External.pyodbc.index import Database

class UserRepositoryInfra(UserRepository):
    def __init__(self, database):
        self.db = database
    
    def save(self, name, email, passoword):

        self.db.insert_user(name, email, passoword)
        
        return 200
    
    def check_user_login(self, email: str, password:str):

        res = self.db.check_user_login(email, password)
        
        return res
    
    def get_user(self, email):

        return self.db.get_user(email)
    

#db = UserRepositoryInfra(Database())

#db.save('wilson', 'email@gmail.com', '25553245')
#db.check_user_login('email@gmail.com', '25553245')
#db.get_user('email@gmail.com')
