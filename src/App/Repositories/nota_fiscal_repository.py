from abc import ABC, abstractmethod
from src.Domain.Extrator.item_nota import NotaFiscal
from src.Domain.Extrator.prestador import Prestador
from src.Domain.Extrator.tomador import Tomador

class NotaFiscalRepository(ABC):
    @abstractmethod
    def save(self, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota) -> NotaFiscal :
        pass

    @abstractmethod
    def insert_data_tomador(self, user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado) -> Prestador:
        pass

    @abstractmethod
    def insert_data_prestacao(self, ser_id, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador) -> Tomador:
        pass