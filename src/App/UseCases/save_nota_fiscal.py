from typing import Optional
from Domain.Extrator import NotaFiscal
from App.Repositories.nota_fiscal_repository import NotaFiscalRepository

from src.Domain.Extrator.item_nota import NotaFiscal
from src.Domain.Extrator.prestador import Prestador
from src.Domain.Extrator.tomador import Tomador

class SalvarNotaFiscal:
    def __init__(self, nota_fiscal_repository: NotaFiscalRepository):
        self.nota_fiscal_repository = nota_fiscal_repository
    
    def save(self):
        return self.nota_fiscal_repository.salvar()
    
    def insert_data_tomador(self, user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado) -> Prestador:
        return self.nota_fiscal_repository.insert_data_tomador(user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado)

    def insert_data_prestacao(self, ser_id, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador) -> Tomador:
        return self.nota_fiscal_repository.insert_data_prestacao(ser_id, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador)
