from src.App.Repositories.nota_fiscal_repository import NotaFiscalRepository
from src.Infra.External.pyodbc.index import Database

class NotaFiscalRepositoryInfra(NotaFiscalRepository):
    def __init__(self, database):
        self.db = database
    
    def save(self, user_id, id_nota, local_incidencia_imposto, descricao_atividades, porcentagem, servicos, deducoes, base_de_calculo, inss, iss_retido, endereco_obra, cno, codigo_servico, valor_total_deducoes, aliquota, valor_total_nota, valor_iss, ir):
        
        id = self.db.insert_nota_fiscal(user_id, id_nota, local_incidencia_imposto, descricao_atividades, porcentagem, servicos, deducoes, base_de_calculo, inss, iss_retido, endereco_obra, cno, codigo_servico, valor_total_deducoes, aliquota, valor_total_nota, valor_iss, ir)
        
        return id

    def insert_data_prestacao(self, user_id, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador):
        
        self.db.insert_data_prestacao(user_id, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador)
        
        return 200
           
    def insert_data_tomador(self, user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado):
        
        self.db.insert_data_tomador(user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado)
        
        return 200