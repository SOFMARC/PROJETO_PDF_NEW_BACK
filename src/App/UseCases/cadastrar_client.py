from typing import Optional
from Domain.Extrator import NotaFiscal
from App.Repositories.client_repository import ClientRepository

class CadastrarClient:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository
    
    def save(self):
        return self.client_repository.salvar()
